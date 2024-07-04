import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import sys


def life_graph(data: pd.DataFrame) -> None:
    data = data.iloc[60]
    print(data)
    # data.plot(kind='line', x='year', color='blue')
    # plt.title('France Life Expectancy Projections')
    # plt.xlabel('Year')
    # plt.ylabel('Life Expectancy')

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            file = life_graph(load(sys.argv[1]))
            # print(f"Loading dataset of dimensions {file.shape}")
            # print(file)
    except Exception as e:
        print(f"Error: {e}")