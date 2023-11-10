from __future__ import annotations
from .functor import DefaultFunctor
from typing import Callable, Iterable, TypeVar, Tuple
from .definitions import SupportsFilter, SupportsZip, Foldable
from .folds import foldl, foldr, _initial_missing, _default_initial

A = TypeVar('A')
B = TypeVar('B')

class FunctionCastable:
    def cast_after(self, f: Callable) -> FunctionCastable:
        self = type(self)(f(self))
        return self
    
    @classmethod
    def cast(cls, x) -> FunctionCastable:
        return cls(x)
    
class DefaultFiltrable(SupportsFilter[A]):
    def filter(self, f: Callable) -> DefaultFiltrable:
        return type(self)(filter(f, self))
    
class DefaultZippable(SupportsZip[A]):
    def zip(self, *others: Iterable) -> DefaultZippable[Tuple]:
        return type(self)(zip(self, *others))

class DefaultMappable(DefaultFunctor[A]): ...

class DefaultZipMappable(DefaultZippable[A], DefaultMappable[A]):
    def zip_map(self, f, other = None) -> DefaultZipMappable[Tuple]:
        if other is not None:
            return self.zip(other.map(f))
        else:
            return self.zip(self.map(f))
        
    def zip_maps(self, *fs, keep=False):
        if keep:
            return type(self)( self.zip(*(self.map(f) for f in fs)) )
        else:
            return type(self)( zip(*(self.map(f) for f in fs)) )
        
class DefaultFoldable(Foldable[A]):
    def foldr(self, binop: Callable, initial=_default_initial):
        return foldr(binop, self, initial)
    
    def foldl(self, binop: Callable, initial=_default_initial):
        return foldl(binop, self, initial)
        

class ExtraFoldable(DefaultFoldable[A]):
    def sum(self) -> A:
        return sum(self)
    
    def prod(self) -> A:
        return self.foldl(lambda a,b: a*b)
    
    def max(self) -> A:
        return max(self)
    
    def min(self) -> A:
        return min(self)
    
class ExtraFiltrable(DefaultFiltrable[A]):
    def split_by(self, f: Callable[[A], bool]) -> Tuple[DefaultFiltrable[A]]:
        return (self.filter(f), self.filter(lambda x: not f(x)))
    
class ExtraFunctor(DefaultFunctor[A]):
    def split_map(self, f: Callable[[A], B]) -> Tuple[ExtraFunctor[A], ExtraFunctor[B]]:
        return (self, self.map(f))
    
    def split_maps(self, *fs: Callable) -> Tuple[ExtraFunctor]:
        return (self, *(self.map(f) for f in fs))