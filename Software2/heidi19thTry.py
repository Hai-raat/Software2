
class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def info(self):
        print(f"Food: {self.name}, Calories: {self.calories}")

class Fruit(Food):
    def __init__(self, name, calories, is_sweet):
        super().__init__(name, calories)
        self.is_sweet = is_sweet

    def info(self):
        super().info()
        print(f"Sweet: {'Yes' if self.is_sweet else 'No'}")

class Vegetable(Food):
    def __init__(self, name, calories, is_leafy):
        super().__init__(name, calories)
        self.is_leafy = is_leafy

    def info(self):
        super().info()
        print(f"Leafy: {'Yes' if self.is_leafy else 'No'}")

class Store:
    def __init__(self):
        self.inventory = {}

    def add_product(self, food_obj):
        self.inventory[food_obj.name.lower()] = food_obj

    def show_inventory(self):
        print("Available Productions:")
        for Item in self.inventory.values():
            Item.info()

    def buy(self, product_name):
        name = product_name.lower()
        if name in self.inventory:
            return self.inventory[name]
        else:
            return None

class Smoothie:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

        total = 0
        for Item in ingredients:
            total += Item.calories

        self.total_calories = total

    def smoothie_info(self):
        print(f"Smoothie name: {self.name}")
        print("Ingredients: ")
        for Item in self.ingredients:
            print("- " + Item.name)
        print("Total calories: ", self.total_calories)





fish = Food("Fish", 250)
fish.info()

b = Fruit("Banana", 500, True)
b.info()

c = Vegetable("Cucumber", 250, False)
c.info()

smarket = Store()
smarket.add_product(b)
smarket.add_product(c)
smarket.add_product(Fruit("Apple", 40, True))
smarket.add_product(Fruit("Tomato", 40, False))
smarket.add_product(Vegetable("Kale", 19, True))
smarket.add_product(Vegetable("Lime", 19, False))

ingredients = []
print("Welcome to the S-Market")
smarket.show_inventory()

while True:
    i = input("Add an ingredient to your smoothie (empty to finish): ")
    if i == "":
        break

    product = smarket.buy(i)
    if product:
        ingredients.append(product)
        print(f"Added {product.name}")
    else:
        print("We dont have that here")

if len(ingredients) == 0:
    print("No ingredients were found")

smoothie = Smoothie("Best Smoothie", ingredients)
smoothie.smoothie_info()