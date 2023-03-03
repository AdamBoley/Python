class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "The {name} menu is available at {start_time}.00 to {end_time}.00".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
      else:
        pass
    return total
  
brunch_menu = {
  'pancakes': 7.50,
  'waffles': 9.00,
  'burger': 11.00,
  'home fries': 4.50,
  'coffee': 1.50,
  'espresso': 3.00,
  'tea': 1.00,
  'mimosa': 10.50,
  'orange juice': 3.50
}

early_bird_menu = {
    "salumeria plate": 8.00,
    "salad and breadsticks (serves 2, no refills)": 14.00,
    "pizza with quattro formaggi": 9.00,
    "duck ragu": 17.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 1.50,
    "espresso": 3.00
}

dinner_menu = {
    "crostinu with eggplant caponata": 13.00,
    "caesar salad": 16.00,
    "pizza with quattro formaggi": 12.00,
    "duck ragu": 19.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 2.00,
    "espresso": 3.00
}

kids_menu = {
    "chicken nuggets": 6.50,
    "fusilli with wild mushrooms": 12.00,
    "apple juice": 3.00
}

arepas_menu = {
  "arepa pabellon": 7.00,
  "pernil arepa": 8.50,
  "guayanes arepa": 8.00,
  "jamon arepa": 7.50
}

brunch = Menu("brunch", brunch_menu, 11, 16)

early_bird = Menu("early bird", early_bird_menu, 15, 18)

dinner = Menu("dinner", dinner_menu, 17, 23)

kids = Menu("kids", kids_menu, 11, 21)

arepas = Menu("arepas", arepas_menu, 10, 20)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "Located at {address}".format(address=self.address)
  
  def available_menus(self, time):
    menus = []
    
    for menu in self.menus:
      if menu.start_time <= time and menu.end_time >= time:
        menus.append(menu.name)
      else:
        pass

    return menus
    

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store)
print(new_installment)

print(new_installment.available_menus(22))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

business_1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas])

business_2 = Business("Take a' Arepa", [ arepas_place])

print(arepas_place)
