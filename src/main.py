import os
from analyser import load_budget, calculate_summary, spending_by_category, highest_spending_category

def display_summary(summary):
    """Display the budget summary."""

    print("\n" + "=" * 50)
    print("         BUDGET SUMMARY - January 2024")
    print("=" * 50)
    print(f"Total Income:       R{summary['total_income']:,.2f}")
    print(f"Total Expenses:     R{summary['total_expenses']:,.2f}")
    print(f"Net Savings:        R{summary['net_savings']:,.2f}")
    
def display_category_spending(category_spending):
    """Display spending broken down by category."""

    print("\n" + "=" * 50)
    print("         SPENDING BY CATEGORY")
    print("=" * 50)
    for category, amount in category_spending.items():
        print(f"{category:<20} R{amount:,.2f}")

def display_highest_spending(category, amount):
    """Display the highest spending category."""

    print("\n" + "=" * 50)
    print(f"Your highest spending category is {category} at R{amount:,.2f}")
    print("=" * 50)

def main():
    """Main function that runs the budget analyser."""

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, 'data', 'budget.csv')

    df = load_budget(filepath)
    summary = calculate_summary(df)
    category_spending = spending_by_category(df)
    category, amount = highest_spending_category(category_spending)

    display_summary(summary)
    display_category_spending(category_spending)
    display_highest_spending(category, amount)

main()