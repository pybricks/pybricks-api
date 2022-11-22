# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors

"""
Tests for correct code completion of the InventorHub class.
"""


import json
from pybricks_jedi import complete, CompletionItem

IMPORT = "from pybricks.hubs import InventorHub"
CREATE_INSTANCE = "hub = InventorHub()"


def _create_snippet(line: str) -> str:
    """
    Creates a code snippet::

        from pybricks.hubs import InventorHub
        hub = InventorHub()
        {line}

    Args:
        line: The value substituted for ``{line}``
    """
    return "\n".join((IMPORT, CREATE_INSTANCE, line))


# Everything else is the same as the Prime Hub.

from test_complete_prime_hub import (  # noqa F401
    test_hub_dot,
    test_hub_dot_battery_dot,
    test_hub_dot_buttons_dot,
    test_hub_dot_charger_dot,
    test_hub_dot_display_dot,
    test_hub_dot_imu_dot,
    test_hub_dot_light_dot,
    test_hub_dot_speaker_dot,
    test_hub_dot_system_dot,
)
