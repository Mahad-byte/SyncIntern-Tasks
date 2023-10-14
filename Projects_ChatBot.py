import json
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initializing
chatbot = chatterbot.ChatBot("ChatBot")
trainer = ListTrainer(chatbot)

# Training on some common gestures in json file
with open("intents.json", "r") as dataset:
    intents_data = json.load(dataset)

for intents in intents_data['intents']:
    patterns = intents['patterns']
    responses = intents['responses']
    for pattern in patterns:
        trainer.train([pattern])

# Training on built in data
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')

while True:
    print("Press '0' to exit")
    question = input("Enter Your Query: ")
    response = chatbot.get_response(question)
    if question == "0":
        break
    else:
        print(chatbot.get_response(question))

