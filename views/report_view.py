from controllers.tournament_controller import TController
from controllers.player_controller import PController
from controllers.round_controller import RController
from controllers.match_controller import MController


class RView:

    @staticmethod
    def actors_view():
        print(PController.players_list)

    @staticmethod
    def all_tournaments_view():
        print(TController.tournament_list)

    @staticmethod
    def tournaments_players_view():
        print(PController.players_list)

    def tournaments_round_view(self, id_tournament):
        for i in range(1, 5):
            print(RController.rounds_list[((id_tournament - 1) * 4 + i) - 1])

    def tournaments_matches_view(self, id_tournament):
        for i in range(1, 17):
            print(MController.match_list[((id_tournament - 1) * 16 + i) - 1])
