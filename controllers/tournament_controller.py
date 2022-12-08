import time

t_controller_list = []


class TController:

    def __init__(self, t_name, t_localisation, t_date,
                 t_number_round, t_matches, t_description):
        self.t_name = t_name
        self.t_localisation = t_localisation
        self.t_date = t_date
        self.t_number_round = t_number_round
        self.t_matches = t_matches
        self.t_description = t_description

    def t_name(self):
        pass

    def t_localisation(self):
        pass

    def t_date(self):
        pass

    @staticmethod
    def t_number_round():
        t_number_round = input("How many rounds?: ")
        if not t_number_round:
            t_number_round = 4
        return t_number_round

    def t_matches(self):
        pass

    def t_description(self):
        pass






