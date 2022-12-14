from controllers.tournament_controller import TController
from controllers.tournament_controller import t_controller


class TView(TController):

    # Print the values of the attributes on the instance
    print("\n")
    print("All the information's about the Tournament you created: ")
    print("Name:", t_controller.name)
    print("Localisation:", t_controller.localisation)
    print("Date:", t_controller.date)
    print("Number of rounds:", t_controller.number_round)
    print("Description:", t_controller.description)

