from datetime import datetime

import boto3


def lambda_handler(event, context):

    
    create_time = datetime.datetime.now()
    create_fmt = create_time.strftime('%Y-%m-%d-%H:%M:%S')

    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        instances = ec2.instances.all()
        for instance in instances:
            intance_id = instance.id 
            ec2_client.create_image( InstanceId=intance_id, 
            Name="Lambda - " + intance_id + " from " + create_fmt, 
            Description="Lambda created AMI of instance " + intance_id + " from " + create_fmt, NoReboot=True, 
            DryRun=False)
            print("AMI created for instance ID : " + intance_id )
