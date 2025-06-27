import os
from agents import RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, function_tool
import asyncio
from dotenv import load_dotenv

load_dotenv()

@function_tool
def getWeather(city):

    return f"the weather of {city} is moderate "

async def main():
    MODEL_NAME = "gemini-2.0-flash"
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        raise ValueError("Gemini Api key not found.")

    external_client = AsyncOpenAI(
        api_key=API_KEY, 
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

    model = OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=external_client)

    config = RunConfig(model=model, model_provider=external_client, tracing_disabled=True)

    assistant = Agent(name="Weather Reporting Agent", instructions="Your Task is to provide the weather related details only on the ask of the user.", model=model, 
                      
                      tools=[getWeather]
                      )

    result = await Runner.run(starting_agent=assistant, input="what is the temperature in karachi?", run_config=config)

    print(result.final_output)



if __name__ == "__main__":
    asyncio.run(main())