from abc import ABC, abstractmethod
from dataclasses import dataclass
from io import StringIO, TextIOBase
from sys import stdout
from typing import Any, List

from lazy_budget.budget import Budget, FinancialOperation
from lazy_budget.money_provider import format_money, get_zero
from lazy_budget.stats import BasicBudgetStats, get_categories_to_spendings


@dataclass
class BaseDisplay(ABC):
    locale: str

    @abstractmethod
    def get_display_data(self) -> dict:
        """
        Returns a dict with data to display.
        """
        raise NotImplementedError

    def __str__(self):
        result = StringIO()
        self.print(result)
        return result.getvalue()

    def print(self, file: TextIOBase = stdout):
        menu_data = self.get_display_data()
        padding = (
            max(len(x) for x in menu_data.keys())  # right-adjusted text
            + 1  # one more space before the ":"
        )
        for stat_name, stat_value in menu_data.items():
            self.print_stat(stat_name, stat_value, padding, file)

    @staticmethod
    def print_stat(stat_name: str, stat_value: Any, padding: int, file: TextIOBase):
        print((stat_name).rjust(padding), ":", stat_value, file=file)


@dataclass
class BaseBudgetStatsDisplay(BaseDisplay):
    budget_stats: BasicBudgetStats

    @property
    def zero(self):
        return get_zero(self.budget_stats.currency)


class BasicStatsDisplay(BaseBudgetStatsDisplay):
    def get_display_data(self):
        data = {
            "today": self.budget_stats.today,
            "total days": self.budget_stats.total_days,
            "days left": self.budget_stats.days_left,
        }
        if self.budget_stats.can_spend_today < get_zero(self.budget_stats.currency):
            data["days until can spend"] = self.budget_stats.days_until_can_spend

        data.update(
            {
                "available / day": format_money(
                    self.budget_stats.available_per_day, locale=self.locale
                ),
                (
                    "CAN spend today"
                    if self.budget_stats.can_spend_today > self.zero
                    else "CANNOT spend today"
                ): format_money(
                    abs(self.budget_stats.can_spend_today), locale=self.locale
                ),
                "spent today": format_money(
                    self.budget_stats.spent_today, locale=self.locale
                ),
                "avg spent / day": format_money(
                    self.budget_stats.avg_spent_per_day, locale=self.locale
                ),
                "kept": format_money(
                    self.budget_stats.currently_keeping, locale=self.locale
                ),
            }
        )
        return data


@dataclass
class SpentByCategoryDisplay(BaseDisplay):
    budget: Budget
    operations: List[FinancialOperation]

    def get_display_data(self) -> dict:
        return {
            ("<no category>" if not category else category): format_money(
                money_value, self.locale
            )
            for category, money_value in get_categories_to_spendings(
                self.budget, self.operations
            ).items()
        }
