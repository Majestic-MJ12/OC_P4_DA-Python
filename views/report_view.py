from controllers.tournament_controller import TController
from controllers.player_controller import PController
from controllers.round_controller import RController


class RView:

    @staticmethod
    def actors_view(self):
        print(PController.players_list)

    @staticmethod
    def tournaments_players_view(self):
        print(PController.players_list)

    @staticmethod
    def tournaments_round_view(self):
        print(RController.rounds_list)

    @staticmethod
    def tournaments_matches_view(self):
        print(TController.tournament_list)
