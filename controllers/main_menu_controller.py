# This is the main menu controller

# importing what is needed
from views.main_view import MView
from controllers.player_controller import PController
from controllers.tournament_controller import TController
from controllers.round_controller import RController
from controllers.match_controller import MController
from views.report_view import RView


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
                    print("\nSorry, that is not a valid selection. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue
            except IOError:
                print("\nAn input/output error occurred. Please try again.")
                continue

    def player_menu(self):
        """function for the player selection"""
        p_controller = PController()
        while True:
            MView.display_player_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    p_controller.creation_player(PController.players_list)
                elif selection == 2:
                    RView.actors_view()
                    PController.modification_player(PController.players_list)
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
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    TController.creation_tournament(TController.tournament_list)
                elif selection == 2:
                    MController.pair_generation(MController.match_list)
                    MController.match_result(MController.match_list)
                    print(MController.match_result(match_list=MController.match_list))
                    RController.round_creation(RController.rounds_list)
                    print(RController.rounds_list)
                elif selection == 3:
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
                id_tournament = int(input("\nChoose a tournament from the all tournament list displayed: ")) - 1
                if id_tournament < 0 or id_tournament >= len(TController.tournament_list):
                    raise IndexError
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue
            except IndexError:
                print("\nSorry, that is not a valid tournament ID. Please try again.")
                break
            try:
                MView.display_report2_menu()
                selection = int(input("Enter a number from 1 to 4: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    RView.tournaments_players_view()
                elif selection == 2:
                    RView.tournaments_round_view(TController.tournament_list, id_tournament)
                elif selection == 3:
                    RView.tournaments_matches_view(PController.players_list, id_tournament)
                elif selection == 4:
                    MMController.report_menu(self)
                else:
                    print("\nSorry, that is not a valid selection. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue
            except IndexError:
                print("\nSorry, that is not a valid tournament ID. Please try again.")
                continue

    def report3_menu(self):
        """function for the third report menu"""
        while True:
            MView.display_report3_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    PController.player_alpha_sort(PController.players_list)
                    RView.actors_view_alpha()
                    PController.player_id_sort(PController.players_list)
                elif selection == 2:
                    PController.player_rank_sort(PController.players_list)
                    RView.actors_view_rank()
                    PController.player_id_sort(PController.players_list)
                elif selection == 3:
                    MMController.report_menu(self)
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue
