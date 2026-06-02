"""
Line Chart Visualization.

This script reads the Vehicle Registrations dataset and generates a
line chart showing the trend of vehicle registrations over fiscal years.
"""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def generate_line_chart():
    """Reads data, calculates registrations by fiscal year, and displays a line chart."""
    csv_path = BASE_DIR / "vehicle_registrations_in_state_of_washington.csv"

    try:
        vehicle = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: The dataset file was not found at {csv_path}")
        return

    vehicle_count = vehicle["Fiscal Year"].value_counts()

    plt.style.use("ggplot")
    vehicle_count.sort_index().plot(
        kind="line", figsize=(7, 5), marker=".", fontsize=10
    )

    plt.title("Vehicle Registrations by Fiscal Year and Transactions", fontsize=14)
    plt.xlabel("Fiscal Year", fontsize=12)
    plt.ylabel("Transactions", fontsize=12)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    generate_line_chart()
