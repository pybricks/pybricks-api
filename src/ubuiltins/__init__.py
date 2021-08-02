# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/builtins.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors
#
# Portions of the documentation copied from:
# https://docs.python.org/3/library/builtins.html
# https://docs.python.org/3/library/constants.html
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/exceptions.html
# Copyright (c) 2001-2021 Python Software Foundation

"""
The following functions and exceptions can be used without importing anything.
"""

from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Literal,
    Mapping,
    Sequence,
    SupportsComplex,
    SupportsFloat,
    SupportsInt,
    Tuple,
    Union,
    overload,
)

import uio
import usys


# These get overridden later on, but we still want to use the originals
# for the purpose of typing the doc strings.
_bool = bool
_bytearray = bytearray
_bytes = bytes
_callable = callable
_complex = complex
_dict = dict
_float = float
_int = int
_str = str
_type = type

# Functions and types


def abs(x: Any) -> Any:
    """
    Returns the absolute value of a number. The argument may be an integer, a
    floating point number, or an object implementing __abs__().

    .. If the argument is a complex number, its magnitude is returned.
    """


def all(iterable: Iterable) -> _bool:
    """
    Returns ``True`` if all elements of the iterable are true (or if the
    iterable is empty).

    Equivalent to::

        def all(iterable):
            for element in iterable:
                if not element:
                    return False
            return True
    """


def any(iterable: Iterable) -> _bool:
    """
    Returns ``True`` if any element of the iterable is true. If the iterable is
    empty, returns ``False``.

    Equivalent to::

        def any(iterable):
            for element in iterable:
                if element:
                    return True
            return False
    """


def bin(x: Any) -> _str:
    """
    Converts an integer number to a binary string prefixed with “0b”. The result
    is a valid Python expression. If ``x`` is not a Python :class:`int` object,
    it has to define an ``__index__()`` method that returns an integer.
    """


class bool:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: Any) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Creates a boolean value, which is ``True`` or ``False``.

        The argument is converted using the standard truth testing procedure.
        If no argument is given, it returns ``False``.
        """


class bytes:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, source: _int) -> None:
        ...

    @overload
    def __init__(self, source: Union[_bytes, _bytearray, Iterable[_int]]) -> None:
        ...

    @overload
    def __init__(self, source: _str, encoding: _str) -> None:
        ...

    def __init__(self, *args):
        r"""
        Creates a new ``bytes`` object, which is a sequence of integers
        in the range :math:`0 \leq x \leq 255`. This object is *immutable*,
        which means that you *cannot* change its contents after you create it.

           * If no argument is given, this creates an empty ``bytes`` object.
           * If the ``source`` argument is an integer, this creates a ``bytes``
             object of zeros. The argument specifies how many zeros.
           * If ``source`` is a ``bytearray``, ``bytes`` object, or some other
             iterable of integers, this creates a ``bytes``
             object with the same byte sequence as the ``source`` argument.
           * If ``source`` is a string, choose ``'utf8'`` as the ``encoding``
             argument. Then this creates a ``bytes`` object containing the
             encoded string.
        """


class bytearray:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, source: _int) -> None:
        ...

    @overload
    def __init__(self, source: Union[_bytes, _bytearray, _str, Iterable[_int]]) -> None:
        ...

    def __init__(self, *args):
        r"""
        Creates a new ``bytearray`` object, which is a sequence of integers
        in the range :math:`0 \leq x \leq 255`. This object is *mutable*, which
        means that you *can* change its contents after you create it.

           * If no argument is given, this creates an empty ``bytearray``.
           * If the ``source`` argument is an integer, this creates a ``bytearray``
             of zeros. The argument specifies how many zeros.
           * For all other valid ``source`` arguments, this creates a bytearray with
             the same byte sequence as the given ``source`` argument.
        """


def callable(object: Any) -> _bool:
    """
    Returns ``True`` if the object argument appears callable, ``False`` if not.
    """


def chr(i: _int) -> _str:
    """
    Returns the string representing a character whose Unicode code point is the
    integer ``i``. For example, ``chr(97)`` returns the string ``'a'``.

    This is the inverse of :meth:`ord`.
    """


def classmethod(method: _callable) -> _callable:
    """
    Transforms a method into a class method.
    """


class complex:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(
        self, real: Union[_float, SupportsFloat, _complex, SupportsComplex]
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        real: Union[_float, SupportsFloat, _complex, SupportsComplex],
        imag: Union[_float, SupportsFloat, _complex, SupportsComplex],
    ) -> None:
        ...

    @overload
    def __init__(self, value: _str) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Returns a complex number with the value `real + imag*1j` or converts a
        string or number to a complex number.

        .. note:: This type is not available on the BOOST Move hub.
        """


