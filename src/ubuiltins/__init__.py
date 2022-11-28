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

Most functions and classes in this module do not accept keyword arguments.
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
_classmethod = classmethod
_complex = complex
_dict = dict
_float = float
_int = int
_str = str
_type = type

# Functions and types


def abs(x: Any) -> Any:
    """abs(x) -> Any

    Returns the absolute value of a number.

    The argument may be an integer, a
    floating point number, or any object implementing ``__abs__()``.
    If the argument is a complex number, its magnitude is returned.

    Arguments:
        x (Any): The value.

    Returns:
        Absolute value of ``x``.
    """


def all(x: Iterable) -> _bool:
    """all(x) -> bool

    Checks if all elements of the iterable are true.

    Equivalent to::

        def all(x):
            for element in x:
                if not element:
                    return False
            return True

    Arguments:
        x (Iterable): The iterable to be checked.

    Returns:
        ``True`` if the iterable ``x`` is empty or if all elements
        are true. Otherwise ``False``.
    """


def any(x: Iterable) -> _bool:
    """any(x) -> bool

    Checks if at least one elements of the iterable is true.

    Equivalent to::

        def any(x):
            for element in x:
                if element:
                    return True
            return False

    Arguments:
        x (Iterable): The iterable to be checked.

    Returns:
        ``True`` if at least one element in ``x`` is true. Otherwise ``False``.
    """


def bin(x: Any) -> _str:
    """bin(x) -> str

    Converts an integer to its binary representation. The result is a
    string prefixed with ``0b``. The result is a valid Python expression.
    For example, ``bin(5)`` gives ``"0b101"``.

    Arguments:
        x (int): Value to be converted.

    Returns:
        A string representing the binary form of the input.
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
        bool(​)
        bool(x)

        Creates a boolean value, which is either ``True`` or ``False``.

        The input value is converted using the standard truth testing
        procedure. If no input is given, it is assumed to be ``False``.

        Arguments:
            x: Value to be converted.

        Returns:
            Result of the truth-test.
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
        bytes(​)
        bytes(integer)
        bytes(iterable)
        bytes(string, encoding)

        Creates a new ``bytes`` object, which is a sequence of integers
        in the range :math:`0 \leq x \leq 255`. This object is *immutable*,
        which means that you *cannot* change its contents after you create it.

        If no argument is given, this creates an empty ``bytes`` object.

        Arguments:
            integer (int): If the argument is a single integer, this creates
              a ``bytes`` object of zeros. The argument specifies how many.
            iterable (iter): If the argument is a ``bytearray``, ``bytes``
              object, or some other iterable of integers, this creates a ``bytes``
              object with the same byte sequence as the argument.
            string (str): If the argument is a string, this creates a ``bytes``
              object containing the encoded string.
            encoding (str): Specifies which encoding to use for the ``string``
              argument. Only ``"utf-8"``  is supported.
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
        bytearray(​)
        bytearray(integer)
        bytearray(iterable)
        bytearray(string)

        Creates a new ``bytearray`` object, which is a sequence of integers
        in the range :math:`0 \leq x \leq 255`. This object is *mutable*, which
        means that you *can* change its contents after you create it.

        If no argument is given, this creates an empty ``bytearray`` object.

        Arguments:
            integer (int): If the argument is a single integer, this creates
              a ``bytearray`` object of zeros. The argument specifies how many.
            iterable (iter): If the argument is a ``bytearray``, ``bytes``
              object, or some other iterable of integers, this creates
              a ``bytearray`` object with the same byte sequence as the argument.
            string (str): If the argument is a string, this creates
              a ``bytearray`` object containing the encoded string.
        """


def callable(object: Any) -> _bool:
    """
    Returns ``True`` if the object argument appears callable, ``False`` if not.
    """


