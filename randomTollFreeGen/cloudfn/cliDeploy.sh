# @$1 create-stack or update-stack
# @$2 environment

aws cloudformation $1 --stack-name randomTollFreeGen-rolodex --template-body file://randomTollFreeGen.yml --parameters file://development.json --capabilities CAPABILITY_NAMED_IAM --profile $2