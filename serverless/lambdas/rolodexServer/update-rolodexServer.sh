zip -g rolodexServer.zip rolodexServer.py
aws lambda update-function-code --function-name rolodexServer --zip-file fileb://rolodexServer.zip --profile $1 
rm rolodexServer.zip