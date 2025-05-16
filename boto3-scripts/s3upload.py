import boto3
from botocore.exceptions import ClientError
import os

def create_bucket(bucket_name, region=None):
    try:
        if region is None or region == "us-east-1":
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"Error creating bucket: {e}")

def upload_file(bucket_name, file_path, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
    except ClientError as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    bucket_name = "my-aws-project-s3-bucket"  # Change to your unique bucket name
    region = "us-east-1"
    file_path = "/home/ec2-user/index.html"  # Full path on your EC2 instance

    create_bucket(bucket_name, region)
    upload_file(bucket_name, file_path)



