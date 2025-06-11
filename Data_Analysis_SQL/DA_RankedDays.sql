WITH ranked_days AS (
    SELECT 
        video_id,
        trending_date,
        ROW_NUMBER() OVER (PARTITION BY video_id ORDER BY trending_date) AS seq
    FROM merged_datas
),
cohort AS (
    SELECT 
        video_id,
        MIN(trending_date) AS first_day,
        MAX(trending_date) AS last_day,
        COUNT(*) AS total_days
    FROM ranked_days
    GROUP BY video_id
)
SELECT 
    video_id,
    total_days AS return_times,
    DATEDIFF(last_day, first_day) AS lifespan
FROM cohort
WHERE total_days >= 2
ORDER BY return_times DESC;
