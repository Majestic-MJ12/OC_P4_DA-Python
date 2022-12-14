# This is the main menu controller
from views.main_view import MView
from controllers.tournament_controller import TController
from controllers.player_controller import PController
from controllers.report_controller import RController


class MMController(MView, TController, PController, RController):
    def __init__(self, main_view, tournament_controller, player_controller, report_controller):
        super().__init__()
        self.main_view = main_view
        self.tournament_controller = tournament_controller
        self.player_controller = player_controller
        self.report_controller = report_controller

    def select(self, selection):
        switcher = {
            1: self.tournament_controller.run,
            2: self.player_controller.run,
            3: self.report_controller.run,
            4: self.main_view.goodbye
        }
        func = switcher.get(selection, lambda: "Invalid input")
        func()

    def run(self):
        while True:
            self.display_choices()
            selection = input("Enter a number from 1 to 4: ")
            print(selection)
            self.select(selection)
            if selection == 4:
                break






