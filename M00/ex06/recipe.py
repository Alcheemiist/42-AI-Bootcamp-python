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

"""" 1 - 
x = cookbook.keys() 

print("keys are {x}".format(x=x))

x = cookbook.values() 

print(" \nvalues are {x}".format(x=x))

x = cookbook.items() 

print("\n items pair are {x}".format(x=x))

"""

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
        print("This option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
    else:
        m = int(m)
        print(m)
        if (m == 3):
            while True:
                print(bcolors.HEADER + "Please enter the recipe's name to get its details:" + bcolors.ENDC)
                string = ""
                string = input(">> ")
                s = cookbook.get(string)
               
                if (s == None):
                    print('\033[93m' + "reciepe not found" + '\033[0m')
                    print("the recipe avalaible are :")    
                    print_cookbook(s)
                else:
                    print("Recipe for {string}:".format(string=string))
                    print("Ingrediens list : {}".format(cookbook[string]["ingredients"]))
                    print("To be eaten for {}".format(cookbook[string]["meal"]))
                    print("Takes {} minutes of cooking.".format( cookbook[string]["prep_time"]))
        elif (m == 1):
            print("name of the recipe =")
                

        else:
            print("This option does not exist, please type the corresponding number.")
            print("To exit, enter 5.")
