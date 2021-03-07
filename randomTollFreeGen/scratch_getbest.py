import random
import time

cust_num = "+12533944742"
cust_num = cust_num[2:]

charList = list(cust_num)

##### move to own function #####
custNumInts = [int(i) for i in charList]
uniqueCustNumObj = {}
print(custNumInts)
for i, num in enumerate(custNumInts):
    uniqueCustNumObj[num] = ""
custNumScore = len(cust_num) - len(uniqueCustNumObj)

#################################
randNums = []

for _ in range(20):
    # TODO: why cant I move p -> int up one scope?
    p = [int(i) for i in charList]

    # NOTE: (enhancement): use unix nanos to seed as can assert value for easy testing. using shuffle - shuffles "in place"
    random.shuffle(charList)

    # convert array elems to ints
    randNums.append(p)

scoredNums = []

for num in randNums:
    print(num)

# loop through number sets
for i, uniqueNumber in enumerate(randNums):

    # map each to get score
    uniqueNumObj = {}
    for j, k in enumerate(uniqueNumber):
        # NOTE: Seed uses the shuffled number index/number at index
        # TODO: Play with seed to see if better range of scores acheivable
        random.seed(int(j / k * 10))
        genVal = random.randint(0, 9)
        print(f"generated random value from {k} is {genVal}")
        uniqueNumber[j] = genVal
        print("assigned: ", uniqueNumber[j])
        # set map to auto-reduce dups
        uniqueNumObj[genVal] = ""
        print(f"adding key: {genVal}")

    randNums[i] = uniqueNumber

    uniqueNumScore = len(cust_num) - len(uniqueNumObj)
    print("\tuniqueNumScore", uniqueNumScore)
    print("\tcustNumScore: ", custNumScore)

    scoredNum = {"phNum": randNums[i], "score": uniqueNumScore - custNumScore}
    # scoredNums[i] = scoredNum
    scoredNums.append(scoredNum)

print("final ran nums", randNums)
print("scoredNums presort: ", scoredNums)

scoredNums.sort(key=lambda x: x["score"], reverse=True)
print("scoredNums postsort: ", scoredNums)
print("top 5 ", scoredNums[:5])
for i in scoredNums[:5]:
    stringNums = [str(num) for num in i["phNum"]]
    num = ""
    i["phNum"] = "1{}".format(num.join(stringNums))

print("return final ", scoredNums[:5])
returnData = {}
returnNums = scoredNums[:3]

for i in range(len(returnNums)):
    returnData[f"vanityNum_{i + 1}"] = scoredNums[i]["phNum"]

print(returnData)
