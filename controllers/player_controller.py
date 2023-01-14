# this is the player controller
# importing what is needed
from models.player_model import PModel
import datetime
from operator import itemgetter


# the controller for the players
class PController:
    # list
    """players_list = [[1, "tttt", "thffhfg", 12-12-2022, "f", 0, 0], [2, "yyyy", "fhffhfg", 12-12-2022, "f", 0, 0],
                    [3, "aaa", "rehffhfg", 12-12-2022, "f", 0, 0], [4, "bbb", "fhffhfg", 12-12-2022, "f", 0, 0],
                    [5, "uuu", "bhffhfg", 12-12-2022, "f", 0, 0], [6, "ggg", "fhffhfg", 12-12-2022, "f", 0, 0],
                    [7, "ff", "fhffhfg", 12 - 12 - 2022, "f", 0, 0],
                    [8, "ffd", "fhffhfg", 12-12-2022, "f", 0, 0], [9, "ffd", "fhffhfg", 12-12-2022, "f", 0, 0]]"""
    players_list = []

    @staticmethod
    def creation_player(players_list):
        """function to create new players"""
        # Asking players data
        cpt_player = len(players_list)

        print("\nPlayer " + str(int(len(players_list) + 1)) + " information: ")
        PModel.id_player = cpt_player + 1
        PModel.lastname = input("Enter the player last name: ")
        PModel.firstname = input("Enter the player's first name : ")
        while True:
            try:
                PModel.birth = input("Enter the player's date of birth, "
                                     "it must be entered like this => YYYY-MM-DD: ")
                PModel.birth = datetime.datetime.strptime(PModel.birth, '%Y-%m-%d')
                date_str = PModel.birth.strftime("%B %d, %Y")
                PModel.birth = date_str
            except ValueError:
                print("\nSorry, that is not a valid date. Please try again.")
            else:
                break

        PModel.gender_input = input("Enter player's gender (f/m): ")
        while PModel.gender_input.lower() not in ['f', 'm']:
            PModel.gender = input("\nInvalid input. Enter player's gender (f/m): ")
        PModel.gender = PModel.gender_input
        PModel.score = 0
        PModel.rank = 0

        player = [PModel.id_player, PModel.lastname, PModel.firstname, PModel.birth, PModel.gender,
                  PModel.score, PModel.rank]
        players_list.append(player)

    @staticmethod
    def modification_player(players_list):
        """function to modify a player"""

        player_id = int(input("\nEnter the ID of the player you want to modify (rank input): "))

        # Find the player in the list
        player = None
        for p in players_list:
            if p[0] == player_id:
                player = p
                break

        # If the player was not found, display an error message
        if player is None:
            print("Player not found.")
            return

        # Get the new player rank from the user
        player_rank = int(input("Enter the new player rank: "))
        while player_rank <= 0:
            player_rank = int(input("Enter the new player rank positive: "))
        if player_rank > len(players_list) + 1:
            player_rank = len(players_list) + 1

        # Update the player's rank
        player[6] = player_rank

        index = players_list.index(player)
        players_list.pop(index)
        players_list.insert(player_rank - 1, player)

        """REZ rang de tous les joueurs"""
        for i in range(len(players_list)):
            players_list[i][6] = i + 1

    @staticmethod
    def player_rank_sort(players_list):
        """function to sort player by their rank"""

        players_list.sort(key=itemgetter(6))

        return players_list

    @staticmethod
    def player_alpha_sort(players_list):
        """function to sort players alphabetical order"""

        # Create a new sorted list from the original list
        players_list.sort(key=itemgetter(1))

        # Return the new sorted list
        return players_list

    @staticmethod
    def player_score_sort(players_list):
        """function to sort player by their rank"""

        players_list.sort(key=itemgetter(5, 6))

        return players_list

    @staticmethod
    def player_id_sort(players_list):
        """function to sort players id order"""

        # Create a new sorted list from the original list
        players_list.sort(key=itemgetter(0))

        # Return the new sorted list
        return players_list
