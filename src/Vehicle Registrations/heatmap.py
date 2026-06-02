"""
Heatmap Visualization.

This script reads the Vehicle Registrations dataset and generates a heatmap
showing the relationship between the top 10 Primary Use Classes and the
top 10 Residential Counties.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def generate_heatmap():
    """Reads data, filters top categories, and displays a heatmap."""
    csv_path = BASE_DIR / "vehicle_registrations_in_state_of_washington.csv"

    try:
        vehicle = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: The dataset file was not found at {csv_path}")
        return

    top_classes = vehicle["Primary Use Class"].value_counts().nlargest(10).index
    top_counties = vehicle["Residential County"].value_counts().nlargest(10).index

    df_filtered = vehicle[
        vehicle["Primary Use Class"].isin(top_classes)
        & vehicle["Residential County"].isin(top_counties)
    ]

    pivot_df = df_filtered.pivot_table(
        index="Primary Use Class",
        columns="Residential County",
        aggfunc="size",
        fill_value=0,
    )

    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_df, cmap="viridis", annot=True, fmt="d")

    plt.title(
        "Heatmap of Vehicle Registrations by Class and Top 10 Counties", fontsize=14
    )
    plt.xlabel("County", fontsize=12)
    plt.ylabel("Primary Use Class", fontsize=12)
    plt.xticks(rotation=60, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    generate_heatmap()
