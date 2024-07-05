import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def parse_row(row: pd.Series) -> pd.Series:
    """
    Parses a row of a DataFrame, converting string representations of numbers
    with suffixes 'K' (thousands) and 'M' (millions) to their respective
    numeric values.

    Parameters:
    row (pd.Series): A row of the DataFrame to be parsed.

    Returns:
    pd.Series: A new Series with parsed numeric values.
    """
    mult = {'K': 10e3, 'M': 10e6}
    parsed_values = []
    for n in row.values:
        if isinstance(n, str) and n[-1].upper() in mult:
            nb, exp = n[0:-1], n[-1].upper()
            n = float(nb) * mult[exp]
        parsed_values.append(n)
    return pd.Series(parsed_values, index=row.index)


def life_graph(data: pd.DataFrame) -> None:
    """
    Plots population projections for France and Belgium from a given DataFrame.
    The DataFrame must contain a 'country' column and years as other columns.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data to be plotted.

    Raises:
    ValueError: If the DataFrame does not contain a 'country' column.
    KeyError: If the data for 'France' or 'Belgium' is not found in the
    DataFrame.
    TypeError: If the data types are not suitable for plotting.
    """
    if 'country' not in data.columns:
        raise ValueError("DataFrame must have a 'country' column")
    data.set_index('country', inplace=True)
    try:
        france_data = data.loc['France']
        belgium_data = data.loc['Belgium']
    except KeyError as e:
        raise KeyError(f"Data for {e.args[0]} not found in the dataset")

    try:
        parsed_france = parse_row(france_data)
        parsed_belgium = parse_row(belgium_data)
        years_1 = parsed_france.index.astype(int)
        years_2 = parsed_belgium.index.astype(int)
        pop_france = parsed_france.values
        pop_belgium = parsed_belgium.values
        plt.plot(years_1, pop_france, label='France')
        plt.plot(years_2, pop_belgium, label='Belgium')
        plt.legend()
        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.show()
    except TypeError:
        raise TypeError("Data types are not suitable for plotting")


if __name__ == "__main__":
    try:
        data = load("population_total.csv")
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
