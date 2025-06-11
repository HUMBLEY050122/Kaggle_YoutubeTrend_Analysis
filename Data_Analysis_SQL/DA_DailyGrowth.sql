WITH daily_growth AS (
    SELECT 
        video_id,
        trending_date,
        views,
        LAG(views) OVER (PARTITION BY video_id ORDER BY trending_date) AS prev_views,
        ROUND((views - LAG(views) OVER (PARTITION BY video_id ORDER BY trending_date)) 
             / NULLIF(LAG(views) OVER (PARTITION BY video_id ORDER BY trending_date), 0), 4) AS growth_rate
    FROM merged_datas
)
SELECT 
    video_id,
    trending_date,
    growth_rate,
    views
FROM daily_growth
WHERE growth_rate >= 1.0  -- 播放量 24h 内翻倍
ORDER BY growth_rate DESC
LIMIT 20;  -- 取前 20 个视频