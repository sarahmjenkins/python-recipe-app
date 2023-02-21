# python-recipe-app

## Description

This project is built using Python and is run through the command line.

## Features

When completed, this app will

- Enable users to create and modify recipes on a locally hosted MySQL database
- Allow users to search for recipes by ingredient
- Rate each recipe based on difficulty
- Display recipe details, including ingredients, cooking time, and difficulty, when prompted by the user

Right now this app asks users to input two numbers and returns the sum.

## App Structure

### Outer Structure

Each recipe is contained in the list `recipes_list`. Storing recipes as a list enables modification of each element, indexing, sorting, and use of any data type. All ingredients are also stored in a list called `ingredients_list`.

### Recipe Structure

This app uses dictionaries to store each recipe. Dictionaries are the best approach because they store key-value pairs, and they allow the keys and values to take any data type. Each recipe in this app is created through user input with the `take_recipe()` function and have the following format:

```python
recipe = {
  'name': 'name of the recipe as a string',
  'cooking_time': 0, # cooking time in minutes as an integer
  'ingredients': ['list', 'of', 'ingredients'],
  'difficulty': 'level of difficulty calculated by cooking time and number of ingredients`
}
```

## Running the app

After installing Python 3.8 or higher, use the command line to do the following:

```bash
git clone https://github.com/sarahmjenkins/python-recipe-app.git
cd python-recipe-app
pip3.8 install -r requirements.txt
mkvirtualenv <name new virtual environment>
python exercise_1.3/exercise_1.3.py
```
