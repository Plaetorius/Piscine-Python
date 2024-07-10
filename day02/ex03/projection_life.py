import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def projection_life(income_data: pd.DataFrame, expectancy_data: pd.DataFrame):
    """
    Plots a scatter plot of Gross Domestic Product (GDP) per capita versus Life
    Expectancy for the year 1900.

    Args:
        income_data (pd.DataFrame): DataFrame containing GDP per capita data.
        expectancy_data (pd.DataFrame): DataFrame containing life expectancy
        data.

    Raises:
        KeyError: If the column '1900' is not found in the DataFrames.
        ValueError: If the DataFrames contain invalid data types.
        TypeError: If the input arguments are not DataFrames.
    """
    try:
        selected_income = income_data['1900']
        selected_expectancy = expectancy_data['1900']
        plt.scatter(selected_income, selected_expectancy)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.show()
    except KeyError as ke:
        raise KeyError(f"KeyError: One of the DataFrames does not contain the \
            column '1900'. Detailed error: {ke}")
    except ValueError as ve:
        raise ValueError(f"ValueError: Invalid data in the DataFrames. \
            Detailed error: {ve}")
    except TypeError as te:
        raise TypeError(f"TypeError: The input arguments must be pandas \
            DataFrames. Detailed error: {te}")


def main():
    try:
        income_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        expectancy_data = load("life_expectancy_years.csv")

        projection_life(income_data, expectancy_data)
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}. Please check the file path.")
    except ValueError as ve:
        print(f"ValueError: {ve}. Please ensure the data is in the correct \
            format.")
    except KeyError as ke:
        print(f"KeyError: {ke}. Please ensure the columns '1900' exist in the \
            data.")
    except TypeError as te:
        print(f"TypeError: {te}. Please ensure the input data is of type \
            pandas DataFrame.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
