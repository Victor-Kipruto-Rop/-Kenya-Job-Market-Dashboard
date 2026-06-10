SELECT
    job_title,
    COUNT(*) AS total_postings,
    COUNT(DISTINCT company_name) AS unique_companies,
    ROUND(AVG(skill_count)::numeric, 1) AS avg_skills_required
FROM {{ ref('int_jobs_cleaned') }}
GROUP BY job_title
ORDER BY total_postings DESC
LIMIT 50
