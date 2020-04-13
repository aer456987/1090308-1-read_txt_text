data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('計算完成,共', len(data), '筆資料') 

sum_len = 0
for d in data:
	sum_len += len(d)
print('平均留言長度為', sum_len / len(data)) 

a = []
b = []
for line_len2 in data:
	if int(len(line_len2)) >= 100:
		a.append(line_len2)
	else:
		b.append(line_len2)
print('-----------------------------------')
print("超過100字的留言有", len(a), '筆')
print("小於100字的留言有", len(b), '筆') 