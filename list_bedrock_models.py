import boto3
from botocore.config import Config

AWS_REGION="us-east-1"

my_config = Config(
    region_name = AWS_REGION
)

def list_bedrock_models():
    """List all available Bedrock foundation models"""
    bedrock = boto3.client('bedrock', config=my_config)
    
    try:
        response = bedrock.list_foundation_models()
        models = response['modelSummaries']
        
        print("Available Bedrock Models:")
        print("-" * 50)
        
        for model in models:
            model_id = model['modelId']
            model_name = model.get('modelName', 'N/A')
            provider = model.get('providerName', 'N/A')
            
            # Filter for Nova models if you're specifically interested
            if 'nova' in model_id.lower():
                print(f"🌟 {model_id} ({provider} - {model_name})")
            else:
                print(f"   {model_id} ({provider} - {model_name})")
                
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_bedrock_models()