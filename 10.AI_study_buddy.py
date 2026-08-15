#Ai ChatBot
import datetime
import time

name = input("enter your name: ")
present_time = datetime.datetime.now().hour

if 5 <= present_time <=11:
  print("Good Morning, ",name)
elif 11 <= present_time <=17:
  print("Good Afternoon, ",name)
elif 17<= present_time <= 20:
  print("Good Evening, ",name)
else:
  print("Good Night, ",name)


print("namaste! Welcome to Ai Chatbot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

#Chatbot Memory Creation [Dictionary of responses ]

responses = {
  "hello":"Hi,Welcome. How can I help You?",
  "how are you":"I am very fine.Thank you",
  "who are you":"I am smart AI chatbot",
  "motivate me":"Keep goind. Every bug of your project makes you a better coder",
  "happy":"Great to hear that"
}
#Method/Function to get response of ChatBot

def get_reponse_of_bot(user_Question):
  user_Question = user_Question.lower()
  for each_key in responses:
    if each_key in user_Question:
      return responses[each_key]

  return "I am nto able to tell that yet. I am still in learning mode"

#take user input
while True:
  user_input = input("Please ask your question: ")
  reply = get_reponse_of_bot(user_input)
  print(f"Bot Response:{reply}")

  if "bye" in user_input.lower():
    break