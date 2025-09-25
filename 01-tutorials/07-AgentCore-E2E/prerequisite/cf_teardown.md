# Teardown after the lab

## CloudFormation delete stack
```
aws cloudformation delete-stack \
  --stack-name customer-support-infrastructure \
  --region us-east-1

aws cloudformation delete-stack \
  --stack-name customer-support-cognito \
  --region us-east-1
```

## Remove artifact of the deployment
```
LAMBDA_NAME={your lambda name}-agentcore-e2e-lambda
aws s3 rm s3://${LAMBDA_NAME} --recursive
aws s3 rb s3://${LAMBDA_NAME}
```