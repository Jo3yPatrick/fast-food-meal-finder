import json

def main():
    menu = load_menu()

    calorie_input = int(input("How many calories do you want to consume?\n"))

    filtered_list = filter_by_calories(menu, calorie_input)
    for item in filtered_list:
        print(f"{item["name"]}-"
              f"{item["calories"]}-"
              f"{item["protein"]}"
              )
        
def load_menu():
    with open("data/taco_bell.json", "r") as f:
        menu_items = json.load(f)

    return menu_items

def filter_by_calories(menu, calorie_limit):
    filtered_list = []

    for item in menu:
        calories = item["calories"]
        if calories <= calorie_limit:
            filtered_list.append(item)
         
    return filtered_list

if __name__ == "__main__":
    main()