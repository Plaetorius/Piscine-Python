import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
 

def projection_life(income_data: pd.DataFrame, expectancy_data: pd.DataFrame) -> None:
    selected_income = income_data['1900']
    selected_expectancy = expectancy_data['1900']
    plt.xcorr(selected_income, selected_expectancy, maxlags=10)
    plt.show()

if __name__ == "__main__":
    try:
        income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        expectancy_data = load("life_expectancy_years.csv")
        projection_life(income_data, expectancy_data)
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
