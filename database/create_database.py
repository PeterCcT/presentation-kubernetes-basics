#!/usr/local/bin/python
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

dynamo_client = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:4566'
)

def create_text_table():
    global dynamo_client
    dynamo_client.create_table(
        TableName='texts',
        BillingMode='PAY_PER_REQUEST',
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ]
    )

is_to_keep_trying_to_create_database = True
while is_to_keep_trying_to_create_database:
    try:
        create_text_table()
        is_to_keep_trying_to_create_database = False
    except ClientError as e:
        error = e.response.get('Error').get('Code')
        if error == 'ResourceInUseException':
            is_to_keep_trying_to_create_database = False
        else:
            raise e
    except EndpointConnectionError:
        continue