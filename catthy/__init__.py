from .definitions import *
from .folds import *

from .functor import *
from .applicative import *
from .extra import *
from .util import *

from collections import deque

@translate({'of': 'de'})
class tupla(DefaultApplicative, ExtraFunctor, DefaultZipMappable, ExtraFoldable, ExtraFiltrable, tuple) : ...

@translate({'of': 'de'})
class lista(DefaultApplicative, ExtraFunctor, DefaultZipMappable, ExtraFoldable, ExtraFiltrable, list): ...

@translate({'of': 'de',
            'popleft': 'desencolar'})
class cola(DefaultApplicative, ExtraFunctor, DefaultZipMappable, ExtraFoldable, ExtraFiltrable, deque) : ...

@translate({'of': 'de',
            'pop': 'desapilar'})
class pila(DefaultApplicative, ExtraFunctor, DefaultZipMappable, ExtraFoldable, ExtraFiltrable, deque) : ...

@translate({'of': 'de'})
class conjunto(DefaultApplicative, ExtraFunctor, DefaultZipMappable, ExtraFoldable, ExtraFiltrable, NaiveHashable, set): ...

