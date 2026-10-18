reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

for i in reviews:
    i['product'] = i['product'].lower()

# средняя оценка каждого товара
products = set([i['id'] for i in reviews])
avg = {}
count = {}

for p in products:
    product_reviews = [i for i in reviews if i['id'] == p]
    name = product_reviews[0]['product']
    avg[name] = sum([i['stars'] for i in product_reviews]) / len(product_reviews)
    count[name] = len(product_reviews)

# худший товар среди тех, у кого хотя бы два отзыва
filtered = [i for i in avg if count[i] >= 2]
worst = sorted(filtered, key=lambda x: avg[x])[0]

# сколько отзывов на 1 или 2 звезды
bad = [i for i in reviews if i['stars'] <= 2]

# какую долю всех отзывов они составляют
share = len(bad) / len(reviews)

print(avg)
print(worst)
print(len(bad))
print(share)
