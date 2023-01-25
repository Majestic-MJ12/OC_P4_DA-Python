# This is the file that is used for the rounds view
# Import what is needed
from prettytable import PrettyTable
"""A simple Python library for easily
displaying tabular data in a visually
appealing ASCII table format."""


class RoView:
    """Class of the round view"""

    def __init__(self):
        """Init of the round view"""
        self.rov_table = PrettyTable()
        self.rov_round_field_names = [
            "r_Match :",
            "r_Name P1",
            "r_Rank P1",
            "r_Score P1",
            " ",
            "r_Name P2",
            "r_Rank P2",
            "r_Score P2"
        ]

        self.rov_results_field_names = [
            "r_Tournament ranking",
            "r_Name",
            "r_Final Score",
            "r_Global ranking"
        ]

    def rov_display_matches(self, rov_matches):
        """Display the matches for current round as table"""
        self.rov_table.clear()
        self.rov_table.field_names = self.rov_round_field_names

        for i in range(len(rov_matches)):
            rov_row = list(rov_matches[i])
            rov_row.insert(0, str(i+1))
            rov_row.insert(4, "versus")

            self.rov_table.add_row(rov_row)

        print(self.rov_table)

    def rov_display_results(self, rov_t):
        """Display the results at the end of the tournament"""
        self.rov_table.clear()
        self.rov_table.field_names = self.rov_results_field_names

        for i in range(len(rov_t.t_players)):
            self.rov_table.add_row([
                i+1,
                rov_t.t_players[i]["p_lastname"] + ", " + rov_t.t_players[i]["p_firstname"],
                rov_t.t_players[i]["p_score"],
                rov_t.t_players[i]["p_rank"]
            ])

        print("\n\n- FINAL SCORES -\n")
        print(f"{rov_t.t_name.upper()}, {rov_t.t_location.title()} | Description : {rov_t.t_description}")
        print(f"Start : {rov_t.t_start_date} | End : {rov_t.t_end_date} | Time control : {rov_t.t_time_control}\n")

        print(self.rov_table)

    @staticmethod
    def rov_round_head(rov_t, rov_t_start_time):
        """Display the tournament info as a round header"""
        print("\n\n")

        rov_h_1 = f"{rov_t.t_name.upper()}, {rov_t.t_location.title()} | Description : {rov_t.t_description}"
        rov_h_2 = f"t_Start date and time : {rov_t.t_start_date} | Time control : {rov_t.t_time_control}\n"
        rov_h_3 = f"- ROUND {rov_t.t_current_round}/{rov_t.t_rounds_total} | {rov_t_start_time} -"

        print(rov_h_1.center(100, " "))
        print(rov_h_2.center(100, " "))
        print(rov_h_3.center(100, " "))

    @staticmethod
    def rov_round_over():
        print("\nLaunch Round matches ? [ok]")
        print("Back to main menu ? [back]")

    @staticmethod
    def rov_score_options(rov_match_number):
        print("\nMatch ", rov_match_number)
        print('[0] Tie')
        print('[1] Player 1 wins')
        print('[2] Player 2 wins')
        print("\n[back] Back to main menu")

    @staticmethod
    def rov_score_prompt():
        print('\nEnter result :', end=' ')
