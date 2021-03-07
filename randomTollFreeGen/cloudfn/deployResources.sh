# @$1 create-stack or update-stack
# @$2 environment

aws s3 cp ../randomTollFreeGen.zip s3://sma-code --profile $2

sleep 10 # sleeping for variable network/AWS api speeds

aws cloudformation $1 --stack-name randomTollFreeGen-rolodex --template-body file://randomTollFreeGen.yml --parameters file://dev-resources.json --capabilities CAPABILITY_NAMED_IAM --profile $2

# Uncomment below for template validation
# aws cloudformation validate-template --template-body file://randomTollFreeGen.yml

