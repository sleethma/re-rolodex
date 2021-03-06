from enum import unique
import boto3
import os
import json
import logging
from boto3.dynamodb.conditions import Key
import collections
from datetime import datetime

dynamodb_client = boto3.client("dynamodb", region_name=os.environ["REGION"])


def lambda_handler(event, context):
    print("input event: {}".format(event))

    # TODO:  Handle request validation, implement auth

    return get_top_five()


def make_resp(status, body, error):

    res = {
        "statusCode": status,
        "body": json.dumps(body),
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Allow-Origin": "*",
            "X-Requested-With": "*",
        },
    }
    if error:
        res["error"] = error
    return res


def get_top_five():
    try:
        resp = dynamodb_client.query(
            TableName=os.environ["TABLE_NAME"],
            IndexName=os.environ["GSI_NAME"],
            KeyConditionExpression="#P = :partit",
            ExpressionAttributeNames={"#P": "partition"},
            ExpressionAttributeValues={":partit": {"S": "partition_0"}},
            ScanIndexForward=False,
        )

    except Exception as e:
        print(f"Error pulling data from dynamo. Message: {e}")
        return make_resp("500", None, e)
    if not resp:
        return make_resp("500", None, "No response from server table")
    if resp["Count"] == 0:
        logging.info(
            "No data in database. DB StatusCode: {}".format(
                resp["ResponseMetadata"]["HTTPStatusCode"]
            )
        )
        return make_resp("404", "No current user data returned", None)

    uniqueItems = collections.OrderedDict()

    # map to autoreduce and format reponse
    for item in resp["Items"]:
        # NOTE: @indivCallID needed as '-#' appended to uuids of same call for unique entries into GSI database (Would like a cleaner way)
        indivCallID = item["uuid"]["S"][:-2]
        if indivCallID not in uniqueItems:
            posixTime = int(item["timestamp"]["N"])
            item["timestamp"] = datetime.utcfromtimestamp(posixTime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            item["score"] = item["score"]["N"]
            item["uuid"] = item["uuid"]["S"]
            item["vanity_number"] = item["vanity_number"]["S"]
            del item["partition"]
            item["callers_num"] = item["callers_num"]["S"]
            uniqueItems[item["uuid"][:-2]] = item
    respItems = list(uniqueItems.values())[:5]
    finalResp = {"data": respItems}
    return make_resp("200", finalResp, None)
