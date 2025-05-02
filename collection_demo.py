from collections import defaultdict

dd = defaultdict(int)
dd['hello'] = 10
print(dd['key'])  # 输出: 0，因为 int() 的默认值是 0
print(dd['hello'])