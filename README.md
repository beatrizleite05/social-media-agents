# Social Media Agents

An AI-powered multi-agent system that automatically discovers marketing trends and creates relevant content for social media platforms.

## Project Overview

This project automates the entire content creation pipeline for marketing posts on Instagram and LinkedIn. It leverages specialized AI agents to research current trends, plan engaging content, and generate platform-optimized posts with accompanying images.

### Key Features

- Automated discovery of recent marketing trends and innovations
- Smart content planning based on relevant industry insights
- Platform-specific content generation for Instagram and LinkedIn
- AI-powered image generation for visual content
- Content review for quality assurance
- Scheduled or on-demand content creation
- Optional direct publishing to social media platforms

## Technologies Used

- **Google ADK**: Framework for creating specialized AI agents with different roles
- **Google Generative AI**: Large language model powering the content generation
- **APScheduler**: For scheduling automated daily posts
- **Vyro.ai API**: For generating custom images for social posts
- **Requests**: For API interactions with social platforms and image services
- **Typer**: CLI interface for manual execution and scheduling
- **Python-dotenv**: For managing environment variables and API keys

## Architecture

The system uses a multi-agent pipeline:

1. **Trend Spotter**: Researches recent marketing developments via Google Search
2. **Content Planner**: Analyzes insights and creates strategic content plans
3. **Content Writer**: Generates platform-specific posts optimized for each network
4. **Content Reviewer**: Reviews for quality, tone, and appropriateness
5. **Image Generator**: Creates relevant visuals to accompany posts

## Installation
```
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

## Run manually
```
python -m scripts.cli run --topic "IA no Ads"
```

## Schedule (daily post 15h)
```
python -m scripts.cli schedule
```

## Configuration

Configure your API keys and social media credentials in the `.env` file:

- Google API key for search and generative AI
- Instagram and LinkedIn credentials
- Vyro.ai API key for image generation# social-media-agents
