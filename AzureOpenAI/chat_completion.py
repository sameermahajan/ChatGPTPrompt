import openai
import sys

openai.api_type = "azure"
openai.api_base = <your org URL>
openai.api_version = "2023-05-15"
openai.api_key = <your token>
engine = <your deployment>
print(engine, openai.api_type, openai.api_key, openai.api_base, openai.api_version, openai.organization)
response = openai.ChatCompletion.create(
    engine=engine, # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
    messages=[
        {"role": "system", "content": "You are blah blah"},
        {"role": "user", "content": sys.argv[1]} # your query
    ]
)

print(response)

print(response['choices'][0]['message']['content'])
