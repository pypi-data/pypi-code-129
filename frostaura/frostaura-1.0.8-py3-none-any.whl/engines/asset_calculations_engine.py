'''This module defines calculations engine components.'''
from frostaura.models import ProfitCalculationResult

class IAssetCalculationsEngine:
    '''Component to perform functions related to asset calculations.'''

    def interpolate_holdings_profits(self, holdings: dict) -> dict:
        '''Determine individual asset profit ratio & profit USD and interpolate them into a copy of the given holdings.'''

        raise NotImplementedError()

    def calculate_holdings_profit(self, holdings: dict) -> ProfitCalculationResult:
        '''Determine the holdings profit percentage & profit USD, given the holdings.'''

        raise NotImplementedError()
