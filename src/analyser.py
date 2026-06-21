import pandas as pd

def load_budget(filepath):
    """
    Load budget data from a CSV file.

    Parameters:
    filepath (str): Path to the CSV file

    Returns:
    DataFrame: A pandas DataFrame containing the budget data
    """
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df

def calculate_summary(df):
    """
    Calculate total income, expenses and savings.

    Parameters:
    df (DataFrame): The budget DataFrame

    Returns:
    dict: A dictionary containing income, expenses and savings
    """
    total_income = df[df['type'] == 'income']['amount'].sum()
    total_expenses = df[df['type'] == 'expense']['amount'].sum()
    net_savings = total_income - total_expenses

    return {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_savings': net_savings
    }

def spending_by_category(df):
    """
    Calculate total spending per category.

    Parameters:
    df (DataFrame): The budget DataFrame

    Returns:
    DataFrame: Spending totals grouped by category
    """
    expenses = df[df['type'] == 'expense']
    category_spending = expenses.groupby('category')['amount'].sum()
    category_spending = category_spending.sort_values(ascending=False)
    return category_spending

def highest_spending_category(category_spending):
    """
    Find the category with the highest spending.

    Parameters: 
    category_spending (DataFrame): Spending totals by category

    Returns:
    tuple: (category_name, amount)
    """
    category = category_spending.idxmax()
    amount = category_spending.max()
    return category, amount