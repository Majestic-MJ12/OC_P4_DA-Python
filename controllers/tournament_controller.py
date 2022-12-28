from datetime import datetime
from models.tournament_model import TModel
from controllers.round_controller import RController
from controllers.player_controller import PController


class TController:
    """tournament_list = [[1, "efze", "zef", 12-12-2022, 4, "bullet", "fffff"], [2, "efze", "zef", 12-12-2022, 4, "bullet", "fffff"]]"""
    tournament_list = []

    @staticmethod
    def creation_tournament(tournament_list, player=None):
        cpt_tournament = len(tournament_list)
        if len(PController.players_list) < 8:
            print("\nThere is not enough players created to start the tournament, create players first")
        else:
            for i in range(1, 2):
                print("\nTournament information: ")
                TModel.id_tournament = cpt_tournament + 1
                TModel.name = input("What's the name of the tournament: ")
                TModel.localisation = input("What's the localisation of the tournament: ")

                while True:
                    try:
                        TModel.date = input("What's the date of the tournament: "
                                            "it must be entered like this => YYYY-MM-DD: ")
                        date_datetime = datetime.strptime(TModel.date, '%Y-%m-%d')
                        TModel.date = date_datetime.date()
                    except ValueError:
                        print("\nSorry, that is not a valid date. Please try again.")
                    else:
                        break

                TModel.number_round = 4

                for t in range(TModel.number_round):
                    TModel.rounds = len(RController.rounds_list) + 1 + t

                print(PController.players_list)

                selected_players = []
                while len(selected_players) < 8:
                    try:
                        selection = int(input("Enter the id of the player you want to add: ")) - 1
                        if selection < len(PController.players_list):
                            selected_players.append(selection)
                        else:
                            raise ValueError\
                                ("Player with this id does not exist in the players list.".format(selection))
                    except ValueError as e:
                        print("\nPlayer with this id does not exist in the players list.".format(e))

                TModel.players = selected_players

                TModel.time_control = input("It's a ""bullet"", a ""blitz"" or a ""quick hit"": ")
                while TModel.time_control.lower() not in ['bullet', 'blitz', 'quick hit']:
                    TModel.time_control = input("\nInvalid input. "
                                                "Enter tournament time control (bullet/blitz/quick hit): ")

                TModel.description = input("Description of the tournament: ")

                tournament = [TModel.id_tournament, TModel.name, TModel.localisation,
                              TModel.date, TModel.number_round, TModel.rounds,
                              TModel.players, TModel.time_control, TModel.description]
                tournament_list.append(tournament)
                cpt_tournament = + 1
