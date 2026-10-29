# ==============================================================================
# Project: Game-Theoretic Analysis of Online Advertising Competition
# Description: Displays the Payoff Matrix, evaluates dominant strategies, 
#              calculates Nash equilibria, and plots the profit comparison graph.
# ==============================================================================

import matplotlib.pyplot as plt
import numpy as np

def run_advertising_game_analysis():
    # Define strategies and payoffs: (Payoff_A, Payoff_B)
    payoff_matrix = {
        ('Low', 'Low'): (5, 5),
        ('Low', 'High'): (2, 8),
        ('High', 'Low'): (8, 2),
        ('High', 'High'): (4, 4)
    }
    
    print("==========================================================")
    print("      GAME-THEORETIC ANALYSIS OF ONLINE ADVERTISING       ")
    print("==========================================================")
    
    # --- 1. PRINT TEXT-BASED PAYOFF MATRIX ---
    print("\n[1] PAYOFF MATRIX (Advertiser A, Advertiser B):")
    print("-" * 58)
    print(f"{'':<18} | {'B: Low (Investment)':<20} | {'B: High (Investment)':<20}")
    print("-" * 58)
    print(f"{'A: Low':<18} | {str(payoff_matrix[('Low', 'Low')]):<20} | {str(payoff_matrix[('Low', 'High')]):<20}")
    print(f"{'A: High':<18} | {str(payoff_matrix[('High', 'Low')]):<20} | {str(payoff_matrix[('High', 'High')]):<20}")
    print("-" * 58)
    
    print("\n[2] STRATEGIC INSIGHTS:")
    print("  - Dominant Strategy for Both: High Advertising Investment[cite: 1]")
    print("  - Pure-Strategy Nash Equilibrium: (High, High)[cite: 1]")
    print("  - Equilibrium Payoffs: A = 4, B = 4 (Combined = 8 units)[cite: 1]")
    print("  - Cooperative Optimum: (Low, Low) (Combined = 10 units)[cite: 1]")
    print("  - Conclusion: Demonstrates the classic Prisoner's Dilemma[cite: 1].\n")
    
    # --- 2. GENERATE VISUALIZATION GRAPH ---
    scenarios = [
        'Both Low\n(Cooperative)', 
        'A: Low, B: High', 
        'A: High, B: Low', 
        'Both High\n(Nash Equilibrium)'
    ]
    
    payoffs_a = [5, 2, 8, 4]
    payoffs_b = [5, 8, 2, 4]
    combined_profits = [a + b for a, b in zip(payoffs_a, payoffs_b)]
    
    x = np.arange(len(scenarios))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.bar(x - width, payoffs_a, width, label='Advertiser A Profit', color='#2b5c8f')
    ax.bar(x, payoffs_b, width, label='Advertiser B Profit', color='#d95f02')
    ax.bar(x + width, combined_profits, width, label='Combined Market Profit', color='#7570b3')
    
    ax.set_ylabel('Profit / Payoff Units', fontsize=12, fontweight='bold')
    ax.set_title('Payoff Comparison: Online Advertising Competition (Prisoner\'s Dilemma)', fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, fontsize=10)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Annotations
    ax.annotate('Nash Equilibrium\n(Total = 8)', 
                xy=(3, 4), xytext=(2.1, 7.5),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                fontsize=10, fontweight='bold', color='darkred')
    
    ax.annotate('Cooperative Optimum\n(Total = 10)', 
                xy=(0, 5), xytext=(-0.3, 8.5),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                fontsize=10, fontweight='bold', color='darkgreen')
    
    ax.set_ylim(0, 11)
    plt.tight_layout()
    
    print("Launching graph window...")
    plt.show()

if __name__ == "__main__":
    run_advertising_game_analysis()