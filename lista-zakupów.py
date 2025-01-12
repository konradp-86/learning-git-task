shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
print("Lista zakupów")
total_items = 0  
for shop, items in shopping_list.items(): 
    shop_name = shop.capitalize()  
    capitalized_items = [item.capitalize() for item in items]  
    print(f"Idę do {shop_name}, kupuję tu następujące rzeczy: {capitalized_items}.")
    total_items += len(items)
print(f"W sumie kupuję {total_items} produktów.")
