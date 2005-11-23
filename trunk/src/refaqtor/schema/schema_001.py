"""Refaqtor schema."""

# All Schevo schema modules must have these lines.
from schevo.schema import *
schevo.schema.prep(locals())

from schevo.icon.schema import SchevoIcon
class SchevoIcon(SchevoIcon): pass


