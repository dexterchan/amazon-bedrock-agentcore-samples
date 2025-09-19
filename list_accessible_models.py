import boto3
from botocore.config import Config

AWS_REGION="us-east-1"

my_config = Config(
    region_name = AWS_REGION
)

def list_accessible_models():
    """List only Bedrock models you have access to, excluding Claude"""
    bedrock = boto3.client('bedrock', config=my_config)
    
    try:
        # Get models with access granted
        response = bedrock.list_foundation_models(
            byOutputModality='TEXT',
            byInferenceType='ON_DEMAND'
        )
        
        accessible_models = []
        
        for model in response['modelSummaries']:
            model_id = model['modelId']
            
            
            # Check if model is accessible by trying to get model info
            try:
                bedrock.get_foundation_model(modelIdentifier=model_id)
                accessible_models.append(model)
            except Exception:
                # Model not accessible, skip it
                continue
        
        print("Accessible Bedrock Models:")
        print("-" * 60)
        
        if not accessible_models:
            print("No accessible models found (excluding Claude)")
            return
            
        for model in accessible_models:
            model_id = model['modelId']
            model_name = model.get('modelName', 'N/A')
            provider = model.get('providerName', 'N/A')
            
            # Highlight Nova models
            if 'nova' in model_id.lower():
                print(f"🌟 {model_id} ({provider} - {model_name})")
            else:
                print(f"   {model_id} ({provider} - {model_name})")
                
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_accessible_models()