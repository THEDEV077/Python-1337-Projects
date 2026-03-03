import sys


def ft_split(text: str, sep: str) -> list[str]:
    text_splited: list[str] = []
    index: int = 0
    for c in text:
        if c == sep:
            text_splited += [text[:index]]
            text_splited += [text[index + 1:]]
            break
        index += 1
    return text_splited


def ft_atoi(nb: str) -> int:
    num = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    index: int = 0
    sign: int = 1
    result: int = 0
    if nb and (nb[0] == '-' or nb[0] == '+'):
        if nb[index] == '-':
            sign = -1
        index = 1
    for c in nb[index:]:
        if c not in num:
            raise ValueError("Not valid number")
        result = result * 10 + num[c]
    return result * sign


def item_mean(items: dict, name: str) -> float:
    total: int = 0
    for item in items:
        total += items[item]
    return items[name] / total * 100


def max_item(items: dict) -> str:
    max: str
    for f in items:
        max = f
        break
    for item in items:
        if items[max] < items[item]:
            max = item
    return max


def min_item(items: dict) -> str:
    min: str
    for f in items:
        min = f
        break
    for item in items:
        if items[min] > items[item]:
            min = item
    return min


def lookup(items: dict, name: str) -> bool:
    for item in items:
        if item == name:
            return True
    return False


def print_dict(parsed: dict, mode: str) -> None:
    len_dict: int = len(parsed.keys())
    count: int = 0
    if mode == "keys":
        for key in parsed:
            count += 1
            if len_dict == count:
                print(key)
            else:
                print(key, end=", ")
    elif mode == "values":
        for value in parsed.values():
            count += 1
            if count == len_dict:
                print(value)
            else:
                print(value, end=", ")
    else:
        print("Invalid mode")


if __name__ == "__main__":
    try:
        print("=== Inventory System Analysis ===")
        parsed: dict = dict()
        for arg in sys.argv[1:]:
            text_splited = ft_split(arg, ":")
            if len(text_splited) != 2:
                raise ValueError(f"Invalid argument format: {arg}")
            parsed[f"{text_splited[0]}"] = ft_atoi(text_splited[1])

        total: int = 0

        categories: dict = {
            "moderate": dict(),
            "scarce": dict()
        }

        restock: list = []

        for item in parsed:
            total += parsed[item]
            if item_mean(parsed, item) > 40:
                categories["moderate"][item] = parsed[item]
            else:
                categories["scarce"][item] = parsed[item]
            if parsed[item] < 2:
                restock += [item,]

        print(f"Total items in inventory: {total}")
        print(f"Unique item types: {len(parsed.keys())}")

        print("\n=== Current Inventory ===")
        items_list: list = ["potion", "armor", "shield", "sword", "helmet"]
        for item1 in items_list:
            if (item1 not in parsed.keys()):
                raise KeyError(f"KeyError: '{item1}'")
            value: float = item_mean(parsed, item1)
            if parsed[item1] != 1:
                print(f"{item1}: {parsed.get(item1)} units ({value:.1f}%)")
            else:
                print(f"{item1}: {parsed.get(item1)} unit ({value:.1f}%)")

        print("\n=== Inventory Statistics ===")
        max: str = max_item(parsed)
        min: str = min_item(parsed)
        print(f"Most abundant: {max} ({parsed[max]} units)")
        print(f"Least abundant: {min} ({parsed[min]} unit)")

        print("\n=== Item Categories ===")
        print(f"Moderate: {categories["moderate"]}")
        print(f"Scarce: {categories["scarce"]}")

        print("\n=== Management Suggestions ===")
        print("Restock needed: ", end="")
        len_res: int = len(restock)
        count: int = 0
        for i in restock:
            count += 1
            if len_res == count:
                print(f"{i}")
            else:
                print(f"{i}, ", end="")

        print("\n=== Dictionary Properties Demo ===")
        len_dict: int = len(parsed.keys())
        count: int = 0

        print("Dictionary keys: ", end="")
        print_dict(parsed, "keys")
        print("Dictionary values: ", end="")
        print_dict(parsed, "values")
        print(
            f"Sample lookup - 'sword' in inventory: {lookup(parsed, 'sword')}")
    except Exception as e:
        print(e)
