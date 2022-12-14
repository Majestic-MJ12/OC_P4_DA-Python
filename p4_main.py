from controllers.main_controller import MController
from controllers.player_controller import PController
from controllers.report_controller import RController
from controllers.tournament_controller import TController
from views.main_view import MView
from views.player_view import PView
from views.report_view import RView
from views.tournament_view import TView
from models.player_model import PModel


def main():
    main_controller = MController

    main_controller.run()
