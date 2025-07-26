import os
import requests
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, function_tool, Tool
from agents.run import RunConfig

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

if not serper_api_key:
    raise ValueError("SERPER_API_KEY is not set in .env")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash-latest",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

@function_tool
def get_user_data(min_age: int) -> list[dict]:
    "Retrieve user data based on a minimum age"
    users = [
        {"name": "Muneeb", "age": 22},
        {"name": "Muhammad Ubaid Hussain", "age": 25},
        {"name": "Azan", "age": 19},
    ]
    return [user for user in users if user["age"] >= min_age]

# ✅ Serper.dev Web Search Tool
class SerperWebSearchTool:
    name = "serper_web_search"
    description = "Performs a web search using Serper.dev and returns top result."

    def call(self, query: str) -> str:
        url = "https://google.serper.dev/search"
        headers = {"X-API-KEY": serper_api_key}
        payload = {"q": query}

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        if "organic" in data and data["organic"]:
            top = data["organic"][0]
            return f"{top['title']}\n{top['link']}\n{top.get('snippet', '')}"
        else:
            return "No search results found."


# ✅ Agent Setup
rishtey_wali_agent = Agent(
    name="Auntie",
    model="gemini-1.5-flash-latest",
    instructions="You are a warm and wise 'Rishtey Wali Auntie' who helps people find matches and finds LinkedIn info.",
    tools=[get_user_data, SerperWebSearchTool()]
)

# ✅ Run Agent
result = Runner.run_sync(
    starting_agent=rishtey_wali_agent,
    input="find a match of 25 minimum age and tell me the details about the match from linkedin"
)

print(result.final_output)
