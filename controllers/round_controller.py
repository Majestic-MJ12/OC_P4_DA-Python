# this is the round controller
# importing what is needed
from datetime import datetime
from models.round_model import RModel
from controllers.match_controller import MController
from controllers.player_controller import PController


# The controller for the rounds
class RController:
    """rounds_list = [1, 3, "Round1", 12-12-2022, 12-12-2022]"""
    rounds_list = []

    @staticmethod
    def round_start(rounds_list):
        """function to create a round"""
        cpt_round = len(rounds_list)
        print("\nThe round number is: " + str(int(len(RController.rounds_list) + 1)))
        if len(PController.players_list) < 8:
            print("\nThere is not enough players created to start the tournament, create players first")
        else:
            """counter"""
            RModel.id_round = "ID_round:" + str(int(cpt_round + 1))
            RModel.matches = []
            RModel.round_name = "Round:" + str(int(cpt_round + 1))
            RModel.time_start = datetime.now()

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
        RModel.time_end = datetime.now()
        rounds_list[-1][-1] = RModel.time_end
