# This is the file that is used for the reports view
# Import what is needed
from prettytable import PrettyTable
"""A simple Python library for easily
displaying tabular data in a visually
appealing ASCII table format."""


class ReView:
    """Class of the report view"""

    def __init__(self):
        """Init of the report view"""
        self.rev_table = PrettyTable()
        self.rev_player_report_field_names = [
            "p_ID",
            "p_Last name",
            "p_First name",
            "p_Gender",
            "p_Date of birth",
            "p_Rank"
        ]

        self.rev_tournament_report_field_names = [
            "t_ID",
            "t_Name",
            "t_Location",
            "t_Description",
            "t_Start date",
            "t_End date",
            "t_Time control",
            "t_Last round played",
            "t_Players (ID : Name)",
        ]

        self.rev_matches_report_field_names = [
            "m_Name P1",
            "m_Rank P1",
            "m_Score P1",
            " ",
            "m_Name P2",
            "m_Rank P2",
            "m_Score P2"
        ]

        self.rev_rounds_report_field_names = [
            "r_Round #",
            "r_Started at",
            "r_Ended at",
            "r_Matches"
        ]

    def rv_display_players(self, rev_players, rev_sorting):
        """Display the player report"""
        self.rev_table.clear()
        self.rev_table.field_names = self.rev_player_report_field_names
        self.rev_table.align = "l"

        for i in range(len(rev_players)):
            self.rev_table.add_row([
                rev_players[i]["p_id"],
                rev_players[i]["p_lastname"],
                rev_players[i]["p_firstname"],
                rev_players[i]["p_gender"],
                rev_players[i]["p_date_of_birth"],
                rev_players[i]["p_rank"]
            ])

        print(f"\n\n\n- All players ({rev_sorting}) -\n")
        print(self.rev_table)

    def rv_display_tournaments_report(self, rev_tournaments):
        """Display the tournament reports"""
        self.rev_table.clear()
        self.rev_table.field_names = self.rev_tournament_report_field_names
        self.rev_table.align = "l"

        for i in range(len(rev_tournaments)):
            participants = []
            players = rev_tournaments[i]["players"]
            for k in range(len(players)):
                participants.append(
                    str(players[k]["p_id"]) + " : " + players[k]["p_lastname"])

            self.rev_table.add_row([
                rev_tournaments[i]["t_id"],
                rev_tournaments[i]["t_name"],
                rev_tournaments[i]["t_location"],
                rev_tournaments[i]["t_description"],
                rev_tournaments[i]["t_start_date"],
                rev_tournaments[i]["t_end_date"],
                rev_tournaments[i]["t_time_control"],
                str(rev_tournaments[i]["t_current_round"]-1) + "/" + str(rev_tournaments[i]["t_rounds_total"]),
                participants
            ])

        print("\n\n\n- All tournaments -\n")
        print(self.rev_table)

    def rv_display_match_report(self, rev_matches):
        """Display the matches in tournament report"""
        self.rev_table.clear()
        self.rev_table.field_names = self.rev_matches_report_field_names
        self.rev_table.align = "l"

        for i in range(len(rev_matches)):
            rev_matches[i].insert(3, "versus.")
            self.rev_table.add_row(rev_matches[i])

        print(f"\n\n- All played matches ({len(rev_matches)} total) -\n")
        print(self.rev_table)

    def rv_display_rounds_report(self, rev_rounds):
        """Display the rounds in tournament report"""
        self.rev_table.clear()
        self.rev_table.field_names = self.rev_rounds_report_field_names
        self.rev_table.align = "l"

        for i in range(len(rev_rounds)):
            for j in range(4):
                if j == 0:
                    self.rev_table.add_row([
                        rev_rounds[i][0],
                        rev_rounds[i][1],
                        rev_rounds[i][2],
                        rev_rounds[i][3][j]
                    ])
                else:
                    self.rev_table.add_row([
                        ' ',
                        ' ',
                        ' ',
                        rev_rounds[i][3][j]
                    ])

        print("\n\n- All played rounds -\n")
        print(self.rev_table)

    @staticmethod
    def rv_report_head(rev_info):
        """Header for tournament reports"""
        print("\n\n")

        rev_header_1 = f"{rev_info['t_name'].upper()}," \
                       f" {rev_info['t_location'].title()} | t_Description : {rev_info['t_description']}"
        rev_header_2 = \
            f"t_Start date : {rev_info['t_start_date']} | " \
            f"t_End date : {rev_info['t_end_date']} | " \
            f"t_Time control : {rev_info['t_time_control']} | " \
            f"t_Rounds played : {rev_info['t_current_round']-1}/{rev_info['t_rounds_total']}"

        print(rev_header_1)
        print(rev_header_2)
