from pprint import pprint

# словарь {меню: ингредиенты, количество, единица измерения}
def prepare_dict(file_name: str) -> dict:
    result: dict = dict()
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            dish_name = line.strip()
            records_quantity = int(file.readline())
            cook_book = []
            for ingredient in range(records_quantity):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                cook_book.append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                )
            result[dish_name] = cook_book
            file.readline()
    return result
cook_book = prepare_dict('recipes.txt')

# словарь с названием ингредиентов и множителем по количеству блюд для персон
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for key, values in cook_book.items():
        for dishes_name in dishes:
            if dishes_name == key:
                for res in values:
                    if res['ingredient_name'] not in shop_list.keys():
                        shop_list[res['ingredient_name']] = {'quantity': res['quantity'] * person_count, 'measure': res['measure']}
                    else:
                        shop_list[res['ingredient_name']] = {'quantity': res['quantity'] * person_count + res['quantity'] * person_count, 'quantity': res['quantity']}
    return shop_list

print(cook_book)
print()
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))




