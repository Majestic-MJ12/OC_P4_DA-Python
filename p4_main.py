# This is the file that is used for controlling the full program
# Import what is needed
from controllers.main_menu_controller import MMController
from views.main_view import MView
"""import sys"""


def main():
    """Load methods from the other files"""
    """try:"""
    MView.mv_title()
    MMController().mmc_menu_start()
    """except Exception:
        print("An error has occurred. Exiting program.")
        sys.exit(1)"""


if __name__ == "__main__":
    main()
    """Name of the environment where top-level code is run"""


"""INFO : wanted to add something to handle the crash of the
program, but it makes it crash more often.
Would be a good idea to investigate in the future.
Also would be a good idea to add "try - except" blocks more often on the whole
code to catch things that make the program exiting due to inputs errors"""
