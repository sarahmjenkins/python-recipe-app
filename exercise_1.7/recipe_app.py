# set up sqlalchemy, create engine and session, run program
from sqlalchemy import create_engine 
engine = create_engine("mysql://cf-python:password@localhost/task_database")

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# create model
class Recipe(Base):
  __tablename__ = "final_recipes"
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))
  def __repr__(self):
    return "<Recipe ID: " + str(self.id) + "-" + self.name + "-" + self.difficulty + ">"
  def __str__(self):
    return "\n" + self.name + "\nRecipe ID: " + str(self.id) + "\nIngredients: " + self.ingredients + "\nCooking time: " + str(self.cooking_time) + " minutes\nDifficulty: " + self.difficulty

def calculate_difficulty(cooking_time, ingredients):
  if cooking_time < 10 and len(ingredients) < 4:
    Recipe.difficulty = 'Easy'
  elif cooking_time < 10 and len(ingredients) >= 4:
    Recipe.difficulty = 'Medium'
  elif cooking_time >= 10 and len(ingredients) < 4:
    Recipe.difficulty = 'Intermediate'
  elif cooking_time >= 10 and len(ingredients) >= 4:
    Recipe.difficulty = 'Hard'
  return Recipe.difficulty

def return_ingredients_as_list():
  if Recipe.ingredients == '':
    return []
  else:
    return list(Recipe.ingredients.lower().split(',').strip())

Base.metadata.create_all(engine)

# create new recipe
def create_recipe():
  print()
  print('='*30)
  print('Create a New Recipe')
  print('-'*30)

  # setting the entered name as the recipe's name if under 50 characters
  name_is_valid = False
  while name_is_valid == False:
    name_input = input('Enter the name of your recipe: ')
    if len(name_input) <=50:
      name = name_input
      name_is_valid = True
    else:
      print()
      print('*'*30)
      print('The name of your recipe must be less than 50 characters. Please try again.')
      print('*'*30)
      print()

  # setting the entered ingredients as the recipe's ingredients
  ingredients = []
  num_ingredients_is_valid = False
  while num_ingredients_is_valid == False:
    number_of_ingredients = input('Enter the number of ingredients in your recipe: ')
    if number_of_ingredients.isnumeric():
      ingredient_number = 1
      while ingredient_number <= int(number_of_ingredients):
        ingredient = input('\tEnter an ingredient: ')
        ingredients.append(ingredient)
        ingredient_number +=1
      num_ingredients_is_valid = True
    else:
      print()
      print('*'*30)
      print('The number of ingredients must be a number. Please try again')
      print('*'*30)
      print()

  # setting the entered cooking time as the recipe's cooking time if a number
  cooking_time_is_valid = False
  while cooking_time_is_valid == False:
    cooking_time_input = input('Enter how long your recipe will take to make in minutes: ')
    if cooking_time_input.isnumeric():
      cooking_time = int(cooking_time_input)
      cooking_time_is_valid = True
    else:
      print()
      print('*'*30)
      print('Your cooking time must be a number. Please try again.')
      print('*'*30)
      print()

  # object based on Recipe model to add new recipe to database
  ingredients_string = ', '.join(ingredients)
  recipe_entry = Recipe(
    name = name,
    ingredients = ingredients_string,
    cooking_time = cooking_time,
    difficulty = calculate_difficulty(cooking_time, ingredients)
  )
  session.add(recipe_entry)
  session.commit()

# view all recipes
def view_all_recipes():
  print('='*30)
  print('All Recipes')
  print('-'*30)
  recipes_list = session.query(Recipe).all()
  if len(recipes_list) == 0:
    print('\n You don\t have any recipes yet! Try creating a new recipe.')
    return None
  else:
    for recipe in recipes_list:
      print(recipe)

# search recipes by ingredient
def search_by_ingredients():
  print('='*30)
  print('All Ingredients')
  print('-'*30)
  
  # check whether there are recipes to search
  if session.query(Recipe).count() == 0:
    print('\n You don\t have any recipes yet! Try creating a new recipe.')
    return None
  else:
   
    # add all ingredients to a list
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for result in results:
      ingredient_list = list(result[0].lower().split(', '))
      for ingredient in ingredient_list:
        if ingredient not in all_ingredients:
          all_ingredients.append(ingredient)
    
    # create a numbered list of ingredients
    printed_ingredients = list(enumerate(all_ingredients, 1))
    for ingredient in printed_ingredients:
      print(str(ingredient[0]) + '. ' + ingredient[1])
    
    # allow users to select ingredients to search
    try: 
      search_input = input('\nSelect the number of one or more ingredients you\'d like to search in recipes (separate numbers by a space): ')
      search_input_list = list(search_input.split(' '))
      search_ingredients = []
      for item in search_input_list:
        search_ingredients.append(all_ingredients[int(item)-1])
      print('\nThe following recipes include your selected ingredients:')
    # if the user made an invalid selection   
    except:
      print()
      print('*'*30)
      print('Ingredient number is not valid.')
      print('*'*30)
      print()
    else:
      conditions = []
      for ingredient in search_ingredients:
        like_term = '%' + ingredient + '%'
        conditions.append(Recipe.ingredients.like(like_term))
      searched_recipes = session.query(Recipe).filter(*conditions).all()
      for recipe in searched_recipes:
        print(recipe)

# edit a recipe

# delete a recipe

# main menu
def main_menu():
  choice = ''

  while(choice != 'quit'):
    print('='*30)
    print('Main Menu')
    print('-'*30)
    print('What would you like to do? Pick an option:\n')
    print('\t1. Create a new recipe.')
    print('\t2. Search for recipes that match an ingredient.')
    print('\t3. Update an existing recipe.')
    print('\t4. Delete a recipe.')
    print('\t5. View all recipes.')
    print('\nType \'quit\' to exit the program.')
    
    choice = input('\nEnter your choice here: ')
    if choice == '1':
      create_recipe()
    elif choice == '2':
      search_by_ingredients()
    # elif choice == '3':
    #   update_recipe()
    # elif choice == '4':
    #   delete_recipe()
    elif choice == '5':
      view_all_recipes()

# run program
main_menu()