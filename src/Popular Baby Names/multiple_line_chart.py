"""
Multiple Line Chart Visualization.

This script reads the Popular Baby Names dataset, processes the data
to find the top 5 most popular names of all time, and generates a
multiple line chart showing their popularity trends over the years.
"""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def generate_line_chart():
    """Reads data, processes it, and displays a multiple line chart."""
    csv_path = BASE_DIR / "Popular_Baby_Names.csv"

    try:
        babies = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: The dataset file was not found at {csv_path}")
        return

    babies.columns = ["Year", "Gender", "Ethnicity", "Name", "Count", "Rank"]

    top_5_names = babies.groupby("Name")["Count"].sum().nlargest(5).index
    top_names_df = babies[babies["Name"].isin(top_5_names)]

    pivot_df = top_names_df.pivot_table(
        index="Year", columns="Name", values="Count", fill_value=0
    )

    plt.style.use("seaborn-v0_8-darkgrid")
    pivot_df.plot(kind="line", figsize=(7, 5), marker=".")

    plt.title("Popularity of the Top 5 All-Time Names Over Time", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Number of Babies Named", fontsize=12)
    plt.legend(title="Name")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    generate_line_chart()
