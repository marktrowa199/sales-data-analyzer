def analyze_data(df):
    print("\n" + "=" * 50)
    print("BUSINESS INSIGHTS")
    print("=" * 50)

    print(f"\nTotal Sales: ${df['Sales'].sum():,.2f}")
    print(f"Total Profit: ${df['Profit'].sum():,.2f}")

    print("\nTop 10 Products by Sales")
    print(
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\nSales by Category")
    print(
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nSales by Region")
    print(
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop 10 States by Profit")
    print(
        df.groupby("State")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )