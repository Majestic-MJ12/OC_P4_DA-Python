# this is the player controller
# importing what is needed
from models.player_model import PModel
import datetime
from operator import itemgetter


# the controller for the players
class PController:
    # list
    """players_list = [[1, "tttt", "thffhfg", 12-12-2022, "f", 1, 3], [2, "yyyy", "fhffhfg", 12-12-2022, "f", 1, 8],
                    [3, "aaa", "rehffhfg", 12-12-2022, "f", 1, 2], [4, "bbb", "fhffhfg", 12-12-2022, "f", 1, 2],
                    [5, "uuu", "bhffhfg", 12-12-2022, "f", 1, 2], [6, "ggg", "fhffhfg", 12-12-2022, "f", 1, 2],
                    [7, "ff", "fhffhfg", 12 - 12 - 2022, "f", 1, 2],
                    [8, "ffd", "fhffhfg", 12-12-2022, "f", 1, 2]]"""
    players_list = []

    @staticmethod
    def creation_player(players_list):
        """function to create new players"""
        # Asking players data
        cpt_player = len(players_list)
        for i in range(1, 9):
            print("Player ", i, " information: ")
            PModel.id_player = cpt_player + 1
            PModel.lastname = input("Enter the player's last name : ")
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

            PModel.gender = input("Enter player's gender (f/m): ")
            while PModel.gender.lower() not in ['f', 'm']:
                PModel.gender = input("\nInvalid input. Enter player's gender (f/m): ")
            PModel.score = 0
            PModel.rank = 0

            player = [PModel.id_player, PModel.lastname, PModel.firstname, PModel.birth, PModel.gender,
                      PModel.score, PModel.rank]
            players_list.append(player)
            cpt_player = cpt_player + 1

    @staticmethod
    def modification_player(players_list):
        """function to modify a player"""
        player_id = int(input("Enter the ID of the player you want to modify: "))

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
        if player_rank > 8:
            player_rank = 8

        # Update the player's rank
        player[6] = player_rank

        players_list.insert(player_rank, players_list[player_id - 1])
        players_list.pop(player_id - 1)

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
