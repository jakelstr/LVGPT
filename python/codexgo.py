import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
#prompt = 'Write a program in Go that  Explicitly use variables. This code should not ask the user any questions. Declare variables with values when logical.'
prompt = 'Write a Go program that takes an array of strings, and appends an element to the end "x number of elements" where x was the number of elements intially.  This code will be processed to convert into a labview VI, so write the code in a way to facilitate that. Becase the code will be converted to a GUI environment, do not rely on console based input for values. Do not ask the user questions. Prepopulate any needed values.'
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