import random
import json

# players tier dictionary (hold them)
tiers = {
    "tier1": [],
    "tier2": [],
    "tier3": [],
    "tier4": []
}

special_cases = {
    "hp": "lmd",
    "ht": "htfriend",
    "lmd": "lmdfriend"
}

# function to add players to a tier
def add_player_to_tier(tier):
    player_name = input(f"Enter player name for {tier}: ")
    tiers[tier].append(player_name)
    print(f"Added {player_name} to {tier}.")

# function to remove players from a tier
def remove_player_from_tier(tier):
    if tiers[tier]:
        player_name = input(f"Enter the player name you want to remove from {tier}: ")
        if player_name in tiers[tier]:
            tiers[tier].remove(player_name)
            print(f"Removed {player_name} from {tier}.")
        else:
            print(f"{player_name} is not in {tier}.")
    else:
        print(f"No players in {tier} to remove.")

# function to view players in a specific tier
def view_tier_data():
    for tier, players in tiers.items():
        if players:
            print(f"\n{tier.capitalize()} Players: {', '.join(players)}")
        else:
            print(f"\n{tier.capitalize()} Players: No players in this tier yet.")

# function to save the tier data to a file (tier_data.json)
def save_tier_data(filename="tier_data.json"):
    with open(filename, "w") as file:
        json.dump(tiers, file, indent=4)
    print("Player information saved successfully.")

# function to load tier data from a file
def load_tier_data(filename="tier_data.json"):
    global tiers
    try:
        with open(filename, "r") as file:
            tiers = json.load(file)
        print("Player information loaded successfully.")
    except FileNotFoundError:
        print("No saved data found. Please add players and save the data.")

# function to ensure that special cases are respected
def handle_special_cases(team1, team2):
    # dan xep lmd hp
    if "hp" in team1 and "lmd" in team1:
        team1.remove("lmd")
        team2.append("lmd")
    elif "hp" in team2 and "lmd" in team2:
        team2.remove("lmd")
        team1.append("lmd")

    # ht va ban ht cung team
    if "ht" in team1 and "htfriend" not in team1:
        team1.append("htfriend")
        team2.remove("htfriend")
    elif "ht" in team2 and "htfriend" not in team2:
        team2.append("htfriend")
        team1.remove("htfriend")
    
    # lmd va ban lmd cung team
    if "lmd" in team1 and "lmdfriend" not in team1:
        team1.append("lmdfriend")
        team2.remove("lmdfriend")
    elif "lmd" in team2 and "lmdfriend" not in team2:
        team2.append("lmdfriend")
        team1.remove("lmdfriend")

    # cap ban than ko cung team ( tranh crash )
    if ("ht" in team1 or "htfriend" in team1) and ("lmd" in team1 or "lmdfriend" in team1):
        team1.remove("ht")
        team1.remove("htfriend")
        team2.append("ht")
        team2.append("htfriend")
    elif ("ht" in team2 or "htfriend" in team2) and ("lmd" in team2 or "lmdfriend" in team2):
        team2.remove("ht")
        team2.remove("htfriend")
        team1.append("ht")
        team1.append("htfriend")

# function to create teams from tiers
def create_teams():
    total_players_needed = int(input("Enter total number of players required in each team: "))
    total_players = sum(len(players) for players in tiers.values())

    if total_players < total_players_needed * 2:
        print(f"Not enough players to create teams. Need at least {total_players_needed * 2} players in total.")
        return

    team1 = []
    team2 = []

    # distribute players based on how many players are needed per team
    for tier, players in tiers.items():
        num_players_in_tier = len(players)
        if num_players_in_tier == 0:
            continue  # skip this tier if no players are present

        # to calculate how many players can be taken from this tier
        max_players_to_take = min(total_players_needed, num_players_in_tier // 2)

        if max_players_to_take == 0:
            continue  # skip if no players are left to take

        # select players for both teams
        selected_players = random.sample(players, max_players_to_take * 2)
        team1 += selected_players[:max_players_to_take]
        team2 += selected_players[max_players_to_take:]

    # handle special cases
    handle_special_cases(team1, team2)

    print("\nTeam 1: ", team1)
    print("Team 2: ", team2)

# Main menu
def main_menu():
    while True:
        print("\n--- Football Team Maker ---")
        print("1. Add player to tier")
        print("2. Remove player from tier")
        print("3. View tier data")
        print("4. Save tier data")
        print("5. Load tier data")
        print("6. Create teams")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tier_choice = input("Enter the tier (tier1, tier2, tier3, tier4): ").lower()
            if tier_choice in tiers:
                add_player_to_tier(tier_choice)
            else:
                print("Invalid tier. Please enter tier1, tier2, tier3, or tier4.")
        elif choice == "2":
            tier_choice = input("Enter the tier (tier1, tier2, tier3, tier4): ").lower()
            if tier_choice in tiers:
                remove_player_from_tier(tier_choice)
            else:
                print("Invalid tier. Please enter tier1, tier2, tier3, or tier4.")
        elif choice == "3":
            view_tier_data()
        elif choice == "4":
            save_tier_data()
        elif choice == "5":
            load_tier_data()
        elif choice == "6":
            create_teams()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

#By dh
