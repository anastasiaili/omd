orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

returned_l = [i for i in orders if i['status'] == 'returned']
delivered_l = [i for i in orders if i['status'] == 'delivered']

# на какую сумму оформили возвраты

print(sum([i['amount'] for i in returned_l]))

# кто хотя бы раз вернул заказ

print(set([i['buyer'] for i in returned_l]))

# сколько заказов доставлено покупателю

print(len(delivered_l))

# средний чек доставленных заказов

print(sum([i['amount'] for i in delivered_l]) / len(delivered_l))
