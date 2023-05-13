class ShoppingList(object):
  def __init__(self, list_name):
    self.list_name = list_name
    self.shopping_list = []
  
  def add_item(self, item): 
    if not item in self.shopping_list:
      self.shopping_list.append(item)
      print('You successfully added ' + item + ' to your list.')
    else:
      print(item.capitalize() + ' is already on your list.')
    
  def remove_item(self, item):
    if item in self.shopping_list:
      self.shopping_list.remove(item)
      print('You successfully removed ' + item + ' from your list.')
    else:
      print(item.capitalize() + ' is not on your list.')

  def view_list(self):
    print('Here is your shopping list: ')
    print(self.shopping_list)

pet_store_list = ShoppingList('Pet Store Shopping List')

print('4.')
pet_store_list.add_item('dog food')
pet_store_list.add_item('frisbee')
pet_store_list.add_item('bowl')
pet_store_list.add_item('collars')
pet_store_list.add_item('flea collars')

print('5.')
pet_store_list.remove_item('flea collars')

print('6.')
pet_store_list.add_item('frisbee')

print('7.')
pet_store_list.view_list()



