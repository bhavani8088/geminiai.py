import google.generativeai as genai

genai.configure(api_key="AIzaSyBopL8NEQVYBorUvFyu8b1zLICTruB8klU")

models = genai.list_models()

print("Available Gemini Models:\n")
for model in models:
    print(model.name)
