from flask import Flask, render_template
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

app = Flask(__name__)

# Folder to save generated charts
STATIC_FOLDER = "static"
os.makedirs(STATIC_FOLDER, exist_ok=True)


def run_customer_segmentation():
    """
    Replace this function with the code from your project.

    It should:
    1. Generate/load the customer data
    2. Perform KMeans clustering
    3. Save the visualization
    4. Return the dashboard data
    """

    # -----------------------------
    # Dummy data (replace with your project code)
    # -----------------------------
    df = pd.DataFrame({
        "Customer_ID": ["CUST001", "CUST002", "CUST003"],
        "Age": [24, 35, 41],
        "Annual_Income": [40000, 70000, 90000],
        "Total_Spent": [2500, 9200, 12500],
        "Segment_Name": [
            "Growing Segment",
            "Frequent Buyers",
            "High Value Customers"
        ]
    })

    total_customers = len(df)
    total_revenue = int(df["Total_Spent"].sum())
    avg_ltv = round(df["Total_Spent"].mean(), 2)
    total_segments = df["Segment_Name"].nunique()

    segment_summary = (
        df.groupby("Segment_Name")
        .agg(
            size=("Customer_ID", "count"),
            revenue=("Total_Spent", "sum")
        )
        .reset_index()
    )

    summary = []

    for _, row in segment_summary.iterrows():
        summary.append({
            "name": row["Segment_Name"],
            "size": int(row["size"]),
            "revenue": int(row["revenue"])
        })

    # Example chart
    plt.figure(figsize=(8, 5))
    plt.bar(df["Customer_ID"], df["Total_Spent"])
    plt.title("Customer Spending")
    plt.tight_layout()
    plt.savefig("static/customer_segmentation_analysis.png")
    plt.close()

    return (
        total_customers,
        total_revenue,
        avg_ltv,
        total_segments,
        summary,
        df.to_dict("records")
    )


@app.route("/")
def home():

    (
        total_customers,
        total_revenue,
        avg_ltv,
        total_segments,
        segment_summary,
        customers
    ) = run_customer_segmentation()

    return render_template(
        "index.html",
        total_customers=total_customers,
        total_revenue=total_revenue,
        avg_ltv=avg_ltv,
        total_segments=total_segments,
        segment_summary=segment_summary,
        customers=customers
    )


if __name__ == "__main__":
    app.run(debug=True)