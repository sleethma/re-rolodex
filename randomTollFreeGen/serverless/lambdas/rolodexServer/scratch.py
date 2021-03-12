import collections
import json
from datetime import datetime

allItems = [
    {
        "score": {"N": "5"},
        "uuid": {"S": "3170c7d8-820f-11eb-9059-5bc8bde5c099-0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "12222263393"},
        "callers_num": {"S": "16478905423"},
        "timestamp": {"N": "1615428732"},
    },
    {
        "score": {"N": "5"},
        "uuid": {"S": "3170c7d8-820f-11eb-9059-5bc8bde5c099-1"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "18896339993"},
        "callers_num": {"S": "16478905423"},
        "timestamp": {"N": "1615428732"},
    },
    {
        "score": {"N": "5"},
        "uuid": {"S": "3170c7d8-820f-11eb-9059-5bc8bde5c099-2"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "14349939336"},
        "callers_num": {"S": "16478905423"},
        "timestamp": {"N": "1615428732"},
    },
    {
        "score": {"N": "5"},
        "uuid": {"S": "3170c7d8-820f-11eb-9059-5bc8bde5c099-4"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "12225535653"},
        "callers_num": {"S": "16478905423"},
        "timestamp": {"N": "1615428732"},
    },
    {
        "score": {"N": "5"},
        "uuid": {"S": "3170c7d8-820f-11eb-9059-5bc8bde5c099-3"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "17633377036"},
        "callers_num": {"S": "16478905423"},
        "timestamp": {"N": "1615428732"},
    },
    {
        "score": {"N": "4"},
        "uuid": {"S": "1f693841-820e-11eb-b082-6baae3e70682"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "14949136399"},
        "callers_num": {"S": "16478905423"},
        "timestamp": {"N": "1615428273"},
    },
    {
        "score": {"N": "4"},
        "uuid": {"S": "7808e82b-820b-11eb-b49a-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "17225565705"},
        "callers_num": {"S": "16478905423"},
        "timestamp": {"N": "1615427133"},
    },
    {
        "score": {"N": "-1"},
        "uuid": {"S": "6d5d8e52-820b-11eb-9369-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "17399993933"},
        "callers_num": {"S": "14343434343"},
        "timestamp": {"N": "1615427115"},
    },
    {
        "score": {"N": "4"},
        "uuid": {"S": "63049f08-820b-11eb-85dc-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "14435339935"},
        "callers_num": {"S": "17462738495"},
        "timestamp": {"N": "1615427098"},
    },
    {
        "score": {"N": "3"},
        "uuid": {"S": "5c668d3e-820b-11eb-97b4-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "17999997939"},
        "callers_num": {"S": "16834442536"},
        "timestamp": {"N": "1615427087"},
    },
    {
        "score": {"N": "2"},
        "uuid": {"S": "56589e37-820b-11eb-a5ed-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "11639533363"},
        "callers_num": {"S": "10278383593"},
        "timestamp": {"N": "1615427076"},
    },
    {
        "score": {"N": "2"},
        "uuid": {"S": "4ec3ab89-820b-11eb-b082-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "18658777999"},
        "callers_num": {"S": "10978675653"},
        "timestamp": {"N": "1615427064"},
    },
    {
        "score": {"N": "1"},
        "uuid": {"S": "487b8085-820b-11eb-9369-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "18255999999"},
        "callers_num": {"S": "17364535553"},
        "timestamp": {"N": "1615427053"},
    },
    {
        "score": {"N": "0"},
        "uuid": {"S": "424e8e8a-820b-11eb-97b4-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "13766577559"},
        "callers_num": {"S": "10909876876"},
        "timestamp": {"N": "1615427043"},
    },
    {
        "score": {"N": "4"},
        "uuid": {"S": "354d402d-820b-11eb-b49a-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "14499337333"},
        "callers_num": {"S": "18493728356"},
        "timestamp": {"N": "1615427021"},
    },
    {
        "score": {"N": "6"},
        "uuid": {"S": "24163b7c-820b-11eb-a73e-45625f915ef0"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "13699030339"},
        "callers_num": {"S": "11234567890"},
        "timestamp": {"N": "1615426992"},
    },
    {
        "score": {"N": "0"},
        "uuid": {"S": "1a11ce8d-8165-11eb-9369-cd61d8f16adf"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "17999393933"},
        "callers_num": {"S": "12223334444"},
        "timestamp": {"N": "1615355679"},
    },
    {
        "score": {"N": "5"},
        "uuid": {"S": "0f6320ff-8165-11eb-85dc-cd61d8f16adf"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "19899997936"},
        "callers_num": {"S": "11234567890"},
        "timestamp": {"N": "1615355661"},
    },
    {
        "score": {"N": "-3"},
        "uuid": {"S": "ba2a322f-8164-11eb-a46d-cd61d8f16adf"},
        "partition": {"S": "partition_0"},
        "vanity_number": {"S": "19930022222"},
        "callers_num": {"S": "11111111111"},
        "timestamp": {"N": "1615355518"},
    },
]


seen = collections.OrderedDict()

for item in allItems:
    # eliminate this check if you want the last item
    if item["callers_num"]["S"] not in seen:
        posix_time = int(item["timestamp"]["N"])
        item["timestamp"] = datetime.utcfromtimestamp(
            int(item["timestamp"]["N"])
        ).strftime("%Y-%m-%d %H:%M:%SZ")
        item["score"] = item["score"]["N"]
        item["uuid"] = item["uuid"]["S"]
        item["vanity_number"] = item["vanity_number"]["S"]
        del item["partition"]
        item["callers_num"] = item["callers_num"]["S"]
        seen[item["callers_num"]] = item

    # print(item["callers_num"]["S"])

respItems = {"data": list(seen.values())[:5]}

print(json.dumps(respItems))


# unique_objects = list({item.callers_num: item for item in allItems}.values())
# print(unique_objects)

# seen = collections.OrderedDict()

# for item in allItems:
#     # eliminate this check if you want the last item
#     if item["callers_num"]["S"] not in seen:
#         posix_time = int(item["timestamp"]["N"])

#         item["timestamp"] = datetime.utcfromtimestamp(
#             int(item["timestamp"]["N"])
#         ).strftime("%Y-%m-%d %H:%M:%SZ")
#         item["score"] = item["score"]["N"]
#         item["uuid"] = item["uuid"]["S"]
#         item["vanity_number"] = item["vanity_number"]["S"]
#         item["callers_num"] = item["callers_num"]["S"]
# del item["partition"]

#         seen[item["callers_num"]["S"]] = item

# print(item["callers_num"]["S"])