class dict:
    @overload
    def __init(self) -> None:
        ...

    @overload
    def __init(self, **kwargs) -> None:
        ...

    def __init__(self, *args, **kwargs) -> None:
        """
        Creates a new dictionary.
        """


@overload
def dir() -> List[_str]:
    ...


@overload
def dir(object: Any) -> List[_str]:
    ...


def dir(*args) -> List[_str]:
    """
    Without arguments, return the list of names in the current local scope. With
    an argument, attempt to return a list of valid attributes for that object.
    """


@overload
def divmod(a: _int, b: _int) -> Tuple[_int, _int]:
    ...


@overload
def divmod(a: _float, b: _float) -> Tuple[_float, _float]:
    ...


def divmod(a, b):
    """
    Takes two (non complex) numbers as arguments and returns a pair of numbers
    consisting of their quotient and remainder when using integer division.
    """


@overload
def enumerate(iterable: Iterable) -> Iterable:
    ...


@overload
def enumerate(iterable: Iterable, start: _int) -> Iterable:
    ...


def enumerate(*args) -> Iterable:
    """
    Returns an enumerate object.

    Equivalent to::

        def enumerate(sequence, start=0):
            n = start
            for elem in sequence:
                yield n, elem
                n += 1

    .. note:: This type is not available on the BOOST Move hub.
    """


@overload
def eval(expression: _str) -> Any:
    ...


@overload
def eval(expression: _str, globals: _dict) -> Any:
    ...


@overload
def eval(expression: _str, globals: _dict, locals: Mapping) -> Any:
    ...


def eval(*args):
    """
    The arguments are a string and optional globals and locals. If provided,
    ``globals`` must be a dictionary. If provided, ``locals`` can be any mapping
    object.

    The return value is the result of the evaluated expression. Syntax errors
    are reported as exceptions.
    """


@overload
def exec(object: Any) -> None:
    ...


@overload
def exec(object: Any, globals: _dict) -> None:
    ...


@overload
def exec(object: Any, globals: _dict, locals: Mapping) -> None:
    ...


def exec(*args):
    """
    This function supports dynamic execution of Python code.
    """


