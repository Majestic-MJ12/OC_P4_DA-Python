from models.player_model import PModel


class PController:
    players_list = []

    @staticmethod
    def creation_player(players_list):
        # Asking players data
        cpt_player = len(players_list)
        for i in range(1, 9):
            print("Player ", i, " information: ")
            PModel.id_player = cpt_player + 1
            PModel.lastname = input("Enter the player's last name : ")
            PModel.firstname = input("Enter the player's first name : ")
            PModel.birth = input("Enter the player's date of birth : ")
            PModel.gender = input("Enter player's gender : ")
            PModel.score = 0
            PModel.rank = 0

            player = [PModel.id_player, PModel.lastname, PModel.firstname, PModel.birth, PModel.gender,
                      PModel.score, PModel.rank]
            players_list.append(player)
            cpt_player = cpt_player + 1

    @staticmethod
    def modification_player(players_list):
        """Vu listée de tous les joueurs d'un tournoi"""
        """Choix du joueur a modifier"""
        PModel.rank = int(input("Enter the new player rank: "))
        while PModel.rank <= 0:
            PModel.rank = int(input("Enter the new player rank positive: "))
        if PModel.rank > 8:
            PModel.rank = 8
        players_list.insert(players_list[player], PModel.rank)
        players_list.pop(player)

    @staticmethod
    def player_rank_sort(players_list):
        """Tri des joueurs par rang du plus petit au plus grand"""
        players_list.sort(key=lambda player: player.rank)



