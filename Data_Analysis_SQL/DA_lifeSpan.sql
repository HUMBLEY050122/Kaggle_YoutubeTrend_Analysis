WITH video_lifespan AS (
    SELECT 
        video_id,
        DATEDIFF(MAX(trending_date), MIN(trending_date)) + 1 AS days_on_trend,
        COUNT(DISTINCT trending_date) AS active_days,
        SUM(views) AS total_views,
        SUM(likes) AS total_likes,
        SUM(comment_count) AS total_comments
    FROM merged_datas
    GROUP BY video_id
)
SELECT 
    CASE 
        WHEN days_on_trend >= 3 THEN '长尾内容'
        WHEN days_on_trend <= 1 THEN '瞬时爆款' 
        ELSE '常规内容'
    END AS content_type,
    COUNT(video_id) AS num_videos,
    ROUND(AVG(total_views), 0) AS avg_views,
    ROUND(AVG((total_likes+total_comments) / total_views), 4) AS avg_interact_rate
FROM video_lifespan
GROUP BY content_type;