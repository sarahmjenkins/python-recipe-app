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

Each recipe is contained in the list `all_recipes`. Storing recipes as a list enables modification of each element, indexing, sorting, and use of any data type.

### Recipe Structure

This app uses dictionaries to store each recipe. Dictionaries are the best approach because they store key-value pairs, and they allow the keys and values to take any data type. Each recipe in this app follows the structure of `recipe_template`:

```python
recipe_template = {
  'name': 'name of the recipe as a string'
  'cooking_time': 0 # cooking time in minutes as an integer
  'ingredients': ['list', 'of', 'ingredients']
}
```

## Running the app

Using Python 3.8 or higher, use the command line to do the following:

```bash
git clone https://github.com/sarahmjenkins/python-recipe-app.git
pip3.8 install -r requirements.txt
python3.8 Exercise\ 1.1/add.py
```
