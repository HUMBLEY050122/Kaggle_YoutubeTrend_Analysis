import pandas as pd
import numpy as np
from pathlib import Path
from pytz import timezone
import pytz
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# ================== 全局配置 ==================
CONFIG = {
    "country_timezones": {
        'US': 'America/New_York',
        'CA': 'America/Toronto',
        'GB': 'Europe/London',
        'IN': 'Asia/Kolkata',
        'FR': 'Europe/Paris',
        'DE': 'Europe/Berlin'
    },
    "analysis_params": {
        "quantile_range": (1.5, 3.5),
        "target_retention": 0.8,
        "contamination": 0.05
    },
    "paths": {
        "input_dir": r"D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Selected_dataset",
        "output_dir": r"D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset",
        "final_output": r"D:\Program Files\Codefield\CODE_Python\Projects\Kaggle_Trending YouTube Video Statistics\Processed_dataset\merged_youtube_data.csv"
    }
}

# ================== 核心工具函数 ==================
def get_country_code(filename: str) -> str:
    """从文件名提取标准化国家代码"""
    base_name = Path(filename).name
    return base_name[:2].upper() if len(base_name) >= 2 else None

def convert_timezone(df: pd.DataFrame, country_code: str) -> pd.DataFrame:
    """时区转换处理"""
    if 'publish_time' in df.columns:
        try:
            df['publish_time'] = pd.to_datetime(df['publish_time'], utc=True)
            if country_code in CONFIG['country_timezones']:
                tz = timezone(CONFIG['country_timezones'][country_code])
                df['publish_time'] = df['publish_time'].dt.tz_convert(tz)
            df['publish_time'] = df['publish_time'].dt.strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            print(f"时间转换错误: {str(e)}")
    
    if 'trending_date' in df.columns:
        try:
            df['trending_date'] = pd.to_datetime(
                df['trending_date'], format='%y.%d.%m', errors='coerce'
            ).dt.strftime('%Y-%m-%d')
        except Exception as e:
            print(f"日期转换错误: {str(e)}")
    return df

def normalize_boolean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """布尔列标准化"""
    bool_cols = ['comments_disabled', 'ratings_disabled', 'video_error_or_removed']
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()
            df[col] = df[col].map({'true': True, 'false': False, 'nan': None})
    return df

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """基础数据清洗（包含删除指定列）"""
    # 删除指定列
    columns_to_drop = ['thumbnail_link', 'comments_disabled', 
                      'ratings_disabled', 'video_error_or_removed']
    existing_cols = [col for col in columns_to_drop if col in df.columns]
    df = df.drop(columns=existing_cols, errors='ignore')
    print(f"已删除冗余列：{', '.join(existing_cols)}")

    # 去重处理
    if all(col in df.columns for col in ['video_id', 'trending_date']):
        initial_count = len(df)
        df = df.drop_duplicates(subset=['video_id', 'trending_date'])
        print(f"去重处理: 移除 {initial_count - len(df)} 条重复记录")
    
    # 处理缺失值
    required_cols = ['publish_time', 'trending_date', 'views', 'likes', 'comment_count']
    df = df.dropna(subset=[c for c in required_cols if c in df.columns])
    
    # 填充辅助列
    for col in ['tags', 'description']:
        if col in df.columns:
            df[col] = df[col].fillna('')
    return df

# ================== 智能过滤模块 ==================
def detect_outliers(df: pd.DataFrame, 
                   features: list = ['views', 'likes', 'comment_count'],
                   action: str = 'mark') -> pd.DataFrame:
    """基于孤立森林的异常检测（修复列删除问题）"""
    df = df.copy()
    valid_features = [col for col in features if col in df.columns]
    
    if not valid_features:
        raise ValueError("没有有效的特征列可用于异常检测")
    
    # 数据预处理（对数变换）
    X = np.log1p(df[valid_features])
    
    # 训练孤立森林模型
    model = IsolationForest(
        n_estimators=100,
        contamination=CONFIG['analysis_params']['contamination'],
        random_state=42
    )
    model.fit(X)
    
    # 预测结果
    scores = model.decision_function(X)
    pred = model.predict(X)
    
    # 结果处理（始终保留异常评分）
    df['anomaly_score'] = scores  # 确保始终添加该列
    df['is_outlier'] = pred == -1
    print(f"检测到异常值数量：{df['is_outlier'].sum()} ({df['is_outlier'].mean():.1%})")
    
    if action == 'remove':
        return df[~df['is_outlier']].drop(columns=['is_outlier'])  # 只删除标记列
    elif action == 'mark':
        return df
    else:
        raise ValueError(f"无效操作类型: {action}")

