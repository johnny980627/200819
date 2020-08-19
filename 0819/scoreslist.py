scores =[]
maxs = 0
mins = 100
total = 0
name = []
for i in range(5):
    n = input("姓名:")
    name.append(n)
    s = int(input("成績:"))
    scores.append(s)
    if s > maxs:
        maxs = s
        maxn = n
    if s < mins:
        mins = s
        minn = n
    total = total + s
t = total/len(scores)
print("總分:",total)
print("平均:",t)
print("最高分:", maxn ,maxs)
print("最低分:", minn ,mins)
