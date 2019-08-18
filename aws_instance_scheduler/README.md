#AWS Instance Scheduler
The AWS Instance Scheduler is a solution that automates the starting and stopping of EC2 and RDS instances.

The Instance Scheduler leverages resource tags and Lambda to automatically stop and restart instances across multiple AWS Regions and accounts on a customer-defined schedule.

The solution is easy to deploy and can help reduce operational costs. For example, an organization can use the Instance Scheduler in a non-production environment to automatically stop instances every day, outside of business hours. For customers who leave all of their instances running at full utilization, this solution can result in up to 70% cost savings for those instances that are only necessary during regular business hours (weekly utilization reduced from 168 hours to 50 hours).