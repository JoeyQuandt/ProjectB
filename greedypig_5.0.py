import random
import matplotlib.pyplot as plt
import numpy as np

"""
Greedy pig function
Takes a lambda function as input for strategy
"""

def greedy_pig(f1, f2, f3):
    game = 0
    turn = 0
    wins = []
    players = [
        {
            "name": "cautious",
            "strategy": f1,
            "current-points":0,
            "turn-points":0,
            "wins":[]
        },
        {
            "name": "risk taker",
            "strategy": f2,
            "current-points":0,
            "turn-points":0,
            "wins":[]
        },
        {
            "name": "boss strategy",
            "strategy": f3,
            "current-points":0,
            "turn-points":0,
            "wins":[]
        }
    ]
    
    while game < 10000:
        run = True
        roll = 0
        while run:
            # Roll the dice
            rand = random.randint(1, 6)
            # If dice rolls a 1, kill the current turn
            if rand == 1:
                players[turn]["turn-points"] = 0
                run = False
                roll = 0
            else:
                roll += 1
                if players[turn]["strategy"](players[turn]["turn-points"], roll, players[turn]["current-points"]) and players[turn]["turn-points"] + players[turn]["current-points"] < 100:
                    players[turn]["turn-points"] += rand
                else:
                    players[turn]["current-points"] += players[turn]["turn-points"]
                    players[turn]["turn-points"] = 0

        # Als punten op of boven 100 staan: game op False
        if players[turn]["current-points"] >= 100:
            game += 1
            players[turn]["wins"].append(True)
            wins.append(turn)
            # Reset points for next game
            players[0]["current-points"] = 0
            players[0]["turn-points"] = 0
            players[1]["current-points"] = 0
            players[1]["turn-points"] = 0
            players[2]["current-points"] = 0
            players[2]["turn-points"] = 0
        else:
            turn += 1
            if turn >= players.__len__():
                turn = 0
    return wins


# Strategies
strat1 = lambda cp, r, p: cp < 12
strat2 = lambda cp, r, p: cp < 33
strat3 = lambda cp, r, p: cp < 12 if p < 75 else cp < 25

# Function call
outcome = greedy_pig(strat1, strat2, strat3)

percentage1 = round(outcome.count(0) / 10000 * 100)
percentage2 = round(outcome.count(1) / 10000 * 100)
percentage3 = round(outcome.count(2) / 10000 * 100)

# Y-as
barWidth = 0.5
strategy_one = [percentage1]
strategy_two = [percentage2]
strategy_three = [percentage3]

# X-as
player_one = ['1']
player_two = ['2']
player_three = ['3']

# Bar plots
plt.bar(player_one, strategy_one, width = barWidth, color = 'red', label='Strategy 1'+' '+'('+str(percentage1)+')'+'%')
plt.bar(player_two, strategy_two, width = barWidth, color = 'grey', label='Strategy 2'+' '+'('+str(percentage2)+')'+'%')
plt.bar(player_three, strategy_three, width = barWidth, color = 'blue', label='Strategy 3'+' '+'('+str(percentage3)+')'+'%')

plt.title('Probalility of winning the pig game')
plt.legend()

# Show graphic
plt.show()

# For tests
print(percentage1)
print(percentage2)
print(percentage3)