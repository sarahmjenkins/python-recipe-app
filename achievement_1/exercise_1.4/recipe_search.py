import pickle

def display_recipe(recipe):
  print('Name: ' + recipe['Name'])
  print('Cooking Time: ' + str(recipe['Cooking time']))
  print('Ingredients: ' + str(recipe['Ingredients']))
  print('Difficulty: ' + recipe['Difficulty'])

def search_ingredient(data):
  print(list(enumerate(data['all_ingredients'], 1)))

  try:
    selection = int(input('Select an ingredient\'s number: '))
    ingredient_searched = data['all_ingredients'][selection-1]
    print('The following recipes include ' + ingredient_searched + ':')
  except:
    print('Ingredient number is not valid.')
  else:
    for recipe in data['recipes_list']:
      for ingredient in recipe['Ingredients']:
        if ingredient == ingredient_searched:
          display_recipe(recipe)

filename = input('Filename where recipes are stored: ')

try: 
  recipe_file = open(filename, 'rb')
  data = pickle.load(recipe_file)
except FileNotFoundError:
  print('File not found.')
except:
  print('There has been an error accessing your recipes.')
else:
  search_ingredient(data)
finally:
  recipe_file.close()
