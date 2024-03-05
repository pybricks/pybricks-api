import json

import pytest
from pybricks_jedi import CompletionItem, complete


def _create_snippet(class_name: str) -> str:
    """
    Creates a code snippet::

        from pybricks.parameters import {class_name}
        {class_name}.

    Args:
        line: The value substituted for ``{class_name}``
    """
    return "\n".join(
        (f"from pybricks.parameters import {class_name}", f"{class_name}.")
    )


ENUMS = [
    pytest.param(
        "Color",
        [
            "BLACK",
            "BLUE",
            "BROWN",
            "CYAN",
            "GRAY",
            "GREEN",
            "MAGENTA",
            "NONE",
            "ORANGE",
            "RED",
            "VIOLET",
            "WHITE",
            "YELLOW",
        ],
    ),
    pytest.param("Direction", ["CLOCKWISE", "COUNTERCLOCKWISE"]),
    pytest.param(
        "Icon",
        [
            "ARROW_DOWN",
            "ARROW_LEFT",
            "ARROW_LEFT_DOWN",
            "ARROW_LEFT_UP",
            "ARROW_RIGHT",
            "ARROW_RIGHT_DOWN",
            "ARROW_RIGHT_UP",
            "ARROW_UP",
            "CIRCLE",
            "CLOCKWISE",
            "COUNTERCLOCKWISE",
            "DOWN",
            "EMPTY",
            "EYE_LEFT",
            "EYE_LEFT_BLINK",
            "EYE_LEFT_BROW",
            "EYE_LEFT_BROW_UP",
            "EYE_RIGHT",
            "EYE_RIGHT_BLINK",
            "EYE_RIGHT_BROW",
            "EYE_RIGHT_BROW_UP",
            "FALSE",
            "FULL",
            "HAPPY",
            "HEART",
            "LEFT",
            "PAUSE",
            "RIGHT",
            "SAD",
            "SQUARE",
            "TRIANGLE_DOWN",
            "TRIANGLE_LEFT",
            "TRIANGLE_RIGHT",
            "TRIANGLE_UP",
            "TRUE",
            "UP",
        ],
    ),
    pytest.param("Port", ["A", "B", "C", "D", "E", "F", "S1", "S2", "S3", "S4"]),
    pytest.param("Side", ["BACK", "BOTTOM", "FRONT", "LEFT", "RIGHT", "TOP"]),
    pytest.param("Stop", ["BRAKE", "COAST", "COAST_SMART", "HOLD", "NONE"]),
]


@pytest.mark.parametrize("class_name,members", ENUMS)
def test_get_parameter_class_member_completion(class_name: str, members: list[str]):

    code = _create_snippet(class_name)
    completions: list[CompletionItem] = json.loads(
        complete(code, 2, len(class_name) + 2)
    )
    assert [c["insertText"] for c in completions] == members


def test_get_parameter_color_completion():
    code = "\n".join(["from pybricks.parameters import Color", "Color.RED."])
    completions: list[CompletionItem] = json.loads(complete(code, 2, 11))
    assert [c["insertText"] for c in completions] == [
        "BLACK",
        "BLUE",
        "BROWN",
        "CYAN",
        "GRAY",
        "GREEN",
        "h",
        "MAGENTA",
        "NONE",
        "ORANGE",
        "RED",
        "s",
        "v",
        "VIOLET",
        "WHITE",
        "YELLOW",
    ]
