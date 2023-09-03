import os
import csv
import time

MAX_WALLET = 500
ALL_DATA = [
    "D:/Dévelopement/Formation/Projet 7/data/dataset1.csv",
    "D:/Dévelopement/Formation/Projet 7/data/dataset2.csv",
]


def ask_path():
    while True:
        path_to_import = input(
            "Choisissez le document à importer:"
            + "\n-dataset1.csv\n-dataset2.csv\n\n(1/2/q)> "
        ).upper()
        if path_to_import == "1":
            return ALL_DATA[0]
        elif path_to_import == "2":
            return ALL_DATA[1]
        elif path_to_import == "Q":
            return None
        else:
            print(path_to_import + " n'est pas valide.")


def import_data(file_path):
    if not file_path:
        return None
    testing_file_path = os.path.exists(file_path)
    if testing_file_path:
        with open(file_path, newline="") as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            return [
                (name, float(value), float(profit))
                for name, value, profit in csv_reader
            ]


def find_best_combination(data_from_csv):
    if not data_from_csv:
        return None
    # ('name','price','profit')
    positive_actions = []
    best_combination = []
    for action in data_from_csv:
        if action[1] > 0:
            positive_actions.append(action)
    sorted_actions = sorted(
        positive_actions, key=lambda data: -data[2] / data[1]
    )
    total_price = 0
    for action in sorted_actions:
        total_price += action[1]
        if total_price > 500:
            break
        best_combination.append(action)
    return best_combination


def display_result(best_combination):
    total_price = sum(value for _, value, _ in best_combination)
    print(
        "Pour un total de: "
        + str(total_price)
        + " euros, vous pouvez acheter:\n"
    )
    total_profit = 0.0
    for (
        action_name,
        price,
        profit,
    ) in best_combination:
        print(
            "l'action: {}".format(action_name)
            + " a {}".format(price)
            + " euros pour un bénéfice de "
            + "{} euros".format(profit)
        )
        total_profit += float(profit)
    print(
        "\nLe total de ces "
        + str(len(best_combination))
        + " achats rapporteront: "
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
            starting_calculation = time.time()
            best_combination = find_best_combination(file)
            if not best_combination:
                return None
            display_result(best_combination)
            ending_calculation = time.time()
            print(
                "L'execution a durée: "
                + str(ending_calculation - starting_calculation)
                + " secondes."
            )
        else:
            print(ask_to_run + " n'est pas valide")


if __name__ == "__main__":
    main()
