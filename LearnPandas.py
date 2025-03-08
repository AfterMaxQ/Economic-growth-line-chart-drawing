import pandas as pd

# 纵向合并（相同列名）
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
print(pd.concat([df1, df2], axis=0).reset_index())  # 垂直堆叠

# 横向合并（相同行数）
print(pd.concat([df1, df2], axis=1).reset_index())  # 水平拼接