

from pathlib import Path
import pandas as pd

def read_data(data: Path):
    df = pd.read_csv(data)