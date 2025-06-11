WITH video_lifespan AS (
    SELECT 
        m.video_id,
        c.category_name,
        DATEDIFF(MAX(m.trending_date), MIN(m.trending_date)) + 1 AS days_on_trend
    FROM merged_datas m
    JOIN category c ON m.category_id = c.category_id
    GROUP BY m.video_id, c.category_name
),
classified_lifespan AS (
    SELECT 
        video_id,
        category_name,
        CASE 
            WHEN days_on_trend >= 3 THEN '长尾内容'
            WHEN days_on_trend <= 1 THEN '瞬时爆款' 
            ELSE '常规内容'
        END AS content_type
    FROM video_lifespan
),
category_counts AS (
    SELECT 
        content_type,
        category_name,
        COUNT(*) AS num_videos
    FROM classified_lifespan
    GROUP BY content_type, category_name
),
content_totals AS (
    SELECT 
        content_type,
        SUM(num_videos) AS total_videos
    FROM category_counts
    GROUP BY content_type
),
category_ratios AS (
    SELECT 
        cc.content_type,
        cc.category_name,
        cc.num_videos,
        cc.num_videos * 1.0 / ct.total_videos AS content_ratio
    FROM category_counts cc
    JOIN content_totals ct ON cc.content_type = ct.content_type
),
ranked_categories AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY content_type ORDER BY content_ratio DESC) AS rn
    FROM category_ratios
)
-- 最终查询：取每类内容下占比最高的 Top 3 分区
SELECT 
    content_type,
    category_name,
    num_videos,
    ROUND(content_ratio * 100, 2) AS percentage
FROM ranked_categories
WHERE content_type IN ('长尾内容', '瞬时爆款') AND rn <= 3
ORDER BY content_type, percentage DESC;
