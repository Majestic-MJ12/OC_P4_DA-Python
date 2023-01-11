# this is the round controller
# importing what is needed
from datetime import datetime
from models.round_model import RModel
from controllers.match_controller import MController
from controllers.player_controller import PController


# The controller for the rounds
class RController:
    rounds_list = []

    def __init__(self):
        self.load_rounds()

    def save_rounds(self):
        from tinydb import TinyDB
        file_path = "Data_base/rounds_list.json"
        try:
            db = TinyDB(file_path)
            table = db.table('rounds')
            table.insert_multiple(self.rounds_list)
        except FileNotFoundError:
            print("Error: Database file not found. Creating new file")
            db = TinyDB('rounds.json')
            table = db.table('rounds')
            table.insert_multiple(self.rounds_list)

    def load_rounds(self):
        from tinydb import TinyDB
        file_path = "Data_base/rounds_list.json"
        try:
            db = TinyDB(file_path)
            table = db.table('rounds')
            self.rounds_list = table.all()
        except FileNotFoundError:
            print("Error: Database file not found")

    @staticmethod
    def round_start(rounds_list):
        """function to create a round"""
        cpt_round = len(rounds_list)
        print("\nThe round number is: " + str(int(len(RController.rounds_list) + 1)))
        if len(PController.players_list) < 8:
            print("\nThere is not enough players created to start the tournament, create players first")
        else:
            """counter"""
            RModel.id_round = cpt_round + 1
            RModel.matches = []
            RModel.round_name = cpt_round + 1
            time_now = datetime.now()
            time_now_less = time_now.strftime("%Y-%m-%d %H:%M:%S")
            RModel.time_start = time_now_less

            RModel.time_end = ""

            rounds = [RModel.id_round, RModel.matches, RModel.round_name,
                      RModel.time_start, RModel.time_end]
            rounds_list.append(rounds)

    @staticmethod
    def round_creation(rounds_list):
        RModel.matches = MController.match_list[-4:]
        rounds_list[-1][1] = RModel.matches

    @staticmethod
    def round_end(rounds_list):
        time_now = datetime.now()
        time_now_less = time_now.strftime("%Y-%m-%d %H:%M:%S")
        RModel.time_end = time_now_less
        rounds_list[-1][-1] = RModel.time_end
