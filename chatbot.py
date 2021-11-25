from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'Chatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sinto muito, mas eu não estou entendendo. Eu ainda estou aprendendo.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training with Personal Ques & Ans
training_data_quesans = open('training_data/ques_ans.txt',encoding='utf-8').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt', encoding= 'utf-8').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)


