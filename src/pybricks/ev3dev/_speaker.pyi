# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Pybricks Authors

from typing import Iterable, Optional, Union

from pybricks.media.ev3dev import SoundFile

class Speaker:
    def beep(self, frequency: int = 500, duration: int = 100) -> None: ...
    def play_notes(self, notes: Iterable[str], tempo: int = 120) -> None: ...
    def play_file(self, file_name: Union[SoundFile, str]) -> None: ...
    def say(self, text: str) -> None: ...
    def set_speech_options(
        self,
        language: Optional[str] = None,
        voice: Optional[str] = None,
        speed: Optional[int] = None,
        pitch: Optional[int] = None,
    ): ...
    def set_volume(self, volume: int, which: str = "_all_") -> None: ...
