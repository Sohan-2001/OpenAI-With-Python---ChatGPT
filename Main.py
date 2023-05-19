

from pickle import NONE
import openai
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()



print('Ask anything to the AI automated chatbot - Sohan')
SpeakText('Ask anything to the AI automated chatbot - Sohan')
print('\nYou can write your query or speak to search, Do you like writing or rely upon voice assistant? ')
SpeakText('You can write your query or speak to search, Do you like writing or rely upon voice assistant? ')


def Listen(MyText,Check,ask):
	x=input('\nIf you want to type your query then type here  or avoid this and press ENTER: ')
	if len(x)!=0:
		Check='YES'
		ask=x
		return ask

	while(Check=='NO'):

		
	
		# Exception handling to handle
		# exceptions at the runtime
		try:
		
			# use the microphone as source for input.
			with sr.Microphone() as source2:
			
				# wait for a second to let the recognizer
				# adjust the energy threshold based on
				# the surrounding noise level					
				r.adjust_for_ambient_noise(source2, duration=1.0)
			
				#listens for the user's input
				print('\nNow Speak...listening...\n')
				audio2 = r.listen(source2)
				# Using google to recognize audio

				print('\n...Recognizing...\n\n...Fetching informations from database...\n\n')
				MyText = r.recognize_google(audio2)
				quitLoop=0
				while quitLoop==0:

					print('Do you want to search [',MyText,'] ? If yes, speak YES, or speak NO to speak your search query again')
					r.adjust_for_ambient_noise(source2, duration=1.0)
					audio2 = r.listen(source2)
					Check=r.recognize_google(audio2)
					if Check.upper()=='YES':
						ask=MyText
						return ask
					elif Check.upper()=='NO':
						Listen('Hello','NO','Hello')
						quitLoop=1
					else:
						quitLoop=0


				

			
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
			ask=MyText
			return ask
		
		except sr.UnknownValueError:
			print("unknown error occurred")
			ask=MyText
			return ask



openai.api_key = '<Your_Own_API_Key>'
messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]


Ask=str(Listen('Hello','NO','Hello'))

while Ask!='NONE':
	print('\n')
	message = Ask
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"Sohan: {reply}")
	SpeakText(reply)
	messages.append({"role": "assistant", "content": reply})
	Ask=str(Listen('Hello','NO','Hello'))





print('\n\nSohan: I think your queries are done for now, happy to help\n\n')
SpeakText('I think your queries are done for now, happy to help')



