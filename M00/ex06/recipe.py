class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_recipe(s):
    print( "Ingredients list : ", str(cookbook[s]["ingredients"]))
    return 


cookbook = {
'sandwich' :  { 
               "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
               "meal": "lunch",
               "prep_time": "10",
              },
'cake': {
        "ingredients" : ["flour", "sugar", "eggs"] , 
        "meal" : "dessert" ,
        "prep_time" : "60" ,
        },

'salad': { 
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : "15",
        } 
}

def delet_recipe(name):
    del cookbook[name]

def add_recipe(name_recipe, ingredients, meal ,prep_time):
    new_recipe = { 
        name_recipe : { 
                "ingredients" : list(ingredients),
                "meal" : meal,
                "prep_time" : prep_time,
            },
    }
    cookbook.update(new_recipe)

def print_cookbook(c):
    for i in cookbook.keys():
        print("- ",i)



def print_prompet():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")

print_prompet()

name_recipe = ""
ingredients = list()
meal = ""
prep_time = ""

while True:
    m = input(">> ")
    if m.isdigit() == False:
        print( bcolors.WARNING + "This option does not exist, please type the corresponding number. To exit, enter 5." + bcolors().ENDC)
        print_prompet()
    else:
        m = int(m)
        if (m == 3):
                print(bcolors.HEADER + "Please enter the recipe's name to get its details:" + bcolors.ENDC)
                string = ""
                string = input(">> ").strip(' ')
                s = cookbook.get(string)
               
                if (s == None):
                    print('\033[93m' + "reciepe {} not found".format(string) + '\033[0m')
                    print("the recipe avalaible are :")    
                    print_cookbook(s)
                else:
                    print("Recipe for {string}:".format(string=string))
                    print("Ingrediens list : {}".format(cookbook[string]["ingredients"]))
                    print("To be eaten for {}".format(cookbook[string]["meal"]))
                    print("Takes {} minutes of cooking.".format( cookbook[string]["prep_time"]))
                    print_prompet()
        elif (m == 2):
            print("put the name of the item you wanna delete ?")
            string = input(">> ").strip(" ")
            cookbook.pop(string)
            print("the {} was delted succesifly".format(string))
            print_prompet()
        elif (m == 1):
            print(bcolors.OKGREEN + "youre now on process to add a recipe to the cookbook" + bcolors.ENDC + "\n")
            print("name of the recipe = ? ")
            new_item_name = input(">> ")
            print("enter the ingeridation on format : [ x , y , z ...]")
            ingredien_meal = list(input(">> ").split(","))
            print("type of meal {} :".format(new_item_name))
            meal_type = input(">> ")
            print("How it take to prepare {} ?".format(new_item_name))
            preparation_time = input(">> ")
            i = 0
            while (i < 3):
                print("adding item to cookbok.......")
                i += 1
            add_recipe(new_item_name , ingredien_meal , meal_type , preparation_time )
        elif m == 4:
            print("the recipes avalaibale on the bookbook are :")
            print_cookbook(" ")
        elif m == 5:
            print("exit cookbook")
            exit()
        else:
            print("This option does not exist, please type the corresponding number.")
            print("To exit, enter 5.")
