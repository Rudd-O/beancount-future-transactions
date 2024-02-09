"""A plugin that suppresses future transactions when enabled.
"""

__author__ = "Manuel Amador (Rudd-O)"
__plugins__ = ("future_transactions_plugin",)
__version__ = "0.0.5"

import datetime
from beancount.core import data

# The name of the metadata field that indicates this is a future transaction
# that should be filtered out if it is past today's date.
META = "future"


# If "suppress_all_future_entries" in options_map, skips all future-dated entries
# else only transactions tagged #future
def future_transactions_plugin(entries, options_map):
    errors = []
    new_entries = []
    today = datetime.date.today()

    def skip(entry):
        if entry.date <= today:
            return False
        return ("suppress_all_future_entries" in options_map) or (
            isinstance(entry, data.Transaction) and META in entry.tags
        )

    for eindex, entry in enumerate(entries):
        if not skip(entry):
            new_entries.append(entry)

    return new_entries, errors
