# set up sqlalchemy, create engine and session
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
    print('-'*30)
    print('Recipe for ', self.name)
    print('\tIngredients: ', self.ingredients)
    print('\tCooking time: ', self.cooking_time, ' minutes')
    print('\tDifficulty: ', self.difficulty)

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
  print('='*30)
  print('Create a New Recipe')
  print('-'*30)

  # setting the entered name as the recipe's name if under 50 characters
  name_is_valid = False
  while name_is_valid == False:
    name_input = input('\tEnter the name of your recipe: ')
    if len(name_input) <=50:
      name = name_input
      name_is_valid = True
    else:
      print('*'*30)
      print('The name of your recipe must be less than 50 characters. Please try again.')
      print('*'*30)

  # setting the entered ingredients as the recipe's ingredients if under 255 characters
  ingredients_are_valid = False
  num_ingredients_is_valid = False
  ingredients = []
  ingredients_string = ', '.join(ingredients)
  while ingredients_are_valid == False:
    if len(ingredients_string) <=255:
      while num_ingredients_is_valid == False:
        number_of_ingredients = input('\tEnter the number of ingredients in your recipe: ')
        if number_of_ingredients.isnumeric():
          for ingredient in number_of_ingredients:
            ingredient = input('\t\tEnter an ingredient: ')
            ingredients.append(ingredient)
          num_ingredients_is_valid = True
        else:
          print('*'*30)
          print('The number of ingredients must be a number. Please try again')
          print('*'*30)
      ingredients_are_valid = True
    else:
      print('*'*30)
      print('Your recipe\'s list of ingredients must be less than 255 characters. Please try again.')
      print('*'*30)

  # setting the entered cooking time as the recipe's cooking time if a number
  cooking_time_is_valid = False
  while cooking_time_is_valid == False:
    cooking_time_input = input('\tEnter how long your recipe will take to make in minutes: ')
    if cooking_time_input.isnumeric():
      cooking_time = int(cooking_time_input)
      cooking_time_is_valid = True
    else:
      print('*'*30)
      print('Your cooking time must be a number. Please try again.')
      print('*'*30)

  # object based on Recipe model to add new recipe to database
  recipe_entry = Recipe(
    name = name,
    ingredients = ingredients_string,
    cooking_time = cooking_time,
    difficulty = calculate_difficulty(cooking_time, ingredients)
  )
  session.add(recipe_entry)
  session.commit()

# view all recipes

# search recipes by ingredient

# edit a recipe

# delete a recipe

# main menu
def main_menu():
  choice = ''

  while(choice != 'quit'):
    print('='*30)
    print('Main Menu')
    print('-'*30)
    print('What would you like to do? Pick an option:')
    print('\t1. Create a new recipe.')
    print('\t2. Search for recipes that match an ingredient.')
    print('\t3. Update an existing recipe.')
    print('\t4. Delete a recipe.')
    # print('\t5. View all recipes.')
    print('\nType \'quit\' to exit the program.')
    choice = input('\nEnter your choice here: ')

    if choice == '1':
      create_recipe()
    # elif choice == '2':
    #   search_recipe()
    # elif choice == '3':
    #   update_recipe()
    # elif choice == '4':
    #   delete_recipe()
    # elif choice == '5':
    #   print_recipes(conn, cursor)