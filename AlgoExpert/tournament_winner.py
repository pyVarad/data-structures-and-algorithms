""" There is an algorithm tournament taking place in which teams of programmers compete against each other  to solve
algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all other
teams. Only two teams compete against each other at a time, and for each competition, one team is designated the
home team, while other team is away team. In each competition there is always one winner and one loser; there are no
ties. A team receives 3 points if it wins and gets 0 points if it loses.

Given an array of pairs of representation of the teams that have competed against each other and an array containing
the results of each competition, write a function that returns the winner of the tournament. The input arrays are named
competitions and results, respectively. The competition array has elements in the form of [homeTeam, awayTeam], where
each team is a string of at most 30 characters representing the name of the team. The results array contains information
about the winner of corresponding competition in the competitions array. Specifically result[i] corresponds to
competition[i], where 1 in the results means the "home" team  in the corresponding competition won and 0 means "away"
team has won.

It's guaranteed that exactly only one team will win the tournament and that each team will compete with each other
exactly once. It's also guaranteed that the tournament will always have at least two teams.


Sample Input
------------
competitions = [
    [ "HTML", "C#" ],
    [ "C#", "Python" ],
    [ "Python", "HTML" ]
]
results = [0, 0, 1]

Sample Output
-------------
"Python"
C# beats HTML, Python beats C# and Python beats HTML
Python: 6 points
C#: 3 points
HTML: 0 points
"""


def tournament_winner(competitions, results):
    ptr = 0
    current_winner = '', 0
    scores = {}

    while ptr < len(competitions):
        winner = competitions[ptr][not results[ptr]]

        if winner not in scores: scores[winner] = 0
        scores[winner] += 3

        if scores[winner] > current_winner[1]:
            current_winner = winner, scores[winner]

        ptr += 1

    return current_winner[0]


def tournament_winner_alternative(competitions, results):
    ptr = 0
    scores = {}

    while ptr < len(competitions):
        home_team, away_team = competitions[ptr][0], competitions[ptr][1]
        if results[ptr] == 1:
            scores[home_team] = scores.get(home_team, 0) + 3
        else:
            scores[away_team] = scores.get(away_team, 0) + 3

        ptr += 1

    return sorted(scores.items(), key=lambda item: item[1], reverse=True)[0][0]


if __name__ == "__main__":
    result = tournament_winner(
        [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]],
        [0, 1, 1]
    )
    print(result)

    result = tournament_winner_alternative(
        [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]],
        [0, 1, 1]
    )
    print(result)
