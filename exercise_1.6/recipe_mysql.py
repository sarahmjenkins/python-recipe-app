# Main Menu
def main_menu(conn, cursor):
  choice = ''

  while(choice != 'quit'):
    print('=============================')
    print('Main Menu')
    print('-----------------------------')
    print('What would you like to do? Pick an option:')
    print('1. Create a new recipe.')
    print('2. Search for recipes that match an ingredient.')
    print('3. Update an existing recipe.')
    print('4. Delete a recipe.')
    print('5. View all recipes.')
    print('Type \'quit\' to exit the program.')
    choice = input('Enter your choice here: ')

    if choice == '1':
      create_recipe(conn, cursor)
    elif choice == '2':
      search_recipe(conn, cursor)
    elif choice == '3':
      update_recipe(conn, cursor)
    elif choice == '4':
      delete_recipe(conn, cursor)
    elif choice == '5':
      print_recipes(conn, cursor)

# Option One: create recipe
def create_recipe(conn, cursor):
  def calc_difficulty(cooking_time, ingredients_list):
    if cooking_time < 10 and len(ingredients_list) < 4:
      difficulty = 'Easy'
    elif cooking_time < 10 and len(ingredients_list) >= 4:
      difficulty = 'Medium'
    elif cooking_time >= 10 and len(ingredients_list) < 4:
      difficulty = 'Intermediate'
    elif cooking_time >= 10 and len(ingredients_list) >= 4:
      difficulty = 'Hard'
    return difficulty
  
  print('=============================')
  print('Create a New Recipe')
  print('-----------------------------')
  name = input('Enter the name of your recipe: ')
  ingredients_string = input('Enter a list of ingredients, separated by commas: ')
  ingredients_list = list(ingredients_string.lower().split(', '))
  cooking_time = int(input('Enter how long your recipe takes to make in minutes: '))
  difficulty = calc_difficulty(cooking_time, ingredients_list)
  print("Difficulty: " + difficulty)

  sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
  val = (name, ingredients_string, cooking_time, difficulty)

  cursor.execute(sql, val)
  conn.commit()
  print('Your recipe is saved to the database.')

# Option Two: search for ingredient
def search_recipe(conn, cursor):
  all_ingredients = []
 
  cursor.execute('SELECT ingredients FROM Recipes')
  results = cursor.fetchall()

  for recipe in results:
    ingredients = recipe[0].split(', ')
    for ingredient in ingredients:
      if ingredient not in all_ingredients:
        all_ingredients.append(ingredient)
  
  print('=============================')
  print('All Ingredients')
  print('-----------------------------')
  
  printed_ingredients = list(enumerate(all_ingredients, 1))
  for ingredient in printed_ingredients:
    print(str(ingredient[0]) + '. ' + ingredient[1])
  
  try:
    selection = int(input('Select an ingredient\'s number: '))
    search_ingredient = all_ingredients[selection-1]
    print('\nThe following recipes include ' + search_ingredient + ':')
  except:
    print('Ingredient number is not valid.')
  else:
    cursor.execute('SELECT name, ingredients, cooking_time, difficulty FROM Recipes WHERE ingredients LIKE %s', ('%' + search_ingredient + '%', ))
    search_results = cursor.fetchall()
    for row in search_results:
      print('Name: '  + row[0])
      print('Ingredients: ' + row[1])
      print('Cooking time:', row[2], 'minutes')
      print('Difficulty: ' + row[3])
      print()

# Option Three: update recipe
def update_recipe(conn, cursor):
  return print('done')

# Option Four: delete a recipe
def delete_recipe(conn, cursor):
  return print('done')

# Option Five: print all recipes
def print_recipes(conn, cursor):
  cursor.execute('SELECT id, name, ingredients, cooking_time, difficulty FROM Recipes')
  results = cursor.fetchall()

  for row in results:
    print('ID:', row[0])
    print('Name:', row[1])
    print('Ingredients:', row[2])
    print('Cooking time:', row[3], 'minutes')
    print('Difficulty:', row[4])

# Running the script
import mysql.connector

conn = mysql.connector.connect(
  host='localhost',
  user='cf-python',
  passwd='password'
)
cursor = conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS task_database')
cursor.execute('USE task_database')

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  ingredients VARCHAR(255),
  cooking_time INT,
  difficulty VARCHAR(20)
)''')

main_menu(conn, cursor)
