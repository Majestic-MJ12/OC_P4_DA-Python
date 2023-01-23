# This is the file that is used for controlling the full program
# Import what is needed
from controllers.main_menu_controller import MMController
from views.main_view import MView


def main():
    """Load methods"""
    MView.title()
    MMController().menu_start()


if __name__ == "__main__":
    main()
    """Name of the environment where top-level code is run"""
