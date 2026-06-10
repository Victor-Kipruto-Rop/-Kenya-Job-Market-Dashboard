SELECT
    id,
    INITCAP(TRIM(title)) AS job_title,
    INITCAP(TRIM(company)) AS company_name,
    INITCAP(TRIM(location)) AS location,
    INITCAP(TRIM(category)) AS category,
    posted_date,
    scraped_at,
    skills,
    is_tech
FROM raw_jobs
WHERE title IS NOT NULL
