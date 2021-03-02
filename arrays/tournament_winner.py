'''
Given an array of pairs representing the teams that have competed against each other and an array containing
the results of each competition, write a function that returns the winner of the tournament.

competitions = [
    ['HTML', 'C#'],
    ['C#', 'Python'],
    ['Python', 'HTML']
]
results = [0,0,1]
Output = 'Python'
'''


def tournamentWinner(competitions, results):

    scores = {}

    winner = ""

    for idx, team in enumerate(competitions):

        result = results[idx]
        winning_score = 0

        if result == 1:
            result = 0
        else:
            result = 1

        if team[result] not in scores:
            scores[team[result]] = 0
        scores[team[result]] += 3

        for x in scores:
            if scores[x] > winning_score:
                winning_score = scores[x]
                winner = x

    return winner


competitions = [
    ['HTML', 'C#'],
    ['C#', 'Python'],
    ['Python', 'HTML']
]

results = [0, 0, 1]

print(tournamentWinner(competitions, results))
