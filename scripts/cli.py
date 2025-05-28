import typer, asyncio, json
from marketing_agents.pipeline import generate_post
from marketing_agents.scheduler import start_scheduler

app = typer.Typer()

@app.command()
def run(
    topic: str = typer.Option(None, help="manual topic (or leave blank to use trending)"),
    publish: bool = typer.Option(False, "--publish/--no-publish", help = "publish on social media?")
    ):
    """Generates and publishes a post."""
    res = asyncio.run(generate_post(topic))
    
    # Handle different return types
    if isinstance(res, str):
        try:
            # Try parsing if it's a JSON string
            parsed_res = json.loads(res)
            print(json.dumps(parsed_res, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            # If not valid JSON, print the string as is
            print(res)
    else:
        # If it's already a dict or other object, directly serialize it
        print(json.dumps(res, indent=2, ensure_ascii=False))

@app.command()
def schedule():
    """Inicia o agendador diário (POST_HOUR em .env)."""
    start_scheduler()

if __name__ == "__main__":
    app()