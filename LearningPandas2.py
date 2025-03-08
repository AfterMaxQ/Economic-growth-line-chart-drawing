import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df1 = pd.read_csv('年度数据.csv')
print("原始数据：")
print(df1)

# 检查缺失值
print("缺失值统计：")
print(df1.isnull().sum())

# 复制数据并清理
cleaned_data = df1.copy()

print("转换前：")
print(cleaned_data)
print(cleaned_data.dtypes)

# 将年份列转换为数值类型
for year in cleaned_data.columns[1:]:
    cleaned_data[year] = pd.to_numeric(cleaned_data[year], errors='coerce')
cleaned_data.reset_index(drop=True, inplace=True)

# 打印转换后的数据和数据类型
print("\n转换后：")
print(cleaned_data)
print(cleaned_data.dtypes)


# 删除任何空行或空列
cleaned_data.dropna(how='all', inplace=True)  # 删除全为空的行
cleaned_data.dropna(axis=1, how='all', inplace=True)  # 删除全为空的列

# 重置索引
cleaned_data.reset_index(drop=True, inplace=True)

# 将除“指标”列外的所有列转换为数值类型
for col in cleaned_data.columns[1:]:
    cleaned_data[col] = pd.to_numeric(cleaned_data[col], errors='coerce')
print(cleaned_data)

# 设置“指标”列为索引
cleaned_data.set_index('指标', inplace=True)

cleaned_data.head()

# 返回 DataFrame

# 对年份列进行升序排序
sorted_columns = sorted(cleaned_data.columns, key=lambda x: int(x[:-1]))
cleaned_data_sorted = cleaned_data[sorted_columns]

# 查看排序后的数据
print(cleaned_data_sorted.head())

# 按行计算增长率
growth_rate = cleaned_data_sorted.pct_change(axis=1).round(4)
print(growth_rate)

plt.figure()

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300
# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制折线图
plt.figure(figsize=(12, 8))

#用于按行迭代 DataFrame。每次迭代会返回一个包含两个元素的元组，
# 第一个元素是当前行的索引，第二个元素是当前行的数据，以 Series 对象的形式呈现。
for index, row in growth_rate.iterrows():
    plt.plot(row.index, row.values, label = index)

# 设置图形标签和标题
plt.xlabel('年份')
plt.ylabel('增长率')
plt.title('各指标年度增长率折线图')

# 添加图例
plt.legend()

# 显示网格线
plt.grid(True)

# 旋转 x 轴标签以便更好显示
plt.xticks(rotation=45)

# 显示图形
plt.show()