from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import pandas as pd

# Initialize the chatbot with a storage adapter to save the state
chatbot = ChatBot('ClassDemoBot', storage_adapter='chatterbot.storage.SQLStorageAdapter', database='db.sqlite3')

# Train with the ChatterBot English corpus
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english.greetings', 'chatterbot.corpus.english.conversations')

# Load and train with your dataset
df = pd.read_csv('qa_pairs_updated.csv')
trainer = ListTrainer(chatbot)
for index, row in df.iterrows():
    trainer.train([row['question'], row['response']])

print("Training complete! Model state saved to db.sqlite3")