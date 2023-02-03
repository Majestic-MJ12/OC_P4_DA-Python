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
        self.mv_view = MView()
        self.rov_view = RoView()
        self.tc_timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def tc_start_tournament(self, tc):
        """Tournament beginning"""
        if tc.t_current_round == 1:
            """Start the first round"""
            tc.t_start_date = self.tc_timer
            """Start the 'chrono'"""
            tc.t_update_the_timer(tc.t_start_date, 't_start_date')
            """Update the time when the tournament begin"""

            self.tc_first_round(tc)
            tc.t_current_round += 1
            """Increment the number of round each time 1 round finish"""
            tc.t_update_tournament_db()
            """Update the DB-data"""

            while tc.t_current_round <= 4:
                """Start the next rounds"""
                self.tc_next_rounds(tc)
                tc.t_current_round += 1
                """Add 1 to the number of rounds"""
                tc.t_update_tournament_db()
                """Update the DB-data"""

            while tc.t_current_round > 4:
                """Must be four rounds in total, so it must stop when there are four rounds"""
                tc.t_end_date = self.tc_timer
                """The end 'chrono' of the tournament"""
                tc.t_update_the_timer(tc.t_end_date, 't_end_date')
                """Update the end 'chrono' of the tournament"""
                self.tc_tournament_end(tc)
                """Call the end method for the tournament"""

    def tc_first_round(self, tc):
        """First round : top players versus bottom players"""
        r = RModel("Round 1", self.tc_timer, "To determine")
        tc.t_sort_players_by_rank()
        """Sorting all the players by their ranks"""
        top_players, bottom_players = tc.t_split_the_players()
        """Top players vs bottom players"""
        self.rov_view.rov_round_head(tc, r.r_start_datetime)
        """View the first round"""

        for i in range(tc.t_rounds_total):
            """The top player is going to fight the bottom player"""
            r.r_get_pairing(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.tc_update_opponents(top_players[i], bottom_players[i])

        self.rov_view.rov_display_matches(r.r_matches)
        """View the matches"""

        self.rov_view.rov_round_over()
        """View the round terminated"""
        self.mv_view.mv_input_prompt()
        """The view of the user prompt"""
        user_input = input().lower()
        tc_scores_list = []

        if user_input == "ok":
            r.end_datetime = self.tc_timer
            """Add the round end time"""
            tc.t_rounds.append(r.r_set_the_round())
            tc.t_merge_the_players(top_players, bottom_players)

            self.tc_end_of_round(tc_scores_list, tc)
            """Call the end of the round"""

        elif user_input == "back":
            self.tc_back_to_menu()
            """Go to the main menu"""

    def tc_next_rounds(self, tc):
        """Next rounds and set possible pairings"""
        r = RModel(("Round " + str(tc.t_current_round)), self.tc_timer, "To determine")
        tc.t_sort_players_by_score()
        """Sorting all players by their scores"""
        self.rov_view.rov_round_head(tc, r.r_start_datetime)
        """View the next rounds"""

        tc_available_list = tc.t_players
        tc_players_added = []

        k = 0
        while k < tc.t_rounds_total:
            if tc_available_list[1]["p_id"] in tc_available_list[0]["p_versus"]:
                try:
                    tc_available_list, tc_players_added = \
                        self.tc_match_other_option(tc_available_list, tc_players_added, r)
                    tc.t_players = tc_players_added

                except IndexError:
                    """Handle index errors"""
                    tc_available_list, tc_players_added = \
                        self.tc_match_first_option(tc_available_list, tc_players_added, r)
                    tc.t_players = tc_players_added

            elif tc_available_list[1]["p_id"] not in tc_available_list[0]["p_versus"]:
                tc_available_list, tc_players_added = \
                    self.tc_match_first_option(tc_available_list, tc_players_added, r)
                tc.t_players = tc_players_added

            k += 1

        self.rov_view.rov_display_matches(r.r_matches)
        """View the matches"""

        self.rov_view.rov_round_over()
        """View the round terminated"""
        self.mv_view.mv_input_prompt()
        """View the user input question"""
        tc_user_input = input().lower()
        tc_scores_list = []

        if tc_user_input == "ok":
            """Get the end time of the round"""
            r.t_end_datetime = self.tc_timer
            tc.t_rounds.append(r.r_set_the_round())
            self.tc_end_of_round(tc_scores_list, tc)

        elif tc_user_input == "back":
            self.tc_back_to_menu()
            """Go back to menu"""

    def tc_match_first_option(self, tc_available_list, tc_players_added, r):
        """Main pairing option"""
        r.r_get_pairing(tc_available_list[0], tc_available_list[1])
        tc_available_list[0], tc_available_list[1] = self.tc_update_opponents(tc_available_list[0],
                                                                              tc_available_list[1])

        tc_available_list, tc_players_added = self.tc_update_player_lists(
            tc_available_list[0],
            tc_available_list[1],
            tc_available_list,
            tc_players_added
        )

        return tc_available_list, tc_players_added

    def tc_match_other_option(self, tc_available_list, tc_players_added, r):
        """Alternative pairing option"""
        r.r_get_pairing(tc_available_list[0], tc_available_list[2])
        tc_available_list[0], tc_available_list[2] = self.tc_update_opponents(tc_available_list[0],
                                                                              tc_available_list[2])

        tc_available_list, tc_players_added = self.tc_update_player_lists(
            tc_available_list[0],
            tc_available_list[2],
            tc_available_list,
            tc_players_added
        )

        return tc_available_list, tc_players_added

    def tc_end_of_round(self, tc_scores_list: list, tc):
        """End of round : update player scores"""
        for i in range(tc.t_rounds_total):
            self.rov_view.rov_score_options(i + 1)
            tc_response = self.tc_input_scores()
            tc_scores_list = self.tc_get_score(tc_response, tc_scores_list)

        tc.t_players = self.tc_update_scores(tc.t_players, tc_scores_list)

        return tc.t_players

    def tc_input_scores(self):
        """Method to get the score inputs"""
        self.rov_view.rov_score_prompt()
        tc_response = input()
        return tc_response

    def tc_get_score(self, tc_response, tc_scores_list: list):
        """Input scores for each match in current round, and it's updating the scores
        depending on who wins and who loose"""
        if tc_response == "0":
            """Tie match"""
            tc_scores_list.extend([0.5, 0.5])
            return tc_scores_list

        elif tc_response == "1":
            """Player 1 wins"""
            tc_scores_list.extend([1.0, 0.0])
            return tc_scores_list

        elif tc_response == "2":
            """Player 2 wins"""
            tc_scores_list.extend([0.0, 1.0])
            return tc_scores_list

        elif tc_response == "back":
            """Stop the matches and go back to menu"""
            self.tc_back_to_menu()

        else:
            self.mv_view.mv_input_errors()
            """Get the inputs errors"""
            self.tc_input_scores()
            """Retrieve all the inputs"""

    @staticmethod
    def tc_update_scores(tc_players, tc_scores_list: list):
        """Update the players scores"""
        for i in range(len(tc_players)):
            tc_players[i]["p_score"] += tc_scores_list[i]

        return tc_players

    @staticmethod
    def tc_update_player_lists(tc_player_1, tc_player_2, tc_available_list, tc_players_added):
        """Update player lists by adding and removing them alternatively"""
        tc_players_added.extend([tc_player_1, tc_player_2])
        tc_available_list.remove(tc_player_1)
        tc_available_list.remove(tc_player_2)

        return tc_available_list, tc_players_added

    @staticmethod
    def tc_update_opponents(tc_player_1, tc_player_2):
        """Who's fighting who"""
        tc_player_1["p_versus"].append(tc_player_2["p_id"])
        tc_player_2["p_versus"].append(tc_player_1["p_id"])

        return tc_player_1, tc_player_2

    def tc_tournament_end(self, tc):
        """End of tournament : display final results,
         and it is also offering te user to update ranks"""
        tc.t_sort_players_by_rank()
        tc.t_sort_players_by_score()
        self.rov_view.rov_display_results(tc)

        self.mv_view.mv_update_ranks()
        tc_user_input = input()
        tc_players = tc.t_players

        if tc_user_input == "n":
            self.tc_back_to_menu()

        elif tc_user_input == "y":
            while True:
                self.tc_update_ranks(tc_players)

    def tc_update_ranks(self, tc_players):
        """Update player ranks and save to DB-data"""
        self.mv_view.mv_select_players(tc_players, "to update")
        self.mv_view.mv_input_prompt()
        tc_user_input = input()

        if tc_user_input == "back":
            self.tc_back_to_menu()
            """Go back to menu"""

        for i in range(len(tc_players)):
            if int(tc_user_input) == tc_players[i]["p_id"]:
                p = tc_players[tc_players.index(tc_players[i])]
                p = PModel(
                    p['p_id'],
                    p['p_lastname'],
                    p['p_firstname'],
                    p['p_date_of_birth'],
                    p['p_gender'],
                    p['p_rank']
                )

                self.mv_view.mv_rank_update_head(p)
                self.mv_view.mv_prompt_text("new rank")
                tc_user_input = input()

                if tc_user_input == "back":
                    self.tc_back_to_menu()
                    """Go back to menu"""

                else:
                    p.p_update_player_db(int(tc_user_input), "p_rank")
                    tc_players[i]["p_rank"] = int(tc_user_input)

                    return tc_players

    @staticmethod
    def tc_back_to_menu():
        """Going back to menu at any time when 'back' is typed and entered"""
        from controllers.main_menu_controller import MMController
        MMController().mmc_menu_start()
