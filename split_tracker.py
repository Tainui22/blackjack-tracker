# Simple Blackjack Team Split Tracker

def calculate_split(total_profit, sb_team_pct=0.7):
    sb_team_share = total_profit * sb_team_pct
    casino_share = total_profit * (1 - sb_team_pct)
    return sb_team_share, casino_share

# Example usage:
if __name__ == "__main__":
    # Replace with actual session profit/loss
    total_profit = float(input("Enter session profit/loss: "))
    sb_team, casino = calculate_split(total_profit)
    print(f"SB-Team (70%): ${sb_team:.2f}")
    print(f"Casino Opponents (30%): ${casino:.2f}")