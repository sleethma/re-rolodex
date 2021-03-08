# @$1 create-stack or update-stack
# @$2 environment

aws cloudformation $1 --stack-name code-bucket-rolodex --template-body file://code-bucket.yml --parameters file://dev-code-bucket.json --profile $2

# Uncomment below for template validation
# aws cloudformation validate-template --template-body file://serverless-res.yml