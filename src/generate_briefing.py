from datetime import datetime


class BriefingGenerator:
    def __init__(self, news):
        self.news = news

    def generate_full_briefing(self):
        today = datetime.now().strftime("%Y-%m-%d")

        briefing = f"""Daily AI News Briefing
Date: {today}

Focus: Healthcare AI, FDA/regulatory AI, pharma AI, LLMs, agents, AI tools, research papers, and career growth.

AI term notes:
- LLM [large language model: an AI model trained on large amounts of text that can understand and generate language]
- AI agent [an AI system that can use tools, plan steps, and complete tasks with less human instruction]
- RWE [real-world evidence: evidence generated from real-world healthcare data, such as EHR or claims data]
- Pharmacovigilance [drug safety monitoring after a drug is used in real-world settings]

Executive Summary:
Today's briefing collects AI-related news from healthcare, regulatory, pharma, and research sources. The goal is to help you track how AI is changing healthcare and what skills may matter for pharmacoepidemiology, FDA AI fellowship preparation, and healthcare AI career development.

Top AI News Items:
"""

        if not self.news:
            briefing += """
No matching AI news was found today from the current RSS sources.

Possible reasons:
1. The RSS feeds did not publish new AI-related articles today.
2. The keyword filter is too strict.
3. Some RSS feeds were temporarily unavailable.

Career Signal:
Even when no major news is found, continue learning core AI concepts such as LLMs, RAG, AI agents, model evaluation, and healthcare AI validation.

Today's 30-minute action:
Read one FDA page or paper about AI/ML-enabled medical products or AI in regulatory science.
"""
            return briefing

        for i, article in enumerate(self.news, 1):
            briefing += f"""
{i}. {article.get("title", "No title")}
Source: {article.get("source", "Unknown")}
Link: {article.get("link", "")}

Summary:
{article.get("summary", "No summary available")[:500]}

Why it matters:
This may be relevant to healthcare AI, regulatory science, pharma, clinical research, or AI-enabled decision-making.

Why it matters for you:
This helps you understand how AI may affect pharmacoepidemiology, real-world evidence, FDA AI fellowship preparation, and healthcare AI career opportunities.

Key AI terms:
AI [artificial intelligence: computer systems designed to perform tasks that usually require human intelligence]
Machine learning [a type of AI where models learn patterns from data]
"""

        briefing += """

Healthcare/Pharma/FDA Deep Dive:
The most important pattern to watch is how AI tools are moving from general technology into regulated healthcare settings. For someone with an epidemiology and RWE background, the key question is not only whether an AI model works, but whether it is valid, reproducible, fair, clinically useful, and safe.

Career Signal:
You should prioritize learning:
1. Python basics for data and APIs
2. LLMs [large language models]
3. RAG [retrieval-augmented generation: an AI method that searches trusted documents before answering]
4. AI model evaluation
5. FDA AI/ML regulatory concepts
6. Healthcare data standards and real-world evidence methods

Today's 30-minute action:
Pick one AI term from this email and write a 3-sentence explanation using a healthcare example.
"""

        return briefing
