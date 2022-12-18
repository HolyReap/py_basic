def get_shop_list(dishes, person_count, cook_book):
    ingridient_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for item in cook_book[dish]:
                if item['ingridient_name'] in ingridient_list.keys():
                    ingridient_list[item['ingridient_name']]['quantity'] += item['quantity']*person_count
                else:
                    ingridient_list[item['ingridient_name']] = {'measure':item['measure'],'quantity':item['quantity']*person_count}
    return(ingridient_list)    

with open('recipes.txt','r', encoding = 'utf-8') as f:
    res = f.readlines()
    recipes_number = 1
    for value in res:
        if value == '\n':
            recipes_number += 1

with open('recipes.txt','r', encoding = 'utf-8') as f:
    cook_book = {}
    for i in range(recipes_number):
        dish = f.readline().rstrip()
        ingridients_num = int(f.readline())
        cook_book[dish] = []
        ingr=[]
        for j in range(ingridients_num):
            ingridient = f.readline().split(' | ')
            ingr += [{'ingridient_name': ingridient[0], 'quantity': int(ingridient[1]), 'measure' : ingridient[2].rstrip()}]
        cook_book[dish] += ingr
        f.readline()


dishes = ['Омлет','Запеченный картофель']
person_count = 2
print(get_shop_list(dishes, person_count, cook_book))
        

                