class float:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: _int) -> None:
        ...

    @overload
    def __init__(self, x: SupportsFloat) -> None:
        ...

    @overload
    def __init__(self, x: _str) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Returns a floating point number constructed from a number or string ``x``.
        """


@overload
def getattr(object: Any, name: _str) -> Any:
    ...


@overload
def getattr(object: Any, name: _str, default: Any) -> Any:
    ...


def getattr(*args):
    """
    Returns the value of the named attribute of object.
    """


def globals() -> Dict[_str, Any]:
    """
    Return a dictionary representing the current global symbol table.
    """


def hasattr(object: Any, name: _str) -> _bool:
    """
    The result is ``True`` if the string is the name of one of the object’s
    attributes, ``False`` if not.
    """


def hash(object: Any) -> _int:
    """
    Returns the hash value of the object (if it has one).
    """


@overload
def help() -> None:
    ...


@overload
def help(object: Any) -> None:
    ...


def help(*args) -> None:
    """
    Prints help for the ``object``. If no argument is given, prints general help.
    If object is ``'modules'``, prints available modules.

    .. note:: This function is not available on the BOOST Move hub.
    """


def hex(x: _int) -> _str:
    """
    Converts an integer number to a lowercase hexadecimal string prefixed with “0x”.
    """


def id() -> _int:
    """
    Returns the “identity” of an object. This is an integer which is guaranteed
    to be unique and constant for this object during its lifetime.
    """


@overload
def input() -> _str:
    ...


@overload
def input(prompt: _str) -> _str:
    ...


def input(*args) -> _str:
    """
    If the prompt argument is present, it is written to standard output without
    a trailing newline. The function then reads a line from input, converts it
    to a string (stripping a trailing newline), and returns that.

    .. note:: This function is not available on the BOOST Move hub.
    """


class int:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: _str) -> None:
        ...

    @overload
    def __init__(self, x: _str, base: _int) -> None:
        ...

    @overload
    def __init__(self, x: Union[_int, SupportsInt]) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Returns an integer object constructed from a number or string ``x``, or
        returns ``0`` if no arguments are given.
        """

    def to_bytes(self, length: _int, byteorder: Literal["little", "big"]) -> _bytes:
        """
        Returns an array of bytes representing an integer.
        """

    @classmethod
    def from_bytes(cls, _bytes: _bytes, byteorder: Literal["little", "big"]) -> _int:
        """
        Returns the integer represented by the given array of bytes.
        """


def isinstance(object: Any, classinfo: Union[_type, Tuple[_type]]) -> _bool:
    """
    Returns ``True`` if the ``object`` argument is an instance of the ``classinfo``
    argument, or of a subclass thereof.
    """


def issubclass(cls: _type, classinfo: Union[_type, Tuple[_type]]) -> _bool:
    """
    Returns ``True`` if ``cls`` is a subclass of ``classinfo``.
    """


def iter(object: Union[Iterable, Sequence]) -> Iterator:
    """
    Returns an iterator object.
    """


def len(s: Sequence) -> _int:
    """
    Returns the length (the number of items) of an object.
    """


class list:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Creates a new list.
        """


def locals() -> _dict:
    """
    Updates and returns a dictionary representing the current local symbol table.
    """


def map(function: Callable, iterable: Iterable, *args: Any) -> Iterator:
    """
    Returns an iterator that applies function to every item of iterable,
    yielding the results.
    """


@overload
def max(iterable: Iterable) -> Any:
    ...


@overload
def max(arg1: Any, arg2: Any, *args: Any) -> Any:
    ...


def max(*args):
    """
    Returns the largest item in an iterable or the largest of two or more arguments.
    """


@overload
def min(iterable: Iterable) -> Any:
    ...


@overload
def min(arg1: Any, arg2: Any, *args: Any) -> Any:
    ...


def min(*args):
    """
    Returns the smallest item in an iterable or the smallest of two or more arguments.
    """


@overload
def next(iterator: Iterator) -> Any:
    ...


@overload
def next(iterator: Iterator, default: Any) -> Any:
    ...


def next(*args):
    """
    Retrieves the next item from the iterator by calling its ``__next__()`` method.
    If ``default`` is given, it is returned if the iterator is exhausted,
    otherwise ``StopIteration`` is raised.
    """


class object:
    def __init__(self) -> None:
        """
        Return a new featureless object.
        """


def oct(x: _int) -> _str:
    """
    Converts an integer number to an octal string prefixed with “0o”.
    """


# .. function:: open()


def ord(c: _str) -> _int:
    """
    Given a string representing one Unicode character, return an integer
    representing the Unicode code point of that character.

    This is the inverse of :meth:`chr`.
    """


@overload
def pow(base: _int, exp: _int) -> Union[_int, _float]:
    ...


@overload
def pow(base: _int, exp: _int, mod: _int) -> Union[_int, _float]:
    ...


def pow():
    """
    Returns ``base`` to the power ``exp``; if ``mod`` is present, returns ``base``
    to the power ``exp``, modulo ``mod``.

    The two-argument form ``pow(base, exp)`` is equivalent to using the power
    operator: ``base ** exp``.
    """


def print(*objects, sep: _str = " ", end: _str = "\n", file: uio.FileIO = usys.stdin):
    """
    Prints ``objects`` to the text stream ``file``, separated by ``sep`` and
    followed by ``end``. ``sep``, ``end`` and ``file``, if present,
    must be given as keyword arguments.

    .. note:: The ``file`` argument is not supported on the BOOST Move hub.
    """


class range:
    @overload
    def __init__(self, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int, step: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Rather than being a function, ``range`` is actually an immutable sequence _type.
        """


