import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyC3STCle_oIovKZE05bJjNq6uCXrowH0Ao"

# Configure API key
genai.configure(api_key=API_KEY)

# List available models
models = genai.list_models()

print("Available Gemini Models:")
for model in models:
    print(model.name)
