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


def find_positive_actions(data_from_csv):
    if not data_from_csv:
        return None
    # ('name','price','profit')
    positive_actions = []
    for action in data_from_csv:
        if action[1] > 0:
            # need to convert price and profit by 100 to conserve it,
            # because all numbers are float(), and need to have integers
            positive_actions.append(
                [action[0], int(action[1] * 100), int(action[2] * 100)]
            )
    return positive_actions


def etablish_matrix(positive_actions, wallet, number_of_actions):
    # Drawing an empty matrix
    matrix = [
        [0 for _ in range(wallet + 1)] for _ in range(number_of_actions + 1)
    ]
    for action_idx in range(0, number_of_actions + 1):
        for capacity in range(0, wallet + 1):
            # if the buying price is less than current wallet capacity
            if positive_actions[action_idx - 1][1] <= capacity:
                matrix[action_idx][capacity] = max(
                    positive_actions[action_idx - 1][2]
                    + matrix[action_idx - 1][
                        capacity - int(positive_actions[action_idx - 1][1])
                    ],
                    matrix[action_idx - 1][capacity],
                )
            else:
                matrix[action_idx][capacity] = matrix[action_idx - 1][capacity]
    return matrix


def find_best_combination(positive_actions):
    recalulating_wallet = MAX_WALLET * 100
    total_of_actions = len(positive_actions)
    matrix = etablish_matrix(
        positive_actions, recalulating_wallet, total_of_actions
    )
    best_combination = []
    while recalulating_wallet >= 0 and total_of_actions >= 0:
        combination = positive_actions[total_of_actions - 1]
        if (
            matrix[total_of_actions][recalulating_wallet]
            == matrix[total_of_actions - 1][
                recalulating_wallet - combination[1]
            ]
            + combination[2]
        ):
            best_combination.append(combination)
            recalulating_wallet -= combination[1]
        total_of_actions -= 1
    return (matrix[-1][-1], best_combination)


def display_result(best_combination):
    total_price = sum(value for _, value, _ in best_combination[1])
    print(
        "Pour un total de: "
        + str(float(total_price) / 100)
        + " euros, vous pouvez acheter:\n"
    )
    total_profit = 0.0
    for (
        action_name,
        price,
        profit,
    ) in best_combination[1]:
        print(
            "l'action: {}".format(action_name)
            + " a {}".format(float(price) / 100)
            + " euros pour un bénéfice de "
            + "{} euros".format(float(profit) / 100)
        )
        total_profit += float(profit / 100)
    print(
        "\nLe total de ces "
        + str(len(best_combination[1]))
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
            positive_actions = find_positive_actions(file)
            if not positive_actions:
                return None
            starting_calculation = time.time()
            best_combination = find_best_combination(positive_actions)
            display_result(best_combination)
            ending_calculation = time.time()
            print(
                "L'execution à durée: "
                + str(ending_calculation - starting_calculation)
                + " secondes."
            )
        else:
            print(ask_to_run + " n'est pas valide")


if __name__ == "__main__":
    main()
