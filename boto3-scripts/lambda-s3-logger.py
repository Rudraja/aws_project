import boto3
import json
from botocore.exceptions import BotoCoreError, ClientError

def invoke_lambda(function_name, payload):
    # Specify your AWS region here
    lambda_client = boto3.client('lambda', region_name='us-east-1')

    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',  # synchronous
            Payload=json.dumps(payload)
        )
        response_payload = json.loads(response['Payload'].read())
        return response_payload
    except (BotoCoreError, ClientError) as error:
        print(f"Error invoking Lambda: {error}")
        return None

if __name__ == "__main__":
    function_name = "lambda-s3-logger"  # Your Lambda function name
    payload = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "my-s3-logger-bucket-2"  # Replace with your bucket name
                    },
                    "object": {
                        "key": "ESSAY-2.pdf"  # Replace with your object key
                    }
                }
            }
        ]
    }

    result = invoke_lambda(function_name, payload)
    if result:
        print(json.dumps(result, indent=2))
