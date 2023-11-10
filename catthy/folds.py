from typing import TypeVar, Callable, Iterable

A = TypeVar('A')
B = TypeVar('B')

# Adapted from functools.reduce

class _initial_missing(object): ...

_default_initial = _initial_missing()

def foldl(function, sequence, initial=_default_initial):
    it = iter(sequence)

    if isinstance(initial, _initial_missing):
        try:
            value = next(it)
        except StopIteration:
            raise TypeError(
                "foldl() of empty iterable with no initial value") from None
    else:
        value = initial

    for element in it:
        value = function(value, element)

    return value

def foldr(binary_operation: Callable[[A,B], B], sequence: Iterable, initial=_default_initial) -> B:
    it = iter(sequence)

    if isinstance(initial, _initial_missing):
        try:
            value = next(it)
        except StopIteration:
            raise TypeError(
                "foldr() of empty iterable with no initial value") from None
    else:
        value = initial

    for element in it:
        value = binary_operation(element, value)

    return value