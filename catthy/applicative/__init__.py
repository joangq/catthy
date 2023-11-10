from __future__ import annotations
from ..definitions import MapFunction
from ..util import FactoryConstructor
from typing import TypeVar
from ..functor import *

A = TypeVar('A')
B = TypeVar('B')

class DefaultApplicative(FactoryConstructor[A]):
    def apply_to(self: DefaultApplicative[MapFunction[A, B]], other: DefaultApplicative[A]) -> DefaultApplicative[B]:
        return type(self)(f(x) for f in self for x in other)

# Concrete Applicatives ================================================= #

class AList(FList[A], DefaultApplicative): ...

class ATuple(FTuple[A], DefaultApplicative): ...

class ASet(FSet[A], DefaultApplicative): ...

class ADeque(FDeque[A], DefaultApplicative): ...