prices = [120, 45, 300, 85, 150]
def get_expensive_products(prices):
   for price in prices:
       if price> 100:
              print(price)
get_expensive_products(prices)