print('Ask anything to the AI automated chatbot - ChatGPT')

import openai
openai.api_key = '<enter-your-own-OpenAI-API>'
messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]

ask=input('\n\nEnter your query here: ')
while len(ask)!=0:
	print('\n')
	message = ask
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})
	ask=input('\n\nEnter your query here: ')

print('\n\nChatGPT: I think your queries are done for now, happy to help\n\n')


