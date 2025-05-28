import asyncio, json, os
from datetime import date
from .agents import make_search_agent, make_planner_agent, make_writer_agent, make_reviewer_agent, call_agent
from .image_generator import generate_image
from .publisher import publish
from .prompts import SEARCH_PROMPT

async def generate_post(topic: str | None = None, publish_post: bool = False):
    # 1) Trend Spotter - default topic: "Marketing"
    topic = topic or "Marketing"
    searcher = make_search_agent(topic=topic)
    insights = await call_agent(searcher, f"Topic: {topic}\n")

    # 2) Plann
    planner = make_planner_agent()
    plan_json = await call_agent(
        planner, 
        f"Topic: {topic}\n\nInsights:\n{insights}\n"
    )

    # 3) Write
    writer = make_writer_agent()
    draft = await call_agent(writer, plan_json)

    # 4) Review
    reviewer = make_reviewer_agent()
    reviewed = await call_agent(reviewer, draft)
    if reviewed.strip().upper() == "APPROVED":
        reviewed = draft  # No changes needed

    # 5) Generate image
    img_url = generate_image(f"generate image: {topic} illustration flat minimal style")

    # Publish
    if publish_post:
        print("Publishing...")
        publish(reviewed, img_url)

    # save to history
    fname = f"src/marketing_agents/outputs/posts/{date.today():%Y-%m-%d}_{topic.lower().replace(' ','_')}.md"
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    with open(fname, "w", encoding="utf-8") as f:
        try:
            data = json.loads(reviewed)
            f.write(f"# {topic}\n\n## Instagram\n{data['instagram']}\n\n![img]({img_url})\n\n## LinkedIn\n{data['linkedin']}\n")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print(f"Raw response: {reviewed}")
            # Fallback to save raw content
            f.write(f"# {topic}\n\n## Raw Content\n{reviewed}\n\n![img]({img_url})\n")
    print("saved", fname)

    return reviewed