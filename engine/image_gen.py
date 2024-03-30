import os


from classes.converstion import Conversation
from random import choice

class ImageGen:
    
    def __init__(self):
        self.model = None
    
    
    def get_response(self, conversationObj: Conversation, prompt: str):
        responses = os.listdir("images")
        return choice(responses)