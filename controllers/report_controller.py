# This is the file that gets the inputs for the reports
# Import what is needed
from models.tournament_model import TModel
from views.main_view import MView
from views.report_view import RView


class RController:
    """Class of the report controller"""
    def __init__(self):
        """Init of the report controller"""
        self.m_view = MView()
        self.r_view = RView()

    def all_players_by_name(self, players):
        """Player report (sorted by last name)"""
        players = sorted(players, key=lambda x: x.get('last_name'))
        self.r_view.display_players(players, "by name")

    def all_players_by_rank(self, players):
        """Player report (sorted by rank)"""
        players = sorted(players, key=lambda x: x.get('rank'))
        self.r_view.display_players(players, "by rank")

    def tournament_players(self):
        """Players in a tournament report
        Select tournament to display players"""
        user_input, tournaments = self.tournament_selection()

        for i in range(len(tournaments)):
            if user_input == str(tournaments[i]['id']):
                return tournaments[i]["players"]

    def all_tournaments(self):
        """All tournaments report"""
        self.r_view.display_tournaments_report(TModel.load_tournament_db())

    def tournament_rounds(self):
        """All rounds from a tournament"""
        user_input, tournaments = self.tournament_selection()

        self.r_view.report_head(tournaments[int(user_input) - 1])
        self.r_view.display_rounds_report(tournaments[int(user_input) - 1]["rounds"])

    def tournament_matches(self):
        """All matches from a tournament"""
        user_input, tournaments = self.tournament_selection()

        self.r_view.report_head(tournaments[int(user_input) - 1])

        rounds = tournaments[int(user_input) - 1]["rounds"]
        round_matches = []
        for i in range(len(rounds)):
            round_matches.append(rounds[i][3])

        matches = []
        for i in range(len(round_matches)):
            for k in range(4):
                matches.append(round_matches[i][k])

        self.r_view.display_match_report(matches)

    def tournament_selection(self):
        """Load all tournaments from the one chosen"""
        tournaments = TModel.load_tournament_db()
        self.m_view.select_tournaments(tournaments)
        self.m_view.input_prompt()
        user_input = input()

        if user_input == "back":
            """Go back to main menu"""
            self.back_to_menu()

        else:
            """Apply the choice"""
            return user_input, tournaments

    @staticmethod
    def back_to_menu():
        """Method that makes the program go back to main menu"""
        from controllers.main_menu_controller import MMController
        MMController().menu_start()
