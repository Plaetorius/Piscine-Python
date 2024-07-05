import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import sys


#TODO parse CSV

def life_graph(data: pd.DataFrame) -> None:


    if 'country' not in data.columns:
        raise ValueError("DataFrame must have a 'country' column")
    data.set_index('country', inplace=True)
    try:
        france_data = data.loc['France']
        belgium_data = data.loc['Zambia']
    except KeyError as e:
        raise KeyError(f"Data for {e.args[0]} not found in the dataset")

    try:
        print(data)
        years_1 = france_data.index.astype(int)
        years_2 = belgium_data.index.astype(int)
        pop_france = france_data.values
        pop_belgium = belgium_data.values
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
        if len(sys.argv) == 2:
            data = load(sys.argv[1])
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
