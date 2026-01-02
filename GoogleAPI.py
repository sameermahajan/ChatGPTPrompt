import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-pro")

response = model.generate_content(
    "Write a short story set in Pune",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 200
    },
    system_instruction="You are a local Pune expert"
)

print(response.text)
