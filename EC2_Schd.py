#Automating Ec2 scheduled Stop

import boto3

def lambda_handler(event, context):
    # get list of regions 
    ec2.client = boto3.client('ec2')
    regions = [region['RegionName']
              for region in ec2_client.describe_regions()['Regions']]

    #iterate over the regions 
    for region in regions:
        ec2 = boto3.resource('ec2', region_name =region)
        print('Region': region)

    # get only running instances
        instances = ec2.instances.filter(
            Filters=[{'Name:' , 'instance-state-name',
                       'Values' , ['running']}])
        
        for instance in instances:
            instances.stop()
            print('Stopped instances', instance.id)
        )
