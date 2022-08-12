"""
Test of pandas accessor functions

@author: T. Guyet, Inria
@date: 08/2022
"""
import sys
sys.path.insert(0,".")

import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas.api.extensions import register_dataframe_accessor


from pychronicles.chronicle_python import Chronicle

@register_dataframe_accessor("pattern")
class TPatternAccessor:
    """Accessor for Pandas DataFrame
    """
    def __init__(self, df: DataFrame):
        self._validate(df)
        self._df = df

    @staticmethod
    def _validate(df):
        # verify there is a no MultiIndex, and that the Index is made of Integers or Timestamps
        if isinstance(df.index, pd.MultiIndex):
            raise AttributeError("Can not handle multi-indexed dataframes.")
        if df.index.dtype!=np.dtype('datetime64[ns]'):
            raise AttributeError("Dataframe index has to be timestamps.")

    def match(self, c : Chronicle):
        """Accessor to the Chronicle function"""
        return c.match(self._df)

if __name__ == "__main__":

    print(sys.argv)

    #create a dataframe from the sequence
    seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('a',15),('c',17),('b',20),('c',23),('c',25),('b',26),('c',28),('b',30)]
    df = pd.DataFrame(
        {
         "labels": [e[0] for e in seq],
         "other_column": [e[0]*2 for e in seq], #illustration of another columns than "label"
        },
        index = pd.to_datetime([e[1] for e in seq]) #use of a datetime format
    )

    c=Chronicle()
    c.add_event(0,'a')
    c.add_event(1,'b')
    c.add_event(2,'c')
    c.add_constraint(0,1, (pd.to_timedelta(4),pd.to_timedelta(10)))
    c.add_constraint(0,2, (pd.to_timedelta(2),pd.to_timedelta(8)))
    c.add_constraint(1,2, (pd.to_timedelta(3),pd.to_timedelta(13)))

    reco = df.pattern.match(c)
    print(f"Reconnaissance de la chronique: [{reco}]!")
