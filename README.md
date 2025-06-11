# 该库为基于[Kaggle_Trending Youtube Video Statistics数据集](https://www.kaggle.com/datasets/datasnaek/youtube-new)**Python**数据清洗代码和**MySQl** 分析代码


## 其中Python部分包含
 ▸ 时区转换
 
 ▸ 多国数据合并
 
 ▸ 冗余字段清洗
 
 ▸ 重复数据清洗
 
 ▸ 基于Isolation Forest的异常值清洗
 
 ### 运行示例为
 正在处理国家: CA
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 0 条重复记录
检测到异常值数量：2044 (5.0%)
国家 CA 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\CA_processed.csv

正在处理国家: DE
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 0 条重复记录
检测到异常值数量：2042 (5.0%)
国家 DE 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\DE_processed.csv

正在处理国家: FR
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 0 条重复记录
检测到异常值数量：2037 (5.0%)
国家 FR 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\FR_processed.csv

正在处理国家: GB
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 174 条重复记录
检测到异常值数量：1937 (5.0%)
国家 GB 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\GB_processed.csv

正在处理国家: IN
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 4894 条重复记录
检测到异常值数量：1623 (5.0%)
国家 IN 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\IN_processed.csv

正在处理国家: US
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 50 条重复记录
检测到异常值数量：2045 (5.0%)
国家 US 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\US_processed.csv

==================================================
📂 开始合并预处理文件...
🔍 找到预处理文件数量：6

[📥 阶段1/2] 数据合并
⏳ 正在加载：CA_processed.csv... 记录数：38,837 ✔️
⏳ 正在加载：DE_processed.csv... 记录数：38,798 ✔️
⏳ 正在加载：FR_processed.csv... 记录数：38,687 ✔️
⏳ 正在加载：GB_processed.csv... 记录数：36,805 ✔️
⏳ 正在加载：IN_processed.csv... 记录数：30,835 ✔️
⏳ 正在加载：US_processed.csv... 记录数：38,854 ✔️

✅ 合并完成！原始总记录数：222,816

[💾 阶段2/2] 最终处理与保存
检测到异常值数量：11141 (5.0%)
✅ 处理完成！最终记录数：211,675
数据处理流程完成
PS D:\Program Files\Codefield\CODE_Python> & "D:/Program Files/Codefield/CODE_Python/.venv/Scripts/python.exe" "d:/Program Files/Codefield/CODE_Python/Projects/Kaggle_Trending YouTube Video Statistics/Kaggle_YoutubeTrend_Analysis/Data_PreProcess.py"

正在处理国家: CA
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 0 条重复记录
检测到异常值数量：2044 (5.0%)
国家 CA 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\CA_processed.csv

正在处理国家: DE
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 0 条重复记录
检测到异常值数量：2042 (5.0%)
国家 DE 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\DE_processed.csv

正在处理国家: FR
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 0 条重复记录
检测到异常值数量：2037 (5.0%)
国家 FR 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\FR_processed.csv

正在处理国家: GB
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 174 条重复记录
检测到异常值数量：1937 (5.0%)
国家 GB 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\GB_processed.csv

正在处理国家: IN
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 4894 条重复记录
检测到异常值数量：1623 (5.0%)
国家 IN 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\IN_processed.csv

正在处理国家: US
已删除冗余列：thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed
去重处理: 移除 50 条重复记录
检测到异常值数量：2045 (5.0%)
国家 US 处理完成，保存至: D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\US_processed.csv

==================================================
📂 开始合并预处理文件...
🔍 找到预处理文件数量：6

[📥 阶段1/2] 数据合并
⏳ 正在加载：CA_processed.csv... 记录数：38,837 ✔️
⏳ 正在加载：DE_processed.csv... 记录数：38,798 ✔️
⏳ 正在加载：FR_processed.csv... 记录数：38,687 ✔️
⏳ 正在加载：GB_processed.csv... 记录数：36,805 ✔️
⏳ 正在加载：IN_processed.csv... 记录数：30,835 ✔️
⏳ 正在加载：US_processed.csv... 记录数：38,854 ✔️

✅ 合并完成！原始总记录数：222,816

[💾 阶段2/2] 最终处理与保存
检测到异常值数量：11141 (5.0%)
✅ 处理完成！最终记录数：211,675
数据处理流程完成
 
## 其中MySQL部分包含
### DaliyGrowth
通过**DailyGrowth**，可查询高爆发视频，设置参数（growth_rate为参数增长倍数）为播放量在上榜后一天内翻了一倍以上的视频，可关注视频热点，进行热点相关推流
同时，异常名字#NAME?为多国语言标题转化出现的异常量，应当忽略

![DG](https://github.com/user-attachments/assets/92884d61-6e9d-43de-86fe-0aa0f53850f4)

### HourlyActivity
通过**HourlyActivity**，可查询互动率（互动量/播放量）较高，供需比较高的时间段，如图所示，中午10-12点，傍晚18-20点均是显著的高互动率时段，

![HA1](https://github.com/user-attachments/assets/1a89275b-025a-42e3-a9e3-4de25c4e0ec1)

按供需比（互动量/发布视频数）可看出，尽管傍晚18-20点为发布高峰时段，但依旧互动率较高，相反凌晨尽管供需比较高，但互动率倒数，不是适合发布的时段

![HA2](https://github.com/user-attachments/assets/06ef5d56-0972-4b9d-841a-7873738c8987)


### LifeSpan
通过**LifeSpan**,可查询长尾（上榜时间大于三天）爆款视频（单日上榜）数据

![LS1](https://github.com/user-attachments/assets/7233fc4f-0425-4605-ac06-226c390fe379)

其中按分区占比分化显著，爆款视频中新闻政治，娱乐八卦均在前三位

![LS2](https://github.com/user-attachments/assets/a1088235-208e-407d-a623-64a32cecc23e)

### VideoStats
通过**VideoStats**，可查询赞与评论四象限，实现视频流量定点投放和舆情监控，高赞高评视频可能质量较高可以进一步推流，低赞低评视频可能出现舆情。

![VS1](https://github.com/user-attachments/assets/57928ff0-a378-489d-990d-6911bbcc0b1b)

下为查询高赞高评视频具体id

![VS2](https://github.com/user-attachments/assets/9cca94e6-d049-40ac-9d75-9b933d61f1ab)

