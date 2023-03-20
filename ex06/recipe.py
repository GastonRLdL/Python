import sys
import string

cookbook = {
    'bocadillo' : {
        'ingredients': ['jamon', 'queso', 'pan'],
        'meal': ['almuerzo'],
        'prep_time': ['10 minutos']
        },
    'tarta' : {
        'ingredients': ['harina', 'azucar', 'huevos'],
        'meal': 'postre',
        'prep_time': '60 minutos'
        },
    'ensalada' : {
        'ingredients': ['aguacate', 'rucula', 'tomates', 'espinacas'],
        'meal': ['almuerzo'],
        'prep_time': ['15 minutos']
    }
}
def platos(cookbook):
    for key in cookbook.keys():
    #    print("\n")
        print(key)

def ingredientes(cookbook, p):
    print("\nRecipe for", p)
    print("Ingredients list:", cookbook[p]['ingredients'], ".")
    print("To be eaten for", cookbook[p]['meal']),
    print("Takes", cookbook[p]['prep_time'], "of cooking.\n")

def add(cookbook):
    new_dish = input("Add name of the new dish:\n")
    new_dish_ingredients = input("Add the ingredients (spaced by a comma)\n")
    new_dish_when = input("Add when to eat it:\n")
    new_dish_time = input("Add preparation time\n")
    new_recipe = {
        'ingredients': new_dish_ingredients.split(","),
        'meal': new_dish_when,
        'prep_time': new_dish_time
    }
    cookbook[new_dish] = new_recipe
    return cookbook

def remove(cookbook, dish):
    del cookbook[dish]
    return cookbook

def menu():
    print("Wlcome to the Python Cookbook !\nList of aviable options")
    print("   1: Add a recipe\n   2: Delete a recipe\n   3: Print a recipe\n   4: Print the cookbook\n   5: Quit")
    
    switch = True
    while switch:
        option = input("\nPlease select an option:\n")
        if option == "1":
            add(cookbook)
        elif option == "2":
            dish = input("Please enter the name of the dish you want to remove:\n")
            remove(cookbook, dish)
        elif option == "3":
            choose = input("\nPlease enter a recipe name to get its details:\n")
            ingredientes(cookbook, choose)
        elif option == "4":
            platos(cookbook)
        elif option == "5":
            print("Cookbook closed. Goodbye !")
            switch = False

if __name__ == '__main__':
    menu()