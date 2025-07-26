import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, function_tool, Tool
from agents.run import RunConfig

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
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


# ✅ Custom simple search tool (replace with real API or scraping later)
class FreeWebSearchTool(Tool):
    name = "free_web_search"
    description = "Performs a basic web search and returns mock data from LinkedIn."

    def call(self, query: str) -> str:
        # In real implementation, call a free search API or scraping
        return f"Mock LinkedIn result for: {query} — [LinkedIn Profile of Muhammad Ubaid Hussain, Software Engineer]"

    def to_openai_tool(self):
        return None  # Not required for Gemini


rishtey_wali_agent = Agent(
    name="Auntie",
    model="gemini-1.5-flash-latest",
    instructions="You are a warm and wise 'Rishtey Wali Auntie' who helps people find matches.",
    tools=[get_user_data, FreeWebSearchTool()]
)

result = Runner.run_sync(
    starting_agent=rishtey_wali_agent,
    input="find a match of 25 minimum age and tell me the details about the match from linkedin"
)

print(result.final_output)
