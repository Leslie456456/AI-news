# AI News Briefing

This repository automatically generates and sends a daily AI news briefing focused on healthcare AI, FDA/regulatory AI, pharma AI, real-world evidence, drug safety, clinical research, LLMs, AI agents, AI tools, business/startups, research papers, and career development.

The goal of this project is to help me stay updated on how AI is changing healthcare, pharma, regulatory science, and future career opportunities in healthcare AI.

---

## What This Project Does

Every day, this project:

1. Collects AI-related news from selected online sources
2. Filters news based on healthcare, FDA, pharma, RWE, and AI-related keywords
3. Generates a personalized daily briefing
4. Explains important AI terms in beginner-friendly language
5. Connects each news item to my interests in pharmacoepidemiology, real-world evidence, FDA AI fellowship preparation, and healthcare AI career growth
6. Sends the briefing to my email using Gmail

---

## Main Topics Covered

The briefing focuses on:

- Healthcare AI
- FDA and regulatory AI
- Pharma AI
- Pharmacovigilance and drug safety
- Real-world evidence and clinical research
- LLMs [large language models]
- AI agents
- AI tools for professional work
- AI business and startup news
- AI research papers
- AI policy, safety, and governance
- English and Chinese AI developments when relevant

---

## Project Structure

```text
AI-news/
├── .github/workflows/
│   └── daily-briefing.yml      # GitHub Actions workflow for automatic daily runs
├── src/
│   ├── __init__.py             # Makes src a Python module
│   ├── main.py                 # Main script that runs the full workflow
│   ├── fetch_news.py           # Collects news from RSS sources
│   └── generate_briefing.py    # Creates the daily briefing text
├── README.md                   # Project documentation
├── CUSTOMIZE.md                # Notes for customization
└── requirements.txt            # Python package dependencies
