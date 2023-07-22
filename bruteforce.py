import itertools

MAX_WALLET = 500

# All action name with price and profit rate
available_action = {
    "Action-1": [20, 5],
    "Action-2": [30, 10],
    "Action-3": [50, 15],
    "Action-4": [70, 20],
    "Action-5": [60, 17],
    "Action-6": [80, 25],
    "Action-7": [22, 7],
    "Action-8": [26, 11],
    "Action-9": [48, 13],
    "Action-10": [34, 27],
    "Action-11": [42, 17],
    "Action-12": [110, 9],
    "Action-13": [38, 23],
    "Action-14": [14, 1],
    "Action-15": [18, 3],
    "Action-16": [8, 8],
    "Action-17": [4, 12],
    "Action-18": [10, 14],
    "Action-19": [24, 21],
    "Action-20": [114, 18],
}


def convert_profit_rate(all_action):
    converted = []
    for action_name, amount in all_action.items():
        converted.append(
            [action_name, amount[0], (amount[1] * amount[0] / 100)]
        )
    return converted


# On ne stock rien, doit renvoie juste des combinaisons
def generate_all_combinations(all_action_converted):
    for combination_length in range(1, len(all_action_converted) + 1):
        for combination in itertools.combinations(
            all_action_converted, combination_length
        ):
            combination_price_total = 0
            for _, price, _ in combination:
                combination_price_total += price
            if combination_price_total <= MAX_WALLET:
                yield combination


def compare_all_combinations(all_combination_converted):
    best_combination = None
    best_profit = 0
    for combination in generate_all_combinations(all_combination_converted):
        profits = 0.0
        for action in combination:
            profits += action[2]
        if profits > best_profit:
            best_combination = combination
            best_profit = profits
    return best_combination, best_profit


def display_action_to_buy(best_combination, best_profit):
    print("La meilleure combinaison trouvée est:\n")
    profit = int(best_profit)
    total_price = 0
    for action in best_combination:
        print(action[0])
        total_price += action[1]
    print(
        "\nCette ensemble vous coutera: {} euros,".format(total_price)
        + "\npour un bénéfice total de {} euros sur 2 ans".format(profit)
    )


def main():
    all_action_converted = convert_profit_rate(available_action)
    best_combination, best_profit = compare_all_combinations(
        all_action_converted
    )
    display_action_to_buy(best_combination, best_profit)


main()
