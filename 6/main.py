import os
import regex as re

for f in[f for f in os.listdir("Uloha6\ENG")if"_i"in f]:
    file = open(f"Uloha6\ENG\{f}").read()
    kdajwkjd = file.split("\n\n")
    shop, shopping_lists = kdajwkjd[0], kdajwkjd[1:]
    shelves = re.findall(r"#\d+\n([^#]*)", shop)
    all_items = [item for shelf in shelves for item in shelf.split("\n")]
    print(all_items)
    for shopping_list in shopping_lists:
        print("\nOptimized list:")
        shopping_list = shopping_list.rstrip().split("\n")
        for i, shelf in enumerate(shelves):
            if len(shelf) == 0:
                continue
            if shelf[-1:] == "\n":
                shelf = shelf.rstrip()
            
            for item in shopping_list:
                has_exact = False
                is_in_shop = False
                for j in all_items:
                    if item.lower() == j.lower():
                        has_exact = True
                        is_in_shop = True
                        break
                    elif item.lower() in j.lower() and not has_exact:
                        is_in_shop = True
                for shelfitem in shelf.rstrip().split("\n"):
                    if item.lower() == shelfitem.lower():
                        print(f"{item} -> #{i} {shelfitem}")
                    elif item.lower() in shelfitem.lower() and not has_exact:
                        print(f"{item} -> #{i} {shelfitem}")
        for item in shopping_list:
            is_in_shop = False
            for j in all_items:
                if item.lower() == j:
                    is_in_shop = True
                    break
                elif item.lower() in j.lower():
                    is_in_shop = True
                    break
            if not is_in_shop:
                print(f"{item} -> N/A")
