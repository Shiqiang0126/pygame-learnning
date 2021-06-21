from matplotlib import pyplot as plt

plt.figure(figsize=(6, 7))
# 定义饼状图的标签，标签是列表
labels = [u'<15K', u'15K-30K', u'>30K']
data = [1,2,3]
plt.pie(data, labels=labels)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend()
plt.show()
