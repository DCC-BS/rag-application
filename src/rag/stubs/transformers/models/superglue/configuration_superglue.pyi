"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING

from ...configuration_utils import PretrainedConfig
from ..superpoint import SuperPointConfig

if TYPE_CHECKING: ...
logger = ...

class SuperGlueConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`SuperGlueModel`]. It is used to instantiate a
    SuperGlue model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the SuperGlue
    [magic-leap-community/superglue_indoor](https://huggingface.co/magic-leap-community/superglue_indoor) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        keypoint_detector_config (`Union[AutoConfig, dict]`,  *optional*, defaults to `SuperPointConfig`):
            The config object or dictionary of the keypoint detector.
        hidden_size (`int`, *optional*, defaults to 256):
            The dimension of the descriptors.
        keypoint_encoder_sizes (`List[int]`, *optional*, defaults to `[32, 64, 128, 256]`):
            The sizes of the keypoint encoder layers.
        gnn_layers_types (`List[str]`, *optional*, defaults to `['self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross', 'self', 'cross']`):
            The types of the GNN layers. Must be either 'self' or 'cross'.
        num_attention_heads (`int`, *optional*, defaults to 4):
            The number of heads in the GNN layers.
        sinkhorn_iterations (`int`, *optional*, defaults to 100):
            The number of Sinkhorn iterations.
        matching_threshold (`float`, *optional*, defaults to 0.0):
            The matching threshold.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.

    Examples:
        ```python
        >>> from transformers import SuperGlueConfig, SuperGlueModel

        >>> # Initializing a SuperGlue superglue style configuration
        >>> configuration = SuperGlueConfig()

        >>> # Initializing a model from the superglue style configuration
        >>> model = SuperGlueModel(configuration)

        >>> # Accessing the model configuration
        >>> configuration = model.config
        ```
    """

    model_type = ...
    def __init__(
        self,
        keypoint_detector_config: SuperPointConfig = ...,
        hidden_size: int = ...,
        keypoint_encoder_sizes: list[int] = ...,
        gnn_layers_types: list[str] = ...,
        num_attention_heads: int = ...,
        sinkhorn_iterations: int = ...,
        matching_threshold: float = ...,
        initializer_range: float = ...,
        **kwargs,
    ) -> None: ...

__all__ = ["SuperGlueConfig"]
