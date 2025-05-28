import pytest, asyncio, json
from marketing_agents import agents as ag, image_generator as ig
from marketing_agents.pipeline import generate_post

class DummyAgent:
    def __init__(self, txt): self.txt = txt
    async def run(self, *_):
        class R: text = self.txt
        return R()

@pytest.mark.asyncio
async def test_full(monkeypatch):
    monkeypatch.setattr(ag, "make_search_agent",  lambda: DummyAgent("##AI Marketing - hot"))
    monkeypatch.setattr(ag, "make_planner_agent", lambda: DummyAgent("{\"topic\":\"AI\"}"))
    monkeypatch.setattr(ag, "make_writer_agent",  lambda: DummyAgent("{\"instagram\":\"ig\", \"linkedin\":\"ln\"}"))
    monkeypatch.setattr(ag, "make_reviewer_agent", lambda: DummyAgent("APROVADOS"))
    monkeypatch.setattr(ig, "generate_image", lambda *_: "https://example.com/img.png")
    import marketing_agents.publisher as pub
    monkeypatch.setattr(pub, "publicar", lambda *_: None)

    res = await generate_post()
    data = json.loads(res)
    assert data["instagram"] == "ig"