# Responses API

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)


# Chat Completion

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4.1",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)


# Legacy Completions

from openai import OpenAI
client = OpenAI()

client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)
