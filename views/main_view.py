# This is the file that is used for the main view
# Import what is needed
import time


class MView:
    """Class of the main view"""

    @staticmethod
    def title():
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n\n----------------------------------")
        print("        CHESS TOURNAMENTS")
        print("----------------------------------")

    @staticmethod
    def main_menu():
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Create new tournament")
        print("[2] Resume a tournament")
        print("[3] Create a new player")
        print("[4] Edit a player")
        print("[5] Reports menu")
        print("\n[exit] Exit the program")

    @staticmethod
    def create_tournament_head():
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n" * 3 + "--- NEW TOURNAMENT ---")

    @staticmethod
    def time_options():
        print("\nSelect the time control :")
        print("[1] Bullet")
        print("[2] Blitz")
        print("[3] Quick")
        print("\n[back] Back to  the main menu")

    @staticmethod
    def review_tournament(info, players):
        """Display all input info to review before saving to database"""
        print("\n\nNew tournament created :\n")
        print(f"{info[0].upper()}, {info[1].title()}", end=' | ')
        print(f"Description : {info[2]}", end=' | ')
        print("Rounds : 4", end=' | ')
        print(f"Time control : {info[3]}")
        print("\nPlayers (total = 8 players) :\n")

        for item in players:
            print(f"Player {players.index(item) + 1} : ", end='')
            print(f"{item['id']}", end=' | ')
            print(f"{item['last_name']}, {item['first_name']}", end=' | ')
            print(f"{item['date_of_birth']}", end=' | ')
            print(f"Rank : {item['rank']}")

        print("\nSave to database ? [y/n] ", end='')

    @staticmethod
    def tournament_saved():
        print("\nTournament successfully saved to database", end=' ')
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\nTournament successfully loaded")

    @staticmethod
    def select_players(players, player_number):
        """Display all players to select"""
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print(f"\nSelect the player {player_number} :\n")
        for i in range(len(players)):
            print(f"[{players[i]['id']}]", end=' ')
            print(f"{players[i]['last_name']}, {players[i]['first_name']}", end=" | ")
            print(f"{players[i]['gender']} | {players[i]['date_of_birth']}", end=" | ")
            print(f"Rank : {players[i]['rank']}")

        print("\n[back] Back to main menu")

    @staticmethod
    def select_tournaments(tournaments):
        """Display all tournaments to select"""
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n" * 3 + "--- SELECT A TOURNAMENT ---\n")

        for i in range(len(tournaments)):
            print(f"[{tournaments[i]['id']}]", end=' ')
            print(tournaments[i]['name'], end=' | ')
            print(tournaments[i]['location'], end=" | ")
            print(tournaments[i]['description'], end=' | ')
            print(f"Started on : {tournaments[i]['start_date']}", end=' | ')
            print(f"Ended on : {tournaments[i]['end_date']}", end=' | ')
            print(f"Round {tournaments[i]['current_round']-1}/{tournaments[i]['rounds_total']}")

        print("\n[back] Back to main menu")

    @staticmethod
    def create_new_player_head():
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n" * 3 + "- NEW PLAYER -\n")

    @staticmethod
    def review_players(info):
        """Display all input info to review before saving to database"""
        print("\n\nNew player created :\n")
        print(f"{info[0]}, {info[1]}", end=' | ')
        print(f"Date of birth : {info[2]}", end=' | ')
        print(f"Gender : {info[3]}", end=' | ')
        print(f"Rank : {info[4]}")
        print("\nSave to the database DB-data ? [y/n] ", end='')

    @staticmethod
    def update_players(p, options):
        """Player info editing prompts"""
        print("\n\n--- UPDATE PLAYER INFORMATION ---\n")
        print(f"Updating {p.last_name}, {p.first_name}\n")
        for i in range(len(options)):
            print(f"[{i+1}] Update {options[i]}")

        print("\n[back] Back to main menu")

    @staticmethod
    def players_saved():
        print("\nPlayer successfully saved")

    @staticmethod
    def reports_menu():
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n" * 3 + "--- REPORTS ---\n")
        print("[1] All players")
        print("[2] Players in one tournament")
        print("[3] All tournaments")
        print("[4] Rounds in one tournament")
        print("[5] Matches in one tournament")
        print("\n[back] Back to main menu")

    @staticmethod
    def reports_player_sort():
        print("\n[1] Sort players by name")
        print("[2] Sort players by rank")
        print("\n[back] Back to main menu")

    @staticmethod
    def prompt_text(option):
        print(f"\nEnter {option} (type [back] for main menu) : ", end='')

    @staticmethod
    def input_prompt():
        print("\nType [option] and press Enter : ", end='')

    @staticmethod
    def are_you_sure_to_exit():
        print("\nAre you sure you want to exit the program ? [y/n] ", end='')

    @staticmethod
    def input_errors():
        print("\nInput error, please enter a valid option.")

    @staticmethod
    def player_already_selected():
        print("\nPlayer already selected. Please select an other player.")

    @staticmethod
    def other_reports():
        print("\nWould you like to view another report ? [y/n] ", end='')

    @staticmethod
    def update_ranks():
        print("\nUpdate ranks of the players ? [y/n] ", end='')

    @staticmethod
    def rank_update_head(player):
        print(f"\nUpdating {player.last_name}, {player.first_name}")