def chr(x: _int) -> _str:
    """chr(x) -> str

    Returns the string representing a character whose Unicode code is the
    integer ``x``. This is the inverse of :meth:`ord`. For
    example, ``chr(97)`` gives ``"a"``.

    Arguments:
        x (int): Value to be converted (0-255).

    Returns:
        A string with one character, corresponding to the given Unicode value.
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
        complex(string)
        complex(a=0, b=0)

        Creates a complex number from a string or from a pair of numbers.

        If a string is given, it must be of the form ``'1+2j'``.
        If a pair of numbers is provided, the result is computed
        as: ``a + b * j``.

        Arguments:
            string (str): A string of the form ``'1+2j'`` .
            a (float or complex): A real-valued or complex number.
            b (float or complex): A real-valued or complex number.

        Returns:
            The resulting complex number.
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
        dict(**kwargs)
        dict(mapping, **kwargs)
        dict(iterable, **kwargs)

        Creates a dictionary object.

        See the standard
        `Python documentation
        <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_
        for a comprehensive reference with examples.
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
    divmod(a, b) -> Tuple[int, int]

    Gets the quotient and remainder for dividing two integers.

    See the standard `Python divmod documentation
    <https://docs.python.org/3/library/functions.html#divmod>`_ for
    the expected behavior when ``a`` or ``b`` are floating point numbers
    instead.

    Arguments:
        a (int): Numerator.
        b (int): Denominator.

    Returns:
        A tuple with the quotient ``a // b`` and the remainder ``a % b``.
    """


class enumerate:
    @overload
    def __init__(self, iterable: Iterable) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable, start: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        enumerate(iterable, start=0)

        Enumerates an existing iterator by adding a numeric index.

        This function is equivalent to::

            def enumerate(sequence, start=0):
                n = start
                for elem in sequence:
                    yield n, elem
                    n += 1
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
    eval(expression) -> Any
    eval(expression, globals) -> Any
    eval(expression, globals, locals) -> Any

    Evaluates the result of an expression.

    Syntax errors are reported as exceptions.

    Arguments:
        expression (str): Expression to evaluate result of.
        globals (dict): If given, this controls what functions are available
            for use in the expression. By default the global scope is accessible.
        locals (dict): If given, this controls what functions are available
            for use in the expression. Defaults to the same as ``globals``.

    Returns:
        The value obtained by executing the expression.
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
    exec(expression)
    exec(expression, globals)
    exec(expression, globals, locals)

    Executes MicroPython code.

    Syntax errors are reported as exceptions.

    Arguments:
        expression (str): Code to be executed.
        globals (dict): If given, this controls what functions are available
            for use in the expression. By default the global scope is accessible.
        locals (dict): If given, this controls what functions are available
            for use in the expression. Defaults to the same as ``globals``.
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
        """float(x=0.0)

        Creates a floating point number from a given object.

        Arguments:
            x (int or float or str): Number or string to be converted.
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
    globals() -> dict

    Gets a dictionary representing the current global symbol table.

    Returns:
        The dictionary of globals.
    """


def hasattr(object: Any, name: _str) -> _bool:
    """
    The result is ``True`` if the string is the name of one of the object’s
    attributes, ``False`` if not.
    """


def hash(object: Any) -> _int:
    """
    hash(object) -> int

    Gets the hash value of an object, if the object supports it.

    Arguments:
        object: Object for which to get a hash value.

    Returns:
        The hash value.
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
    """


def hex(x: int) -> _str:
    """hex(x) -> str

    Converts an integer to its hexadecimal representation. The result is a
    lowercase string prefixed with ``0x``. The result is a valid Python
    expression. For example, ``hex(25)`` gives ``"0x19"``.

    Arguments:
        x (int): Value to be converted.

    Returns:
        A string representing the hexadecimal form of the input.
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
    """input() -> str
    input(prompt) -> str

    Gets input from the user in the terminal window. It waits until
    the user presses :kbd:`Enter`.

    Arguments:
        prompt (str): If given, this is printed in the terminal window first.
            This can be used to ask a question so the user knows what to type.

    Returns:
        Everything the user typed before pressing :kbd:`Enter`.
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
        """int(x=0)

        Creates an integer.

        Arguments:
            x (int or float or str): Object to be converted.
        """

    def to_bytes(self, length: _int, byteorder: Literal["little", "big"]) -> _bytes:
        """
        to_bytes(length, byteorder) -> bytes

        Get a :class:`bytes` representation of the integer.

        Arguments:
            length (int): How many bytes to use.
            byteorder (str): Choose ``"big"`` to put the most significant byte
                first. Choose ``"little"`` to put the least significant byte
                first.

        Returns:
            Byte sequence that represents the integer.
        """

    @_classmethod
    def from_bytes(cls, _bytes: _bytes, byteorder: Literal["little", "big"]) -> _int:
        """from_bytes(bytes, byteorder) -> int

        Convert a byte sequence to the number it represents.

        Arguments:
            bytes (bytes): The bytes to convert.
            byteorder (str): Choose ``"big"`` if the most significant byte is
                the first element. Choose ``"little"`` if the least significant
                byte is the first element.

        Returns:
            The number represented by the bytes.
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
    iter(object) -> Iterator

    Gets the iterator of the object if available.

    Arguments:
        object: Object for which to get the iterator.

    Returns:
        The iterator.
    """


