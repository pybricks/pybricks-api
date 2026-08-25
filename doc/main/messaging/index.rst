:mod:`messaging <pybricks.messaging>` -- Send and receive messages
==================================================================

.. automodule:: pybricks.messaging
    :no-members:

.. pybricks-requirements:: ble

.. blockimg:: pybricks_variables_set_ble_radio

.. autoclass:: pybricks.messaging.BLERadio
    :no-members:

    .. blockimg:: pybricks_blockBleBroadcast2

    .. automethod:: pybricks.messaging.BLERadio.broadcast

    .. blockimg:: pybricks_blockBleObserve2

    .. automethod:: pybricks.messaging.BLERadio.observe

    .. automethod:: pybricks.messaging.BLERadio.signal_strength

    .. automethod:: pybricks.messaging.BLERadio.version

    .. blockimg:: pybricks_variables_set_app_data_app_data_color_tracker

    .. blockimg:: pybricks_variables_set_app_data_app_data_teachable_machine

    .. blockimg:: pybricks_variables_set_app_data_app_data_object_detection

    .. blockimg:: pybricks_variables_set_app_data_app_data_line_follower

    .. blockimg:: pybricks_variables_set_app_data_app_data_custom

.. autoclass:: pybricks.messaging.AppData
    :no-members:

    .. automethod:: pybricks.messaging.AppData.get_bytes

    .. blockimg:: pybricks_blockAppDataGetValues

    .. automethod:: pybricks.messaging.AppData.write_bytes

    .. automethod:: pybricks.messaging.AppData.configure

    .. automethod:: pybricks.messaging.AppData.close

BLERadio examples
------------------

Broadcasting data to other hubs
*******************************

.. literalinclude::
    ../../../examples/pup/ble_radio/ble_broadcast.py

Observing data from other hubs
******************************

.. literalinclude::
    ../../../examples/pup/ble_radio/ble_observe.py
