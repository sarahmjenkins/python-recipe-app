# Define the recipe class
class Recipe(object):
    all_ingredients = []
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def get_name(self):
        return self.name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def set_name(self, name):
        self.name = name
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
    
    def add_ingredients(self, *args):
        self.ingredients = args
        Recipe.update_all_ingredients(self)

    def get_ingredients(self):
        return self.ingredients
    
    def calculate_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'Easy'
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'Medium'
        elif cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'Intermediate'
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'Hard'
        self.difficulty = difficulty
    
    def get_difficulty(self):
        if self.difficulty:
            return self.difficulty
        else:
            self.calculate_difficulty(self.cooking_time, self.ingredients)
    
    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False
    
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if not ingredient in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
    
    def __str__(self):
        output = '-----Recipe-----\nName: ' + str(self.name) + '\nCooking Time: ' + str(self.cooking_time) + ' minutes\nIngredients: ' + ', '.join(self.ingredients) + '\nDifficulty: ' + str(self.difficulty)
        return output

# print all recipes with ingredient that is searched for
def recipe_search(data, search_term):
    print('\n-----\n-----\nRecipes that include ' + search_term + ':')
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)

# creating new objects in Recipe class and a list to hold recipes
tea = Recipe('Tea')
tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')
tea.set_cooking_time(5)
tea.get_difficulty()
print(tea)

coffee = Recipe('Coffee')
coffee.add_ingredients('Coffee Powder', 'Sugar', 'Water')
coffee.set_cooking_time(5)
coffee.get_difficulty()
print(coffee)

cake = Recipe('Cake')
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Extract', 'Flour', 'Baking Powder', 'Milk')
cake.set_cooking_time(50)
cake.get_difficulty()
print(cake)

banana_smoothie = Recipe('Banana Smoothie')
banana_smoothie.add_ingredients('Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes') 
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]

# searching recipes for specific ingredients
recipe_search(recipes_list, 'Water')
recipe_search(recipes_list, 'Sugar')
recipe_search(recipes_list, 'Bananas')