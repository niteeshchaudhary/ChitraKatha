"""
A Chat class designed to handle elements of a conversation, including text, images, and music.
"""

class Chat:
    """
    A Chat class designed to handle elements of a conversation, including text, images, and music.
    
    Attributes:
        request (str): The request message in the conversation.
        response (str): The response message in the conversation.
        image (str): The URL or path to an image related to the conversation.
        music (str): The URL or path to a music file related to the conversation.
        conversation_id (str): A unique identifier for the conversation.
    """

    def __init__(self, conversation_id: str) -> None:
        """
        Initializes a new instance of the Chat class.
        
        Parameters:
            conversation_id (str): A unique identifier for the conversation.
        """
        self.request: str | None = None  # Initially, there's no request message
        self.response: str | None = None  # Initially, there's no response message
        self.image: str | None = None  # Initially, there's no image associated with conversation
        self.music: str | None = None  # Initially, there's no music associated with conversation
        self.conversation_id: str = conversation_id  # A unique identifier for the conversation
