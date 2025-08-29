import pandas as pd

def analyze_sessions(log_file='session_data.csv'):
    df = pd.read_csv(log_file)
    # Calculate team/casino split
    df['SB_Team'] = df['Total_Profit'] * 0.7
    df['Casino'] = df['Total_Profit'] * 0.3
    # Find best strategy by average profit
    best_strategy = df.groupby('Strategy_Used')['Total_Profit'].mean().idxmax()
    print(f"Best strategy so far: {best_strategy}")
    # Print cumulative stats
    print(f"Total SB-Team profit: ${df['SB_Team'].sum():.2f}")
    print(f"Total Casino profit: ${df['Casino'].sum():.2f}")
    return df

if __name__ == "__main__":
    df = analyze_sessions()
    print(df[['Session_Date', 'Total_Profit', 'SB_Team', 'Casino', 'Strategy_Used']])