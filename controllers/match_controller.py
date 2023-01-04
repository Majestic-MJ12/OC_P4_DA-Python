# this is the match controller
# importing what is needed
from models.match_model import MModel
from controllers.player_controller import PController


# the controller for the matches
class MController:
    match_list = []

    @staticmethod
    def pair_generation(match_list):
        cpt_match = len(match_list) + 1
        """function to generate a battle between two players"""
        players_ids = []
        for i in range(8):
            players_ids.append([i, False])
        already_battle_player = []
        if cpt_match % 16 == 1:
            """verify if it's the first match of the tournament"""
            PController.player_rank_sort(PController.players_list)

            for player in range(4):
                match_list.append(MModel(cpt_match, PController.players_list[player][0], 0,
                                         PController.players_list[player + 4][0], 0))

                cpt_match = cpt_match + 1
                already_battle_player.append([player, player + 4])
        else:
            PController.player_score_sort(PController.players_list)

            for player in range(4):
                i = 1
                while ([player, player + i] or [player + i, player] or i < 8) in already_battle_player:
                    i = i + 1

                match_list.append(MModel(cpt_match, PController.players_list[player][0], 0,
                                         PController.players_list[player + i][0], 0))
                players_ids[player][1] = True
                players_ids[player + i][1] = True

                already_battle_player.append([player, player + i])
                cpt_match = cpt_match + 1

    @staticmethod
    def match_result(match_list):
        """function to enter the match results"""
        from controllers.tournament_controller import TController

        while len(TController.tournament_list) <= 0:
            print("\n")
            print("No tournament information have been created, please create the information before launching")
            return
        cpt_match = len(match_list)
        print("The matches begin!")
        for i in range(4):
            match = cpt_match - 4 + i

            print("\n")
            print("MATCH INFORMATION "
                  "====================")
            print(f"id_match: {match_list[match].id_match}")
            print(f"player1: {match_list[match].player1}")
            print(f"player1_score: {match_list[match].player1_score}")
            print(f"player2: {match_list[match].player2}")
            print(f"player2_score: {match_list[match].player2_score}")
            print("\n")

            while True:
                try:
                    result = int(input("Enter the winner player number or 0 if tie match: "))
                    if not (result == 0 or result == 1 or result == 2):
                        raise ValueError("Invalid input")
                    break
                except ValueError as e:
                    print("Error: ", e)

            MModel.update_match_scores(match_list[match], result)
            """Player winner : score +1"""
            if result == 1 or 2:
                i = 0
                while PController.players_list[i][0] != match_list[match].player1:
                    i = i + 1
                PController.players_list[i][-1] = PController.players_list[i][-1] + 1
            else:
                """Player 1 : score +0.5"""
                i = 0
                while PController.players_list[i][0] != match_list[match].player1:
                    i = i + 1
                PController.players_list[i][-1] = PController.players_list[i][-1] + 0.5

                """Player 2 : score +0.5"""
                i = 0
                while PController.players_list[i][0] != match_list[match].player2:
                    i = i + 1
                PController.players_list[i][-1] = PController.players_list[i][-1] + 0.5


