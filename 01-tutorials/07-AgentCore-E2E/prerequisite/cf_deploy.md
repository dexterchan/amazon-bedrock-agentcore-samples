# Prerequiste to setup the account for the lab

## 1. Pack the lambda package
```
pushd lambda/python
zip -r ../../lambda-code.zip . -x "ddgs-layer.zip"
popd
```

### 2. Upload both files to S3
Here, please inject the lambda name as you want.
```
LAMBDA_NAME={your lambda name}-agentcore-e2e-lambda
aws s3 mb s3://${LAMBDA_NAME}
aws s3 cp lambda-code.zip s3://${LAMBDA_NAME}/
aws s3 cp lambda/python/ddgs-layer.zip s3://${LAMBDA_NAME}/python/ddgs-layer.zip
```


### 3. deploy the cloudformation of the infrastructure

```
aws cloudformation deploy \
  --template-file infrastructure.yaml \
  --stack-name customer-support-infrastructure \
  --parameter-overrides \
    LambdaS3Bucket=${LAMBDA_NAME} \
    LambdaS3Key=lambda-code.zip \
    LayerS3Key=python/ddgs-layer.zip \
  --capabilities CAPABILITY_NAMED_IAM \
  --s3-bucket ${LAMBDA_NAME} \
  --region us-east-1
```

### 4. deploy the cognito setup

```
aws cloudformation deploy \
  --template-file cognito.yaml \
  --stack-name customer-support-cognito \
  --parameter-overrides \
    UserPoolName=MyCustomerPool \
    MachineAppClientName=MyMachineClient \
    WebAppClientName=MyWebClient \
  --capabilities CAPABILITY_IAM \
  --region us-east-1
  ```