def repr(object: Any) -> _str:
    """
    Returns a string containing a printable representation of an object.
    """


def reversed(seq: Sequence) -> Iterator:
    """
    Returns a reverse iterator.

    .. note:: This function is not available on the BOOST Move hub.
    """


@overload
def round(number: _float) -> _int:
    ...


@overload
def round(number: _float, ndigits: _int) -> _float:
    ...


def round(*args):
    """
    Returns ``number`` rounded to ``ndigits`` precision after the decimal point.
    If ``ndigits`` is omitted or is ``None``, it returns the nearest integer to
    its input.

    .. tip:: To print a number use a format function instead. Since many floating
        point numbers don't have exact representations, :meth:`round` often gives
        unexpected results!

        Example::

            # print two decimal places
            print('my number: %.2f' % number)
            print('my number: {:.2f}'.format(number))
    """


class set:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Returns a new set object, optionally with elements taken from ``iterable``.
        """


def setattr(object: Any, name: _str, value: Any) -> None:
    """
    Assigns the value to the attribute, provided the object allows it.

    This is the counterpart of :meth:`getattr`.
    """


class slice:
    @overload
    def __init__(self, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int, step: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Returns a slice object representing the set of indices specified by
        ``range(start, stop, step)``.

        Slice objects are also generated when extended indexing syntax is used.
        For example: ``a[start:stop:step]`` or ``a[start:stop, i]``.

        .. note:: This type is not available on the BOOST Move hub.
        """


def sorted(iterable: Iterable, key=None, reverse=False) -> List:
    """
    Returns a new sorted list from the items in ``iterable``.
    """


def staticmethod(method: _callable) -> _callable:
    """
    Transforms a method into a static method.
    """


class str:
    @overload
    def __init__(self, object: Any = "") -> None:
        ...

    @overload
    def __init__(
        self, object: _bytes = b"", encoding: _str = "utf-8", errors: _str = "strict"
    ) -> None:
        ...

    def __init__(self) -> None:
        """
        Return a :class:`str` version of object.
        """


@overload
def sum(iterable: Iterable) -> _int:
    ...


@overload
def sum(iterable: Iterable, start: _int) -> _int:
    ...


def sum(*args):
    """
    Sums ``start`` and the items of an ``iterable`` from left to right and
    returns the total.
    """


@overload
def super() -> _type:
    ...


@overload
def super(_type: _type) -> _type:
    ...


@overload
def super(_type: _type, object_or_type: Any) -> _type:
    ...


def super(*args):
    """
    Returns am object that delegates method calls to a parent or sibling class
    of ``_type``.
    """


class tuple:
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, iterable: Iterable):
        ...

    def __init__(self, *args) -> None:
        """
        Rather than being a function, :class:`tuple` is actually an immutable
        sequence type.
        """


class type:
    def __init__(self, object: Any) -> None:
        """
        With one argument, returns the _type of an ``object``.
        """


