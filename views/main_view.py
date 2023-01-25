# This is the file that is used for the main view
# Import what is needed
import time


class MView:
    """Class of the main view"""

    @staticmethod
    def mv_title():
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n\n----------------------------------")
        print("        CHESS TOURNAMENTS")
        print("----------------------------------")

    @staticmethod
    def mv_main_menu():
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Create new tournament")
        print("[2] Resume a tournament")
        print("[3] Create a new player")
        print("[4] Edit a player")
        print("[5] Reports menu")
        print("\n[exit] Exit the program")

    @staticmethod
    def mv_create_tournament_head():
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n" * 3 + "--- NEW TOURNAMENT ---")

    @staticmethod
    def mv_time_options():
        print("\nSelect the time control :")
        print("[1] Bullet")
        print("[2] Blitz")
        print("[3] Quick")
        print("\n[back] Back to  the main menu")

    @staticmethod
    def mv_review_tournament(mv_info, mv_players):
        """Display all input info to review before saving to database"""
        print("\n\nNew tournament created :\n")
        print(f"{mv_info[0].upper()}, {mv_info[1].title()}", end=' | ')
        print(f"Description : {mv_info[2]}", end=' | ')
        print("Rounds : 4", end=' | ')
        print(f"Time control : {mv_info[3]}")
        print("\nPlayers (total = 8 players) :\n")

        for item in mv_players:
            print(f"Player {mv_players.index(item) + 1} : ", end='')
            print(f"{item['id']}", end=' | ')
            print(f"{item['last_name']}, {item['first_name']}", end=' | ')
            print(f"{item['date_of_birth']}", end=' | ')
            print(f"Rank : {item['rank']}")

        print("\nSave to database ? [y/n] ", end='')

    @staticmethod
    def mv_tournament_saved():
        print("\nTournament successfully saved to database", end=' ')
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\nTournament successfully loaded")

    @staticmethod
    def mv_select_players(mv_players, mv_player_number):
        """Display all players to select"""
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print(f"\nSelect the player {mv_player_number} :\n")
        for i in range(len(mv_players)):
            print(f"[{mv_players[i]['p_id']}]", end=' ')
            print(f"{mv_players[i]['p_lastname']}, {mv_players[i]['p_firstname']}", end=" | ")
            print(f"{mv_players[i]['p_gender']} | {mv_players[i]['p_date_of_birth']}", end=" | ")
            print(f"p_Rank : {mv_players[i]['p_rank']}")

        print("\n[back] Back to main menu")

    @staticmethod
    def mv_select_tournaments(mv_tournaments):
        """Display all tournaments to select"""
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n" * 3 + "--- SELECT A TOURNAMENT ---\n")

        for i in range(len(mv_tournaments)):
            print(f"[{mv_tournaments[i]['id']}]", end=' ')
            print(mv_tournaments[i]['name'], end=' | ')
            print(mv_tournaments[i]['location'], end=" | ")
            print(mv_tournaments[i]['description'], end=' | ')
            print(f"Started on : {mv_tournaments[i]['start_date']}", end=' | ')
            print(f"Ended on : {mv_tournaments[i]['end_date']}", end=' | ')
            print(f"Round {mv_tournaments[i]['current_round']-1}/{mv_tournaments[i]['rounds_total']}")

        print("\n[back] Back to main menu")

    @staticmethod
    def mv_create_new_player_head():
        print("Loading.", end=' ')
        time.sleep(0.5)
        print(".", end=' ')
        time.sleep(0.5)
        print(".")
        print("\n" * 3 + "- NEW PLAYER -\n")

    @staticmethod
    def mv_review_players(mv_info):
        """Display all input info to review before saving to database"""
        print("\n\nNew player created :\n")
        print(f"{mv_info[0]}, {mv_info[1]}", end=' | ')
        print(f"p_Date of birth : {mv_info[2]}", end=' | ')
        print(f"p_Gender : {mv_info[3]}", end=' | ')
        print(f"p_Rank : {mv_info[4]}")
        print("\nSave to the database DB-data ? [y/n] ", end='')

    @staticmethod
    def mv_update_players(mv_p, mv_options):
        """Player info editing prompts"""
        print("\n\n--- UPDATE PLAYER INFORMATION ---\n")
        print(f"Updating {mv_p.p_lastname}, {mv_p.p_firstname}\n")
        for i in range(len(mv_options)):
            print(f"[{i+1}] Update {mv_options[i]}")

        print("\n[back] Back to main menu")

    @staticmethod
    def mv_players_saved():
        print("\nPlayer successfully saved")

    @staticmethod
    def mv_reports_menu():
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
    def mv_reports_player_sort():
        print("\n[1] Sort players by their names")
        print("[2] Sort players by their ranks")
        print("\n[back] Back to main menu")

    @staticmethod
    def mv_prompt_text(mv_option):
        print(f"\nEnter {mv_option} (type [back] for main menu) : ", end='')

    @staticmethod
    def mv_input_prompt():
        print("\nType [option] and press Enter : ", end='')

    @staticmethod
    def mv_are_you_sure_to_exit():
        print("\nAre you sure you want to exit the program ? [y/n] ", end='')

    @staticmethod
    def mv_input_errors():
        print("\nInput error, please enter a valid option.")

    @staticmethod
    def mv_player_already_selected():
        print("\nPlayer already selected. Please select an other player.")

    @staticmethod
    def mv_other_reports():
        print("\nWould you like to view another report ? [y/n] ", end='')

    @staticmethod
    def mv_update_ranks():
        print("\nUpdate the ranks of the players ? [y/n] ", end='')

    @staticmethod
    def mv_rank_update_head(mv_player):
        print(f"\nUpdating {mv_player.p_lastname}, {mv_player.p_firstname}")
