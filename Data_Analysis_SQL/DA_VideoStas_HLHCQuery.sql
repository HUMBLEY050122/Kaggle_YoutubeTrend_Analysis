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
    video_id,
    views,
    likes,
    comment_count,
    ROUND(like_rate, 4) AS like_rate,
    ROUND(comment_rate, 4) AS comment_rate
FROM video_stats
WHERE like_rate >= 0.05 AND comment_rate >= 0.02
ORDER BY like_rate DESC;
