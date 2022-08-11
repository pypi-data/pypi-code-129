'''This module defines projection engine components.'''
import pandas as pd

class IAssetProjectionEngine:
    '''Component to perform functions related to asset projections.'''

    def project_daily_asset_growth(self, n_days: int, annual_growth_rate: float, current_value: float) -> pd.DataFrame:
        '''Determine an asset's growth at a given annual rate over a specified number of days.'''

        raise NotImplementedError()
