# Customization Guide: Advanced Configuration

## 📋 Overview

This guide covers advanced customization options for your AI News Briefing system.

---

## ⏰ Change Schedule/Time

### Current Schedule: Daily at 9:00 PM UTC

### To modify:

1. Open `.github/workflows/daily-briefing.yml`
2. Find this line (line 5):
   ```yaml
   - cron: '0 21 * * *'  # 9:00 PM UTC daily
   ```

3. Change the cron value. Examples:
   - `0 13 * * *` = 1:00 PM UTC (13:00)
   - `0 9 * * *` = 9:00 AM UTC
   - `0 21 * * 1-5` = 9:00 PM UTC, Monday-Friday only
   - `0 */6 * * *` = Every 6 hours

4. **Cron format:** `minute hour day month day-of-week`
   - Use [crontab.guru](https://crontab.guru/) for help

---

## 📰 Add/Remove News Sources

### Current sources included:
- FDA News (regulatory)
- arXiv (AI research)
- Nature Machine Intelligence
- The Lancet Digital Health
- medRxiv (medical research)
- JAMA Network
- Stat News
- Biopharmguy (pharma)

### To customize:

1. Edit `src/fetch_news.py` method `get_default_sources()`
2. Add or remove sources:
   ```python
   {
     "name": "Source Name",
     "url": "https://example.com/rss",
     "category": "healthcare-ai",
     "priority": 5,
     "active": True
   }
   ```

3. Categories:
   - `healthcare-ai` - AI in medicine
   - `regulatory` - FDA, regulatory science
   - `pharma` - Pharmaceutical industry
   - `ai-research` - AI research papers
   - `medical-research` - Medical studies
   - `clinical-research` - Clinical research

---

## 🔑 Modify Keywords & Filters

### Current keywords target:
- Healthcare AI, medical AI
- FDA, regulatory, drug approval
- Drug safety, pharmacovigilance
- Clinical trials, RWE
- LLMs, RAG, AI agents
- Career opportunities

### To customize:

1. Edit `src/fetch_news.py` method `get_default_keywords()`
2. Modify keyword groups:
   ```python
   {
     "category": "healthcare-ai",
     "keywords": ["healthcare AI", "medical AI", "clinical AI"],
     "weight": 5,
     "active": True
   }
   ```

3. Higher weight = higher priority in results

---

## 📧 Change Email Settings

### Recipient email:
- **Change from:** lesuiuedu@gmail.com → your preferred email
- **How:** Update GitHub Secret `EMAIL_ADDRESS`
  1. Go to Settings → Secrets → Actions
  2. Edit `EMAIL_ADDRESS`
  3. Save

### Email subject format:
- **Current:** `[AI News Briefing] Daily Update - YYYY-MM-DD`
- **To change:** Edit `src/send_email.py` line ~20

---

## 🎯 Customize Briefing Format

### Current sections:
1. Executive summary (3-5 sentences)
2. Top news table (8 stories)
3. Healthcare/pharma deep dive
4. AI learning concept
5. Career signal
6. Action item

### To modify sections:

1. Open `src/generate_briefing.py`
2. Edit methods like:
   - `generate_executive_summary()`
   - `generate_top_news_table()`
   - `generate_deep_dive()`
   - etc.

3. Save and manually test workflow

---

## 🧪 Testing Changes Locally

### Before deploying to automation:

1. Clone repository:
   ```bash
   git clone https://github.com/Leslie456456/AI-news.git
   cd AI-news
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set environment variables:
   ```bash
   export EMAIL_ADDRESS="lesuiuedu@gmail.com"
   export EMAIL_APP_PASSWORD="your_16_char_password"
   ```

4. Test locally:
   ```bash
   python -c "from src.fetch_news import NewsAggregator; agg = NewsAggregator(); news = agg.fetch_all_news(); print(f'Fetched {len(news)} articles')"
   ```

5. Once working, commit and push to trigger workflow

---

## 💡 Best Practices

✅ **Do:**
- Test changes locally before deploying
- Keep GitHub Secrets secure
- Document any custom modifications
- Monitor workflow runs regularly
- Update sources periodically for quality

❌ **Don't:**
- Share GitHub Secrets publicly
- Add low-quality sources
- Overload with too many keywords
- Schedule too frequently (risk of API limits)
- Hardcode sensitive information

---

## 📊 Monitor Performance

### Track workflow runs:
1. Go to **Actions** tab
2. See **Daily AI News Briefing** workflow
3. Check run history, logs, and success rate

### View email delivery:
1. Check Gmail sent folder for confirmation
2. Verify email receipt daily
3. Report issues via repository Issues tab

---

## 🆘 Need Help?

- **Cron scheduling:** [crontab.guru](https://crontab.guru/)
- **GitHub Actions:** [docs.github.com/en/actions](https://docs.github.com/en/actions)
- **Python:** [python.org/doc](https://www.python.org/doc/)

---

**Happy customizing! 🚀**
