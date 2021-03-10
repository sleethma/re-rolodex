cd $(dirname $0)

# @$1 create-stack or update-stack
# @$2 environment
# @$3 codebucketname

#### Create Lambda Binaries ####
# FILES ALWAYS INVALID WITH??? -->  zip -g ../serverless/lambdas/randomTollFreeGen/randomTollFreeGen.zip ../serverless/lambdas/randomTollFreeGen/randomTollFreeGen.py 
# FILES ALWAYS INVALID WITH??? -->  zip -g  ../serverless/lambdas/rolodexServer/rolodexServer.zip ../serverless/lambdas/rolodexServer/rolodexServer.py 
# Because of ^^ I had to do the below mess...

# cd ../serverless/lambdas/rolodexServer/ &&
# zip -g rolodexServer.zip rolodexServer.py &&
# cp rolodexServer.zip  ../../../cloudfn/ &&

# cd ../randomTollFreeGen &&
# zip -g randomTollFreeGen.zip randomTollFreeGen.py &&
# cp randomTollFreeGen.zip  ../../../cloudfn/ 

# cd ../../../cloudfn

# #### Copy Binaries to S3 ####
# #TODO: make flags for deployment instead fo positional (eg $1 -> -u)
# aws s3 cp randomTollFreeGen.zip s3://$3 --profile $2
# aws s3 cp rolodexServer.zip s3://$3 --profile $2

# # ### Deploy Cloudformation template ####
# sleep 10 # sleep acounts for variable network/AWS api time needed to res copying
aws cloudformation $1 --stack-name randomTollFreeGen-rolodex --template-body file://serverless-res.yml \
--parameters file://dev-resources.json --capabilities CAPABILITY_NAMED_IAM --profile $2

#### Uncomment Below to validate Template pre-deploy ####
# aws cloudformation validate-template --template-body file://serverless-res.yml