def len(s: Sequence) -> _int:
    """
    len(s) -> int

    Gets the length (the number of items) of an object.

    Arguments:
        s (Sequence): The sequence of which to get the length.

    Returns:
        The length.
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
        list(​)
        list(iterable)

        Creates a new list. If no argument is given, this creates an empty
        ``list`` object.

        A list is *mutable*, which means that you *can* change its contents
        after you create it.

        Arguments:
            iterable (iter): Iterable from which to build the list.
        """


def locals() -> _dict:
    """
    locals() -> dict

    Gets a dictionary representing the current local symbol table.

    Returns:
        The dictionary of locals.
    """


def map(function: Callable, iterable: Iterable, *args: Any) -> Iterator:
    """
    map(function, iterable) -> Iterator
    map(function, iterable1, iterable2...) -> Iterator

    Creates a new iterator that applies the given function to each item in the
    given iterable and yields the results.

    Arguments:
        function (callable): Function that computes a result for one item in the
            iterable(s). The number of arguments to this function must match
            the number of iterables given.
        iterable (iter): One or more source interables from which to draw data.
            With multiple iterables, the iterator stops when the shortest
            iterable is exhausted.

    Returns:
        The new, mapped iterator.
    """


@overload
def max(iterable: Iterable) -> Any:
    ...


@overload
def max(arg1: Any, arg2: Any, *args: Any) -> Any:
    ...


def max(*args):
    """
    max(iterable) -> Any
    max(arg1, arg2, ....) -> Any

    Gets the object with largest value.

    The argument may be a single iterable, or any number of objects.

    Returns:
        The object with the largest value.
    """


@overload
def min(iterable: Iterable) -> Any:
    ...


@overload
def min(arg1: Any, arg2: Any, *args: Any) -> Any:
    ...


def min(*args):
    """
    min(iterable) -> Any
    min(arg1, arg2, ....) -> Any

    Gets the object with smallest value.

    The argument may be a single iterable, or any number of objects.

    Returns:
        The object with the smallest value.
    """


def next(iterator: Iterator) -> Any:
    """
    next(iterator) -> Any

    Retrieves the next item from the iterator by calling its ``__next__()`` method.

    Arguments:
        iterator (iter): Initialized generator object from which to draw the next
            value.

    Returns:
        The next value from the generator.
    """


class object:
    def __init__(self) -> None:
        """
        Creates a new, featureless object.
        """


def oct(x: _int) -> _str:
    """oct(x) -> str

    Converts an integer to its octal representation. The result is a
    string prefixed with ``0o``. The result is a valid Python
    expression. For example, ``oct(25)`` gives ``"0o31"``.

    Arguments:
        x (int): Value to be converted.

    Returns:
        A string representing the octal form of the input.
    """


# .. function:: open()


def ord(c: _str) -> _int:
    """ord(c) -> int

    Converts a string consisting of one Unicode character to the
    corresponding number. This is the inverse of :meth:`chr`.

    Arguments:
        c (str): Character to be converted.

    Returns:
        Number that represents the character (0--255).
    """


def pow(base: Union[_int, _float], exp: Union[_int, _float]) -> Union[_int, _float]:
    """
    pow(base, exp) -> Number

    Raises the base to the given exponent: :math:`\\text{base}^{\\mathrm{exp}}`.

    This is the same as doing ``base ** exp``.

    Arguments:
        base (Number): The base.
        exp (Number): The exponent.

    Returns:
        The result.
    """


@overload
def print(*objects):
    ...


@overload
def print(*objects, sep: _str = " ", end: _str = "\n", file: uio.FileIO = usys.stdin):
    ...


def print(*args):
    """print(*objects, sep=" ", end="\\n", file=usys.stdin)

    Prints text or other objects in the terminal window.

    Arguments:
        objects: Zero or more objects to print.

    Keyword Arguments:
        sep: This is printed between objects, if there is more than one.
        end: This is printed after the last object.
        file: By default, the result is printed in the terminal window. This
              argument lets you print it to a file instead, if files are
              supported.
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
        range(stop)
        range(start, stop)
        range(start, stop, step)

        Creates a generator that yields values from ``start`` up to
        ``stop``, with increments of ``step``.

        Arguments:
            start (int): Starting value. Defaults to ``0`` if only one argument is given.
            stop (int): Endpoint. This value is *not* included.
            step (int): Increment between values. Defaults to ``1`` if only one
                or two arguments are given.
        """


