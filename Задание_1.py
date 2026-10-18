moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

# товары, которые есть на обоих складах
moscow_and_kazan = moscow.intersection(kazan)

# товары только в Москве
only_moscow = moscow.difference(kazan)

# товары только в Казани
only_kazan = kazan.difference(moscow)

# количество разных товаров на двух складах
count_all_products = len(moscow.union(kazan))

print(moscow_and_kazan)
print(only_moscow)
print(only_kazan)
print(count_all_products)
