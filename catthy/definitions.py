from __future__ import annotations
from typing import *
from abc import ABC, abstractmethod, abstractstaticmethod

A = TypeVar('A')
B = TypeVar('B')

K = TypeVar('K')
V = TypeVar('V')
K_1 = TypeVar('K_1')
V_1 = TypeVar('V_1')

Rule = Callable[[A], bool]
MapFunction = Callable[[A], B]
BinaryOperation = Callable[[A, A], B]
DictMapFunction = Callable[[K,V], Tuple[K_1, V_1]]

class SupportsIter(Protocol[A]):
    def __iter__(self) -> A: ...

class SupportsNext(Protocol[A]):
    def __next__(self) -> A: ...

class SupportsIterNext(SupportsIter, SupportsNext): ...

class SupportsMap(Protocol[A]):
    @abstractmethod
    def map(self, f: MapFunction[A, B]) -> SupportsMap[B]: ...

class SupportsZip(Protocol[A]):
    @abstractmethod
    def zip(self, *Is: Iterable) -> SupportsZip: ...

class Foldable(Protocol[A]):
    @abstractmethod
    def foldr(self, binop: BinaryOperation[A, B]) -> B: ...

    @abstractmethod
    def foldl(self, binop: BinaryOperation[A, B]) -> B: ...

class SupportsFilter(Protocol[A]):
    @abstractmethod
    def filter(self, f: Rule[A]) -> SupportsFilter: ...

class SupportsZipMap(SupportsZip[A], SupportsMap[A]):
    @abstractmethod
    def zip_map(self, f: MapFunction[A, B]) -> SupportsZipMap: ...

    @abstractmethod
    def zip_maps(self, *fs: Callable) -> SupportsZipMap: ...


class Functor(SupportsMap[A]):
    @abstractmethod
    def map(self, f: MapFunction[A, B]) -> Functor[B]: ...

class Applicative(Functor[A]):
    @abstractstaticmethod
    def of(cls, *xs) -> Applicative[A]: ...

    @abstractmethod
    def apply_to(self: Applicative[MapFunction[A, B]], other: Applicative[A]) -> Applicative[B]: ...
