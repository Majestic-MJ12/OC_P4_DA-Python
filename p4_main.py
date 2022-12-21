# this is the script to launch the program
# importing what is needed
from controllers.main_menu_controller import MMController


def main():
    """function to execute other function"""
    main_menu_controller = MMController()

    main_menu_controller.main_menu()


if __name__ == "__main__":
    main()
