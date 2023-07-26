import os
import csv

MAX_WALLET = 500
ALL_DATA = [
    "D:/Dévelopement/Formation/Projet 7/data/dataset1.csv",
    "D:/Dévelopement/Formation/Projet 7/data/dataset2.csv",
]


def ask_path():
    while True:
        path_to_import = input("Choisissez-le document à importer (1/2):\n>")
        if path_to_import == "1":
            return ALL_DATA[0]
        elif path_to_import == "2":
            return ALL_DATA[1]
        else:
            print(path_to_import + " n'est pas valide.")


def import_data(file_path):
    testing_file_path = os.path.exists(file_path)
    if testing_file_path:
        with open(file_path, newline="") as csvfile:
            csv_reader = csv.reader(csvfile)
            csv_reader = list(csv_reader)
            csv_reader.remove(["name", "price", "profit"])
            return csv_reader


def define_total_price(data):
    total = 0.0
    for line in data:
        try:
            price = float(line[1])
        except TypeError:
            print("Il y a une erreur d'import")
        total += price
    return total


def compare(first_element, second_element):
    # SI le prix du premier élément est inf au deuxième et sont benef sup
    if (
        first_element[1] < second_element[1]
        and first_element[2] > second_element[2]
    ):
        return first_element
    # SI le prix du premier élément est inf au deuxième et sont benef égal
    elif (
        first_element[1] < second_element[1]
        and first_element[2] == second_element[2]
    ):
        return first_element
    # SI le prix du premier élément est sup au deuxième et sont benef sup
    elif (
        first_element[1] > second_element[1]
        and first_element[2] > second_element[2]
    ):
        return first_element
    # SI le prix du premier élément est égal au deuxième et sont benef sup
    elif (
        first_element[1] == second_element[1]
        and first_element[2] > second_element[2]
    ):
        return first_element
    else:
        return second_element


def found_best_combination(data_from_csv):
    total_price = define_total_price(data_from_csv)
    all_actions_remains = data_from_csv.copy()
    index = 0
    while total_price > MAX_WALLET:
        total_price = define_total_price(all_actions_remains)
        if total_price <= MAX_WALLET:
            return all_actions_remains
        try:
            first_element = all_actions_remains[index]
            print("first = " + str(first_element) + "\n")
            second_element = all_actions_remains[index + 1]
            print("second = " + str(second_element) + "\n")
        except IndexError:
            index = 0
            continue
        best_of_two = compare(first_element, second_element)
        print("best_of_two = " + str(best_of_two) + "\n")
        if best_of_two == first_element:
            all_actions_remains.remove(second_element)
        else:
            all_actions_remains.remove(first_element)
        index += 1
        print("taille de la liste: " + str(len(all_actions_remains)) + "\n")
    return all_actions_remains


def display_result(best_combination):
    total_price = define_total_price(best_combination)
    print(
        "Pour un total de: "
        + str(total_price)
        + " euros, vous pouvez acheté:\n"
    )
    total_profit = 0.0
    for action_name, price, profit in best_combination:
        print(
            "l'action: "
            + action_name
            + " à "
            + price
            + " euros pour un bénéfice de "
            + profit
            + " euros"
        )
        total_profit += float(profit)
    print(
        "\nLe total de ces "
        + str(len(best_combination))
        + " achats vous rapporterons: "
        + str(total_profit)
        + " euros."
    )


def main():
    ask_to_run = None
    while ask_to_run != "N":
        ask_to_run = input(
            "\nVoulez-vous lancer une analyse?\n(y/n)> "
        ).capitalize()
        if ask_to_run == "N":
            break
        elif ask_to_run == "Y":
            path = ask_path()
            file = import_data(path)
            best_combination = found_best_combination(file)
            display_result(best_combination)
        else:
            print(ask_to_run + " n'est pas valide")


if __name__ == "__main__":
    main()
