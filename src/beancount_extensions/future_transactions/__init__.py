"""A plugin that suppresses future transactions when enabled.
"""

__author__ = 'Manuel Amador (Rudd-O)'
__plugins__ = ('future_transactions_plugin',)
__version__ = "0.0.3"

import datetime
from beancount.core import data

# The name of the metadata field that indicates this is a future transaction
# that should be filtered out if it is past today's date.
META = 'future'


def future_transactions_plugin(entries, unused_options_map):
    errors = []
    new_entries = []
    today = datetime.date.today()

    def skip(entry):
        return isinstance(entry, data.Transaction) and entry.date > today and META in entry.tags

    for eindex, entry in enumerate(entries):
        if not skip(entry):
            new_entries.append(entry)

    return new_entries, errors


if __name__ == '__main__':
    main()
