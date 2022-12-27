# This is the main menu controller

# importing what is needed
from views.main_view import MView
from controllers.player_controller import PController
from controllers.tournament_controller import TController
from views.report_view import RView

# counters
cpt_match = 1
cpt_rounds = 1

# lists
players_list = [[1, "tttt", "fhffhfg", 12-12-2022, "f", 1, 2], [2, "yyyy", "fhffhfg", 12-12-2022, "f", 1, 2],
                    [3, "aaa", "fhffhfg", 12-12-2022, "f", 1, 2], [4, "dfhgdf", "fhffhfg", 12-12-2022, "f", 1, 2],
                    [5, "dfhgdf", "fhffhfg", 12-12-2022, "f", 1, 2], [6, "dfhgdf", "fhffhfg", 12-12-2022, "f", 1, 2],
                    [7, "dfhgdf", "fhffhfg", 12 - 12 - 2022, "f", 1, 2],
                    [8, "dfhgdf", "fhffhfg", 12-12-2022, "f", 1, 2]]
tournament_list = [[1, "efze", "zef", 12-12-2022, 4, "bullet", "fffff"], [2, "efze", "zef", 12-12-2022, 4, "bullet", "fffff"]]


# the controller for the main menu
class MMController:

    def main_menu(self):
        """function to choose the first choices of the menu"""
        while True:
            MView.display_main_menu()
            try:
                selection = int(input("Enter a number from 1 to 4: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    MMController.tournament_menu(self)
                elif selection == 3:
                    MMController.report_menu(self)
                elif selection == 2:
                    MMController.player_menu(self)
                elif selection == 4:
                    print("\nGoodbye !")
                    break
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except (ValueError, IOError):
                print("\nSorry, that is not a valid number. Please try again.")
                continue

    def player_menu(self):
        """function for the player selection"""
        while True:
            MView.display_player_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    PController.creation_player(players_list)
                elif selection == 2:
                    RView.actors_view()
                    PController.modification_player(players_list)
                elif selection == 3:
                    MMController.main_menu(self)
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except (ValueError, IOError):
                print("\nSorry, that is not a valid number. Please try again.")
                continue

    def tournament_menu(self):
        """function for the tournament selection"""
        while True:
            MView.display_tournament_menu()
            try:
                selection = int(input("Enter a number from 1 to 2: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    TController.creation_tournament(tournament_list)
                elif selection == 2:
                    MMController.main_menu(self)
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue

    def report_menu(self):
        """function for the first report menu"""
        while True:
            MView.display_report_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    RView.actors_view()
                    MMController.report3_menu(self)
                elif selection == 2:
                    RView.all_tournaments_view()
                    MMController.report2_menu(self)
                elif selection == 3:
                    MMController.main_menu(self)
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue

    def report2_menu(self):
        """function for the second report menu"""
        while True:
            try:
                id_tournament = int(input("\nChoose a tournament from the list displayed: "))
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue
            MView.display_report2_menu()
            try:
                selection = int(input("Enter a number from 1 to 4: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    RView.tournaments_players_view()
                elif selection == 2:
                    RView.tournaments_round_view(id_tournament)
                elif selection == 3:
                    RView.tournaments_matches_view(id_tournament)
                elif selection == 4:
                    MMController.report_menu(self)
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue

    def report3_menu(self):
        """function for the third report menu"""
        while True:
            MView.display_report3_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    PController.player_alpha_sort(players_list)
                    RView.actors_view()
                elif selection == 2:
                    PController.player_rank_sort(players_list)
                    RView.actors_view()
                elif selection == 3:
                    MMController.report2_menu(self)
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue
