shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]}
print("Lista zakupów")
total_items = 0
for shop, items in shopping_list.items():
    shop_name = shop.capitalize()
    capitalized_items = [item.capitalize() for item in items]
    print(f"Idę do {shop_name}, kupuję tu następujące rzeczy: {capitalized_items}.")
    total_items += len(items)
print(f"W sumie kupuję {total_items} produktów.")
print("\n" * 3)
name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
name_dictionary = {name: len(name) for name in name_list}
print("Lista Imion:", name_dictionary)
print("\n" * 3)
def print_gwiazdka(lines):
    gwiazdka = 2
    for i in range(1, lines + 1):
        print('*' * gwiazdka)
        if i % 2 == 0:
            gwiazdka += 2
print_gwiazdka(6)
