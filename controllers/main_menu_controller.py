# This is the main menu controller
from views.main_view import MView
from controllers.player_controller import PController
from controllers.tournament_controller import TController
from views.report_view import RView

cpt_match = 1
cpt_rounds = 1

players_list = []
tournament_list = []


class MMController:

    def main_menu(self):
        while True:
            MView.display_main_menu()
            try:
                selection = int(input("Enter a number from 1 to 4: "))
                print("You chose: ", selection)
                if selection == 1:
                    MMController.tournament_menu(self)
                elif selection == 3:
                    MMController.report_menu(self)
                elif selection == 2:
                    MMController.player_menu(self)
                elif selection == 4:
                    print("Goodbye !")
                    break
                else:
                    print("Sorry, that is not a valid number. Please try again.")
            except (ValueError, IOError):
                print("Sorry, that is not a valid number. Please try again.")
                continue

    def player_menu(self):
        while True:
            MView.display_player_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("You chose: ", selection)
                if selection == 1:
                    PController.creation_player(players_list)
                elif selection == 2:
                    PController.modification_player(players_list)
                elif selection == 3:
                    MMController.main_menu(self)
                else:
                    print("Sorry, that is not a valid number. Please try again.")
            except (ValueError, IOError):
                print("Sorry, that is not a valid number. Please try again.")
                continue

    def tournament_menu(self):
        while True:
            MView.display_tournament_menu()
            try:
                selection = int(input("Enter the tournament information: "))
                print("You chose: ", selection)
                if selection == 1:
                    TController.creation_tournament(tournament_list)
                elif selection == 2:
                    MMController.main_menu(self)
                else:
                    print("Sorry, that is not a valid number. Please try again.")
            except ValueError:
                print("Sorry, that is not a valid number. Please try again.")
                continue

    def report_menu(self):
        while True:
            MView.display_report_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("You chose: ", selection)
                if selection == 1:
                    RView.actors_view(self)
                elif selection == 2:
                    MMController.report2_menu(self)
                elif selection == 3:
                    MMController.main_menu(self)
                else:
                    print("Sorry, that is not a valid number. Please try again.")
            except ValueError:
                print("Sorry, that is not a valid number. Please try again.")
                continue

    def report2_menu(self):
        while True:
            MView.display_report2_menu()
            try:
                selection = int(input("Enter a number from 1 to 4: "))
                print("You chose: ", selection)
                if selection == 1:
                    RView.tournaments_players_view(self)
                elif selection == 2:
                    RView.tournaments_round_view(self)
                elif selection == 3:
                    RView.tournaments_matches_view(self)
                elif selection == 4:
                    MMController.report_menu(self)
                else:
                    print("Sorry, that is not a valid number. Please try again.")
            except ValueError:
                print("Sorry, that is not a valid number. Please try again.")
                continue

