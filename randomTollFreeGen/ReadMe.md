# Rolodex

## Overview

Provides a call center that converts phone numbers to vanity numbers and saves the "Best" 5
resulting vanity numbers, score, and the caller's number in a DynamoDB table.

_Best_ = Greater variation of digits == harder to remember.  
 _Score_ = unique digits of original number - unique digits of vanity number. Positive score represents better derived vanity number.
_algorithm_ = a random shuffle of phone digit order then seeded with algorithm of digit value divided by index (d/i \* 100) and spread over number range 0 - 9 to derive new value.

## Usage

- Phone Number: 1 877-381-4096

## Deploy

- Specify parameters in deploy template for respective target enviroments (Bash scripts to run...all that)
- Remember to add the created lambda resource in the Amazon Connect panel by navigating to 'AWS Connect service > Contact flows > AWSLambda'

### Rolodex UI

- Find the app endpoint by navigating to: AWS Console > S3 > Bucket > Properties > Static Website Hosting > Endpoint

## Challenges

- #### Portable Deployment:

  Not knowing clients setup required the looking into portability.

  - _Attempted_: Using `DependsOn` S3 bucket property wouldn't work seems no way to load zipped code through template, and could (given time, write a shell script to deploy bucket, check for resource creation, hit awscli putObject on target bucket, then programatically run rest of resources deploy script)
  - _Resolved_: To have client run each shell script following instructions after another (Little Clunky and curious of your method!).

- #### DBs

  1. Using scan can be efficient for returning last 5 entries into table. (Relational dbs excel for these query types) Scaning doesn't scale well in cost and performance. Using a ttl can help reduce this and mitigate this by reducing records in table to a relavent set. Considerations need to be made like:

  - size fluctuations based on user load variances over time
  - what to do with expired data that want to keep. (DynamoStreams to cold storage on insert etc.)

  2. Using a partition key of yyyy-mm-dd and sort key. Can pull data from subsets to avoid large calls/scans. Limitation, multiple calls "polling for data"

# Todo: flesh out from below article considerations and choice for this effort

3. https://www.dynamodbguide.com/leaderboard-write-sharding/

## Enhancements

- Add security cert to app
- Lexbot asking user number of cycles to run vanity number algorithm for better unique results
- python controller for deploy/template management
- Use of nested stacks and contolling stack creation order (ex: bin code bucket, before lambda deployments)
- Wrap deployment in python program to generate cloudformation parameter files.
