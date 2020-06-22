
Church of Jesus Christ API
==========================

This Python package implements an unofficial API for accessing data from churchofjesuschrist.org.
The endpoints are the same ones used by the Church's website and mobile app, and are therefore
subject to change in the future.

By default, most methods can be called with default parameters and will return information for the
user's unit. In the case where a method is to request information for a member, the default
is to return information about the current user.

In order to get unit numbers for other units that the user has access to, use user_details to find
different unit numbers available to the user.

.. Link to full documentation

Full documentation with examples can be found on `read the docs <https://church-of-jesus-christ-api.readthedocs.io/en/latest/index.html>`_