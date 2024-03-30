import streamlit as st

# Dummy data for the purpose of demonstration
# Assume each item in the list is a title of a conversation
conversation_titles = ["Conversation 1", "Conversation 2", "Conversation 3"]

def main():
    # Streamlit layout
    # Creating a sidebar for navigation
    st.sidebar.title("Conversations")
    selected_conversation = st.sidebar.radio("Select a conversation:", conversation_titles)

    # Main content area
    st.title("Chat Application")
    st.write(f"Selected Conversation: {selected_conversation}")

    # Prompt box in the main frame
    user_input = st.text_input("Enter your message:", key="chat_input")

    if st.button('Send'):
        # Here you would handle sending the user's message to the selected conversation
        # For demonstration purposes, we'll just display the message
        st.write(f"Your message to {selected_conversation}: {user_input}")

if __name__ == "__main__":
    main()
