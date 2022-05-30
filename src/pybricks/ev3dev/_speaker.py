# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 The Pybricks Authors


class Speaker:
    """Plays beeps and sounds using a speaker."""

    def beep(self, frequency=500, duration=100):
        """Play a beep/tone.

        Arguments:
            frequency (:ref:`frequency`):
                Frequency of the beep. Frequencies below 100
                are treated as 100.
            duration (:ref:`time`):
                Duration of the beep. If the duration is less
                than 0, then the method returns immediately and the frequency
                play continues to play indefinitely.
        """
        pass

    def play_notes(self, notes, tempo=120):
        """Plays a sequence of musical notes. For example:
        ``['C4/4', 'C4/4', 'G4/4', 'G4/4']``.

        Each note is a string with the following format:

            - The first character is the name of the note, ``A`` to ``G``
              or ``R`` for a rest.
            - Note names can also include an accidental ``#`` (sharp) or
              ``b`` (flat). ``B#``/``Cb`` and ``E#``/``Fb`` are not
              allowed.
            - The note name is followed by the octave number ``2``
              to ``8``. For example ``C4`` is middle C. The octave changes
              to the next number at the note C, for example, ``B3`` is the
              note below middle C (``C4``).
            - The octave is followed by ``/`` and a number that indicates
              the size of the note. For example ``/4`` is a quarter note,
              ``/8`` is an eighth note and so on.
            - This can optionally followed by a ``.`` to make a dotted
              note. Dotted notes are 1-1/2 times as long as notes without a
              dot.
            - The note can optionally end with a ``_`` which is a tie or a
              slur. This causes there to be no pause between this note and
              the next note.

        Arguments:
            notes (iter):
                A sequence of notes to be played.
            tempo (int):
                Beats per minute. A quarter note is one beat.
        """
        pass

    def play_file(self, file):
        """Plays a sound file.

        Arguments:
            file (str):
                Path to the sound file, including the file extension.
        """

        pass

    def say(self, text):
        """Says a given text string.

        You can configure the language and voice of the text using
        :meth:`.set_speech_options`.

        Arguments:
            text (str): What to say.
        """

        pass

    def set_speech_options(self, language=None, voice=None, speed=None, pitch=None):
        """Configures speech settings used by the :meth:`.say` method.

        Any option that is set to ``None`` will not be changed. If an option
        is set to an invalid value :meth:`.say` will use the default value
        instead.

        Arguments:
            language (str):
                Language of the text. For example, you can choose ``'en'``
                (English) or ``'de'`` (German). [#espeak_lang]_
            voice (str):
                The voice to use. For example, you can choose ``'f1'`` (female
                voice variant 1) or ``'m3'`` (male voice variant 3).
                [#espeak_lang]_
            speed (int):
                Number of words per minute.
            pitch (int):
                Pitch (0 to 99). Higher numbers make the voice higher pitched
                and lower numbers make the voice lower pitched.
        """
        pass

    def set_volume(self, volume, which="_all_"):
        """Sets the speaker volume.

        Arguments:
            volume (:ref:`percentage`):
                Volume of the speaker.
            which (str):
                Which volume to set. ``'Beep'`` sets the volume for
                `beep` and `play_notes`. ``'PCM'`` sets the
                volume for :meth:`.play_file` and :meth:`.say`. ``'_all_'``
                sets both at the same time.
        """
        pass
