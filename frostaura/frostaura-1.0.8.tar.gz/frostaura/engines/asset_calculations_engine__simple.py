'''This module defines calculations engine components.'''
from datetime import datetime
import pandas as pd
from frostaura.data_access.public_asset_data_access import IPublicAssetDataAccess
from frostaura.engines.asset_calculations_engine import IAssetCalculationsEngine
from frostaura.models import ProfitCalculationResult

class SimpleAssetCalculationsEngine(IAssetCalculationsEngine):
    '''Calculations-related functionality using some maths under-the-hood.'''

    def __init__(self, public_asset_data_access: IPublicAssetDataAccess):
        self.public_asset_data_access = public_asset_data_access

    def interpolate_holdings_profits(self, holdings: dict) -> dict:
        '''Determine individual asset profit ratio & profit USD and interpolate them into a copy of the given holdings.'''

        __holdings__: dict = holdings.copy()

        for holding_symbol in __holdings__:
            context: dict = __holdings__[holding_symbol]
            history: pd.DataFrame = self.public_asset_data_access.get_symbol_history(symbol=context['symbol'])
            transactions_by_date_asc: list = sorted(context['transactions'], key=lambda i: i['date'])
            total_purchased_usd: float = 0
            total_purchased_shares: float = 0

            for transaction in transactions_by_date_asc:
                transaction_date: datetime = transaction['date']
                transaction_value: float = transaction['value']
                transaction_close: float = history.loc[transaction_date].Close

                transaction['usd'] = transaction_close * transaction_value
                total_purchased_usd += transaction_close * transaction_value
                total_purchased_shares += transaction_value

            total_current_usd: float = history.iloc[-1].Close * total_purchased_shares
            context['total_purchased_usd'] = total_purchased_usd
            context['total_purchased_shares'] = total_purchased_shares
            context['total_current_usd'] = total_current_usd
            context['total_profit_ratio'] = (1 - min(total_purchased_usd, total_current_usd) / max(total_purchased_usd, total_current_usd)) * 100
            context['total_profit_usd'] = total_current_usd - total_purchased_usd

        return __holdings__

    def calculate_holdings_profit(self, holdings: dict) -> ProfitCalculationResult:
        '''Determine the holdings profit percentage & profit USD, given the holdings.'''

        holdings: dict = self.interpolate_holdings_profits(holdings=holdings)
        total_purchased_usd: float = sum([holdings[k]['total_purchased_usd'] for k in holdings])
        total_current_usd: float = sum([holdings[k]['total_current_usd'] for k in holdings])
        total_profit_ratio: float = (1 - min(total_purchased_usd, total_current_usd) / max(total_purchased_usd, total_current_usd)) * 100
        total_profit_usd: float = total_current_usd - total_purchased_usd

        return ProfitCalculationResult(percentage=total_profit_ratio, value=total_profit_usd)
