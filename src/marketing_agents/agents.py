from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from .prompts import SEARCH_PROMPT, PLANNER_PROMPT, WRITER_PROMPT, REVIEW_PROMPT
from .tools import build_search_tool
from .config import DEFAULT_MODEL

session_service = InMemorySessionService()

def make_search_agent(topic: str):
    return Agent(
        name="Trend_Spotter",
        model=DEFAULT_MODEL,
        instruction=SEARCH_PROMPT.format(topic=topic),
        tools= [build_search_tool()]
    )

def make_planner_agent():
    return Agent(
        name="Content_Planner",
        model=DEFAULT_MODEL,
        instruction=PLANNER_PROMPT,
        tools=[build_search_tool()]
    )

def make_writer_agent():
    return Agent(
        name="Content_Writer",
        model=DEFAULT_MODEL,
        instruction=WRITER_PROMPT
    )

def make_reviewer_agent():
    return Agent(
        name="Content_Reviewer",
        model=DEFAULT_MODEL,
        instruction=REVIEW_PROMPT
    )


async def call_agent(agent: Agent, message_text: str) -> str:
    # Create session with fixed user ID
    session = await session_service.create_session(app_name=agent.name, user_id="user1")
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)

    # Set up the message as a user content part
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    async for event in runner.run_async(user_id="user1", session_id=session.id, new_message=content):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text:
                    final_response += part.text + "\n"

    return final_response.strip()