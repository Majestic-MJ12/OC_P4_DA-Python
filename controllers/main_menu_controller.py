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

    def mmc_menu_start(self):
        """Main menu selector :
        Redirects to selected submenus"""

        self.m_view.mv_main_menu()
        self.m_view.mv_input_prompt()
        mmc_user_input = input().lower()

        if mmc_user_input == "1":
            """Launch a new tournament"""
            self.mmc_new_tournament()

        elif mmc_user_input == "2":
            """Resuming a tournament already started"""
            self.mmc_resume_tournament()

        elif mmc_user_input == "3":
            """Creating new player"""
            self.mmc_new_player()

        elif mmc_user_input == "4":
            """Updating a existing player"""
            self.mmc_update_player()

        elif mmc_user_input == "5":
            """Access to the report menu"""
            self.mmc_reports_menu()

        elif mmc_user_input == "exit":
            """Leaving the program"""
            self.m_view.mv_are_you_sure_to_exit()
            mmc_user_input = input().lower()

            if mmc_user_input == "y":
                """Confirm that you want to leave the program"""
                exit()
            elif mmc_user_input == "n":
                """Well, in fact no I don't want to leave"""
                self.mmc_menu_start()

        else:
            self.m_view.mv_input_errors()
            """Catch the inputs errors made by the user"""
            self.mmc_menu_start()
            """Going back to the beginning of the program (main menu)"""

    def mmc_new_tournament(self):
        """Create new tournament, serialize (dict) and save to DB-data"""
        self.m_view.mv_create_tournament_head()
        """Create the header of what's going to be stored"""
        mmc_tournament_information = []
        mmc_options = [
            "t_name",
            "t_location",
            "t_description"
        ]

        for item in mmc_options:
            """Get the inputs"""
            self.m_view.mv_prompt_text(item)
            mmc_user_input = input()

            if mmc_user_input == "back":
                self.mmc_menu_start()
                """Going back to main menu"""

            else:
                mmc_tournament_information.append(mmc_user_input)
                """Add the inputs"""

        mmc_tournament_information.append(self.mmc_time_control())
        """Adding the date, ..."""
        mmc_tour_players = self.mmc_selected_players(8)
        """Players that going to participate to the tournament"""

        self.m_view.mv_review_tournament(mmc_tournament_information, mmc_tour_players)
        """Review the tournament information"""
        mmc_user_input = input().lower()

        if mmc_user_input == "y" or "Y":
            mmc_tournament = TModel(
                t_id=0,
                t_name=mmc_tournament_information[0],
                t_location=mmc_tournament_information[1],
                t_start_date="Not started",
                t_end_date="To Determine",
                t_description=mmc_tournament_information[2],
                t_time_control=mmc_tournament_information[3],
                t_players=mmc_tour_players,
                t_current_round=1,
                t_rounds=[]
            )
            mmc_tournament.t_save_tournament_db()
            """Saving the tournament with tinydb"""
            self.m_view.mv_tournament_saved()
            """View that the tournament is saved"""

            self.m_view.mv_input_prompt()
            """Get the inputs for the "options"""
            mmc_user_input = input()

            if mmc_user_input == "y" or "Y":
                self.t_controller.tc_begin_tournament(mmc_tournament)
                """Start the tournament"""
            elif mmc_user_input == "n" or "N":
                """Don't start the tournament and go back to main menu"""
                self.mmc_menu_start()

        elif mmc_user_input == "n" or "N":
            self.mmc_menu_start()
            """Go back to main menu"""

    def mmc_time_control(self):
        """Select time control for new tournament"""
        self.m_view.mv_time_options()
        """View the time option that can be selected"""
        self.m_view.mv_input_prompt()
        """Get the inputs for the "options"""
        mmc_user_input = input()

        if mmc_user_input == "1":
            return "Bullet"
        elif mmc_user_input == "2":
            return "Blitz"
        elif mmc_user_input == "3":
            return "Quick"
        elif mmc_user_input == "back":
            self.mmc_menu_start()
            """Go back to main menu"""
        else:
            self.m_view.mv_input_errors()
            """Handle the errors with the inputs from the users"""
            self.mmc_time_control()
            """Re start the method from the beginning"""

    def mmc_selected_players(self, mmc_players_total):
        """Select players for new tournament"""
        mmc_players = PModel.p_load_player_db()
        """Load the players present in the DB-data"""
        mmc_ids_list = []
        for i in range(len(mmc_players)):
            """Add players to the selected players"""
            mmc_ids_list.append(mmc_players[i]["p_id"])

        mmc_tournament_players = []

        i = 0
        while i < mmc_players_total:
            """Waiting to have all the players needed selected"""
            self.m_view.mv_select_players(mmc_players, i+1)
            self.m_view.mv_input_prompt()
            mmc_user_input = input()

            if mmc_user_input == "back":
                """Go back to main menu"""
                self.mmc_menu_start()

            elif not mmc_user_input.isdigit():
                """Handle errors again"""
                self.m_view.mv_input_errors()

            elif int(mmc_user_input) in mmc_ids_list:
                """Handle the selection of players"""
                mmc_index = mmc_ids_list.index(int(mmc_user_input))
                mmc_tournament_players.append(mmc_players[mmc_index])
                mmc_ids_list.remove(mmc_ids_list[mmc_index])
                mmc_players.remove(mmc_players[mmc_index])
                i += 1
                """Add the selected players and remove them from the list once
                they've been already selected"""

            else:
                self.m_view.mv_player_already_selected()
                """Warn user that player already been selected"""

        return mmc_tournament_players

    def mmc_resume_tournament(self):
        """Select existing tournament to resume"""
        mmc_tournament_list = TModel.t_load_tournament_db()
        """Load the tournament from DB-data"""

        self.m_view.mv_select_tournaments(mmc_tournament_list)
        """Get a view of the the tournaments"""
        self.m_view.mv_input_prompt()
        """Waiting for user input"""
        mmc_user_input = input()

        if mmc_user_input == "back":
            self.mmc_menu_start()
            """Go back to main menu"""

        for i in range(len(mmc_tournament_list)):
            if mmc_user_input == str(mmc_tournament_list[i]["t_id"]):
                mmc_t = mmc_tournament_list[i]
                mmc_t = TModel(
                    mmc_t["t_id"],
                    mmc_t["t_name"],
                    mmc_t["t_location"],
                    mmc_t["t_start_date"],
                    mmc_t["t_end_date"],
                    mmc_t["t_description"],
                    mmc_t["t_time_control"],
                    mmc_t["t_current_round"],
                    mmc_t["t_players"],
                    mmc_t["t_rounds"],
                    mmc_t["t_rounds_total"]
                )
                self.t_controller.tc_begin_tournament(mmc_t)
                """Begin the tournament"""

    def mmc_new_player(self):
        """Create new player, serialize and save to DB"""
        self.m_view.mv_create_new_player_head()
        """Create header for the players"""
        mmc_player_information = []
        mmc_options = [
            "p_last name",
            "p_first name",
            "p_date of birth (dd/mm/yyyy)",
            "p_gender [M/F]",
            "p_rank"
        ]
        for item in mmc_options:
            """Waiting for the input of user of what's going to be modified"""
            self.m_view.mv_prompt_text(item)
            mm_user_input = input()
            if mm_user_input == "back":
                self.mmc_menu_start()
                """Go back to main menu"""
            else:
                mmc_player_information.append(mm_user_input)
                """Making the change real"""

        MView.mv_review_players(mmc_player_information)
        """View the players information"""
        mmc_user_input = input().lower()

        if mmc_user_input == "y" or "Y":
            """Saving the player to DB-data"""

            mmc_player = PModel(
                p_id=0,
                p_lastname=mmc_player_information[0],
                p_firstname=mmc_player_information[1],
                p_birth=mmc_player_information[2],
                p_gender=mmc_player_information[3],
                p_rank=int(mmc_player_information[4])
            )

            mmc_player.p_save_player_db()
            self.m_view.mv_players_saved()
            """View the players saved"""
            self.mmc_menu_start()
            """Going back to menu"""

        elif mmc_user_input == "n" or "N":
            """Don't save it, and go back to main menu"""
            self.mmc_menu_start()
            """Going back to menu"""

    def mmc_update_player(self):
        """Update existing player info"""
        mmc_players = PModel.p_load_player_db()
        """Load players already created from DB-data"""

        self.m_view.mv_select_players(mmc_players, "to update")
        """Display the player to update"""
        self.m_view.mv_input_prompt()
        mmc_user_input = input()

        if mmc_user_input == "back":
            self.mmc_menu_start()
            """Go back to main menu"""

        mmc_p = mmc_players[int(mmc_user_input) - 1]
        mmc_p = PModel(
            mmc_p['p_id'],
            mmc_p['p_lastname'],
            mmc_p['p_firstname'],
            mmc_p['p_date_of_birth'],
            mmc_p['p_gender'],
            mmc_p['p_rank']
        )

        mmc_options = [
            "p_lastname",
            "p_firstname",
            "p_date_of_birth",
            "p_gender",
            "p_rank"
        ]
        self.m_view.mv_update_players(mmc_p, mmc_options)
        """See the update player information view"""
        self.m_view.mv_input_prompt()
        mmc_user_input = input()

        if mmc_user_input == "back":
            self.mmc_menu_start()
            """Go back to main menu"""

        elif int(mmc_user_input) <= len(mmc_options):
            """Handle bad user input if superior to what's proposed"""
            updated_info = (mmc_options[int(mmc_user_input) - 1]).replace(" ", "_")
            self.m_view.mv_prompt_text(
                f"new {mmc_options[int(mmc_user_input) - 1]}")
            mmc_user_input = input()

            if mmc_user_input == "back":
                self.mmc_menu_start()
                """Go back to main menu"""

            else:
                """Update the DB-data"""
                mmc_p.p_update_player_db(mmc_user_input, updated_info)
                self.m_view.mv_players_saved()

                self.mmc_update_player()

        else:
            """Handle errors from the user inputs"""
            self.m_view.mv_input_errors()
            self.mmc_update_player()
            """Go back to the beginning of the method"""

    def mmc_reports_menu(self):
        """Reports menu"""
        self.m_view.mv_reports_menu()
        """Get the view of the report menu"""
        self.m_view.mv_input_prompt()
        """Waiting for a user input to choose what's next"""
        mmc_user_input = input()

        if mmc_user_input == "1":
            """Get the view of all players"""
            self.mmc_player_sorting(PModel.p_load_player_db())

        elif mmc_user_input == "2":
            """Get the view of players from one tournament"""
            self.mmc_player_sorting(self.r_controller.rc_tournament_players())

        elif mmc_user_input == "3":
            """Get the view of all tournament"""
            self.r_controller.rc_all_tournaments()

        elif mmc_user_input == "4":
            """Get the view of all rounds from one tournament"""
            self.r_controller.rc_tournament_rounds()

        elif mmc_user_input == "5":
            """Get the view of all matches from one tournament"""
            self.r_controller.rc_tournament_matches()

        elif mmc_user_input == "back":
            self.mmc_menu_start()
            """Go back to main menu"""

        else:
            """Handle errors from user inputs"""
            self.m_view.mv_input_errors()
            self.mmc_reports_menu()
            """Start the method again"""

        self.m_view.mv_other_reports()
        """Asking if you want to see an other report or no"""
        user_input = input()

        if user_input == "y":
            """Display the report menu again"""
            self.mmc_reports_menu()

        elif user_input == "n":
            """Go back to main menu because no I don't want to see another report"""
            self.mmc_menu_start()

    def mmc_player_sorting(self, players):
        """Select sorting option (name or rank choices) for players"""
        self.m_view.mv_reports_player_sort()
        """How you want to sort the players"""
        self.m_view.mv_input_prompt()
        mmc_user_input = input()

        if mmc_user_input == "1":
            """Sort them by their names"""
            self.r_controller.rc_all_players_by_name(players)

        elif mmc_user_input == "2":
            """Sort them by their ranks"""
            self.r_controller.rc_all_players_by_rank(players)

        elif mmc_user_input == "back":
            """Go back to main menu"""
            self.mmc_menu_start()
