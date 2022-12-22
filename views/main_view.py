# this is the main view for the scripts
class MView:
    @staticmethod
    def display_main_menu():
        print('''
MAIN MENU
=================
Select an option:
1. Tournaments
2. Players
3. Reports
4. Quit''')

    @staticmethod
    def display_player_menu():
        print('''
PLAYER MENU
=================
Select an option:
1. Player creation
2. Player modification
3. Return''')

    @staticmethod
    def display_tournament_menu():
        print('''
TOURNAMENT MENU
=================
Select an option:
1. Tournament creation
2. Return''')

    @staticmethod
    def display_report_menu():
        print('''
REPORT MENU
=================
Select an option:
1. Actor list
2. Tournament list
3. Return''')

    @staticmethod
    def display_report2_menu():
        print('''
TOURNAMENT LIST
=================
Select an option:
1. Players from one tournament
2. All rounds from one tournament
3. All matches from one tournament
4. Return''')

    @staticmethod
    def display_report3_menu():
        print('''
PLAYERS LIST
=================
Select an option:
1. By alphabetic order
2. By rank
3. Return''')
