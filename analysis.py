import os
import csv

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


def find_nb_actions(data):
    print("Sur ce jeu de donnée, vous avez: \n")
    neg = []
    equal_to_0 = []
    zero_to_10 = []
    ten_to_20 = []
    twenty_and_30 = []
    more = []
    for action in data:
        if action[1] < 0.0:
            neg.append(action)
        elif action[1] == 0.0:
            equal_to_0.append(action)
        elif action[1] > 0.0 and action[1] <= 10.0:
            zero_to_10.append(action)
        elif action[1] > 10.0 and action[1] <= 20.0:
            ten_to_20.append(action)
        elif action[1] > 20.0 and action[1] <= 30.0:
            twenty_and_30.append(action)
        else:
            more.append(action)
    print(
        "Il y a dans ce jeu de données:\n"
        + str(len(neg))
        + " actions négatives\n"
        + str(len(equal_to_0))
        + " actions égales à 0\n"
        + str(len(zero_to_10))
        + " actions entre 0 et 10 euros\n"
        + str(len(ten_to_20))
        + " actions entre 10 et 20 euros\n"
        + str(len(twenty_and_30))
        + " actions entre 20 et 30 euros\n"
        + str(len(more))
        + " actions qui dépassent les 30 euros de prix d'achats.\n\n"
    )
    neg = []
    equal_to_0 = []
    zero_to_10 = []
    ten_to_20 = []
    twenty_and_30 = []
    more = []
    for action in data:
        if action[2] < 0.0:
            neg.append(action)
        elif action[2] == 0.0:
            equal_to_0.append(action)
        elif action[2] > 0.0 and action[2] <= 10.0:
            zero_to_10.append(action)
        elif action[2] > 10.0 and action[2] <= 20.0:
            ten_to_20.append(action)
        elif action[2] > 20.0 and action[2] <= 30.0:
            twenty_and_30.append(action)
        else:
            more.append(action)
    print(
        "Et pour le profit:\n"
        + str(len(neg))
        + " actions négatives\n"
        + str(len(equal_to_0))
        + " actions égales à 0\n"
        + str(len(zero_to_10))
        + " actions entre 0 et 10 euros\n"
        + str(len(ten_to_20))
        + " actions entre 10 et 20 euros\n"
        + str(len(twenty_and_30))
        + " actions entre 20 et 30 euros\n"
        + str(len(more))
        + " actions qui dépassent les 30 euros de bénéfice.\n"
        + "Pour un total de: "
        + str(
            len(neg)
            + len(equal_to_0)
            + len(zero_to_10)
            + len(ten_to_20)
            + len(twenty_and_30)
            + len(more)
        )
        + " actions.\n"
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
            find_nb_actions(file)


if __name__ == "__main__":
    main()
