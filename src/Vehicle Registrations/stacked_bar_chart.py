"""
Stacked Bar Chart Visualization.

This script reads the Vehicle Registrations dataset and generates a stacked
bar chart showing the composition of the top 7 vehicle classes over
different fiscal years.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def generate_stacked_bar_chart():
    """Reads data, creates a crosstab, and displays a stacked bar chart."""
    csv_path = BASE_DIR / "vehicle_registrations_in_state_of_washington.csv"

    try:
        vehicle = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: The dataset file was not found at {csv_path}")
        return

    top_classes = vehicle["Primary Use Class"].value_counts().nlargest(7).index

    vehicle_filtered = vehicle[vehicle["Primary Use Class"].isin(top_classes)]
    crosstab_df = pd.crosstab(
        vehicle_filtered["Fiscal Year"], vehicle_filtered["Primary Use Class"]
    )

    crosstab_df.plot(
        kind="bar", stacked=True, figsize=(10, 6), fontsize=9, colormap="viridis"
    )

    sns.despine()
    plt.title("Composition of Top 7 Vehicle Classes Over Fiscal Years", fontsize=14)
    plt.xlabel("Fiscal Year", fontsize=12)
    plt.ylabel("Number of Registrations", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title="Vehicle Class", loc="upper left", fontsize=8)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    generate_stacked_bar_chart()
