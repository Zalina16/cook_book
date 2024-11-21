def read_file(recipes):
    with open('recipes.txt', 'r', encoding = 'utf-8') as file:
        content = file.read()
        return content

file_content = read_file('recipes.txt')

def parse_file(file_content):
    lines = file_content.splitlines()
    for line in lines:
        print (line)

def parse_file(file_content):
    lines = file_content.splitlines()
    cook_book = {}
    i = 0

    while i < len(lines):
        dish_name = lines[i]
        i += 1
        num_ingredients = int(lines[i])
        i += 1
        ingredients = []

        for _ in range(num_ingredients):
            ingredient_data = lines[i].split(' | ')
            ingredient = {
                'ingredient_name': ingredient_data[0],
                'quantity': int(ingredient_data[1]),
                'measure': ingredient_data[2]
            }
            ingredients.append(ingredient)
            i += 1

        cook_book[dish_name] = ingredients

        if i < len(lines) and lines[i] == '':
            i += 1

    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shopping_list = {}
    for dish in dishes:
        ingredients = cook_book.get(dish, [])
        for ingredient in ingredients:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name not in shopping_list:
                shopping_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shopping_list[ingredient_name]['quantity'] += quantity

    return shopping_list


file_content = read_file('recipes.txt')
cook_book = parse_file(file_content)

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shopping_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shopping_list)






