"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING

from torch import nn

if TYPE_CHECKING: ...

def is_fsdp_managed_module(module: nn.Module) -> bool: ...
