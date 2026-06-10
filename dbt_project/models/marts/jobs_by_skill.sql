SELECT
    skill,
    COUNT(*) AS job_count
FROM {{ ref('int_jobs_cleaned') }},
     UNNEST(skills) AS skill
GROUP BY skill
ORDER BY job_count DESC
