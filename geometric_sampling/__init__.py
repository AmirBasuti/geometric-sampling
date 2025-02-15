from importlib import metadata

from .design import Design
from . import criteria
from . import search
from . import method
from . import clustering
from . import random
from . import measure


__version__ = metadata.version("geometric_sampling")

__all__ = ["Design", "criteria", "search", "method", "clustering", "random", "measure"]
