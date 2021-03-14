import boto3
import random
import os
import time
import logging
import uuid

dynamodb = boto3.resource("dynamodb", region_name=os.environ["REGION"])

table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    try:
        custNum = event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
        contactId = event["Details"]["ContactData"]["ContactId"]
        print(f"ContactID: {contactId}")
        logging.debug(f"CustomerNumber: {custNum}")
    except Exception as ex:
        logging.debug(f"input event{event}")
        logging.fatal("Missing input parameters for function {ex}")
        raise

    return handle_ani(custNum)


def get_best(cust_num):

    phChars = list(cust_num)

    custNumScore = score_orig_num(phChars)

    randNums = []

    for _ in range(30):

        # NOTE: (enhancement): use unix nanos to seed as can assert value for easy testing. using shuffle - shuffles "in place"
        # This also forces to have to do int casting for both original, and generated numbers.
        random.shuffle(phChars)

        phDigits = [int(i) for i in phChars]

        # convert array elems to ints
        randNums.append(phDigits)

    scoredNums = []

    # NOTE: nested for loops loop through generated numbers, seeds random and saves object  new number and score
    for i, uniqueNumber in enumerate(randNums):
        uniqueNumObj = {}
        for j, v in enumerate(uniqueNumber):
            # NOTE: Seed uses the shuffled number index/number at new shuffled index
            random.seed(int(v * 17 / (j + 1)))
            genVal = random.randint(0, 9)
            uniqueNumber[j] = genVal
            # set to map to auto-reduce dups
            uniqueNumObj[genVal] = ""

        randNums[i] = uniqueNumber

        uniqueNumScore = len(uniqueNumObj)

        scoredNum = {"phNum": randNums[i], "score": custNumScore - uniqueNumScore}
        scoredNums.append(scoredNum)

    scoredNums.sort(key=lambda x: x["score"], reverse=True)

    # NOTE: add 1 to phone number and casts int phone array val to string
    for i in scoredNums[:5]:
        stringNums = [str(num) for num in i["phNum"]]
        num = ""
        i["phNum"] = "1{}".format(num.join(stringNums))

    return scoredNums[:5]


def score_orig_num(custNum):
    custNumInts = [int(i) for i in custNum]
    uniqueCustNumObj = {}
    for num in custNumInts:
        uniqueCustNumObj[num] = ""
    return len(uniqueCustNumObj)


def handle_ani(custNum):

    # NOTE: calculate 5 "Best" vanity Numbers Note: best = Most mnuemonic for customer. i.e. fewest different numbers
    # TODO:   (enhancement for "Best": weighted with most consecutive numbers )
    bestNums = get_best(custNum[2:])
    writeNums = bestNums[:5]

    try:
        print("writing to db ", writeNums)
        currentTimeMs = int(time.time())
        uuid_id = str(uuid.uuid1())
        for i in range(len(writeNums)):
            uuidKey = f"{uuid_id}-{i}"
            table.put_item(
                Item={
                    "uuid": uuidKey,
                    "vanity_number": writeNums[i]["phNum"],
                    "score": writeNums[i]["score"],
                    "callers_num": custNum[1:],
                    "timestamp": currentTimeMs,
                    "partition": "partition_0",
                }
            )
    except Exception as e:
        logging.warning(f"Error: {e}")

    returnData = {}
    returnNums = bestNums[:3]

    for i in range(len(returnNums)):
        returnData[f"vanityNum_{i + 1}"] = bestNums[i]["phNum"]

    return returnData