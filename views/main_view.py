# this is the main view for the scripts
import time


class MView:
    @staticmethod
    def display_main_menu():
        print("\nMAIN MENU", end="")
        for i in range(5):
            time.sleep(0.1)
            print(".", end="")
        print("\n" + "=" * 20)
        print("Select an option:")
        print("1. Tournaments")
        print("2. Players")
        print("3. Reports")
        print("4. Quit")

    @staticmethod
    def display_player_menu():
        print("\nPLAYER MENU", end="")
        for i in range(5):
            time.sleep(0.1)
            print(".", end="")
        print("\n" + "=" * 20)
        print("Select an option:")
        print("1. Player creation")
        print("2. Player modification")
        print("3. Return")

    @staticmethod
    def display_tournament_menu():
        print("\nTOURNAMENT MENU", end="")
        for i in range(5):
            time.sleep(0.1)
            print(".", end="")
        print("\n" + "=" * 20)
        print("Select an option:")
        print("1. Tournament creation")
        print("2. Launch the tournament")
        print("3. Return")

    @staticmethod
    def display_report_menu():
        print("\nREPORT MENU", end="")
        for i in range(5):
            time.sleep(0.1)
            print(".", end="")
        print("\n" + "=" * 20)
        print("Select an option:")
        print("1. Actor list")
        print("2. Tournament list")
        print("3. Return")

    @staticmethod
    def display_report2_menu():
        print("\nTOURNAMENT LIST CHOICES", end="")
        for i in range(5):
            time.sleep(0.1)
            print(".", end="")
        print("\n" + "=" * 20)
        print("Select an option:")
        print("1. Players from one tournament")
        print("2. All rounds from one tournament")
        print("3. All matches from one tournament")
        print("4. Return")

    @staticmethod
    def display_report3_menu():
        print("\nACTORS SORT CHOICES", end="")
        for i in range(5):
            time.sleep(0.1)
            print(".", end="")
        print("\n" + "=" * 20)
        print("Select an option:")
        print("1. By alphabetic order")
        print("2. By rank")
        print("3. Return")
