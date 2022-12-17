from datetime import datetime
from models.match_model import MModel


class RModel:
    def __init__(self, matches=None, round_name="", time_start="", time_end=""):

        self.matches = matches
        self.round_name = round_name
        self.time_start = time_start
        self.time_end = time_end

    def date_time_now(self):
        begin_date = datetime.now()
        date_human_readable = begin_date.strftime("%d/%m/%Y %H:%M:%S")
        return date_human_readable

    def round_time_start(self):
        self.time_start = self.date_time_now()

    def round_time_end(self):
        self.date_time_now()


