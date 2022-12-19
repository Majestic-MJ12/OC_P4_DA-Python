from models.round_model import RModel
from controllers.match_controller import MController
import datetime
from datetime import timezone


class RController:
    rounds_list = []

    @staticmethod
    def round_creation(rounds_list):
        cpt_round = len(rounds_list)
        for i in range(1, 5):
            RModel.matches = "Match", MController.match_list[1]
            RModel.round_name = "Round ", cpt_round + 1
            RModel.round_time_start = datetime.datetime.now(tz=timezone.utc)
            RModel.round_time_end = datetime.datetime.now(tz=timezone.utc)

            rounds = [RModel.round_name, RModel.round_time_start, RModel.round_time_end]
            rounds_list.append(rounds)
            cpt_round = cpt_round + 1
