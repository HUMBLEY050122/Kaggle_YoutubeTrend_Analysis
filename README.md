# YouTube Trending Video 数据分析项目

本项目基于 [Kaggle Trending YouTube Video Statistics 数据集](https://www.kaggle.com/datasets/datasnaek/youtube-new)，通过 **Python** 进行数据清洗，结合 **MySQL** 实现多维度数据分析，挖掘视频热点、用户行为及内容投放策略。

---

## 数据清洗（Python）
清洗过程主要包括：
- **时区转换**：统一各国数据时间格式
- **多国数据合并**：整合多语言国家上榜视频
- **冗余字段清洗**：剔除无效字段
- **重复数据去除**：消除重复记录
- **异常值检测**：基于 Isolation Forest 清洗播放量等异常项

---

## 数据分析（MySQL）

主要包含以下模块：

### 1. `DailyGrowth` — 视频爆发增长识别

- 识别播放量在上榜后一日内**增长翻倍**的视频（设置参数 `growth_rate`）
- 可用于监测热点视频并进行推流推荐

> 注意：标题字段中 `#NAME?` 是因多语言编码异常产生，可忽略

---

### 2. `HourlyActivity` — 高互动时段分析

- 计算各小时互动率（互动量 / 播放量）
- 识别**高互动时段**（如 10–12 点、18–20 点）
- 提供**供需比**（互动量 / 视频数）辅助判断发布时机

---

### 3. `LifeSpan` — 长尾爆款识别

- 筛选生命周期超过三天的上榜视频
- 分析其内容分区占比（如新闻、娱乐等）
- 可指导内容创作方向

---

### 4. `VideoStats` — 舆情与流量四象限分析

- 基于点赞数与评论数构建四象限
    - **高赞高评**：优质内容，适合重点投放
    - **低赞低评**：冷门或负面舆情，需警惕
- 用于投放策略与舆情预警
