# This is the main menu controller
# importing what is needed
from views.main_view import MView
from controllers.player_controller import PController
from controllers.tournament_controller import TController
from controllers.round_controller import RController
from controllers.match_controller import MController
from models.player_model import PModel
from views.report_view import RView


# the controller for the main menu
class MMController:

    @staticmethod
    def main_menu():
        """function to choose the first choices of the menu"""
        while True:
            MView.display_main_menu()
            try:
                selection = int(input("Enter a number from 1 to 4: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    MMController.tournament_menu()
                elif selection == 3:
                    MMController.report_menu()
                elif selection == 2:
                    MMController.player_menu()
                elif selection == 4:
                    print("\nGoodbye !")
                    exit()
                else:
                    print("\nSorry, that is not a valid selection. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue
            except IOError:
                print("\nAn input/output error occurred. Please try again.")
                continue

    @staticmethod
    def player_menu():
        """function for the player selection"""
        while True:
            MView.display_player_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    try:
                        PController.creation_player(PController.players_list)
                        p = PModel(PController.creation_player(PController.players_list), PController.)


                    except ValueError as e:
                        print(e)
                elif selection == 2:
                    try:
                        if not PController.players_list:
                            raise ValueError("No players in the list.")
                    except (ValueError, IOError):
                        print("\nNo players in the list.")
                        continue
                    PController.player_id_sort(PController.players_list)
                    RView.actors_view()
                    PController.modification_player(PController.players_list)
                elif selection == 3:
                    MMController.main_menu()
                else:
                    print("\nSorry, that is not a valid selection. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue
            except IOError:
                print("\nAn input/output error occurred. Please try again.")
                continue

    @staticmethod
    def tournament_menu():
        """function for the tournament selection"""
        while True:
            MView.display_tournament_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    TController.creation_tournament(TController.tournament_list, TController.permanent_selected_player)
                elif selection == 2:
                    for r in range(4):
                        RController.round_start(RController.rounds_list)
                        MController.pair_generation(MController.match_list)
                        MController.match_result(MController.match_list)
                        RController.round_creation(RController.rounds_list)
                        RController.round_end(RController.rounds_list)
                    for p in str(int(len(TController.permanent_selected_player))):
                        PController.modification_player(p)
                elif selection == 3:
                    MMController.main_menu()
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue

    @staticmethod
    def report_menu():
        """function for the first report menu"""
        while True:
            MView.display_report_menu()
            try:
                selection = int(input("Enter a number from 1 to 3: "))
                print("\nYou chose: ", selection)
                if selection == 1:
                    PController.player_id_sort(PController.players_list)
                    RView.actors_view()
                    MMController.report3_menu()
                elif selection == 2:
                    MMController.report2_menu()
                elif selection == 3:
                    MMController.main_menu()
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue

    @staticmethod
    def report2_menu():
        """function for the second report menu"""
        if len(TController.tournament_list) <= 0:
            print("No tournament found")
            MMController.report_menu()
        else:
            while True:
                try:
                    RView.all_tournaments_view()
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
                        PController.player_id_sort(PController.players_list)
                        RView.tournaments_players_view(id_tournament)
                    elif selection == 2:
                        PController.player_alpha_sort(PController.players_list)
                        RView.tournaments_players_view(id_tournament)
                    elif selection == 3:
                        PController.player_rank_sort(PController.players_list)
                        RView.tournaments_players_view(id_tournament)
                    elif selection == 4:
                        RView.tournaments_round_view(id_tournament)
                    elif selection == 5:
                        RView.tournaments_matches_view(id_tournament)
                    elif selection == 6:
                        MMController.report_menu()
                    else:
                        print("\nSorry, that is not a valid selection. Please try again.")
                except ValueError:
                    print("\nSorry, that is not a valid number. Please try again.")
                    continue

    @staticmethod
    def report3_menu():
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
                    MMController.report_menu()
                else:
                    print("\nSorry, that is not a valid number. Please try again.")
            except ValueError:
                print("\nSorry, that is not a valid number. Please try again.")
                continue

    @staticmethod
    def save_player_db():
        PController.save_players(PController.players_list)

    @staticmethod
    def load_player_db():
        PController.load_players()

