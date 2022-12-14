from models.player_model import PModel


class RView(PModel):

    # Create a list of players
    players = []

    # Sort player list alphabetically
    players.sort(key=lambda x: x["name"])

    # Show list of players in alphabetical order
    print("\nList of players in alphabetical order :")
    for player in players:
        print(player["name"])

    # Sort player list by rating
    players_by_rank = sorted(players, key=lambda x: x["rank"])

    # Show list of players by rating
    print("\nList of players by rating :")
    for player in players_by_rank:
        print(player["name"])

    # Create a tournament list
    tournaments = []

    # Show list of all tournaments
    print("\nList of all tournaments :")
    for tournament in tournaments:
        print(tournament)

    # Create a list of rounds for a tournament
    rounds = ["First round", "Second round", "Third round", "Last round"]

    # Show the list of all rounds of a tournament
    print("\nList of all rounds of a tournament :")
    for round in rounds:
        print(round)

    # Create a match list for a tournament
    matches = []

    # Display the list of all matches in a tournament
    print("\nList of all matches in a tournament :")
    for match in matches:
        print("{} vs. {} : {}".format(match["player1"], match["player2"], match["score"]))

