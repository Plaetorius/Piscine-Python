import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import sys


def life_graph(data: pd.DataFrame) -> None:
    """
    Plots the life expectancy projections for France from a given dataset.

    Parameters:
    data (pd.DataFrame): DataFrame containing life expectancy data with
    countries as rows and years as columns.

    Raises:
    ValueError: If the 'country' column is not present in the DataFrame.
    KeyError: If 'France' is not present in the DataFrame's index.
    TypeError: If the data types are not suitable for plotting.
    """

    if 'country' not in data.columns:
        raise ValueError("DataFrame must have a 'country' column")
    data.set_index('country', inplace=True)
    try:
        france_data = data.loc['France']
    except KeyError:
        raise KeyError("Data for 'France' not found in the dataset")

    try:
        years = france_data.index.astype(int)
        life_expectancy = france_data.values
        plt.plot(years, life_expectancy)
        plt.title('France Life Expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.show()
    except TypeError:
        raise TypeError("Data types are not suitable for plotting")


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            data = load(sys.argv[1])
        else:
            data = load("life_expectancy_years.csv")
        life_graph(data)
    except FileNotFoundError:
        print("File not found! Please check the file path.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
