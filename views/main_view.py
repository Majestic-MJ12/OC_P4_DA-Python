class MainView:
    @staticmethod
    def display_choices():
        print('''
MAIN MENU
=================
Select an option:
1. Tournaments
2. Players
3. Reports
4. Quit''')

    @staticmethod
    def goodbye():
        print("Goodbye !")


MainView.display_choices()
MainView.goodbye()

