# Game-Theoretic Analysis of Online Advertising Competition

A Python-based simulation and visualization tool modeling strategic decision-making, dominant strategies, and Nash equilibria in digital advertising competition using game theory (Prisoner's Dilemma framework).

---

## 📌 Project Overview
In digital marketing, competing firms must decide how much to invest in advertising to capture user attention. Because one company's payoff depends directly on its competitors' choices, real-time market dynamics can be analyzed effectively using **Game Theory**. 

This project implements a $2 \times 2$ strategic game model simulating two competing online advertisers. It evaluates individual incentives versus collective profitability, illustrating the classic **Prisoner's Dilemma** where rational individual choices lead to a suboptimal market outcome.

---

## 🎯 Objectives
* Model two competing advertisers as strategic players.
* Construct and evaluate a 2X2 payoff matrix for different advertising investment decisions.
* Identify dominant strategies and compute pure-strategy Nash equilibria.
* Compare individual rational choices with combined market profitability.
* Implement the model using Python and generate automated visualizations (`matplotlib`).

---

## 📊 Theoretical Background & Payoff Matrix

The model considers two players—**Advertiser A** and **Advertiser B**—each choosing between two strategies: **Low Investment** ($L$) or **High Investment** ($H$)[cite: 1].

| Advertiser A / B | B: Low Investment | B: High Investment |
| :--- | :--- | :--- |
| **A: Low Investment** | (5, 5) *[Cooperative Optimum]* | (2, 8) *[B Exploits A]* |
| **A: High Investment** | (8, 2) *[A Exploits B]* | (4, 4) *[Nash Equilibrium]* |

* **Dominant Strategy:** High investment is the dominant strategy for both players[cite: 1].
* **Nash Equilibrium:** (High, High) yielding individual payoffs of $(4, 4)$ and a combined market profit of **8 units**[cite: 1].
* **The Dilemma:** If both cooperated at (Low, Low), each would receive $(5, 5)$ for a combined total of **10 units**, demonstrating that individual rationality can lead to lower collective profits[cite: 1].

## 🛠️ Prerequisites & Installation

Make sure you have Python 3.x installed along with the required numerical and plotting libraries:

```bash
pip install matplotlib numpy
