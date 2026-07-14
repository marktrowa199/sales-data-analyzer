import matplotlib.pyplot as plt
import seaborn as sns

# Set chart style
sns.set_theme(style="whitegrid")


def create_charts(df):

    # ==========================
    # 1. Sales by Category
    # ==========================
    plt.figure(figsize=(8, 5))

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    sns.barplot(
        x=category_sales.index,
        y=category_sales.values
    )

    plt.title("Total Sales by Category", fontsize=14, fontweight="bold")
    plt.xlabel("Category")
    plt.ylabel("Sales ($)")
    plt.tight_layout()
    plt.show()

    # ==========================
    # 2. Sales by Region
    # ==========================
    plt.figure(figsize=(8, 5))

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    sns.barplot(
        x=region_sales.index,
        y=region_sales.values
    )

    plt.title("Total Sales by Region", fontsize=14, fontweight="bold")
    plt.xlabel("Region")
    plt.ylabel("Sales ($)")
    plt.tight_layout()
    plt.show()

    # ==========================
    # 3. Profit by Category
    # ==========================
    plt.figure(figsize=(8, 5))

    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    sns.barplot(
        x=category_profit.index,
        y=category_profit.values
    )

    plt.title("Profit by Category", fontsize=14, fontweight="bold")
    plt.xlabel("Category")
    plt.ylabel("Profit ($)")
    plt.tight_layout()
    plt.show()

    # ==========================
    # 4. Monthly Sales Trend
    # ==========================
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

    monthly_sales = (
        df.groupby("Month")["Sales"]
        .sum()
    )

    plt.figure(figsize=(12, 5))

    plt.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o"
    )

    plt.title("Monthly Sales Trend", fontsize=14, fontweight="bold")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # ==========================
    # 5. Correlation Heatmap
    # ==========================
    plt.figure(figsize=(7, 5))

    numeric_columns = df[["Sales", "Profit", "Quantity", "Discount"]]

    sns.heatmap(
        numeric_columns.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()