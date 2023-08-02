import openai
import sys

openai.api_type = "azure"
openai.api_base = <your org URL>
openai.api_version = "2022-12-01"
openai.api_key = <your token>
engine = <your deployment>
print(engine, openai.api_type, openai.api_key, openai.api_base, openai.api_version, openai.organization)
codex_query=sys.argv[1] # <your query>
response = openai.Completion.create(engine=engine, prompt=codex_query, stop="#")
print (response)
print (response['choices'][0]['text'])
