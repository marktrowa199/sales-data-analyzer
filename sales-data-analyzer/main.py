
from eda import run_eda
from visualization import create_charts
from analysis import analyze_data

def main():
    df = run_eda()
    analyze_data(df)
    create_charts(df)

if __name__ == "__main__":
    main()