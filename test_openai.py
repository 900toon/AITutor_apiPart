from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a soilder can only response any scentence with 'yea sir' as beginning"},
    {"role": "user", "content": "Are you ready? reply me"}
  ]
)


print(completion.choices[0].message)

with open("testting1.txt", "w") as f:
  f.write("message0: ")
  f.write(completion.choices[0].message.content)
  

