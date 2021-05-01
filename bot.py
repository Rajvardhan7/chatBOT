import pandas as pd
import numpy as np
import streamlit as st
import math

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer 
import json

cbot = ChatBot('RAj', read_only = False,preprocessors=['chatterbot.preprocessors.clean_whitespace',\
               'chatterbot.preprocessors.convert_to_ascii','chatterbot.preprocessors.unescape_html'],\
               logic_adapters = ['chatterbot.logic.MathematicalEvaluation',\
                                 'chatterbot.logic.BestMatch'])

#data input
data = json.loads(open(r'data_tolokers.json','r').read()) #change path accordingly

def get_text():
    input_text = st.text_input("You: ","So, what's in your mind")
    return input_text



tra = []
for k, row in enumerate(data):
    #print(k)
    tra.append(row['dialog'][0]['text'])
    
st.sidebar.title("NLP Bot")
st.title(""" chatbot""")

ind = 1
if st.sidebar.button('Initialize bot'):
    st.write('training in')
    # Create a new trainer for the chatbot
    trainer2 = ListTrainer(cbot) 
    trainer2.train(tra)

    st.title("Your bot is ready to talk to you")
    ind = ind +1

user_input = get_text()

if True:
    st.text_area("Bot:", value=cbot.get_response(user_input), height=200, max_chars=None, key=None)
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)









