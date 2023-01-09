# this is the views for the reports menu section
# importing what is needed
import pprint
import time
from controllers.tournament_controller import TController
from controllers.player_controller import PController
from controllers.round_controller import RController
from controllers.match_controller import MController


class RView:
    @staticmethod
    def actors_view():
        try:
            print("\nACTORS LIST", end="")
            for i in range(5):
                time.sleep(0.1)
                print(".", end="")
            print("\n")
            for i in range(len(PController.players_list)):
                print(PController.players_list[i])
        except IndexError:
            print("There are no players created")

    @staticmethod
    def actors_view_alpha():
        try:
            print("\nACTORS LIST (ALPHABETIC ORDER)", end="")
            for i in range(5):
                time.sleep(0.1)
                print(".", end="")
            print("\n")
            for i in PController.player_alpha_sort(players_list=PController.players_list):
                print(i)
        except Exception as e:
            # Handling code for any exception that occurs
            print(f"An error occurred: {e}")

    @staticmethod
    def actors_view_rank():
        try:
            print("\nACTORS LIST (BY RANK)", end="")
            for i in range(5):
                time.sleep(0.1)
                print(".", end="")
            print("\n")
            for i in PController.player_rank_sort(players_list=PController.players_list):
                print(i)
        except Exception as e:
            # Handling code for any exception that occurs
            print(f"An error occurred: {e}")

    @staticmethod
    def all_tournaments_view():
        try:
            print("\nALL TOURNAMENTS LIST", end="")
            for i in range(5):
                time.sleep(0.1)
                print(".", end="")
            print("\n")
            for i in range(len(TController.tournament_list)):
                print(TController.tournament_list[i])
        except IndexError:
            print("There are no players in this tournament.")

    @staticmethod
    def tournaments_players_view(id_tournament):
        try:
            print("\nPLAYERS FROM ONE TOURNAMENT", end="")
            for i in range(5):
                time.sleep(0.1)
                print(".", end="")
            print("\n")
            print(TController.permanent_selected_player[id_tournament - 1])
        except IndexError:
            print("There are no players in this tournament.")

    @staticmethod
    def tournaments_round_view(id_tournament):
        try:
            print("\nALL ROUNDS FROM ONE TOURNAMENT", end="")
            for i in range(5):
                time.sleep(0.1)
                print(".", end="")
            print("\n")
            for i in range(1, 5):
                print(RController.rounds_list[((id_tournament - 1) * 4 + i) - 1])
        except IndexError:
            print("There are no rounds in this tournament.")

    @staticmethod
    def tournaments_matches_view(id_tournament):
        try:
            print("\nALL MATCHES FROM ONE TOURNAMENT", end="")
            for i in range(5):
                time.sleep(0.1)
                print(".", end="")
            print("\n")
            for i in range(1, 17):
                print(MController.match_list[((id_tournament - 1) * 16 + i) - 1])
        except IndexError:
            print("There are no matches in this tournament.")
