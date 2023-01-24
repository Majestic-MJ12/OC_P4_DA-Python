# This is the file that gets the inputs for the tournament
# Import what is needed
from datetime import datetime
from models.player_model import PModel
from models.round_model import RModel
from views.round_view import RView
from views.main_view import MView


class TController:
    """Class of the tournament controller"""

    def __init__(self):
        """Init of the tournament controller"""
        self.menu_view = MView()
        self.round_view = RView()
        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def begin_tournament(self, t):
        """Tournament beginning"""
        if t.current_round == 1:
            """Start the first round"""
            t.start_date = self.timer
            t.update_the_timer(t.start_date, 'start_date')

            self.first_round(t)
            t.current_round += 1
            t.update_tournament_db()

            while t.current_round <= t.rounds_total:
                """Start the next rounds"""
                self.next_rounds(t)
                t.current_round += 1
                t.update_tournament_db()

        elif 1 < t.current_round <= t.rounds_total:
            while t.current_round <= t.rounds_total:
                """Their must be four rounds, so it continue until their is four rounds"""
                self.next_rounds(t)
                t.current_round += 1
                t.update_tournament_db()

            t.end_date = self.timer
            t.update_the_timer(t.end_date, 'end_date')
            self.tournament_ending(t)

        elif t.current_round > t.rounds_total:
            """Ending of the tournament"""
            self.tournament_ending(t)

    def first_round(self, t):
        """First round : top players versus bottom players"""
        r = RModel("Round 1", self.timer, "TBD")
        t.sort_players_by_rank()
        top_players, bottom_players = t.split_the_players()
        self.round_view.round_head(t, r.start_datetime)

        for i in range(t.rounds_total):
            r.get_pairing(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.update_opponents(top_players[i], bottom_players[i])

        self.round_view.display_matches(r.matches)

        self.round_view.round_over()
        self.menu_view.input_prompt()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok" or "OK":
            r.end_datetime = self.timer
            t.rounds.append(r.set_the_round())
            t.merge_the_players(top_players, bottom_players)

            self.end_of_round(scores_list, t)

        elif user_input == "back" or "BACK":
            self.going_back_to_menu()

    def next_rounds(self, t):
        """Next rounds : set possible pairings"""
        r = RModel(("Round " + str(t.current_round)), self.timer, "TBD")
        t.sort_players_by_score()
        self.round_view.round_head(t, r.start_datetime)

        available_list = t.players
        players_added = []

        k = 0
        while k < t.rounds_total:
            if available_list[1]["id"] in available_list[0]["opponents"]:
                try:
                    available_list, players_added = \
                        self.match_other_option(available_list, players_added, r)
                    t.players = players_added

                except IndexError:
                    available_list, players_added = \
                        self.match_begin_option(available_list, players_added, r)
                    t.players = players_added

            elif available_list[1]["id"] not in available_list[0]["opponents"]:
                available_list, players_added = \
                    self.match_begin_option(available_list, players_added, r)
                t.players = players_added

            k += 1

        self.round_view.display_matches(r.matches)

        self.round_view.round_over()
        self.menu_view.input_prompt()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok" or "OK":
            r.end_datetime = self.timer
            t.rounds.append(r.set_the_round())
            self.end_of_round(scores_list, t)

        elif user_input == "back" or "BACK":
            self.going_back_to_menu()

    def match_begin_option(self, available_list, players_added, r):
        """Main pairing option"""
        r.get_pairing(available_list[0], available_list[1])
        available_list[0], available_list[1] = self.update_opponents(available_list[0], available_list[1])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[1],
            available_list,
            players_added
        )

        return available_list, players_added

    def match_other_option(self, available_list, players_added, r):
        """Alternative pairing option"""
        r.get_pairing(available_list[0], available_list[2])
        available_list[0], available_list[2] = self.update_opponents(available_list[0], available_list[2])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[2],
            available_list,
            players_added
        )

        return available_list, players_added

    def end_of_round(self, scores_list: list, t):
        """End of round : update player scores"""
        for i in range(t.rounds_total):
            self.round_view.score_options(i + 1)
            response = self.input_scores()
            scores_list = self.get_scores(response, scores_list)

        t.players = self.update_scores(t.players, scores_list)

        return t.players

    def input_scores(self):
        """Score input"""
        self.round_view.score_prompt()
        response = input()
        return response

    def get_scores(self, response, scores_list: list):
        """Input scores for each match in current round"""
        if response == "0":
            scores_list.extend([0.5, 0.5])
            return scores_list
        elif response == "1":
            scores_list.extend([1.0, 0.0])
            return scores_list
        elif response == "2":
            scores_list.extend([0.0, 1.0])
            return scores_list
        elif response == "back" or "BACK":
            self.going_back_to_menu()
        else:
            self.menu_view.input_errors()
            self.input_scores()

    @staticmethod
    def update_scores(players, scores_list: list):
        """Update player scores"""
        for i in range(len(players)):
            players[i]["score"] += scores_list[i]

        return players

    @staticmethod
    def update_player_lists(player_1, player_2, available_list, players_added):
        """Update player lists :"""
        players_added.extend([player_1, player_2])
        available_list.remove(player_1)
        available_list.remove(player_2)

        return available_list, players_added

    @staticmethod
    def update_opponents(player_1, player_2):
        player_1["opponents"].append(player_2["id"])
        player_2["opponents"].append(player_1["id"])

        return player_1, player_2

    def tournament_ending(self, t):
        """End of tournament : display final results
        and also offer user to update ranks"""
        t.sort_players_by_rank()
        t.sort_players_by_score()

        self.round_view.display_results(t)

        self.menu_view.update_ranks()
        user_input = input()

        players = t.players

        if user_input == "n" or "N":
            self.going_back_to_menu()

        elif user_input == "y" or "Y":
            while True:
                self.update_ranks(players)

    def update_ranks(self, players):
        """Update player ranks and save to DB"""
        self.menu_view.select_players(players, "to update")
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back" or "BACK":
            self.going_back_to_menu()

        for i in range(len(players)):
            if int(user_input) == players[i]["id"]:
                p = players[players.index(players[i])]
                p = PModel(
                    p['id'],
                    p['last_name'],
                    p['first_name'],
                    p['date_of_birth'],
                    p['gender'],
                    p['rank']
                )

                self.menu_view.rank_update_head(p)
                self.menu_view.prompt_text("new rank")
                user_input = input()

                if user_input == "back" or "BACK":
                    self.going_back_to_menu()

                else:
                    p.update_player_db(int(user_input), "rank")
                    players[i]["rank"] = int(user_input)

                    return players

    @staticmethod
    def going_back_to_menu():
        """Go to the main menu"""
        from controllers.main_menu_controller import MMController
        MMController().menu_start()
