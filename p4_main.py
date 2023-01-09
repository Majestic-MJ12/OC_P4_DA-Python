# this is the script to launch the program
# importing what is needed
import sys
from controllers.main_menu_controller import MMController


def main():
    """function to execute other functions"""
    main_menu_controller = MMController()
    """try:"""
    main_menu_controller.main_menu()
    """except Exception:
        print("An error has occurred. Exiting program.")
        sys.exit(1)"""


if __name__ == "__main__":
    main()
