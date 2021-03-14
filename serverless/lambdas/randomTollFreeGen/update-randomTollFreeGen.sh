zip -g randomTollFreeGen.zip randomTollFreeGen.py 
aws lambda update-function-code --function-name randomTollFreeGen --zip-file fileb://randomTollFreeGen.zip --profile $1 
rm randomTollFreeGen.zip