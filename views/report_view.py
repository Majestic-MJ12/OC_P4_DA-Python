# this is the views for the reports menu section
# importing what is needed
from controllers.tournament_controller import TController
from controllers.player_controller import PController
from controllers.round_controller import RController
from controllers.match_controller import MController


class RView:

    @staticmethod
    def actors_view():
        print("\n")
        for i in range(len(PController.players_list)):
            print(PController.players_list[i])

    @staticmethod
    def all_tournaments_view():
        print("\n")
        for i in range(len(TController.tournament_list)):
            print(TController.tournament_list[i])

    @staticmethod
    def tournaments_players_view():
        print("\n")
        for i in range(len(PController.players_list)):
            print(PController.players_list[i])

    def tournaments_round_view(self, id_tournament):
        print("\n")
        for i in range(1, 5):
            print(RController.rounds_list[((id_tournament - 1) * 4 + i) - 1])

    def tournaments_matches_view(self, id_tournament):
        print("\n")
        for i in range(1, 17):
            print(MController.match_list[((id_tournament - 1) * 16 + i) - 1])
