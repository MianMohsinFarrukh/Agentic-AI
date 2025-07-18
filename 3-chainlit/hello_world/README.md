repo Link = https://github.com/panaversity/learn-agentic-ai
api Link = https://aistudio.google.com/

0- create folder and cd > folder  .

              ****************** UV & Virtusl env   ******************

1- uv init .       install uv pakge first .
2- uv venv         add virtual environment .
3- .venv\Scripts\activate   activate virtual env .
4- uv run explore-uv        uv.lock file create .




               ****************** FOR CHAINLIT   ******************

5. **Installation (Chainlit):**
```bash
uv add chainlit
```

6. **Check Chainlit:**
```bash
uv run chainlit hello
```

7. **Run Main File:**
```bash
uv run chainlit run chatbot.py -w
```


DECORATORS:

@on_chat_start    // New Chat Session.
@on_message       // New Message from the User.    
@on_stop          // User Clicks the stop Button.
@on_chat_resume   // User Continue the chat Session.
@on_chat_end      // User disconnected or started new session.












8- .env                     create .env file for api .
9- GEMINI_API_KEY=your api key  //set .env file 

                   ****************** FOR AGENTS  ******************
10- uv add openai-agents
11- 




