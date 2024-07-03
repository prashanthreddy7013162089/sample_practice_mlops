class FruitBasket:
    def __init__(self):
        self.fruits = []  # This is similar to our active_connections

# Using the class
my_basket = FruitBasket()
my_basket.fruits.append("apple")
my_basket.fruits.append("banana")
print(my_basket.fruits)  # Output: ['apple', 'banana']