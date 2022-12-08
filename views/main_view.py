class MView:
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


MView.display_choices()
MView.goodbye()

