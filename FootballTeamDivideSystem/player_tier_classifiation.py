import random
import json
tiers = {
    "tier1": [],
    "tier2": [],
    "tier3": [],
    "tier4": []
}

def add_player_to_tier(tier):
    player_name = input(f"Enter player name for {tier}: ")
    tiers[tier].append(player_name)
    print(f"Added {player_name} to {tier}.")

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

def view_tier_data():
    for tier, players in tiers.items():
        if players:
            print(f"\n{tier.capitalize()} Players: {', '.join(players)}")
        else:
            print(f"\n{tier.capitalize()} Players: No players in this tier yet.")

def save_tier_data(filename="tier_data.json"):
    with open(filename, "w") as file:
        json.dump(tiers, file, indent=4)
    print("Player information saved successfully.")

def load_tier_data(filename="tier_data.json"):
    global tiers
    try:
        with open(filename, "r") as file:
            tiers = json.load(file)
        print("Player information loaded successfully.")
    except FileNotFoundError:
        print("No saved data found. Please add players and save the data.")

def calculate_players_per_tier(total_players_needed):
    total_players = sum(len(players) for players in tiers.values())
    
    if total_players < total_players_needed * 2:
        print(f"Not enough players to create teams. Need at least {total_players_needed * 2} players in total.")
        return None
    
    players_per_tier = {}
    remaining_players_needed = total_players_needed
    for tier, players in tiers.items():
        if len(players) > 0:
            tier_share = min(len(players), remaining_players_needed)
            players_per_tier[tier] = tier_share
            remaining_players_needed -= tier_share
            if remaining_players_needed == 0:
                break
    
    return players_per_tier

def create_teams():
    total_players_needed = int(input("Enter total number of players required in each team: "))
    total_players = sum(len(players) for players in tiers.values())
    
    if total_players < total_players_needed * 2:
        print(f"Not enough players to create teams. Need at least {total_players_needed * 2} players in total.")
        return

    team1 = []
    team2 = []

    for tier, players in tiers.items():
        num_players_in_tier = len(players)
        if num_players_in_tier == 0:
            continue 

        max_players_to_take = min(total_players_needed, num_players_in_tier // 2)

        if max_players_to_take == 0:
            continue 

        selected_players = random.sample(players, max_players_to_take * 2)
        team1 += selected_players[:max_players_to_take]
        team2 += selected_players[max_players_to_take:]

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
