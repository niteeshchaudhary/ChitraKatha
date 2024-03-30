"""
A Conversation class that aggregates multiple Chat instances into a conversation.
"""

from classes.chat import Chat

class Conversation:
    """
    A Conversation class that aggregates multiple Chat instances into a conversation.
    
    This class is responsible for managing a collection of chats that together 
    form a complete conversation identified by a unique conversation ID.
    
    Attributes:
        conversation_id (str): A unique identifier for the conversation.
        title (str): The title of the conversation.
        conversation (list[Chat]): A list to store instances of Chat associated with this 
                                        conversation.
    """

    def __init__(self, conversation_id: str) -> None:
        """
        Initializes a new instance of the Conversation class.
        
        Parameters:
            conversation_id (str): A unique identifier for the conversation.
        """
        self.conversation_id: str = conversation_id  # Unique identifier for the conversation
        self.title: str | None = None # Initially, there's no title for the conversation
        self.conversation: list[Chat] = []  # Initializes an empty list to hold Chat instances
