from classes.converstion import Conversation
from random import choice
import os

class MusicGen:
    
    def __init__(self):
        self.model = None
    
    
    def get_response(self, conversationObj: Conversation, prompt: str):
        responses = os.listdir("music")
        return choice(responses)