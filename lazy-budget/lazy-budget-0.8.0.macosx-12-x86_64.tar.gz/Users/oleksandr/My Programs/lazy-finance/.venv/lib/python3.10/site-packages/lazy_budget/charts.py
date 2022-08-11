from abc import abstractmethod
from dataclasses import dataclass
from itertools import takewhile
from typing import Iterable

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame

from lazy_budget.budget import Budget, FinancialOperation
from lazy_budget.stats import get_categories_to_spendings


@dataclass
class BaseChart:
    budget: Budget
    operations: Iterable[FinancialOperation]

    def plot(self):
        df = self.get_dataframe()
        self.display_dataframe(df)
        plt.show()

    @abstractmethod
    def get_dataframe(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def display_dataframe(self, dataframe: pd.DataFrame):
        pass


@dataclass
class BurnDownChart(BaseChart):
    show_zero: bool = False

    def get_dataframe(self):
        max_date = self.budget.today
        operations = self.budget.filter(self.operations)
        spent_per_day = self.budget.get_spent_by_day(operations)
        for_df = []
        total_spent = self.budget.total.amount
        for day in takewhile(lambda x: x <= max_date, iter(self.budget)):
            self.budget.today = day
            ops = self.budget.filter(operations)
            total_spent += spent_per_day[day].amount
            should_be_available = (
                self.budget.days_left * self.budget.available_per_day.amount
                + self.budget.keep.amount
            )
            for_df.append(
                (
                    day.strftime("%d"),
                    total_spent,
                    should_be_available,
                    0,
                    self.budget.available_per_day.amount,
                    self.budget.get_currently_keeping(ops).amount,
                    self.budget.keep.amount,
                )
            )
        return pd.DataFrame(
            for_df,
            columns=[
                "day",
                "money",
                "should_be_available",
                "zero",
                "available_per_day",
                "currently_keeping",
                "keep",
            ],
        )

    def display_dataframe(self, dataframe: DataFrame):
        sns.set_theme()
        sns.set_style("darkgrid")

        plt.plot("day", "money", data=dataframe, color="red", label="real burndown")
        plt.plot(
            "day",
            "should_be_available",
            data=dataframe,
            linestyle="dashed",
            color="red",
            label="planned burndown",
        )
        if self.show_zero:
            plt.plot("day", "zero", data=dataframe, linestyle="dashed")

        plt.plot(
            "day",
            "currently_keeping",
            data=dataframe,
            color="green",
            label="real savings",
        )
        plt.plot(
            "day",
            "keep",
            data=dataframe,
            color="green",
            linestyle=":",
            label="planned savings",
        )
        plt.legend()


class CategoryBarPlot(BaseChart):
    def get_dataframe(self) -> pd.DataFrame:
        operations = self.budget.filter(self.operations)
        sps = get_categories_to_spendings(self.budget, operations)
        return pd.DataFrame(
            map(lambda x: (x[0], x[1].amount), sps.items()),
            columns=["category", "money_spent"],
        )

    def display_dataframe(self, dataframe: pd.DataFrame):
        sns.set(style="darkgrid")

        # Set the figure size
        # plt.figure(figsize=(10, 7))

        # plot a bar chart
        ax = sns.barplot(
            x="category",
            y="money_spent",
            data=dataframe,
            estimator=sum,
            ci=None,
            color="#69b3a2",
        )
        ax.set(xlabel="category", ylabel=f"money spent, {self.budget.currency.name}")
        plt.gca().invert_yaxis()
