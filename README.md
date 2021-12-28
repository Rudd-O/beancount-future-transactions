# Beancount future transactions

This is a very simple plugin for Beancount that filters out transactions with a future date, provided they are tagged with the `#future` tag.

To use:

* Install using your favorite Python method — probably `pip` or `python setup.py install`, although you may want to install to your user directory (`pip --user`).
* Include the stanza `plugin "beancount_extensions.future_transactions"` in your Beancount file.

That's it.

From this point on, any transaction with a future tagged `#future` will not appear in your reports and queries.
