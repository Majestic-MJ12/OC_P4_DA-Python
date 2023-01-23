from controllers.main_menu_controller import MenuController
from views.main_view import MainViews


def main():
    MainViews.title()
    MenuController().main_menu_start()


if __name__ == "__main__":
    main()
