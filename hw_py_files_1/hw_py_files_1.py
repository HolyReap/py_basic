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
print(cook_book)
          

                