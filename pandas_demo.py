import pandas as pd

# 指定CSV文件路径
csv_file_path = 'text.csv'

# 使用pandas的read_csv函数读取CSV文件
df = pd.read_csv(csv_file_path)
print("yes————————")
print(df.head())  # 查看前几行数据
print("yes————————")
print(df.info())  # 显示数据集的列名、数据类型和非空值数量
print("yes————————")
print(df.describe())  # 统计数值型列的基本统计信息
print("yes————————")

# 输出CSV文件的前5行数据，如果你想输出所有行，可以使用df.to_string()，但请注意，如果文件非常大，这可能会消耗大量内存
print(df.head())
print("yes————————")