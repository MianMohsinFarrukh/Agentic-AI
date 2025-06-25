import chainlit as cl

@cl.on_chain_start
async def handle_chat_start():
    await cl.Message(
        content="Welcome to the chatbot! How can I assist you today?",
    ).send()



@cl.on_message        
async def main(message: cl.Message): 
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()


# Our custom logic goes here...
# Send a fake response back to the user