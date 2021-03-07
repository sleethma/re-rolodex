import boto3
import json
import random
import os
import time
from botocore.exceptions import ClientError
from base64 import b64decode
from boto3.dynamodb.conditions import Key, Attr
import logging

# TODO: get region dynamically
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

table = dynamodb.Table(os.environ["TABLE_NAME"])

# NOTE:  Client deliverable code intentionally trades conscise nature for easier readability/customer enhancements


def lambda_handler(event, context):
    print("input event{}".format(event))
    try:
        custNum = event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
        contactId = event["Details"]["ContactData"]["ContactId"]
        logging.info(f"ContactID: {contactId}")
        logging.info(f"CustomerNumber: {custNum}")
    except Exception as ex:
        logging.debug(f"input event{event}")
        logging.fatal("Missing input parameters for function {ex}")
        raise

    return handle_ani(custNum)


def get_best(vanity_nums):
    cust_num = vanity_nums

    charList = list(cust_num)

    custNumScore = score_orig_num(charList)

    randNums = []

    for _ in range(100):
        # TODO: why cant I move p -> int up one scope?
        p = [int(i) for i in charList]

        # NOTE: (enhancement): use unix nanos to seed as can assert value for easy testing. using shuffle - shuffles "in place"
        random.shuffle(charList)

        # convert array elems to ints
        randNums.append(p)

    scoredNums = []

    # loop through number sets
    for i, uniqueNumber in enumerate(randNums):

        # map each to get score
        uniqueNumObj = {}
        for j, k in enumerate(uniqueNumber):
            # NOTE: Seed uses the shuffled number index/number at index
            # TODO: Play with seed to see if better range of scores acheivable
            random.seed(int(k / (j + 1) * 10))
            genVal = random.randint(0, 9)
            uniqueNumber[j] = genVal
            # set map to auto-reduce dups
            uniqueNumObj[genVal] = ""

        randNums[i] = uniqueNumber

        uniqueNumScore = len(cust_num) - len(uniqueNumObj)
        # print("\tuniqueNumScore", uniqueNumScore)
        # print("\tcustNumScore: ", custNumScore)

        scoredNum = {"phNum": randNums[i], "score": uniqueNumScore - custNumScore}
        # scoredNums[i] = scoredNum
        scoredNums.append(scoredNum)

    scoredNums.sort(key=lambda x: x["score"], reverse=True)
    print("top 5 ", scoredNums[:5])
    for i in scoredNums[:5]:
        stringNums = [str(num) for num in i["phNum"]]
        num = ""
        i["phNum"] = "1{}".format(num.join(stringNums))

    print("return final ", scoredNums[:5])

    return scoredNums[:5]


def score_orig_num(custNum):
    custNumInts = [int(i) for i in custNum]
    uniqueCustNumObj = {}
    print(custNumInts)
    for i, num in enumerate(custNumInts):
        uniqueCustNumObj[num] = ""
    return len(custNum) - len(uniqueCustNumObj)


def handle_ani(custNum):

    # NOTE: calculate 5 "Best" vanity Numbers Note: best = Most mnuemonic for customer. i.e. fewest different numbers
    # TODO:   (enhancement for "Best": weighted with most consecutive numbers )
    bestNums = get_best(custNum[2:])
    writeNums = bestNums[:5]
    deleteBySec = 172800
    # TODO: write 5 vanity Numbs to dynamo

    try:
        print("writing to db ", writeNums)
        currentTimeMs = int(time.time())
        for i in range(len(writeNums)):
            print("vanity_number: {}".format(writeNums[i]["phNum"]))
            print("score: {}".format(writeNums[i]["score"]))
            print("ttl: {}".format(currentTimeMs))
            table.put_item(
                Item={
                    "vanity_number": writeNums[i]["phNum"],
                    "score": writeNums[i]["score"],
                    "ttl": int(time.time()) + deleteBySec,
                    "timestamp": currentTimeMs,
                }
            )
    except Exception as e:
        logging.warning(f"Error: {e}")

    # TODO: return obj with original and three objects
    returnData = {}
    returnNums = bestNums[:3]

    for i in range(len(returnNums)):
        returnData[f"vanityNum_{i + 1}"] = bestNums[i]["phNum"]

    return returnData