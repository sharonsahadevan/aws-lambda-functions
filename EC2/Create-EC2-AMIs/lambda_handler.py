import datetime

import boto3


def lambda_handler(event, context):

    
    create_time = datetime.datetime.now()
    create_fmt = create_time.strftime('%Y-%m-%d-%H-%M-%S')

    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['running']}])
        if instances:
            for instance in instances:
                instance_id = instance.id 
                try:
                    ec2_client.create_image( InstanceId=instance_id, 
                    Name="Lambda- " + instance_id + "-" + create_fmt, 
                    Description="Lambda created AMI of instance " + instance_id + " from " + create_fmt, NoReboot=True, 
                    DryRun=False)
                except:
                        print("Invalid instance_id error: " + instance_id)
                        
                print("AMI created for instance ID : " + instance_id )
        else:
            print("There are no running Ec2 Instances in ",region)
            

    