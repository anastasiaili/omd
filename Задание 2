queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone"
]

# сколько всего поисковых запросов в ленте

all_queries = len(queries)

# сколько раз ввели каждый запрос

res = {}
for i in queries:
    if i not in res:
        res[i] = queries.count(i)

# какой запрос вводили чаще всего

popular = ''
max_count = 0
for i in res:
    if res[i] > max_count:
        popular = i
        max_count = res[i]

# какую долю всех поисков он занимает

share = max_count / all_queries

# какие запросы встретились один раз

once = []
for i in res:
    if res[i] == 1:
        once.append(i)

print(all_queries)
print(res)
print(popular)
print(share)
print(once)
