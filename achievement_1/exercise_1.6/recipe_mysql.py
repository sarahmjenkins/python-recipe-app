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
    # print('5. View all recipes.')
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
    # elif choice == '5':
    #   print_recipes(conn, cursor)

# Option One: create recipe
def create_recipe(conn, cursor):
  
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

# Function to calculate difficulty. Used when creating or updating a recipe
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
  print('Search Recipes by Ingredient')
  print('-----------------------------')
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
      print('Difficulty: ' + row[3] + '\n')

# Option Three: update recipe
def update_recipe(conn, cursor):
  print('=============================')
  print('Update a Recipe')
  view_recipes(conn, cursor)
  
  selected_recipe = input('Select a recipe to update by entering its ID: ')
  column_to_update = input('Would you like to update the recipe\'s name, ingredients, or cooking time? ')

  if column_to_update == 'name':
    new_name = input('Enter a new name for the recipe: ')
    cursor.execute('UPDATE Recipes SET name = %s WHERE id = %s', (new_name, selected_recipe))
    print('The name of your recipe has been updated.')
  
  elif column_to_update == 'ingredients':
    # Updating the list of ingredients
    new_ingredients = input('Enter an updated list of ingredients: ')
    cursor.execute('UPDATE Recipes SET ingredients = %s WHERE id = %s', (new_ingredients, selected_recipe))
    
    # Updating the difficulty
    cursor.execute('SELECT cooking_time FROM Recipes WHERE id = %s', (selected_recipe, ))
    result = cursor.fetchall()
    cooking_time = result[0][0]
    new_ingredients_list = list(new_ingredients.lower().split(', '))
    cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s', (calc_difficulty(cooking_time, new_ingredients_list), selected_recipe))
    print('Your recipe\'s ingredients and difficulty have been updated.')
  
  elif column_to_update == 'cooking time':
    # Updating the cooking time
    new_cooking_time = int(input('Enter the updated cooking time in minutes: '))
    cursor.execute('UPDATE Recipes SET cooking_time = %s WHERE id = %s', (new_cooking_time, selected_recipe))
    
    # Updating the difficulty
    cursor.execute('SELECT ingredients FROM Recipes WHERE id = %s', (selected_recipe, ))
    result = cursor.fetchall()
    ingredients = result[0][0]
    print(ingredients)
    ingredients_list = list(ingredients.split(', '))
    cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s', (calc_difficulty(new_cooking_time, ingredients_list), selected_recipe))
    print('Your recipe\'s cooking time and difficulty have been updated.')

  conn.commit()
  print('Update saved.')

# Option Four: delete a recipe
def delete_recipe(conn, cursor):
  print('=============================')
  print('Delete a Recipe')
  view_recipes(conn, cursor)
  selected_recipe = input('Select a recipe to delete by entering its ID: ')
  cursor.execute('DELETE FROM Recipes WHERE id = %s', (selected_recipe, ))
  conn.commit()
  print('The selected recipe has been deleted.')

# View all recipes function to be used in update and delete recipe functions
def view_recipes(conn, cursor):
  cursor.execute('SELECT * FROM Recipes')
  results = cursor.fetchall()
  print('-----------------------------')
  print('Your Recipes ')
  print('-----------------------------')
  for row in results:
    print('ID:', row[0])
    print('Name: ' + row[1])
    print('Ingredients: ' + row[2])
    print('Cooking time:', row[3], 'minutes')
    print('Difficulty: ' + row[4] + '\n')

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
               
cursor.execute('ALTER TABLE Recipes MODIFY COLUMN id INT AUTO_INCREMENT;')

main_menu(conn, cursor)
