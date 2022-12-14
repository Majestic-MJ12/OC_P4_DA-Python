from controllers.player_controller import PController
from controllers.player_controller import player_controller


class PView(PController):

    # Player data display
    print("\n")
    print("All the information's about the Players you created: ")
    print("Last name :", player_controller.lastname)
    print("First name :", player_controller.firstname)
    print("Birth :", player_controller.birth)
    print("Gender :", player_controller.gender)
    print("Ranking :", player_controller.score)
