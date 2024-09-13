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
        if (len(path.strip()) == 0):
            raise FileNotFoundError("Empty path!")
        return pd.read_csv(path)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return pd.DataFrame([])
    except Exception:
        print(f"Error: Unsupported file format!", file=sys.stderr)
        return pd.DataFrame([])


def main():
    try:
        if len(sys.argv) == 2:
            file = load(sys.argv[1])
            print(f"Loading dataset of dimensions {file.shape}")
            print(file)
        else:
            print(f"Usage: python3 {sys.argv[0]} path_to_csv")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