# ================== 可视化模块 ==================
def generate_country_report(df: pd.DataFrame, country_code: str):
    """生成国家维度分析报告（增加列存在检查）"""
    output_dir = Path(CONFIG['paths']['output_dir']) / 'visualizations'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 异常评分分布（增加安全检查）
    if 'anomaly_score' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['anomaly_score'], bins=50, kde=True)
        plt.axvline(df['anomaly_score'].quantile(0.05), color='r', linestyle='--')
        plt.title(f'{country_code} Anomaly Score Distribution')
        plt.savefig(output_dir / f'{country_code}_anomaly_scores.png')
        plt.close()
    else:
        print(f"⚠️ 警告：国家 {country_code} 数据缺少异常评分列")

# ================== 文件处理模块 ==================
def process_single_file(file_path: Path, output_dir: Path) -> Path:
    """单文件处理流水线（调整处理顺序）"""
    df = pd.read_csv(file_path)
    country_code = get_country_code(file_path.name)
    
    if not country_code:
        print(f"跳过无法识别的文件: {file_path.name}")
        return None
    
    print(f"\n正在处理国家: {country_code}")
    
    # 执行处理流程
    df = convert_timezone(df, country_code)
    df = normalize_boolean_columns(df)
    df = basic_cleaning(df)
    
    # 先生成报告再删除列
    temp_df = detect_outliers(df, action='mark')  # 先标记不删除
    generate_country_report(temp_df, country_code)
    
    # 最终删除异常值和标记列
    processed_df = temp_df[~temp_df['is_outlier']].drop(columns=['is_outlier'])
    
    # 保存结果
    output_path = output_dir / f"{country_code}_processed.csv"
    processed_df.to_csv(output_path, index=False)
    print(f"国家 {country_code} 处理完成，保存至: {output_path}")
    return output_path

def enhanced_merge_all_files(output_dir: Path, final_path: Path):
    """增强版合并函数"""
    print("\n" + "="*50)
    print("📂 开始合并预处理文件...")
    
    all_files = list(output_dir.glob("*_processed.csv"))
    print(f"🔍 找到预处理文件数量：{len(all_files)}")
    
    if not all_files:
        print("❌ 错误：未找到任何预处理文件")
        return

    try:
        print("\n[📥 阶段1/2] 数据合并")
        dfs = []
        total_raw = 0
        
        for f in all_files:
            print(f"⏳ 正在加载：{f.name}...", end="")
            df = pd.read_csv(f)
            dfs.append(df)
            total_raw += len(df)
            print(f" 记录数：{len(df):,} ✔️")
        
        merged_df = pd.concat(dfs, ignore_index=True)
        print(f"\n✅ 合并完成！原始总记录数：{total_raw:,}")

    except Exception as e:
        print(f"\n❌ 数据合并失败：{str(e)}")
        return

    try:
        print("\n[💾 阶段2/2] 最终处理与保存")
        # 全局异常检测
        final_df = detect_outliers(merged_df, action='remove')
        final_df.to_csv(final_path, index=False)
        print(f"✅ 处理完成！最终记录数：{len(final_df):,}")

    except Exception as e:
        print(f"\n❌ 文件保存失败：{str(e)}")

# ================== 主执行流程 ==================
def main():
    input_dir = Path(CONFIG['paths']['input_dir'])
    output_dir = Path(CONFIG['paths']['output_dir'])
    final_path = Path(CONFIG['paths']['final_output'])
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    processed_files = []
    for file_path in input_dir.glob("*.csv"):
        if result := process_single_file(file_path, output_dir):
            processed_files.append(result)
    
    if processed_files:
        enhanced_merge_all_files(output_dir, final_path)
    
    print("数据处理流程完成")

if __name__ == "__main__":
    main()