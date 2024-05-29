import numpy as np
from typing import Tuple
from colors import *

"""
Is it a floor? a wall? Can I see it?
"""
# Define color
color = Color()

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype([ # dtype creates a data type which Numpy can use, which behaves similarly to a struct in a language like C.

    ("ch", np.int32), # The character, represented in integer format. We’ll translate it from the integer into Unicode.
    ("fg", "3B"), # Foreground color, 3 unsigned bytes, for RGB colors.
    ("bg", "3B"), # Background color, -""- 
])

# Tile struct used for statically defined tile data.
tile_dt = np.dtype([
    ("walkable", bool), # True if this tile can be walked over.
    ("transparent", bool), # True if this tile doesn't block FOV.
    ("dark", graphic_dt), # Graphics for when this tile is not in FOV.
])

def new_tile(*, walkable: int, transparent: int, dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]) -> np.ndarray:
    # '*' Enforce the use of keywords, so that parameter order doesn't matter.
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(walkable=True, transparent=True, dark=(ord(" "), color.white, color.green_forest))
wall = new_tile(walkable=False, transparent=False, dark=(ord(" "), color.white, color.green_dark))

