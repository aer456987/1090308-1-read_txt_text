# 讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 50000 == 0:
            print(len(data))
print('共有', len(data), '筆留言')

# 平均留言字數
sum_len = 0
for line_len in data:
    sum_len += len(line_len)
print('每則留言平均有', sum_len / len(data), '個字')
print('================================')

# 印出字數範圍內的筆數
a = []
b = []
for len2 in data:
    if int(len(len2)) >= 1000:
        a.append(len2)
    else:
        b.append(len2)
print("超過1000字的留言有", len(a), '筆')
print("小於1000字的留言有", len(b), '筆')

# 印出含有特定單字的留言
good = []
for g in data:
    if 'good' in g:
        good.append(g)
print('含有Good的留言共有', len(good), '筆')
print('=================================================')

# 計算每個單字出現的次數並加入字典裡
word_count = {}
for d in data:
    words = d.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
print('================================')

# 印出字典裡的單字和次數
for word in word_count:
    print(word, '共出現', word_count[word], '次')
print('================================')

# 印出出現超過10000次的單字
for word in word_count:
    if word_count[word] > 10000:
        print(word, '共出現', word_count[word], '次')
print('字典裡共有', len(word_count), '筆資料')
print('================================')

# 自行輸入想要查詢的單字
while True:
    user_input = input('輸入想要查詢的字(quit離開): ')
    if user_input == 'quit':
        break
    elif user_input in word_count:
        print(user_input, '共出現', word_count[user_input], '次')
    else:
        print('找不到資料。')