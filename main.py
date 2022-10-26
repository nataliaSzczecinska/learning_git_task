shopping_list = {
    "beker" : ["bread", "bread roll", "doughnut"],
    "greengrocery" : ["carrots", "celery", "rocket"]
}

number_of_products = 0
print("Shopping list")
for key, value in shopping_list.items():
    values = ', '.join((str(element.title()) for element in value))
    print(f"I am going to {key.title()} and buy there [{values}]")
    number_of_products = number_of_products + len(value)
print(f"I will buy {number_of_products} products")