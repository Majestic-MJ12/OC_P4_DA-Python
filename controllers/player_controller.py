from models.player_model import PModel


class PController:
    players_list = []

    def creation_player(self, players_list):

        # Asking players data
        i = 1
        for i in range(8):
            PModel.id_player = i
            PModel.lastname = input("Enter the player's last name : ")
            PModel.firstname = input("Enter the player's first name : ")
            PModel.birth = input("Enter the player's date of birth : ")
            PModel.gender = input("Enter player's gender : ")
            PModel.rank = 0

            player = {PModel.lastname, PModel.firstname, PModel.birth, PModel.gender, PModel.rank}
            players_list.append(player)

    def modification_player(self, players_list):
        """Vu listée de tous les joueurs d'un tournoi"""
        """Choix du joueur a modifier"""
        PModel.rank = input("Enter the new player rank: ")
        while PModel.rank <= 0:
            PModel.rank = input("Enter the new player rank positive: ")
        if PModel.rank > 8:
            PModel.rank = 8
        players_list.insert(players_list[player], PModel.rank)
        players_list.pop(player)

    def player_rank_sort(self, players_list):
        """Tri des joueurs par rang du plus petit au plus grand"""
        players_list.sort(key=lambda player: player.rank)




