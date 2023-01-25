# This is the file that gets the inputs for the tournament
# Import what is needed
from datetime import datetime
from models.player_model import PModel
from models.round_model import RModel
from views.round_view import RoView
from views.main_view import MView


class TController:
    """Class of the tournament controller"""

    def __init__(self):
        """Init of the tournament controller"""
        self.m_view = MView()
        self.ro_view = RoView()
        self.tc_chrono = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def tc_begin_tournament(self, tc):
        """Tournament beginning"""
        if tc.t_current_round == 1:
            """Start the first round"""
            tc.start_date = self.tc_chrono
            """Start the 'chrono'"""
            tc.t_update_the_timer(tc.t_start_date, 't_start_date')
            """Update the time when the tournament begin"""

            self.tc_first_round(tc)
            tc.t_current_round += 1
            """Increment the number of round each time 1 round finish"""
            tc.t_update_tournament_db()
            """Update the DB-data"""

            while tc.t_current_round <= tc.t_rounds_total:
                """Start the next rounds"""
                self.tc_next_rounds(tc)
                tc.t_current_round += 1
                """Add 1 to the number of rounds"""
                tc.t_update_tournament_db()
            """Update the DB-data"""

        elif 1 < tc.t_current_round <= tc.t_rounds_total:
            while tc.t_current_round <= tc.t_rounds_total:
                """Must be four rounds in total, so it continue until their is four rounds"""
                self.tc_next_rounds(tc)
                """Next round coming up"""
                tc.t_current_round += 1
                """Add 1 to the number of rounds"""
                tc.t_update_tournament_db()
                """Update the DB-data"""

            tc.t_end_date = self.tc_chrono
            """The end 'chrono' of the tournament"""
            tc.t_update_the_timer(tc.t_end_date, 'end_date')
            """Update the end 'chrono' of the tournament"""
            self.t_tournament_end(tc)
            """Call the end method for the tournament"""

        elif tc.t_current_round > tc.rounds_total:
            """Ending of the tournament"""
            self.t_tournament_end(tc)
            """Call the end method for the tournament"""

    def tc_first_round(self, tc):
        """First round : top players versus bottom players"""
        r = RModel("Round 1", self.tc_chrono, "To Determine")
        tc.t_sort_players_by_rank()
        top_players, bottom_players = tc.t_split_the_players()
        self.ro_view.rov_round_head(tc, r.r_start_datetime)

        for i in range(tc.t_rounds_total):
            r.r_get_pairing(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.t_update_opponents(top_players[i], bottom_players[i])

        self.ro_view.rov_display_matches(r.r_matches)

        self.ro_view.rov_round_over()
        self.m_view.mv_input_prompt()
        tc_user_input = input().lower()
        tc_scores_list = []

        if tc_user_input == "ok" or "OK":
            r.end_datetime = self.tc_chrono
            tc.rounds.append(r.r_set_the_round())
            tc.merge_the_players(top_players, bottom_players)

            self.t_end_of_round(tc_scores_list, tc)

        elif tc_user_input == "back" or "BACK":
            self.tc_going_back_to_menu()

    def tc_next_rounds(self, tc):
        """Next rounds : set possible pairings"""
        r = RModel(("r_Round " + str(tc.r_current_round)), self.tc_chrono, "r_To determine")
        tc.t_sort_players_by_score()
        self.ro_view.rov_round_head(tc, r.r_start_datetime)

        tc_available_list_p = tc.t_players
        tc_players_added = []

        k = 0
        while k < tc.t_rounds_total:
            if tc_available_list_p[1]["p_id"] in tc_available_list_p[0]["p_versus"]:
                try:
                    available_list, players_added = \
                        self.t_match_other_option(tc_available_list_p, tc_players_added, r)
                    tc.t_players = players_added

                except IndexError:
                    available_list, players_added = \
                        self.tc_match_begin_option(tc_available_list_p, tc_players_added, r)
                    tc.t_players = players_added

            elif tc_available_list_p[1]["p_id"] not in tc_available_list_p[0]["p_versus"]:
                available_list, players_added = \
                    self.tc_match_begin_option(tc_available_list_p, tc_players_added, r)
                tc.t_players = players_added

            k += 1

        self.ro_view.rov_display_matches(r.r_matches)

        self.ro_view.rov_round_over()
        self.m_view.mv_input_prompt()
        tc_user_input = input().lower()
        tc_scores_list = []

        if tc_user_input == "ok" or "OK":
            r.end_datetime = self.tc_chrono
            tc.rounds.append(r.r_set_the_round())
            self.t_end_of_round(tc_scores_list, tc)

        elif tc_user_input == "back" or "BACK":
            self.tc_going_back_to_menu()

    def tc_match_begin_option(self, t_available_list_p, t_players_added, r):
        """Main pairing option"""
        r.get_pairing(t_available_list_p[0], t_available_list_p[1])
        t_available_list_p[0], t_available_list_p[1] = self.t_update_opponents(t_available_list_p[0],
                                                                               t_available_list_p[1])

        t_available_list_p, t_players_added = self.t_update_player_lists(
            t_available_list_p[0],
            t_available_list_p[1],
            t_available_list_p,
            t_players_added
        )

        return t_available_list_p, t_players_added

    def t_match_other_option(self, t_available_list_p, t_players_added, r):
        """Alternative pairing option"""
        r.get_pairing(t_available_list_p[0], t_available_list_p[2])
        t_available_list_p[0], t_available_list_p[2] = self.t_update_opponents(t_available_list_p[0],
                                                                               t_available_list_p[2])

        t_available_list_p, t_players_added = self.t_update_player_lists(
            t_available_list_p[0],
            t_available_list_p[2],
            t_available_list_p,
            t_players_added
        )

        return t_available_list_p, t_players_added

    def t_end_of_round(self, t_scores_list: list, t):
        """End of round : update player scores"""
        for i in range(t.rounds_total):
            self.ro_view.rov_score_options(i + 1)
            t_response = self.t_input_scores()
            t_scores_list = self.t_get_scores(t_response, t_scores_list)

        t.t_players = self.t_update_scores(t.t_players, t_scores_list)

        return t.t_players

    def t_input_scores(self):
        """Score input"""
        self.ro_view.rov_score_prompt()
        selection = input()
        return selection

    def t_get_scores(self, selection, scores_list: list):
        """Input scores for each match in current round"""
        if selection == "0":
            scores_list.extend([0.5, 0.5])
            return scores_list
        elif selection == "1":
            scores_list.extend([1.0, 0.0])
            return scores_list
        elif selection == "2":
            scores_list.extend([0.0, 1.0])
            return scores_list
        elif selection == "back" or "BACK":
            self.tc_going_back_to_menu()
        else:
            self.m_view.mv_input_errors()
            self.t_input_scores()

    @staticmethod
    def t_update_scores(players, scores_list: list):
        """Update player scores"""
        for i in range(len(players)):
            players[i]["score"] += scores_list[i]

        return players

    @staticmethod
    def t_update_player_lists(player_1, player_2, t_available_list_p, t_players_added):
        """Update player lists :"""
        t_players_added.extend([player_1, player_2])
        t_available_list_p.remove(player_1)
        t_available_list_p.remove(player_2)

        return t_available_list_p, t_players_added

    @staticmethod
    def t_update_opponents(player_1, player_2):
        player_1["p_versus"].append(player_2["p_id"])
        player_2["p_versus"].append(player_1["p_id"])

        return player_1, player_2

    def t_tournament_end(self, tc):
        """End of tournament : display final results
        and also offer user to update ranks"""
        tc.sort_players_by_rank()
        tc.sort_players_by_score()

        self.ro_view.rov_display_results(tc)

        self.m_view.mv_update_ranks()
        tc_user_input = input()

        tc_players = tc.players

        if tc_user_input == "n" or "N":
            self.tc_going_back_to_menu()

        elif tc_user_input == "y" or "Y":
            while True:
                self.tc_update_ranks(tc_players)

    def tc_update_ranks(self, tc_players):
        """Update player ranks and save to DB"""
        self.m_view.mv_select_players(tc_players, "to update")
        self.m_view.mv_input_prompt()
        user_input = input()

        if user_input == "back" or "BACK":
            self.tc_going_back_to_menu()

        for i in range(len(tc_players)):
            if int(user_input) == tc_players[i]["id"]:
                tc_p = tc_players[tc_players.index(tc_players[i])]
                tc_p = PModel(
                    tc_p['p_id'],
                    tc_p['p_lastname'],
                    tc_p['p_firstname'],
                    tc_p['p_date_of_birth'],
                    tc_p['p_gender'],
                    tc_p['p_rank']
                )

                self.m_view.mv_rank_update_head(tc_p)
                self.m_view.mv_prompt_text("new rank")
                tc_user_input = input()

                if tc_user_input == "back" or "BACK":
                    self.tc_going_back_to_menu()

                else:
                    tc_p.p_update_player_db(int(user_input), "p_rank")
                    tc_players[i]["p_rank"] = int(user_input)

                    return tc_players

    @staticmethod
    def tc_going_back_to_menu():
        """Go to the main menu"""
        from controllers.main_menu_controller import MMController
        MMController().mmc_menu_start()
