'''This module defines projection engine components.'''
from logging import debug
import pandas as pd
from frostaura.engines.asset_projection_engine import IAssetProjectionEngine

class SimpleAssetProjectionEngine(IAssetProjectionEngine):
    '''Calculations-related functionality using some maths under-the-hood.'''

    def project_daily_asset_growth(self, n_days: int, annual_growth_rate: float, current_value: float) -> pd.DataFrame:
        '''Determine an asset's growth at a given annual rate over a specified number of days.'''

        raise NotImplementedError()
