import pandas as pd
import sys


def load(path: str) -> pd.DataFrame:
    """
    Load an CSV file in to a pandas' DataFrame

    Parameters:
    path (str): the path to the image.

    Returns:
    pd.DataFrame with the dimensions of the CSV file and its content

    Raises:
    FileNotFoundError: If the path doesn't lead to any image
    Exception: other errors (corrupted / wrong file...)
    """
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print("File not found!")
        return pd.DataFrame([])
    except Exception:
        print("Unsupported file!")
        return pd.DataFrame([])


def main():
    try:
        if len(sys.argv) == 2:
            file = load(sys.argv[1])
            print(f"Loading dataset of dimensions {file.shape}")
            print(file)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
