import pandas as pd
import numpy as np

def exchange_seats(s: pd.DataFrame) -> pd.DataFrame:
    return s.assign(student = np.where(s.id%2 & (s.id==len(s)), s.student, np.where(s.id%2, s.student.shift(-1), s.student.shift(1))))
    