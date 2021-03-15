cd $(dirname $0)

# @$1 create-stack or update-stack
# @$2 codebucketname
# @$3 environment

#### Create Lambda Binaries ####
# Zip FILES ALWAYS INVALID WITH?!? -->  zip -g ../serverless/lambdas/randomTollFreeGen/randomTollFreeGen.zip ../serverless/lambdas/randomTollFreeGen/randomTollFreeGen.py 
# Zip FILES ALWAYS INVALID WITH?!? -->  zip -g  ../serverless/lambdas/rolodexServer/rolodexServer.zip ../serverless/lambdas/rolodexServer/rolodexServer.py 
# Because of ^^ had to do below workaround...
echo Creating binaries...

cd ../serverless/lambdas/rolodexServer/ &&
zip -g rolodexServer.zip rolodexServer.py &&
cp rolodexServer.zip  ../../../cloudfn/ &&

cd ../randomTollFreeGen &&
zip -g randomTollFreeGen.zip randomTollFreeGen.py &&
cp randomTollFreeGen.zip  ../../../cloudfn/ 

cd ../../../cloudfn

#### Copy Binaries to S3 ####
#TODO: make flags for deployment instead fo positional (eg $1 -> -u)
echo uploading binaries to S3 $2 to account profile $3....

aws s3 cp randomTollFreeGen.zip s3://$2 --profile $3
aws s3 cp rolodexServer.zip s3://$2 --profile $3

### Deploy Cloudformation template ####
sleep 10 # contingency for variable network/AWS api time possibly needed (TODO: hit S3 api to check this instead)

echo using $1 to deploy back-end resources....

aws cloudformation $1 --stack-name randomTollFreeGen-rolodex --template-body file://serverless-res.yml \
--parameters file://conf-resources.json --capabilities CAPABILITY_NAMED_IAM --profile $3


#### Uncomment Below to validate Template pre-deploy ####
# aws cloudformation validate-template --template-body file://serverless-res.yml