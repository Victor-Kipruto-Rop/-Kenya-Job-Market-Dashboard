import re

SKILL_KEYWORDS = [
    "python", "sql", "java", "javascript", "react", "node",
    "excel", "powerbi", "tableau", "dbt", "airflow", "kafka",
    "docker", "kubernetes", "aws", "gcp", "azure", "spark",
    "machine learning", "data engineering", "analytics",
]

def extract_skills(text: str) -> list:
    text = text.lower()
    return [skill for skill in SKILL_KEYWORDS if skill in text]

def parse_job(raw: dict) -> dict:
    return {
        "title": raw.get("title", "").strip(),
        "company": raw.get("company", "").strip(),
        "location": raw.get("location", "").strip(),
        "category": raw.get("category", "").strip(),
        "posted_date": raw.get("posted_date"),
        "scraped_at": raw.get("scraped_at"),
        "skills": extract_skills(raw.get("title", "") + " " + raw.get("category", "")),
        "is_tech": any(k in raw.get("title","").lower() for k in ["engineer","developer","analyst","data","tech"]),
    }
