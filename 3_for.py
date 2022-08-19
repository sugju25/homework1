phones =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_sum(items_sold):
    items_sum = sum(items_sold)
    return items_sum
for one_phone in phones:
  items_sum =count_sum(one_phone['items_sold'])
  print(f"Сумма товаров для телефона {one_phone['product']}: {items_sum}")

whole_sum  = 0
for items_sum in whole_sum:
  whole_sum += count_sum(one_phone['items_sold'])
print(f"Сумма единиц товара всего {whole_sum}")

def count_average(items_sold):
  items_sum = 0
  for item in items_sold:
    items_sum += item
  items_avg = items_sum/ len(items_sold)
  return items_avg

for one_phone in phones:
  phone_items_avg = count_average(one_phone['items_sold'])
  print(f"Среднее количество единиц товара для телефона {one_phone['product']}: {phone_items_avg}")

avg_items_sum = 0
for one_phone in phones:
  avg_items_sum += count_average(one_phone['items_sold'])
allphones_avg = avg_items_sum /len(phones)
print(f"Среднее количество единиц товара для всех телефонов: {allphones_avg}") 
