days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3}
]

# выручка за всю неделю

print(sum([i['revenue'] for i in days]))

# день с самой большой выручкой

print(sorted(days, key=lambda x: -x['revenue'])[0]['day'])

# средняя выручка на один заказ в каждый день

print({i['day']: i['revenue'] / i['orders'] for i in days})

# дни, где возвратов больше 20% заказов

print([i['day'] for i in days if i['returns'] / i['orders'] > 0.2])
