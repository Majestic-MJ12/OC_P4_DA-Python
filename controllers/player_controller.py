# this is the player controller
# importing what is needed
from models.player_model import PModel
from datetime import datetime
from operator import itemgetter


# the controller for the players
class PController:
    # list
    players_list = [[1, "tttt", "fhffhfg", 12-12-2022, "f", 1, 2], [2, "yyyy", "fhffhfg", 12-12-2022, "f", 1, 2],
                    [3, "aaa", "fhffhfg", 12-12-2022, "f", 1, 2], [4, "dfhgdf", "fhffhfg", 12-12-2022, "f", 1, 2],
                    [5, "dfhgdf", "fhffhfg", 12-12-2022, "f", 1, 2], [6, "dfhgdf", "fhffhfg", 12-12-2022, "f", 1, 2],
                    [7, "dfhgdf", "fhffhfg", 12 - 12 - 2022, "f", 1, 2],
                    [8, "dfhgdf", "fhffhfg", 12-12-2022, "f", 1, 2]]


    def creation_player(self, players_list):
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
                    # Parse the string input into a datetime object
                    birth_datetime = datetime.strptime(PModel.birth, '%Y-%m-%d')
                    # Extract the date part of the datetime object
                    PModel.birth = birth_datetime.date()
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
        """Vu listée de tous les joueurs d'un tournoi"""
        for player in players_list:
            print(player)
        """Choix du joueur a modifier"""
        player_id = int(input("Enter the ID of the player you want to modify: "))
        if player_id > len(players_list) - 1:
            # player not found
            print("Player not found.")
        else:
            i = 0
            while players_list[i][0] != player_id:
                i = i + 1

            # player found, modify the player's attributes here
            player_rank = int(input("Enter the new player rank: "))
            while player_rank <= 0:
                player_rank = int(input("Enter the new player rank positive: "))
            if player_rank > 8:
                player_rank = 8
            players_list[player_id][6] = player_rank

        players_list.insert(player_rank, players_list[player_id])
        players_list.pop(player_id)

        """REZ rang de tous les joueurs"""
        for i in range(len(players_list)):
            players_list[i][6] = i + 1

        print(players_list)

    @staticmethod
    def player_rank_sort(players_list):
        """function to sort player by their rank"""
        players_list.sort(key=players_list[6])

    @staticmethod
    def player_alpha_sort(players_list):
        """function to sort players alphabetical order"""
        sorted(players_list, key=players_list[1])

    @staticmethod
    def player_score_sort(players_list):
        """function to sort player by their rank"""
        sorted(players_list, key=itemgetter(5, 6))
