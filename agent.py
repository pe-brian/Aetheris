from ollama import chat, ChatResponse

context = [
  "This is a web page screenshot",
  "Your goal is to categorize the web page items"
  "Each item can only have one category : an URL, a button or a field",
  "A field is composed of a label and a value, you must format it like this : '<label>|<value>'",
  # "You can identify a field by its value",
  # "A field is composed of a label and a value",
  # "For fields, you must associate the right label with the right value",
  "You must identify the items present in the screenshot",
  "Don't introduce, translate, format, nor comment the result",
  "If you list something, separate items with comma",
  "If you don't find something, return 'None'",
  "Wait for the user to ask you something"
]

questions = [
  'Return the URL',
  'Return the buttons',
  'Return the inputs fields.'
]
items = [
  'URL',
  'buttons',
  'fields'
]
res = {}

for item, question in zip(items, questions):
  response: ChatResponse = chat(model='llama3.2-vision:11b', options={"temperature": 0.0}, messages=[
    {
      'role': 'user',
      'content': ". ".join(context) + "\n\n" + question,
      "images": ["./input/0.png"]
    },
  ])
  print(response.message.content)
  content = response.message.content.strip(".")
  res[item] = None if content == "none" else [x.strip("'").strip() for x in content.split(",")]

print(res)
