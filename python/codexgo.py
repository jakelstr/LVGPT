import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = 'Write a program in Go that takes 2 string variables, contatenates them and assigns that result to a 3rd string variable. Explicitly use variables. This code should not ask the user any questions. Declare variables with values when logical.'
model = 'text-davinci-002'

completions = openai.Completion.create(
    engine=model,
    prompt=prompt,
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