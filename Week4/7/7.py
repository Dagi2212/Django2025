import json
from pathlib import Path
data=Path("Django2025/Week4/7/products.json").read_text()
products=json.loads(data)
print("Product Name: ",products[0]["product"])
print("Product Price: ",products[0]["price"])
