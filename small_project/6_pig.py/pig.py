import random


def roll_die():
    """Roll a six-sided die and return the result."""
    return random.randint(1, 6)


def get_number_of_players():
    """Prompt for and return a valid number of players (2-4)."""
    while True:
        players = input("Enter the number of players (2 - 4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Must be between 2 - 4 players.")
        else:
            print("Invalid, try again.")


def get_winners(scores):
    """Return a list of indices for all players with the highest score."""
    max_score = max(scores)
    return [i for i, score in enumerate(scores) if score == max_score]


def main():
    players = get_number_of_players()
    target_score = 50
    player_scores = [0 for _ in range(players)]

    # Game loop: continue until someone reaches the target
    while max(player_scores) < target_score:
        for player_idx in range(players):
            print(f"\n--- Player {player_idx + 1}'s turn ---")
            print(f"Your total score is: {player_scores[player_idx]}\n")
            current_score = 0

            while True:
                should_roll = input("Would you like to roll (y/n)? ").lower().strip()
                if should_roll != "y":
                    break

                value = roll_die()
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a: {value}")

                print(f"Your score this turn is: {current_score}")
                if current_score > 50:
                    break

            player_scores[player_idx] += current_score
            print(f"Your total score is: {player_scores[player_idx]}")

            # Check if this player just won (optional early exit)
            if player_scores[player_idx] >= target_score:
                break

    # Determine winner(s) — handles ties properly
    winning_indices = get_winners(player_scores)
    winning_score = max(player_scores)

    print("\n" + "=" * 30)
    if len(winning_indices) == 1:
        winner = winning_indices[0] + 1
        print(f"Player {winner} is the winner with a score of: {winning_score}")
    else:
        winners = ", ".join(str(i + 1) for i in winning_indices)
        print(f"It's a tie! Players {winners} are the winners with a score of: {winning_score}")
    print("=" * 30)


if __name__ == "__main__":
    main()