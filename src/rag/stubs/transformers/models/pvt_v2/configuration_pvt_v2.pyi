"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable

from ...configuration_utils import PretrainedConfig
from ...utils.backbone_utils import BackboneConfigMixin

"""Pvt V2 model configuration"""
logger = ...

class PvtV2Config(BackboneConfigMixin, PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`PvtV2Model`]. It is used to instantiate a Pvt V2
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the Pvt V2 B0
    [OpenGVLab/pvt_v2_b0](https://huggingface.co/OpenGVLab/pvt_v2_b0) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        image_size (`Union[int, Tuple[int, int]]`, *optional*, defaults to 224):
            The input image size. Pass int value for square image, or tuple of (height, width).
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        num_encoder_blocks (`[int]`, *optional*, defaults to 4):
            The number of encoder blocks (i.e. stages in the Mix Transformer encoder).
        depths (`List[int]`, *optional*, defaults to `[2, 2, 2, 2]`):
            The number of layers in each encoder block.
        sr_ratios (`List[int]`, *optional*, defaults to `[8, 4, 2, 1]`):
            Spatial reduction ratios in each encoder block.
        hidden_sizes (`List[int]`, *optional*, defaults to `[32, 64, 160, 256]`):
            Dimension of each of the encoder blocks.
        patch_sizes (`List[int]`, *optional*, defaults to `[7, 3, 3, 3]`):
            Patch size for overlapping patch embedding before each encoder block.
        strides (`List[int]`, *optional*, defaults to `[4, 2, 2, 2]`):
            Stride for overlapping patch embedding before each encoder block.
        num_attention_heads (`List[int]`, *optional*, defaults to `[1, 2, 5, 8]`):
            Number of attention heads for each attention layer in each block of the Transformer encoder.
        mlp_ratios (`List[int]`, *optional*, defaults to `[8, 8, 4, 4]`):
            Ratio of the size of the hidden layer compared to the size of the input layer of the Mix FFNs in the
            encoder blocks.
        hidden_act (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        drop_path_rate (`float`, *optional*, defaults to 0.0):
            The dropout probability for stochastic depth, used in the blocks of the Transformer encoder.
        layer_norm_eps (`float`, *optional*, defaults to 1e-06):
            The epsilon used by the layer normalization layers.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether or not a learnable bias should be added to the queries, keys and values.
        linear_attention (`bool`, *optional*, defaults to `False`):
            Use linear attention complexity. If set to True, `sr_ratio` is ignored and average pooling is used for
            dimensionality reduction in the attention layers rather than strided convolution.
        out_features (`List[str]`, *optional*):
            If used as backbone, list of features to output. Can be any of `"stem"`, `"stage1"`, `"stage2"`, etc.
            (depending on how many stages the model has). If unset and `out_indices` is set, will default to the
            corresponding stages. If unset and `out_indices` is unset, will default to the last stage.
        out_indices (`List[int]`, *optional*):
            If used as backbone, list of indices of features to output. Can be any of 0, 1, 2, etc. (depending on how
            many stages the model has). If unset and `out_features` is set, will default to the corresponding stages.
            If unset and `out_features` is unset, will default to the last stage.
    Example:

    ```python
    >>> from transformers import PvtV2Model, PvtV2Config

    >>> # Initializing a pvt_v2_b0 style configuration
    >>> configuration = PvtV2Config()

    >>> # Initializing a model from the OpenGVLab/pvt_v2_b0 style configuration
    >>> model = PvtV2Model(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = ...
    def __init__(
        self,
        image_size: int | tuple[int, int] = ...,
        num_channels: int = ...,
        num_encoder_blocks: int = ...,
        depths: list[int] = ...,
        sr_ratios: list[int] = ...,
        hidden_sizes: list[int] = ...,
        patch_sizes: list[int] = ...,
        strides: list[int] = ...,
        num_attention_heads: list[int] = ...,
        mlp_ratios: list[int] = ...,
        hidden_act: str | Callable = ...,
        hidden_dropout_prob: float = ...,
        attention_probs_dropout_prob: float = ...,
        initializer_range: float = ...,
        drop_path_rate: float = ...,
        layer_norm_eps: float = ...,
        qkv_bias: bool = ...,
        linear_attention: bool = ...,
        out_features=...,
        out_indices=...,
        **kwargs,
    ) -> None: ...

__all__ = ["PvtV2Config"]
