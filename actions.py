# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions




from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class CalculateColumnStatsAction(Action):
    def name(self) -> Text:
        return "action_calculate_column_stats"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the column name and stat type from the user
        requested_column = tracker.get_slot("column_name")
        requested_stat = tracker.get_slot("stat_type")

        # Load your DataFrame
        try:
            df = pd.read_csv(r"C:\Users\ntalashilkar\Downloads\data.csv")
        except FileNotFoundError:
            dispatcher.utter_message("File not found.")
            return []

        if requested_column in df.columns and pd.api.types.is_numeric_dtype(df[requested_column]):
            if requested_stat == 'sum':
                response = df[requested_column].sum()
                dispatcher.utter_message(text=f"The sum of {requested_column} column is {response}")
            elif requested_stat == 'count':
                response = df[requested_column].count()
                dispatcher.utter_message(text=f"The count of {requested_column} column is {response}")
            elif requested_stat == 'mean':
                response = df[requested_column].mean()
                dispatcher.utter_message(text=f"The mean of {requested_column} column is {response}")
            elif requested_stat == 'std':
                response = df[requested_column].std()
                dispatcher.utter_message(text=f"The standard deviation of {requested_column} column is {response}")
            elif requested_stat == 'min':
                response = df[requested_column].min()
                dispatcher.utter_message(text=f"The minimum of {requested_column} column is {response}")
            elif requested_stat == 'max':
                response = df[requested_column].max()
                dispatcher.utter_message(text=f"The maximum of {requested_column} column is {response}")
            else:
                response = "Invalid stat type. Supported types: sum, count, mean, std, min, max"
                dispatcher.utter_message(text=response)
        else:
            response = f"Column '{requested_column}' is either not present or not numeric."
            dispatcher.utter_message(text=response)

        return []

class CalculateColumnInsightsAction(Action):
    def name(self) -> Text:
        return "action_calculate_column_insights"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the column name and stat type from the user
        requested_column = tracker.get_slot("column_name")
        requested_type = tracker.get_slot("h_l_type")
        requested_n = tracker.get_slot("n_type")

        # Load your DataFrame
        try:
            df = pd.read_csv(r"C:\Users\ntalashilkar\Downloads\data.csv")
        except FileNotFoundError:
            dispatcher.utter_message("File not found.")
            return []

        if requested_column in df.columns and pd.api.types.is_numeric_dtype(df[requested_column]):
            if requested_type == 'highest':
                requested_n = int(requested_n)
                response = df[requested_column].nlargest(requested_n).to_list()
                dispatcher.utter_message(text=f"The top {requested_n} values in {requested_column} column are: {response}")
            elif requested_type == 'lowest':
                requested_n = int(requested_n)
                response = df[requested_column].nsmallest(requested_n).to_list()
                dispatcher.utter_message(text=f"The bottom {requested_n} values in {requested_column} column are: {response}")
            else:
                response = "Invalid type. Supported types: highest, lowest"
                dispatcher.utter_message(text=response)
        else:
            response = f"Column '{requested_column}' is either not present or not numeric."
            dispatcher.utter_message(text=response)

        return []




  
