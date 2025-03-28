"""
This type stub file was generated by pyright.
"""

from ctypes import c_float
from enum import Enum
from typing import TYPE_CHECKING

from .. import AutoFeatureExtractor, AutoProcessor, AutoTokenizer

if TYPE_CHECKING: ...

class ParameterFormat(Enum):
    Float = c_float
    @property
    def size(self) -> int:
        """
        Number of byte required for this data type

        Returns:
            Integer > 0
        """
        ...

def compute_effective_axis_dimension(dimension: int, fixed_dimension: int, num_token_to_add: int = ...) -> int:
    """

    Args:
        dimension:
        fixed_dimension:
        num_token_to_add:

    Returns:

    """
    ...

def compute_serialized_parameters_size(num_parameters: int, dtype: ParameterFormat) -> int:
    """
    Compute the size taken by all the parameters in the given the storage format when serializing the model

    Args:
        num_parameters: Number of parameters to be saved
        dtype: The data format each parameter will be saved

    Returns:
        Size (in byte) taken to save all the parameters
    """
    ...

def get_preprocessor(model_name: str) -> AutoTokenizer | AutoFeatureExtractor | AutoProcessor | None:
    """
    Gets a preprocessor (tokenizer, feature extractor or processor) that is available for `model_name`.

    Args:
        model_name (`str`): Name of the model for which a preprocessor are loaded.

    Returns:
        `Optional[Union[AutoTokenizer, AutoFeatureExtractor, AutoProcessor]]`:
            If a processor is found, it is returned. Otherwise, if a tokenizer or a feature extractor exists, it is
            returned. If both a tokenizer and a feature extractor exist, an error is raised. The function returns
            `None` if no preprocessor is found.
    """
    ...
