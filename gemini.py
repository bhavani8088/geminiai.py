import google.generativeai as genai

# Paste your API key between the quotes
genai.configure(api_key="AIzaSyB-wv_BtNPuDPx8nyg2oLUg9f8sLMeK_Lk")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Hello Gemini")

print(response.text)
genai.configure(api_key=“ABC123”)
import google.generativeai as genai

import google.generativeai as genai

genai.configure(api_key="AIzaSyB-wv_BtNPuDPx8nyg2oLUg9f8sLMeK_Lk")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Hello Gemini")

print(response.text)
