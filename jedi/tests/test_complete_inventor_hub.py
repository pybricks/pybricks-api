# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors

"""
Tests for correct code completion of the InventorHub class.
"""


import json
from pybricks_jedi import SignatureHelp, complete, get_signatures, CompletionItem

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


def test_hub_dot():
    line = "hub."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "battery",
        "buttons",
        "charger",
        "display",
        "imu",
        "light",
        "speaker",
        "system",
    ]


def test_hub_dot_battery_dot():
    line = "hub.battery."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "current",
        "voltage",
    ]


def test_hub_dot_battery_dot_current():
    line = "hub.battery.current("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == ["current() -> int"]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None]


def test_hub_dot_battery_dot_voltage():
    line = "hub.battery.voltage("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == ["voltage() -> int"]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None]


def test_hub_dot_buttons_dot():
    line = "hub.buttons."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "pressed",
    ]


def test_hub_dot_battery_dot_pressed():
    line = "hub.buttons.pressed("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "pressed() -> Tuple[Button]"
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None]


def test_hub_dot_charger_dot():
    line = "hub.charger."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "connected",
        "current",
        "status",
    ]


def test_hub_dot_charger_dot_connected():
    line = "hub.charger.connected("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == ["connected() -> bool"]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None]


def test_hub_dot_charger_dot_current():
    line = "hub.charger.current("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == ["current() -> int"]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None]


def test_hub_dot_display_dot():
    line = "hub.display."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "animate",
        "char",
        "image",
        "number",
        "off",
        "orientation",
        "pixel",
        "text",
    ]


def test_hub_dot_imu_dot():
    line = "hub.imu."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "acceleration",
        "angular_velocity",
        "heading",
        "reset_heading",
        "tilt",
        "up",
    ]


def test_hub_dot_light_dot():
    line = "hub.light."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "animate",
        "blink",
        "off",
        "on",
    ]


def test_hub_dot_light_dot_animate():
    line = "hub.light.animate("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "animate(colors: Collection[Color], interval: Number) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [0]
    assert [
        [p["label"] for p in s["parameters"]] for s in signatures["signatures"]
    ] == [["colors: Collection[Color]", "interval: Number"]]


def test_hub_dot_light_dot_animate2():
    line = "hub.light.animate([],"
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "animate(colors: Collection[Color], interval: Number) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [1]
    assert [
        [p["label"] for p in s["parameters"]] for s in signatures["signatures"]
    ] == [["colors: Collection[Color]", "interval: Number"]]


def test_hub_dot_light_dot_blink():
    line = "hub.light.blink("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "blink(color: Color, durations: Collection[int]) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [0]


def test_hub_dot_light_dot_blink2():
    line = "hub.light.blink(Color.RED,"
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "blink(color: Color, durations: Collection[int]) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [1]


def test_hub_dot_light_dot_on():
    line = "hub.light.on("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "on(color: Color) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [0]


def test_hub_dot_speaker_dot():
    line = "hub.speaker."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "beep",
        "play_notes",
        "volume",
    ]


def test_hub_dot_speaker_dot_beep():
    line = "hub.speaker.beep("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "beep(frequency: Number=500, duration: Number=100) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [0]


def test_hub_dot_speaker_dot_beep2():
    line = "hub.speaker.beep(100,"
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "beep(frequency: Number=500, duration: Number=100) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [1]


def test_hub_dot_speaker_dot_play_notes():
    line = "hub.speaker.play_notes("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "play_notes(notes: Iterable[str], tempo: Number=120) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [0]


def test_hub_dot_speaker_dot_play_notes2():
    line = "hub.speaker.play_notes([],"
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "play_notes(notes: Iterable[str], tempo: Number=120) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [1]


def test_hub_dot_speaker_dot_volume():
    line = "hub.speaker.volume("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "volume() -> int",
        "volume(volume: Number) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None, 0]


def test_hub_dot_system_dot():
    line = "hub.system."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "name",
        "reset_reason",
        "set_stop_button",
        "shutdown",
    ]


def test_hub_dot_system_dot_name():
    line = "hub.system.name("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "name() -> str",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None]


def test_hub_dot_system_dot_reset_reason():
    line = "hub.system.reset_reason("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "reset_reason() -> int",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None]


def test_hub_dot_system_dot_set_stop_button():
    line = "hub.system.set_stop_button("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "set_stop_button(button: Optional[Union[Button, Iterable[Button]]]) -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [0]


def test_hub_dot_system_dot_shutdown():
    line = "hub.system.shutdown("
    code = _create_snippet(line)
    signatures: SignatureHelp = json.loads(get_signatures(code, 3, len(line) + 1))
    assert [s["label"] for s in signatures["signatures"]] == [
        "shutdown() -> None",
    ]
    assert [s.get("activeParameter") for s in signatures["signatures"]] == [None]