def zip(*iterables: Iterable) -> Iterable[Tuple]:
    """
    Returns an iterator of tuples, where the i-th tuple contains the i-th
    element from each of the argument sequences or iterables. The iterator
    stops when the shortest input iterable is exhausted.

    With a single iterable argument, it returns an iterator of 1-tuples.
    With no arguments, it returns an empty iterator.

    Equivalent to::

        def zip(*iterables):
            # zip('ABCD', 'xy') --> Ax By
            sentinel = object()
            iterators = [iter(it) for it in iterables]
            while iterators:
                result = []
                for it in iterators:
                    elem = next(it, sentinel)
                    if elem is sentinel:
                        return
                    result.append(elem)
                yield tuple(result)
    """


# base exceptions


class BaseException:
    """
    The base class for all built-in exceptions.

    It is not meant to be directly inherited by user-defined classes (for that,
    use :class:`Exception`).
    """

    args: Tuple
    """
    The tuple of arguments given to the exception constructor.
    """


class Exception(BaseException):
    """
    All built-in exceptions are derived from this class.

    All user-defined exceptions should also be derived from this class.
    """


class ArithmeticError(Exception):
    """
    The base class for those built-in exceptions that are raised for various
    arithmetic errors.
    """


class LookupError(Exception):
    """
    The base class for the exceptions that are raised when a key or index used
    on a mapping or sequence is invalid.
    """


# concrete exceptions


class AssertionError(Exception):
    """
    Raised when an assert statement fails.
    """


class AttributeError(Exception):
    """
    Raised when an attribute reference or assignment fails.
    """


class EOFError(Exception):
    """
    Raised when the :meth:`input` function hits an end-of-file condition (EOF)
    without reading any data.
    """


class GeneratorExit(BaseException):
    """
    Raised when a generator or coroutine is closed.
    """


class ImportError(Exception):
    """
    Raised when the ``import`` statement is unable to load a module.
    """


class IndentationError(SyntaxError):
    """
    Base class for syntax errors related to incorrect indentation.
    """


class IndexError(LookupError):
    """
    Raised when a sequence subscript is out of range.
    """


class KeyError(LookupError):
    """
    Raised when a mapping (dictionary) key is not found in the set of existing keys.
    """


class KeyboardInterrupt(BaseException):
    """
    Raised when the user hits the interrupt key (normally :kbd:`Control-C`).
    """


class MemoryError(Exception):
    """
    Raised when an operation runs out of memory.
    """


class NameError(Exception):
    """
    Raised when a local or global name is not found.
    """


class NotImplementedError(RuntimeError):
    """
    In user defined base classes, abstract methods should raise this exception
    when they require derived classes to override the method, or while the
    class is being developed to indicate that the real implementation still
    needs to be added.
    """


class OSError(Exception):
    """
    This exception is raised by the firmware, which is
    the Operating System that runs on the hub.
    For :ref:`example <device_detection>`, it
    raises an ``OSError`` if you call ``Motor(Port.A)`` when there is no
    motor on port A.
    """

    errno: _int
    """
    Specifies which kind of ``OSError`` occurred, as listed in the
    :mod:`uerrno` module.
    """


class OverflowError(ArithmeticError):
    """
    Raised when the result of an arithmetic operation is too large to be represented.
    """


class RuntimeError(Exception):
    """
    Raised when an error is detected that doesn’t fall in any of the other categories.

    The associated value is a string indicating what precisely went wrong.
    """


class StopIteration(Exception):
    """
    Raised by built-in function :meth:`next` and an iterator’s ``__next__()``
    method to signal that there are no further items produced by the iterator.

    Generator functions should return instead of raising this directly.
    """


class SyntaxError(Exception):
    """
    Raised when the parser encounters a syntax error.
    """


class SystemExit(BaseException):
    """
    Raised when you press the stop button on the hub or in the Pybricks Code app.
    """


class TypeError(Exception):
    """
    Raised when an operation or function is applied to an object of inappropriate type.
    """


class ValueError(Exception):
    """
    Raised when an operation or function receives an argument that has the right
    type but an inappropriate value. This is used when the situation is
    not described by a more precise exception such as :class:`IndexError`.
    """


class ZeroDivisionError(ArithmeticError):
    """
    Raised when the second argument of a division or modulo operation is zero.
    """
