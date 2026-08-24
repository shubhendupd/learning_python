
Write a program for a turn-based dice game where **2 to 4 players** compete to reach a target score of **50 points**.

#### Game Rules:

1. **Setup**: Ask the user for the number of players (must be 2–4). Initialize each player's score to 0.
    
2. **Turn Structure**: Players take turns in order. On a player's turn:
    
    - Display the player's total score.
        
    - The player may choose to roll the die by entering **"y"**.
        
    - Each roll generates a random number between **1 and 6**.
        
3. **Scoring per Turn**:
    
    - If the player rolls a **1**, they lose all points accumulated during that turn, their turn ends immediately, and they score **0** for the round.
        
    - If the player rolls **2–6**, that value is added to their current turn score. They may then choose to roll again or stop.
        
    - If the player chooses **not** to roll (enters anything other than "y"), they "bank" their current turn score, adding it to their total score.
        
4. **Winning Condition**: The game continues in rounds until at least one player's total score reaches or exceeds **50**. Once the current round completes (so all players get an equal number of turns), the player with the highest score is declared the winner.