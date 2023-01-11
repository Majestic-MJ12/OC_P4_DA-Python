import datetime
import pprint
from models.tournament_model import TModel
from controllers.round_controller import RController
from controllers.player_controller import PController


class TController:
    tournament_list = []
    permanent_selected_player = []

    def __init__(self):
        self.load_tournaments()

    def save_tournaments(self):
        from tinydb import TinyDB
        file_path = "Data_base/tournaments_list.json"
        try:
            db = TinyDB(file_path)
            table = db.table('tournaments')
            table.insert_multiple(self.tournament_list)
        except FileNotFoundError:
            print("Error: Database file not found. Creating new file")
            db = TinyDB('tournaments.json')
            table = db.table('tournaments')
            table.insert_multiple(self.tournament_list)

    def load_tournaments(self):
        from tinydb import TinyDB
        file_path = "Data_base/tournaments_list.json"
        try:
            db = TinyDB(file_path)
            table = db.table('tournaments')
            self.tournament_list = table.all()
        except FileNotFoundError:
            print("Error: Database file not found")

    @staticmethod
    def creation_tournament(tournament_list, permanent_selected_player):
        cpt_tournament = len(tournament_list)
        if len(PController.players_list) < 8:
            print("\nThere is not enough players created to start the tournament, create players first")
        else:
            PController.player_id_sort(PController.players_list)
            for i in range(1, 2):
                print("\nTournament number: " + str(int(len(TController.tournament_list) + 1)) + " creation: ")
                TModel.id_tournament = cpt_tournament + 1
                TModel.name = input("\nWhat's the name of the tournament: ")
                TModel.localisation = input("What's the localisation of the tournament: ")

                while True:
                    try:
                        TModel.date = input("What's the date of the tournament: "
                                            "it must be entered like this => YYYY-MM-DD: ")
                        TModel.date = datetime.datetime.strptime(TModel.date, '%Y-%m-%d')
                        date_str = TModel.date.strftime("%B %d, %Y")
                        TModel.date = date_str
                    except ValueError:
                        print("\nSorry, that is not a valid date. Please try again.")
                    else:
                        break

                TModel.number_round = "Number of rounds: 4"
                number_round = 4

                for t in range(number_round):
                    round_number = len(RController.rounds_list) + 1 + t
                    TModel.rounds = f"Round{round_number}"

                pprint.pprint(PController.players_list)
                print("\n")
                print("Choose 8 players for the tournament: ")
                print("\n")

                selected_players = []
                while len(selected_players) < 8:
                    try:
                        selection = int(input("Enter the id of the player you want to add: ")) - 1
                        if selection < 0 or selection >= len(PController.players_list):
                            raise ValueError("Player with this id does not exist in the players list.")
                        elif selection in selected_players:
                            raise ValueError("Player has already been selected.")
                        else:
                            selected_players.append(selection)
                            permanent_selected_player.append([PController.players_list[selection]])
                    except ValueError as e:
                        if "invalid literal for int() with base 10" in str(e):
                            print("Invalid input. Please try again")
                        else:
                            print(e)

                TModel.players = selected_players

                TModel.time_control = input("It's a ""bullet"", a ""blitz"" or a ""quick hit"": ")
                while TModel.time_control.lower() not in ['bullet', 'blitz', 'quick hit']:
                    TModel.time_control = input("\nInvalid input. "
                                                "Enter tournament time control (bullet/blitz/quick hit): ")

                TModel.description = input("Description of the tournament: ")

                tournament = [TModel.id_tournament, TModel.name, TModel.localisation, TModel.date, TModel.number_round]

                TModel.rounds = []
                for t in range(number_round):
                    round_number = t + 1
                    TModel.rounds.append(f"Round{round_number}")

                tournament.extend([TModel.rounds, TModel.players, TModel.time_control, TModel.description])

                tournament_list.append(tournament)
                cpt_tournament = + 1
