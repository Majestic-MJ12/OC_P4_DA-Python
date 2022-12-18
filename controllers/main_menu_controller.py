# This is the main menu controller
from views.main_view import MView
from controllers.player_controller import PController
from controllers.report_controller import RController

"""A garder"""

cpt_match = 1

players_list = []


class MMController:

    def main_menu(self):
        while True:
            MView.display_main_menu()
            selection = int(input("Enter a number from 1 to 4: "))
            print(selection)
            if selection == 4:
                print("Goodbye !")
                break
            elif selection == 2:
                MMController.player_menu(self)
            else:
                print("Invalid input")

    def player_menu(self):
        MView.display_player_menu()
        selection = int(input("Enter a number from 1 to 3: "))
        print(selection)
        if selection == 1:
            PController.creation_player(players_list)
        elif selection == 2:
            PController.modification_player(players_list)
        elif selection == 3:
            MMController.main_menu(self)
        else:
            print("Invalid input")
