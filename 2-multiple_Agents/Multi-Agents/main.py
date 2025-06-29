import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner
from agents.run import RunConfig


# Load the environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

backend_agent = Agent(
    name="Backend Expert",
    handoff_description="Specialist agent for Backend Development",
    instructions="You are a backend development expert. Help users with backend topics.",
    model=model
)

frontend_agent = Agent(
    name="Frontend Expert",
    handoff_description="Specialist agent for frontend Development",
    instructions="You are a frontend expert. Help users with frontend topics.",
    model=model
)

web_dev_agent = Agent(
    name="Web Developer Agent",
    handoffs=[frontend_agent, backend_agent],
    instructions="Route the question to the appropriate agent.", 
    model=model
)

user_question = input("Enter your question: ")
 
 
try:
    result = Runner.run_sync(web_dev_agent, user_question, run_config=config)
    print("Result:", result.final_output)
    #print("agent response:", result.last_agent.name)
except Exception as e:
    print("Error:", e)


