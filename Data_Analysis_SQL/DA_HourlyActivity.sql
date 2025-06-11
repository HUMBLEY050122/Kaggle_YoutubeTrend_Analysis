-- 计算每小时用户互动效率（点赞率+评论率）与内容供给量
WITH hourly_activity AS (
    SELECT 
        HOUR(publish_time) AS hour,
        COUNT(DISTINCT video_id) AS video_count,
        SUM(views) AS total_views,
        SUM(likes) AS total_likes,
        SUM(comment_count) AS total_comments,
        ROUND((SUM(likes) + SUM(comment_count)) / SUM(views), 4) AS interaction_score
    FROM merged_datas
    GROUP BY hour
)
SELECT 
    hour,
    video_count,
    interaction_score,
    -- 供需比：互动效率 / 内容量（值越高时段越优质）
    ROUND(interaction_score / NULLIF(video_count, 0), 8) AS supply_demand_ratio
FROM hourly_activity
ORDER BY supply_demand_ratio DESC;