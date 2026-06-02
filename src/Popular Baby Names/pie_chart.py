"""
Pie Chart Visualization.

This script reads the Popular Baby Names dataset and generates a pie chart
showing the overall distribution of babies by gender.
"""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def generate_pie_chart():
    """Reads data, calculates gender distribution, and displays a pie chart."""
    csv_path = BASE_DIR / "Popular_Baby_Names.csv"

    try:
        baby_name = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: The dataset file was not found at {csv_path}")
        return

    baby_name_count = baby_name["Gender"].value_counts()

    plt.figure(figsize=(6, 5))
    baby_name_count.plot(
        kind="pie", autopct="%1.1f%%", startangle=140, cmap="tab10", fontsize=10
    )

    plt.title("Distribution of Babies by Gender", fontsize=14)
    plt.xlabel("")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    generate_pie_chart()
