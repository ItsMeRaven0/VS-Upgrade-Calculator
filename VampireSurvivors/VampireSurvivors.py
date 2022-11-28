import os
os.system('cls' if os.name == 'nt' else 'clear')

upgrades = {
    "MoveSpeed": [2, 300],
    "Speed": [2, 300],
    "Area": [2, 300],
    "Duration": [2, 300],
    "Magnet": [2, 300],

    "Recovery": [5, 200],
    "Might": [5, 200],
    "Greed": [5, 200],

    "Banish": [5, 100],
    "Skip": [5, 100],

    "Luck": [3, 600],
    "Armor": [3, 600],

    "Max Health": [3, 200],
    
    "Curse": [5, 1666],

    "Omni": [5, 1000],

    "Growth": [5, 900],

    "Reroll": [4, 1000],

    "Cooldown":  [2, 900],

    "Revival": [1, 10000],

    "Amount": [1, 5000]

}
costs = {}

level = {
    "lvl1": 1,
    "lvl2": 2,
    "lvl3": 1.5,
    "lvl4": 1.333,
    "lvl5": 1.25
}

def cost_of_upgrade_itself_estimate(upgrade):
    cost = 0
    current_upgrades = 0
    x = 1
    while x <= upgrades[upgrade][0]:
        cost = cost + upgrades[upgrade][1] * (level["lvl" + str(x)])
        current_upgrades = current_upgrades + 1 
        x = x + 1
        continue
    return cost

def estimate_total():
    estimate_total = 0
    for upgrade in upgrades:
        estimate_total = estimate_total + cost_of_upgrade_itself_estimate(upgrade)
    return estimate_total

def cost_of_upgrade_itself_true(upgrade):
    cost_total = ((estimate_total() * 51) - ((estimate_total() - cost_of_upgrade_itself_estimate(upgrade)) * (51 - upgrades[upgrade][0]))) / cost_of_upgrade_itself_estimate(upgrade)
    return cost_total

def upgrade_order():
    for upgrade in upgrades:
        costs[upgrade] = cost_of_upgrade_itself_true(upgrade)
    upgrade_order = []
    for upgrade in {k: v for k, v in sorted(costs.items(), key=lambda item: item[1], reverse=True)}:
            upgrade_order.insert(0, upgrade)
    return upgrade_order

def cost_of_upgrade_itself_exact(upgrade, total_upgrades):
    cost = 0
    current_upgrades = 0
    x = 1
    while x <= upgrades[upgrade][0]:
        cost = cost + upgrades[upgrade][1] * (level["lvl" + str(x)] + 0.1 * total_upgrades + 0.1 * total_upgrades * current_upgrades)
        current_upgrades = current_upgrades + 1 
        x = x + 1
        continue
    return cost

def total_cost():
    total_cost = 0
    total_upgrades = 0
    for upgrade in upgrade_order():
        total_cost = total_cost + cost_of_upgrade_itself_exact(upgrade, total_upgrades)
        total_upgrades = total_upgrades + upgrades[upgrade][0]
    return total_cost

def order_of_operations():
    check_list = []
    print()
    print("Order of Upgrades")
    print()
    for upgrade in upgrade_order():
        if costs[upgrade] not in check_list:
            check_list.append(costs[upgrade])
            print("----------")
        print(upgrade)
    print()
    print()
    print()
    print("Upgrade Cost")
    print()
    print("the (minimum) cost of all upgrades is about: ", total_cost(), " Gold.")
    print()
    print()
    print()

order_of_operations()