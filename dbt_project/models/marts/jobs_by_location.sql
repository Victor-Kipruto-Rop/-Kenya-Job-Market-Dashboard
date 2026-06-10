SELECT
    city,
    COUNT(*) AS total_postings,
    COUNT(*) FILTER (WHERE is_tech) AS tech_postings,
    ROUND(COUNT(*) FILTER (WHERE is_tech)::numeric / NULLIF(COUNT(*),0) * 100, 1) AS tech_pct
FROM {{ ref('int_jobs_cleaned') }}
GROUP BY city
ORDER BY total_postings DESC
