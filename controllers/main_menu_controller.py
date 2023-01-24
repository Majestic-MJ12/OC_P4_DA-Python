# This is the file that gets the inputs for the menu
# Import what is needed
from models.player_model import PModel
from models.tournament_model import TModel
from controllers.report_controller import RController
from controllers.tournament_controller import TController
from views.main_view import MView


class MMController:
    """Class of the main menu controller"""

    def __init__(self):
        """Init of the main menu"""
        self.m_view = MView()
        self.t_controller = TController()
        self.r_controller = RController()

    def menu_start(self):
        """Main menu selector :
        Redirects to selected submenus"""

        self.m_view.main_menu()
        self.m_view.input_prompt()
        user_input = input().lower()

        if user_input == "1":
            """Launch a new tournament"""
            self.new_tournament()

        elif user_input == "2":
            """Resuming a tournament already started"""
            self.resume_tournament()

        elif user_input == "3":
            """Creating new player"""
            self.new_player()

        elif user_input == "4":
            """Updating a existing player"""
            self.update_player()

        elif user_input == "5":
            """Access to the report menu"""
            self.reports_menu()

        elif user_input == "exit":
            """Leaving the program"""
            self.m_view.are_you_sure_to_exit()
            user_input = input().lower()

            if user_input == "y":
                """Confirm that you want to leave the program"""
                exit()
            elif user_input == "n":
                """Well, in fact no I don't want to leave"""
                self.menu_start()

        else:
            self.m_view.input_errors()
            """Catch the inputs errors made by the user"""
            self.menu_start()
            """Going back to the beginning of the program (main menu)"""

    def new_tournament(self):
        """Create new tournament, serialize (dict) and save to DB-data"""
        self.m_view.create_tournament_head()
        """Create the header of what's going to be stored"""
        tournament_info = []
        options = [
            "name",
            "location",
            "description"
        ]

        for item in options:
            """Get the inputs"""
            self.m_view.prompt_text(item)
            user_input = input()

            if user_input == "back":
                self.menu_start()
                """Going back to main menu"""

            else:
                tournament_info.append(user_input)
                """Add the inputs"""

        tournament_info.append(self.time_control())
        """Adding the date, ..."""
        tour_players = self.selected_players(8)
        """Players that going to participate to the tournament"""

        self.m_view.review_tournament(tournament_info, tour_players)
        """Review the tournament information"""
        user_input = input().lower()

        if user_input == "y" or "Y":
            tournament = TModel(
                t_id=0,
                t_name=tournament_info[0],
                location=tournament_info[1],
                start_date="Not started",
                end_date="To Determine",
                description=tournament_info[2],
                time_control=tournament_info[3],
                players=tour_players,
                current_round=1,
                rounds=[]
            )
            tournament.save_tournament_db()
            """Saving the tournament with tinydb"""
            self.m_view.tournament_saved()
            """View that the tournament is saved"""

            self.m_view.input_prompt()
            """Get the inputs for the "options"""
            user_input = input()

            if user_input == "y" or "Y":
                self.t_controller.begin_tournament(tournament)
                """Start the tournament"""
            elif user_input == "n" or "N":
                """Don't start the tournament and go back to main menu"""
                self.menu_start()

        elif user_input == "n" or "N":
            self.menu_start()
            """Go back to main menu"""

    def time_control(self):
        """Select time control for new tournament"""
        self.m_view.time_options()
        """View the time option that can be selected"""
        self.m_view.input_prompt()
        """Get the inputs for the "options"""
        user_input = input()

        if user_input == "1":
            return "Bullet"
        elif user_input == "2":
            return "Blitz"
        elif user_input == "3":
            return "Quick"
        elif user_input == "back":
            self.menu_start()
            """Go back to main menu"""
        else:
            self.m_view.input_errors()
            """Handle the errors with the inputs from the users"""
            self.time_control()
            """Re start the method from the beginning"""

    def selected_players(self, players_total):
        """Select players for new tournament"""
        players = PModel.load_player_db()
        """Load the players present in the DB-data"""
        id_list = []
        for i in range(len(players)):
            """Add players to the selected players"""
            id_list.append(players[i]["id"])

        tour_players = []

        i = 0
        while i < players_total:
            """Waiting to have all the players needed selected"""
            self.m_view.select_players(players, i+1)
            self.m_view.input_prompt()
            user_input = input()

            if user_input == "back":
                """Go back to main menu"""
                self.menu_start()

            elif not user_input.isdigit():
                """Handle errors again"""
                self.m_view.input_errors()

            elif int(user_input) in id_list:
                """Handle the selection of players"""
                index = id_list.index(int(user_input))
                tour_players.append(players[index])
                id_list.remove(id_list[index])
                players.remove(players[index])
                i += 1
                """Add the selected players and remove them from the list once
                they've been already selected"""

            else:
                self.m_view.player_already_selected()
                """Warn user that player already been selected"""

        return tour_players

    def resume_tournament(self):
        """Select existing tournament to resume"""
        tournament_list = TModel.load_tournament_db()
        """Load the tournament from DB-data"""

        self.m_view.select_tournaments(tournament_list)
        """Get a view of the the tournaments"""
        self.m_view.input_prompt()
        """Waiting for user input"""
        user_input = input()

        if user_input == "back":
            self.menu_start()
            """Go back to main menu"""

        for i in range(len(tournament_list)):
            if user_input == str(tournament_list[i]["id"]):
                t = tournament_list[i]
                t = TModel(
                    t["id"],
                    t["name"],
                    t["location"],
                    t["start_date"],
                    t["end_date"],
                    t["description"],
                    t["time_control"],
                    t["current_round"],
                    t["players"],
                    t["rounds"],
                    t["rounds_total"]
                )
                self.t_controller.begin_tournament(t)
                """Begin tournament"""

    def new_player(self):
        """Create new player, serialize and save to DB"""
        self.m_view.create_new_player_head()
        """Create header for the players"""
        player_info = []
        options = [
            "last name",
            "first name",
            "date of birth (dd/mm/yyyy)",
            "gender [M/F]",
            "rank"
        ]
        for item in options:
            """Waiting for the input of user of what's going to be modified"""
            self.m_view.prompt_text(item)
            user_input = input()
            if user_input == "back":
                self.menu_start()
                """Go back to main menu"""
            else:
                player_info.append(user_input)
                """Making the change real"""

        MView.review_players(player_info)
        """View the players information"""
        user_input = input().lower()

        if user_input == "y" or "Y":
            """Saving the player to DB-data"""
            player = PModel(
                p_id=0,
                last_name=player_info[0],
                first_name=player_info[1],
                birthday=player_info[2],
                gender=player_info[3],
                rank=int(player_info[4])
            )

            player.save_player_db()
            self.m_view.players_saved()
            self.menu_start()

        elif user_input == "n" or "N":
            """Don't save it, and go back to main menu"""
            self.menu_start()

    def update_player(self):
        """Update existing player info"""
        players = PModel.load_player_db()
        """Load players already created from DB-data"""

        self.m_view.select_players(players, "to update")
        self.m_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.menu_start()
            """Go back to main menu"""

        p = players[int(user_input) - 1]
        p = PModel(
            p['id'],
            p['last_name'],
            p['first_name'],
            p['date_of_birth'],
            p['gender'],
            p['rank']
        )

        options = [
            "last name",
            "first name",
            "date of birth",
            "gender",
            "rank"
        ]
        self.m_view.update_players(p, options)
        """See the update player information view"""
        self.m_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.menu_start()
            """Go back to main menu"""

        elif int(user_input) <= len(options):
            """Handle bad user input if superior to what's proposed"""
            updated_info = (options[int(user_input) - 1]).replace(" ", "_")
            self.m_view.prompt_text(
                f"new {options[int(user_input) - 1]}")
            user_input = input()

            if user_input == "back":
                self.menu_start()
                """Go back to main menu"""

            else:
                """Update the DB-data"""
                p.update_player_db(user_input, updated_info)
                self.m_view.players_saved()

                self.update_player()

        else:
            """Handle errors from the user inputs"""
            self.m_view.input_errors()
            self.update_player()
            """Go back to the beginning of the method"""

    def reports_menu(self):
        """Reports menu"""
        self.m_view.reports_menu()
        """Get the view of the report menu"""
        self.m_view.input_prompt()
        """Waiting for a user input to choose what's next"""
        user_input = input()

        if user_input == "1":
            """Get the view of all players"""
            self.player_sorting(PModel.load_player_db())

        elif user_input == "2":
            """Get the view of players from one tournament"""
            self.player_sorting(self.r_controller.tournament_players())

        elif user_input == "3":
            """Get the view of all tournament"""
            self.r_controller.all_tournaments()

        elif user_input == "4":
            """Get the view of all rounds from one tournament"""
            self.r_controller.tournament_rounds()

        elif user_input == "5":
            """Get the view of all matches from one tournament"""
            self.r_controller.tournament_matches()

        elif user_input == "back":
            self.menu_start()
            """Go back to main menu"""

        else:
            """Handle errors from user inputs"""
            self.m_view.input_errors()
            self.reports_menu()
            """Start the method again"""

        self.m_view.other_reports()
        """Asking if you want to see an other report or no"""
        user_input = input()

        if user_input == "y":
            """Display the report menu again"""
            self.reports_menu()

        elif user_input == "n":
            """Go back to main menu because no I don't want to see another report"""
            self.menu_start()

    def player_sorting(self, players):
        """Select sorting option (name or rank choices) for players"""
        self.m_view.reports_player_sort()
        """How you want to sort the players"""
        self.m_view.input_prompt()
        user_input = input()

        if user_input == "1":
            """Sort them by their names"""
            self.r_controller.all_players_by_name(players)

        elif user_input == "2":
            """Sort them by their ranks"""
            self.r_controller.all_players_by_rank(players)

        elif user_input == "back":
            """Go back to main menu"""
            self.menu_start()
