# TODO: LOAD zip with deployment
zip -g randomTollFreeGen.zip randomTollFreeGen.py 
aws lambda update-function-code --function-name randomTollFreeGen --zip-file fileb://randomTollFreeGen.zip --profile $1 
# rm randomTollFreeGen.zip

# aws lambda update-function-code --function-name campaignCallRouter --zip-file fileb:///$GOPATH/src/go.ftdr.com/connect/lambdas/campaignCallRouter/campaignCallRouter.zip --profile $1 &&