def repr(x: Any) -> _str:
    """repr(object) -> str

    Gets the string that represents an object.

    Arguments:
        x (object): Object to be converted.

    Returns:
        String representation implemented by the object's ``__repr__`` method.
    """


def reversed(seq: Sequence) -> Iterator:
    """
    reversed(seq) -> Iterator

    Gets an iterator that yields the values from the sequence in the reverse, if
    supported.

    Arguments:
        seq: Sequence from which to draw samples.

    Returns:
        Iterator that yields values in reverse order, starting with the last value.
    """


@overload
def round(number: _float) -> _int:
    ...


@overload
def round(number: _float, ndigits: _int) -> _float:
    ...


def round(*args):
    """
    round(number) -> int
    round(number, ndigits) -> float

    Round a number to a given number of digits after the decimal point.

    If ``ndigits`` is omitted or ``None``, it returns the nearest integer.

    Rounding with one or more digits after the decimal point will not always
    truncate trailing zeros. To print numbers nicely, format strings instead::

        # print two decimal places
        print('my number: %.2f' % number) print('my number:
        {:.2f}'.format(number))

    Arguments:
        number (float): The number to be rounded.
        ndigits (int): The number of digits remaining after the decimal point.
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
        slice(​)

        Creating instances of this class is not supported.

        Use indexing syntax instead. For
        example: ``a[start:stop:step]`` or ``a[start:stop, i]``.
        """


def sorted(iterable: Iterable, key=None, reverse=False) -> List:
    """
    Sorts objects.

    Arguments:
        iterable (iter): Objects to be sorted. This can also be a generator that
            yield a finite number of objects.
        key (callable): Function ``def(item) -> int`` that maps an object to a
            numerical value. This is used to figure out the order of the sorted
            items.
        reverse (bool): Whether to sort in reverse, putting the highest value
            first.


    Returns:
        A new list with the sorted items.
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
        str(​)
        str(object)
        str(object, encoding)

        Gets the string representation of an object.

        If no argument is given, this creates an empty ``str`` object.

        Arguments:
            object: If only this argument is given, this returns the stirng
              representation of the object.
            encoding (str): If the first argument is a ``bytearray`` or ``bytes``
              object and the encoding argument is ``"utf-8"``, this will decode
              the byte data to get a string representation.
        """


@overload
def sum(iterable: Iterable) -> _int:
    ...


@overload
def sum(iterable: Iterable, start: _int) -> _int:
    ...


def sum(*args):
    """
    sum(iterable) -> Number
    sum(iterable, start) -> Number

    Sums the items from the iterable and the start value.

    Arguments:
        iterable (iter): Values to be summed, starting with the first value.
        start (Number): Value added to the total.

    Returns:
        The total sum.
    """


@overload
def super() -> _type:
    ...


@overload
def super(type: _type) -> _type:
    ...


@overload
def super(type: _type, object_or_type: Any) -> _type:
    ...


def super(*args):
    """
    Returns an object that delegates method calls to a parent or sibling class
    of ``type``.
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
        tuple(​)
        tuple(iterable)

        Creates a new tuple. If no argument is given, this creates an empty
        ``tuple`` object.

        A tuple is *immutable*, which means that you *cannot* change its
        contents after you create it.

        Arguments:
            iterable (iter): Iterable from which to build the tuple.
        """


class type:
    def __init__(self, object: Any) -> None:
        """type(object)

        Gets the type of an object. This can be used to check if an object
        is an instance of a particular class.

        Arguments:
            object: Object of which to check the type.
        """


def zip(*iterables: Iterable) -> Iterable[Tuple]:
    """
    zip(iter_a, iter_b, ...) -> Iterable[Tuple]

    Returns an iterator of tuples, where the *i*-th tuple contains the *i*-th
    element from each of the argument sequences or iterables. The iterator
    stops when the shortest input iterable is exhausted.

    With a single iterable argument, it returns an iterator of 1-tuples.
    With no arguments, it returns an empty iterator.

    This functionality is equivalent to::

        def zip(*iterables):
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

    Arguments:
        iter_a (iter): The first iterable. This provides the first value for
            each of the yielded tuples.
        iter_b (iter): The second iterable. This provides the second value in
            each of the yielded tuples. And so on.

    Returns:
        A new iterator that yields tuples containing the values of the
        individual iterables.
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
