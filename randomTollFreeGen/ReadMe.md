# Rolodex

## Usage

- Phone Number: 1 877-381-4096

## Deploy

- Specify parameters in deploy template for respective target enviroments (Bash scripts to run...all that)
- Remember to add the created lambda resource in the Amazon Connect panel by navigating to 'AWS Connect service > Contact flows > AWSLambda'

## Challenges

- Portable Deployment:
  Not knowing clients setup required the looking into portability.
  - _Attempted_: Using `DependsOn` S3 bucket property wouldn't work seems no way to load zipped code through template, and could (given time, write a shell script to deploy bucket, check for resource creation, hit awscli putObject on target bucket, then programatically run rest of resources deploy script)
  - _Resolved_: To have client run each shell script following instructions after another (Little Clunky and curious of your method!).
