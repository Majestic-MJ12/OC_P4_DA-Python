# This is the file that gets the inputs for the reports

# Import what is needed
from models.tournament_model import TModel
from views.main_view import MView
from views.report_view import ReView


class RController:
    """Class of the report controller"""
    def __init__(self):
        """Init of the report controller"""
        self.m_view = MView()
        self.re_view = ReView()

    def rc_all_players_by_name(self, rc_players):
        """Player report (sorted by last name)"""
        rc_players = sorted(rc_players, key=lambda x: x.get('p_lastname'))
        self.re_view.rv_display_players(rc_players, "by name")

    def rc_all_players_by_rank(self, rc_players):
        """Player report (sorted by rank)"""
        rc_players = sorted(rc_players, key=lambda x: x.get('p_rank'))
        self.re_view.rv_display_players(rc_players, "by rank")

    def rc_tournament_players(self):
        """Players in a tournament report
        Select tournament to display players"""
        rc_user_input, rc_tournaments = self.rc_tournament_selection()

        for i in range(len(rc_tournaments)):
            if rc_user_input == str(rc_tournaments[i]['t_id']):
                return rc_tournaments[i]["t_players"]

    def rc_all_tournaments(self):
        """All tournaments report"""
        self.re_view.rv_display_tournaments_report(TModel.t_load_tournament_db())

    def rc_tournament_rounds(self):
        """All rounds from a tournament"""
        rc_user_input, rc_tournaments = self.rc_tournament_selection()

        self.re_view.rv_report_head(rc_tournaments[int(rc_user_input) - 1])
        self.re_view.rv_display_rounds_report(rc_tournaments[int(rc_user_input) - 1]["t_rounds"])

    def rc_tournament_matches(self):
        """All matches from a tournament"""
        rc_user_input, rc_tournaments = self.rc_tournament_selection()

        self.re_view.rv_report_head(rc_tournaments[int(rc_user_input) - 1])

        rc_rounds = rc_tournaments[int(rc_user_input) - 1]["t_rounds"]
        rc_round_matches = []
        for i in range(len(rc_rounds)):
            rc_round_matches.append(rc_rounds[i][3])

        rc_matches = []
        for i in range(len(rc_round_matches)):
            for k in range(4):
                rc_matches.append(rc_round_matches[i][k])

        self.re_view.rv_display_match_report(rc_matches)

    def rc_tournament_selection(self):
        """Load all tournaments from the one chosen"""
        rc_tournaments = TModel.t_load_tournament_db()
        self.m_view.mv_select_tournaments(rc_tournaments)
        self.m_view.mv_input_prompt()
        rc_user_input = input()

        if rc_user_input == "back":
            """Go back to main menu"""
            self.rc_back_to_menu()

        else:
            """Apply the choice"""
            return rc_user_input, rc_tournaments

    @staticmethod
    def rc_back_to_menu():
        """Method that makes the program go back to main menu"""
        from controllers.main_menu_controller import MMController
        MMController().mmc_menu_start()
