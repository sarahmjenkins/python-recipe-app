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
  id INT PRIMARY KEY,
  name VARCHAR(50),
  ingredients VARCHAR(255),
  cooking_time INT,
  difficulty VARCHAR(20)
)''')

# Main Menu
def main_menu(conn, cursor):
  choice = ''
  
  while(choice != 'quit'):
    print('-----------------------------')
    print('Main Menu')
    print('-----------------------------')
    print('What would you like to do? Pick an option:')
    print('1. Create a new recipe.')
    print('2. Search for recipes that match an ingredient.')
    print('3. Update an existing recipe.')
    print('4. Delete a recipe.')
    print('Type "quit" to exit the program.')
    choice = input('Enter your choie here: ')

    if choice == '1':
      create_recipe(conn, cursor)
    elif choice == '2':
      search_recipe(conn, cursor)
    elif choice == '3':
      update_recipe(conn, cursor)
  
  if(choice == 'quit'):
    quit_program(conn, cursor)

# Option One: create recipe
def create_recipe(conn, cursor):
  def calc_difficulty(cooking_time, ingredients_list):
    if cooking_time < 10 and ingredients_list < 4:
      difficulty = 'Easy'
    elif cooking_time < 10 and ingredients_list >= 4:
      difficulty = 'Medium'
    elif cooking_time >= 10 and ingredients_list < 4:
      difficulty = 'Intermediate'
    elif cooking_time >= 10 and ingredients_list >= 4:
      difficulty = 'Hard'
    return difficulty
  
  print('-----------------------------')
  print('Create a new recipe')
  print('-----------------------------')
  name = input('Enter the name of your recipe: ')
  ingredients_string = input('Enter a list of ingredients, separated by commas: ')
  ingredients_list = list(ingredients_string.lower().split(', '))
  cooking_time = input('Enter how long your recipe takes to make in minutes: ')
  difficulty = calc_difficulty(cooking_time, ingredients_list)

  sql = 'INSERT INTO Recipes(name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
  val = (name, ingredients_string, cooking_time, difficulty)

  cursor.execute(sql, val)

  conn.commit()
  print('Your recipe is saved to the database.')



# Option Two: search for ingredient
def search_recipe(conn, cursor):
  return print('done')

# Option Three: update recipe
def update_recipe(conn, cursor):
  return print('done')

# Option Four: delete a recipe
def delete_recipe(conn, cursor):
  return print('done')

# Option Five: quit
def quit_program(conn, cursor):
  return print('done')

# Main menu
