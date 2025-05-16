import boto3

def list_running_instances():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
            print(f"Availability Zone: {instance['Placement']['AvailabilityZone']}")
            print("-" * 30)

if __name__ == "__main__":
    list_running_instances()
