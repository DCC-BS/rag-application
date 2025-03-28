"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping

from ...configuration_utils import PretrainedConfig
from ...onnx import OnnxConfig

"""MobileViT model configuration"""
logger = ...

class MobileViTConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`MobileViTModel`]. It is used to instantiate a
    MobileViT model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the MobileViT
    [apple/mobilevit-small](https://huggingface.co/apple/mobilevit-small) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        image_size (`int`, *optional*, defaults to 256):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 2):
            The size (resolution) of each patch.
        hidden_sizes (`List[int]`, *optional*, defaults to `[144, 192, 240]`):
            Dimensionality (hidden size) of the Transformer encoders at each stage.
        neck_hidden_sizes (`List[int]`, *optional*, defaults to `[16, 32, 64, 96, 128, 160, 640]`):
            The number of channels for the feature maps of the backbone.
        num_attention_heads (`int`, *optional*, defaults to 4):
            Number of attention heads for each attention layer in the Transformer encoder.
        mlp_ratio (`float`, *optional*, defaults to 2.0):
            The ratio of the number of channels in the output of the MLP to the number of channels in the input.
        expand_ratio (`float`, *optional*, defaults to 4.0):
            Expansion factor for the MobileNetv2 layers.
        hidden_act (`str` or `function`, *optional*, defaults to `"silu"`):
            The non-linear activation function (function or string) in the Transformer encoder and convolution layers.
        conv_kernel_size (`int`, *optional*, defaults to 3):
            The size of the convolutional kernel in the MobileViT layer.
        output_stride (`int`, *optional*, defaults to 32):
            The ratio of the spatial resolution of the output to the resolution of the input image.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the Transformer encoder.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        classifier_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for attached classifiers.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon used by the layer normalization layers.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        aspp_out_channels (`int`, *optional*, defaults to 256):
            Number of output channels used in the ASPP layer for semantic segmentation.
        atrous_rates (`List[int]`, *optional*, defaults to `[6, 12, 18]`):
            Dilation (atrous) factors used in the ASPP layer for semantic segmentation.
        aspp_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the ASPP layer for semantic segmentation.
        semantic_loss_ignore_index (`int`, *optional*, defaults to 255):
            The index that is ignored by the loss function of the semantic segmentation model.

    Example:

    ```python
    >>> from transformers import MobileViTConfig, MobileViTModel

    >>> # Initializing a mobilevit-small style configuration
    >>> configuration = MobileViTConfig()

    >>> # Initializing a model from the mobilevit-small style configuration
    >>> model = MobileViTModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = ...
    def __init__(
        self,
        num_channels=...,
        image_size=...,
        patch_size=...,
        hidden_sizes=...,
        neck_hidden_sizes=...,
        num_attention_heads=...,
        mlp_ratio=...,
        expand_ratio=...,
        hidden_act=...,
        conv_kernel_size=...,
        output_stride=...,
        hidden_dropout_prob=...,
        attention_probs_dropout_prob=...,
        classifier_dropout_prob=...,
        initializer_range=...,
        layer_norm_eps=...,
        qkv_bias=...,
        aspp_out_channels=...,
        atrous_rates=...,
        aspp_dropout_prob=...,
        semantic_loss_ignore_index=...,
        **kwargs,
    ) -> None: ...

class MobileViTOnnxConfig(OnnxConfig):
    torch_onnx_minimum_version = ...
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float: ...

__all__ = ["MobileViTConfig", "MobileViTOnnxConfig"]
