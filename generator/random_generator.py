import random
import pandas as pd
import time
import os

class RandomGenerator:
    """
    Generates a synthetic numeric dataset based on column specifications 
    and exports generated datasets to CSV files with optional rate limiting.

    Parameters
    ----------
    n_rows : int
        Number of rows to generate.

    columns : list of dict
        List of column definitions. Each dict must contain:
        - 'name': str
        - 'min': int
        - 'max': int

    max_columns : int, optional
        Maximum number of allowed columns (default is 100).

    Class Attributes
    ----------------
    _save_counter : int
        Tracks how many times CSV files have been saved in the current session.

    _save_limit : int
        Maximum number of allowed saves per session (default is 10).
    """
    _save_counter = 0
    _save_limit = 10  # Max files that can be saved per session to prevent abuse.

    def __init__(self, n_rows, columns=None, max_columns=100):
        """
        Initialize the RandomGenerator with row and column specifications.

        Parameters
        ----------
        n_rows : int
            Number of rows to generate.

        columns : list of dict, optional
            List of column definitions. Each dict must contain:
            - 'name': str
            - 'min': int
            - 'max': int
            If not provided, defaults to a research-dataset-like structure with 5 fields and 1 bonus field.

        max_columns : int, optional
            Maximum number of allowed columns. Defaults to 100. 
            Raises a ValueError if exceeded.
        """
        
        self.n_rows = n_rows
        self.max_columns = max_columns

        if columns is None:
            # Default to the structure of this research dataset-like setup
            self.columns = [{"name": f"N{i+1}", "min": 1, "max": 69} for i in range(5)] + [{"name": "B", "min": 1, "max": 26}]
        else:
            if len(columns) > max_columns:
                raise ValueError(f"Too many columns: {len(columns)} exceeds max_columns={max_columns}.")
            self.columns = columns

    def generate(self):
        """
        Generate the dataset in memory as a pandas DataFrame.

        Returns
        -------
        pd.DataFrame
            A DataFrame with randomly generated numeric values per column spec.
        """        
        data = []
        for _ in range(self.n_rows):
            row = [random.randint(col["min"], col["max"]) for col in self.columns]
            data.append(row)
        return pd.DataFrame(data, columns=[col["name"] for col in self.columns])

    def to_csv(self, path=None, auto_folder="output"):
        """
        Export the generated dataset to a CSV file. 

        If no path is specified, automatically saves to a timestamped file 
        in the specified folder. Enforces a per-session save limit.

        Parameters
        ----------
        path : str, optional
            File path where the CSV will be saved. If not specified, 
            a timestamped file is saved to the 'auto_folder'.

        auto_folder : str, optional
            Directory to store auto-generated files (default is 'notebooks/output/').

        Raises
        ------
        RuntimeError
            If the per-session file save limit is exceeded.
        """
        if RandomGenerator._save_counter >= RandomGenerator._save_limit:
            print(f"[SECURITY] Save limit of {self._save_limit} reached. File not saved.")
            # return None               # Skip both saving and generation
            return                      # Graceful exit without raising an error
        
        if path is None:
            os.makedirs(auto_folder, exist_ok=True)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            path = os.path.join(auto_folder, f"random_generated_{timestamp}.csv")

        df = self.generate()
        df.to_csv(path, index=False)
        RandomGenerator._save_counter += 1
        print(f"[INFO] CSV saved to: {path} ({RandomGenerator._save_counter}/{RandomGenerator._save_limit})")
        

    @classmethod
    def reset_save_counter(cls):
        """
        Reset the save counter back to zero. 
        Useful for long-running sessions or testing.
        
        Can be called from outside the class using:
            RandomGenerator.reset_save_counter()
        """
        cls._save_counter = 0
        print("[INFO] Save counter reset.")