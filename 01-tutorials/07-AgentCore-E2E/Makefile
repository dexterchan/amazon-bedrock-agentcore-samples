.IPHONY: init

AWS_ACCOUNT := $(shell aws sts get-caller-identity --query Account --output text)
REGION := us-east-1

init:
	uv venv -p python3.12 .venv
	source .venv/bin/activate && uv pip install -U -r requirements.txt -q

mock-delete-bucket:
	aws s3vectors list-indexes --vector-bucket-name ${AWS_ACCOUNT}-${REGION}-kb-vector-bucket --region ${REGION}
	
delete-vector-bucket:
	aws s3vectors list-indexes --vector-bucket-name ${AWS_ACCOUNT}-${REGION}-kb-vector-bucket --region ${REGION}

	aws s3vectors delete-index --vector-bucket-name ${AWS_ACCOUNT}-${REGION}-kb-vector-bucket --index-name ${AWS_ACCOUNT}-${REGION}-kb-vector-index --region ${REGION}

	aws s3vectors delete-vector-bucket \
	--vector-bucket-name "${AWS_ACCOUNT}-${REGION}-kb-vector-bucket"
