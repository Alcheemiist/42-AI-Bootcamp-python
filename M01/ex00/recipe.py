class Recipe:
  def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
    
    if (name == "" or str(cooking_lvl).isdigit() == False):
        raise Exception("error name")
    else: 
        self.name = name

    if str(cooking_lvl).isdigit() == False or cooking_lvl < 1 and cooking_lvl > 5:
        raise Exception("Error")
    else:
        self.cooking_lvl = cooking_lvl
    
    if str(cooking_time).isdigit() == False:
        raise Exception("Error")
    else:
        self.cooking_time = cooking_time
    
    if not ingredients:
        raise Exception("Error")
    else:
        self.ingredients = ingredients
    
    self.description = description
    if not recipe_type == "starter" and  not recipe_type == "lunch" and not recipe_type == "dessert":
        raise Exception("Error")
    else: 
        self.recipe_type = recipe_type
        
    def __str__(self):
        """Return The string to print with recipe info"""
        return '{} Ingredients are {} It Takes {} minutes To be Prepared for {}.' \
               '\nRecipe Description : {}'.format(self.name, ", ".join(map(str, self.ingredients)), self.cooking_time, self.recipe_type,self.description)