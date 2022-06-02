# 前几天有人在群里给小编出了个数学题：
#
# 假设你有无限数量的邮票, 面值分别为6角，7
# 角，8
# 角, 请问你最大的不可支付邮资是多少元？
# 小编掰着手指头和脚趾头算了下，答案是：1.7元

a = 6
b = 7
c = 8
t = 50
s = []
for i in range(t+1):
    s1=a*i
    s.append(s1)
    for j in range(t+1):
        s2 = a*i + b*j
        s.append(s2)
        for k in range(t+1):
            s3 = a*i + b*j + c*k
            s.append(s3)
            # 显示制定金额时显示各类的张数
            # if s3 == 80:
            #     print(i,j,k)

#排序去重
s.sort()
news = []
for i in s:
    if i not in news:
        news.append(i)
print("组合生产的最大数%s"%news[0:20])
#提取不在队里里面的数字
r = []
for i in range(6*t):
    if i in news:
        pass
    else:
        r.append(i)
print("组合不能生产的数字%s"%r)
print("不能生产的最大的数字为%s"%r[-1])