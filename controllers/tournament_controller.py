import time


class TController:

    t_controller_list = []

    def __init__(self, name, localisation, date,
                 number_round, matches, description):
        self.name = name
        self.localisation = localisation
        self.date = date
        self.number_round = number_round
        self.matches = matches
        self.description = description

    def t_name(self, name):
        self.name = input("What's the name of the tournament?: ")
        return name

    def t_localisation(self, localisation):
        self.localisation = input("What's the localisation of the tournament?: ")
        return localisation

    def t_date(self, date):
        self.date = time.time()
        return date

    def t_number_round(self, number_round):
        self.number_round = input("How many rounds?: ")
        if not number_round:
            number_round = 4
        return number_round

    def t_matches(self, matches):
        self.matches = input("How many rounds?: ")
        return matches

    def t_description(self, description):
        self.description = input("Description of the tournament: ")
        return description

    t_controller_list.append(t_name)
    t_controller_list.append(t_localisation)
    t_controller_list.append(t_date)
    t_controller_list.append(t_number_round)
    t_controller_list.append(t_matches)
    t_controller_list.append(t_description)

    print(t_controller_list)





