# this is the script to launch the program
# importing what is needed
import sys
from controllers.main_menu_controller import MMController
from controllers.player_controller import PController
from controllers.tournament_controller import TController
from controllers.round_controller import RController
from controllers.match_controller import MController


def main():
    """function to execute other functions"""
    player_controller = PController()
    round_controller = RController()
    tournament_controller = TController()
    match_controller = MController()

    player_controller.load_players()
    tournament_controller.load_tournaments()
    round_controller.load_rounds()
    match_controller.load_matches()
    main_menu_controller = MMController()
    try:
        main_menu_controller.main_menu()
    except Exception:
        print("An error has occurred. Exiting program.")
        tournament_controller.save_tournaments()
        player_controller.save_players()
        match_controller.save_matches()
        round_controller.save_rounds()
        sys.exit(1)


if __name__ == "__main__":
    main()
