"""Extension of the dict class.

adds a coalesce method
"""

from typing import Any


class ExtenDict(dict):
    """Docstring for ExtenDict."""

    def coalesce(self, key: Any, default: Any = None) -> Any:
        """Returns the default value even when the key exists and is None."""
        return self.get(key) or default
