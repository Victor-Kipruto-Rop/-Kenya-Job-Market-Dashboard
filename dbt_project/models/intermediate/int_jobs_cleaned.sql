SELECT
    id,
    job_title,
    company_name,
    CASE
        WHEN location ILIKE '%nairobi%' THEN 'Nairobi'
        WHEN location ILIKE '%mombasa%' THEN 'Mombasa'
        WHEN location ILIKE '%kisumu%' THEN 'Kisumu'
        WHEN location ILIKE '%eldoret%' THEN 'Eldoret'
        ELSE 'Other'
    END AS city,
    category,
    scraped_at,
    skills,
    is_tech,
    CARDINALITY(skills) AS skill_count
FROM {{ ref('stg_jobs') }}
