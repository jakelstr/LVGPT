import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
#prompt = 'Write a program in Go that  Explicitly use variables. This code should not ask the user any questions. Declare variables with values when logical.'
prompt = 'write a go program that uses a switch statement to convert a string charachter to a number, with a=1, b=2 and so on'
promptTail = ' Do not ask the user questions. Prepopulate any needed values. Any values that a user would enter should be their own variables.'
model = 'text-davinci-002'

completions = openai.Completion.create(
    engine=model,
    prompt=prompt + promptTail,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0,
)

answer = completions.choices[0].text
print(answer)

file = open("python/codexout.go", "w+")
file.write(answer)
file.close()