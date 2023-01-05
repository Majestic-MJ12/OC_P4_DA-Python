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
            RModel.round_name = "Round ", cpt_round + 1
            try:
                start_time_string = input("Enter the start time for the round (mm-dd-yyyy hh:mm:ss): ")
                RModel.round_time_start = start_time_string
                end_time_string = input("Enter the start time for the round (mm-dd-yyyy hh:mm:ss): ")
                RModel.round_time_end = end_time_string
            except ValueError:
                print("Invalid input. Please enter the start time in the correct format (mm-dd-yyyy hh:mm:ss).")

            matches = []
            for match in MController.match_list:
                # For each `MModel` object in the list, add its `id_match` attribute to the `matches` list
                matches.append(match.id_match)
                RModel.matches = matches

            rounds = [RModel.id_round, RModel.matches, RModel.round_name,
                      RModel.round_time_start, RModel.round_time_end]
            rounds_list.append(rounds)

            rounds_list.append(rounds)
            cpt_round = cpt_round + 1

