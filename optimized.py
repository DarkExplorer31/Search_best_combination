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
            "Choisissez-le document à importer:"
            + "\n-dataset1\n-dataset2\n\n(1/2/q)> "
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


def drawing_table(positive_actions):
    # Drawing an empty table
    table = [
        [(0, []) for cell in range((MAX_WALLET * 100) + 1)]
        for cell in range(len(positive_actions) + 1)
    ]
    for action in range(1, len(positive_actions) + 1):
        for index in range(1, (MAX_WALLET * 100) + 1):
            # if the buying price is less than current wallet capacity
            if positive_actions[action - 1][1] <= index:
                if (
                    positive_actions[action - 1][2]
                    + table[action - 1][
                        index - positive_actions[action - 1][1]
                    ][0]
                    > table[action - 1][index][0]
                ):
                    table[action][index] = (
                        positive_actions[action - 1][2]
                        + table[action - 1][
                            index - positive_actions[action - 1][1]
                        ][0],
                        [positive_actions[action - 1]]
                        + table[action - 1][
                            index - positive_actions[action - 1][1]
                        ][1],
                    )
                else:
                    table[action][index] = table[action - 1][index]
            else:
                table[action][index] = table[action - 1][index]
    return table[-1][-1]


def display_result(best_combination):
    total_price = sum(value for _, value, _ in best_combination[1])
    print(
        "Pour un total de: "
        + str(float(total_price) / 100)
        + " euros, vous pouvez acheté:\n"
    )
    total_profit = 0.0
    for (
        action_name,
        price,
        profit,
    ) in best_combination[1]:
        print(
            "l'action: {}".format(action_name)
            + " à {} ".format(float(price) / 100)
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
            best_combination = drawing_table(positive_actions)
            display_result(best_combination)
            ending_calculation = time.time()
            print(
                "L'execution à durée: "
                + str(ending_calculation - starting_calculation)
            )
        else:
            print(ask_to_run + " n'est pas valide")


if __name__ == "__main__":
    main()
