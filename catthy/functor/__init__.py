from __future__ import annotations
from ..definitions import MapFunction, DictMapFunction
from ..util import FactoryConstructor
from typing import TypeVar, Generic
from typing import List, Tuple, Set, Deque, Dict, OrderedDict

A = TypeVar('A')
B = TypeVar('B')

K = TypeVar('K')
V = TypeVar('V')
K_1 = TypeVar('K_1')
V_1 = TypeVar('V_1')

class DefaultFunctor(Generic[A]):
    def map(self, f: MapFunction[A, B]) -> DefaultFunctor[B]:
        self = type(self)(f(x) for x in self)
        return self
    
class DefaultFunctorDict(Generic[A]):
    def map(self, f: DictMapFunction[K,V, K_1,V_1]) -> DefaultFunctorDict[K_1, V_1]:
        self = type(self)({f(k,v) for k,v in self.items()})
        return self
    
# Concrete Functors ===================================================== #

class FList(List[A], DefaultFunctor): ...

class FTuple(Tuple[A], DefaultFunctor): ...

class FSet(Set[A], DefaultFunctor): ...

class FDeque(Deque[A], DefaultFunctor): ...
    
class FDict(Dict[K,V], DefaultFunctorDict): ...

class FOrderedDict(OrderedDict[K,V], DefaultFunctorDict): ...