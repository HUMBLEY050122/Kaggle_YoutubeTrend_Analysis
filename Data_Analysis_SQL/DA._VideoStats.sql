WITH video_stats AS (
    SELECT 
        video_id,
        views,
        likes,
        comment_count,
        likes * 1.0 / views AS like_rate,
        comment_count * 1.0 / views AS comment_rate
    FROM merged_datas
)
SELECT 
    CASE 
        WHEN like_rate >= 0.05 AND comment_rate >= 0.02 THEN '高赞高评'
        WHEN like_rate >= 0.05 THEN '高赞低评'
        WHEN comment_rate >= 0.02 THEN '低赞高评'
        ELSE '低赞低评'
    END AS interaction_type,
    COUNT(video_id) AS num_videos,
    ROUND(AVG(views), 0) AS avg_views
FROM video_stats
GROUP BY interaction_type;