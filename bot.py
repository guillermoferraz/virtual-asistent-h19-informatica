from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging
logging.basicConfig(level=logging.CRITICAL)

class Botty(object):

    def __init__(self):
        pass

    def ResponseBot(self,message):
        bot = ChatBot ('h19',
                       storage_adapter='chatterbot.storage.SQLStorageAdapter',
                       logic_adapters=['chatterbot.logic.BestMatch'],
                       database_uri='sqlite://database.sqlite3')

        bot_input = bot.get_response(message)
        return bot_input
