from datetime import datetime
from models.tournament_model import TModel
from controllers.round_controller import RController
from controllers.player_controller import PController


class TController:
    tournament_list = []

    @staticmethod
    def creation_tournament(tournament_list):
        cpt_tournament = len(tournament_list)
        for i in range(1, 2):
            print("Tournament information: ")
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
                    print("Sorry, that is not a valid date. Please try again.")
                else:
                    break

            TModel.number_round = 4

            for t in range(len(RController.rounds_list)):
                TModel.rounds = (RController.rounds_list[t])

            for t in range(len(PController.players_list)):
                TModel.players = (PController.players_list[t])

            TModel.time_control = input("It's a ""bullet"", a ""blitz"" or a ""quick hit"": ")
            while TModel.time_control.lower() not in ['bullet', 'blitz', 'quick hit']:
                TModel.time_control = input("Invalid input. Enter tournament time control (bullet/blitz/quick hit): ")

            TModel.description = input("Description of the tournament: ")

            tournament = [TModel.id_tournament, TModel.name, TModel.localisation,
                          TModel.date, TModel.number_round, TModel.rounds,
                          TModel.players, TModel.time_control, TModel.description]
            tournament_list.append(tournament)
            cpt_tournament = + 1


