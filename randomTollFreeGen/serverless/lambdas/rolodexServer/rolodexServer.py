import boto3
import os
import time
import logging

dynamodb = boto3.resource("dynamodb", region_name=os.environ["REGION"])

table = dynamodb.Table(os.environ["TABLE_NAME"])

# NOTE:  Client deliverable code intentionally trades conscise nature for easier readability/customer enhancements


def lambda_handler(event, context):
    print("input event: {}".format(event))
    return {
        "body": "Hello there {0}".format(
            event["requestContext"]["identity"]["sourceIp"]
        ),
        "headers": {"Content-Type": "text/plain"},
        "statusCode": 200,
    }
