# this is the round controller
# importing what is needed
from models.round_model import RModel
from controllers.match_controller import MController


# The controller for the rounds
class RController:
    """rounds_list = [1, 3, "Round1", 12-12-2022, 12-12-2022]"""
    rounds_list = []

    @staticmethod
    def round_start(rounds_list):
        """function to create a round"""
        cpt_round = len(rounds_list)
        """counter"""
        RModel.id_round = "ID_round:" + str(int(cpt_round + 1))
        RModel.matches = []
        RModel.round_name = "Round:" + str(int(cpt_round + 1))

        while True:
            try:
                start_time_string = input("Enter the start time for the round (mm-dd-yyyy hh:mm:ss): ")
                RModel.time_start = start_time_string
                break
            except ValueError:
                print("Invalid input. Please enter the start time in the correct format (mm-dd-yyyy hh:mm:ss).")

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
        while True:
            try:
                end_time_string = input("Enter the end time for the round (mm-dd-yyyy hh:mm:ss): ")
                RModel.time_end = end_time_string
            except ValueError:
                print("Invalid input. Please enter the start time in the correct format (mm-dd-yyyy hh:mm:ss).")
            break
        rounds_list[-1][-1] = RModel.time_end
