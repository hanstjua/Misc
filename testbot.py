import random
import cmath
import time
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telepot.delegate import per_from_id, per_chat_id, create_open, pave_event_space, include_callback_query_chat_id

class solo(telepot.helper.UserHandler):
    def __init__(self, *args, **kwargs):
        super(solo, self).__init__(*args, **kwargs)

    def on_caht_messgae(self, msg):
        self.sender.sendMessage(msg)

class tester(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(tester, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        self.sender.sendMessage("say whut")
        solo.sender.sendMessage("I hate you")

TOKEN = "347707642:AAGeEmnFe6q-FkkV_D9V78RCk389E7Rm81Q" # NIppleskittles

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, tester, timeout=10),
    pave_event_space()(
        per_from_id(), create_open, solo, timeout=12),
])


