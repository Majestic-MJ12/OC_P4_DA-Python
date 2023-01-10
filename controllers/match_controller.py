# this is the match controller
# importing what is needed
from models.match_model import MModel
from controllers.player_controller import PController


# the controller for the matches
class MController:
    match_list = []

    @staticmethod
    def update_scores(match_list, result, match):
        if result == 1:
            match_list[match][2] += 1
            """Player winner : score +1"""
            i = 0
            while PController.players_list[i][0] != match_list[match][1]:
                i = i + 1
            PController.players_list[i][-2] += 1
        elif result == 2:
            match_list[match][-1] += 1
            """Player winner : score +1"""
            i = 0
            while PController.players_list[i][0] != match_list[match][3]:
                i = i + 1
            PController.players_list[i][-2] += 1
        else:
            """Player 1 : score +0.5"""
            i = 0
            while PController.players_list[i][0] != match_list[match][1]:
                i = i + 1
            PController.players_list[i][-2] += 0.5
            match_list[match][2] += 0.5

            """Player 2 : score +0.5"""
            i = 0
            while PController.players_list[i][0] != match_list[match][3]:
                i = i + 1
            PController.players_list[i][-2] += 0.5
            match_list[match][-1] += 0.5

    @staticmethod
    def pair_generation(match_list):
        from controllers.tournament_controller import TController
        from controllers.main_menu_controller import MMController
        cpt_match = len(match_list) + 1
        """function to generate a battle between two players"""
        players_ids = []

        if len(TController.tournament_list) <= 0:
            print("\n")
            print("No tournament information have been created, please create the information before launching")
            MMController.tournament_menu()
        else:

            for i in range(8):
                players_ids.append([i, False])
            already_battle_player = []
            if cpt_match % 16 == 1:
                """verify if it's the first match of the tournament"""
                PController.player_rank_sort(PController.players_list)

                for player in range(4):
                    MModel.id_match = cpt_match
                    MModel.player1 = PController.players_list[player][0]
                    MModel.player1_score = 0
                    MModel.player2 = PController.players_list[player + 4][0]
                    MModel.player2_score = 0

                    match_model = [MModel.id_match, MModel.player1, MModel.player1_score,
                                   MModel.player2, MModel.player2_score]
                    match_list.append(match_model)

                    cpt_match = cpt_match + 1
                    already_battle_player.append([player, player + 4])
            else:
                PController.player_score_sort(PController.players_list)

                for player in range(4):
                    i = 1
                    while ([player, player + i] or [player + i, player] or i < 8) in already_battle_player:
                        i = i + 1

                    MModel.id_match = cpt_match
                    MModel.player1 = PController.players_list[player][0]
                    MModel.player1_score = 0
                    MModel.player2 = PController.players_list[player + i][0]
                    MModel.player2_score = 0

                    match_model = [MModel.id_match, MModel.player1, MModel.player1_score,
                                   MModel.player2, MModel.player2_score]

                    match_list.append(match_model)
                    players_ids[player][1] = True
                    players_ids[player + i][1] = True

                    already_battle_player.append([player, player + i])
                    cpt_match = cpt_match + 1

    @staticmethod
    def match_result(match_list):
        """function to enter the match results"""
        from controllers.tournament_controller import TController
        from controllers.main_menu_controller import MMController

        if len(TController.tournament_list) <= 0:
            print("\n")
            print("No tournament information have been created, please create the information before launching")
            MMController.tournament_menu()
        else:
            cpt_match = len(match_list)
            print("\nThe matches begin!")
            for i in range(4):
                match = cpt_match - 4 + i

                print("\n")
                print("MATCH INFORMATION "
                      "====================")
                print(f"id_match: {match_list[match][0]}")
                print(f"player1: {match_list[match][1]}")
                print(f"player1_score: {match_list[match][2]}")
                print(f"player2: {match_list[match][3]}")
                print(f"player2_score: {match_list[match][4]}")
                print("\n")

                while True:
                    try:
                        result = int(input("Enter the winner player number or 0 if tie match: "))
                        if not (result == 0 or result == 1 or result == 2):
                            raise ValueError("Invalid input")
                        break
                    except ValueError:
                        print("Error: Invalid input")

                MController.update_scores(match_list, result, match)
