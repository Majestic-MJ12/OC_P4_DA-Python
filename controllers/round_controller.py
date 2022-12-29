# this is the round controller
# importing what is needed
from models.round_model import RModel
from controllers.match_controller import MController
from datetime import datetime


# The controller for the rounds
class RController:
    """rounds_list = [1, 3, "Round1", 12-12-2022, 12-12-2022]"""
    rounds_list = []

    @staticmethod
    def round_creation(rounds_list):
        """function to create a round"""
        cpt_round = len(rounds_list)
        """counter"""
        for i in range(1, 5):
            RModel.id_round = cpt_round + 1
            for r in range(len(MController.match_list)):
                round_number = len(MController.match_list) + 1 + r
                RModel.matches = f"Round{round_number}"

            RModel.round_name = "Round ", cpt_round + 1
            RModel.round_time_start = datetime.strptime
            RModel.round_time_end = datetime.strptime

            rounds = [RModel.id_round]

            RModel.matches = []
            for r in range(RModel.id_round):
                round_number = r + 1
                RModel.matches.append(f"Round{round_number}")

            rounds.extend([RModel.matches, RModel.round_name,
                           RModel.round_time_start, RModel.round_time_end])

            rounds_list.append(rounds)
            cpt_round = cpt_round + 1

