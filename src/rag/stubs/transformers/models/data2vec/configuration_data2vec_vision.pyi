"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping

from ...configuration_utils import PretrainedConfig
from ...onnx import OnnxConfig

"""Data2VecVision model configuration"""
logger = ...

class Data2VecVisionConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`Data2VecVisionModel`]. It is used to instantiate
    an Data2VecVision model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the Data2VecVision
    [facebook/data2vec-vision-base](https://huggingface.co/facebook/data2vec-vision-base) architecture.

    Args:
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        image_size (`int`, *optional*, defaults to 224):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 16):
            The size (resolution) of each patch.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        use_mask_token (`bool`, *optional*, defaults to `False`):
            Whether to use a mask token for masked image modeling.
        use_absolute_position_embeddings (`bool`, *optional*, defaults to `False`):
            Whether to use BERT-style absolute position embeddings.
        use_relative_position_bias (`bool`, *optional*, defaults to `False`):
            Whether to use T5-style relative position embeddings in the self-attention layers.
        use_shared_relative_position_bias (`bool`, *optional*, defaults to `False`):
            Whether to use the same relative position embeddings across all self-attention layers of the Transformer.
        layer_scale_init_value (`float`, *optional*, defaults to 0.1):
            Scale to use in the self-attention layers. 0.1 for base, 1e-5 for large. Set 0 to disable layer scale.
        drop_path_rate (`float`, *optional*, defaults to 0.1):
            Stochastic depth rate per sample (when applied in the main path of residual layers).
        use_mean_pooling (`bool`, *optional*, defaults to `True`):
            Whether to mean pool the final hidden states of the patches instead of using the final hidden state of the
            CLS token, before applying the classification head.
        out_indices (`List[int]`, *optional*, defaults to `[3, 5, 7, 11]`):
            Indices of the feature maps to use for semantic segmentation.
        pool_scales (`Tuple[int]`, *optional*, defaults to `[1, 2, 3, 6]`):
            Pooling scales used in Pooling Pyramid Module applied on the last feature map.
        use_auxiliary_head (`bool`, *optional*, defaults to `True`):
            Whether to use an auxiliary head during training.
        auxiliary_loss_weight (`float`, *optional*, defaults to 0.4):
            Weight of the cross-entropy loss of the auxiliary head.
        auxiliary_channels (`int`, *optional*, defaults to 256):
            Number of channels to use in the auxiliary head.
        auxiliary_num_convs (`int`, *optional*, defaults to 1):
            Number of convolutional layers to use in the auxiliary head.
        auxiliary_concat_input (`bool`, *optional*, defaults to `False`):
            Whether to concatenate the output of the auxiliary head with the input before the classification layer.
        semantic_loss_ignore_index (`int`, *optional*, defaults to 255):
            The index that is ignored by the loss function of the semantic segmentation model.

    Example:

    ```python
    >>> from transformers import Data2VecVisionConfig, Data2VecVisionModel

    >>> # Initializing a Data2VecVision data2vec_vision-base-patch16-224-in22k style configuration
    >>> configuration = Data2VecVisionConfig()

    >>> # Initializing a model (with random weights) from the data2vec_vision-base-patch16-224-in22k style configuration
    >>> model = Data2VecVisionModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = ...
    def __init__(
        self,
        hidden_size=...,
        num_hidden_layers=...,
        num_attention_heads=...,
        intermediate_size=...,
        hidden_act=...,
        hidden_dropout_prob=...,
        attention_probs_dropout_prob=...,
        initializer_range=...,
        layer_norm_eps=...,
        image_size=...,
        patch_size=...,
        num_channels=...,
        use_mask_token=...,
        use_absolute_position_embeddings=...,
        use_relative_position_bias=...,
        use_shared_relative_position_bias=...,
        layer_scale_init_value=...,
        drop_path_rate=...,
        use_mean_pooling=...,
        out_indices=...,
        pool_scales=...,
        use_auxiliary_head=...,
        auxiliary_loss_weight=...,
        auxiliary_channels=...,
        auxiliary_num_convs=...,
        auxiliary_concat_input=...,
        semantic_loss_ignore_index=...,
        **kwargs,
    ) -> None: ...

class Data2VecVisionOnnxConfig(OnnxConfig):
    torch_onnx_minimum_version = ...
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float: ...

__all__ = ["Data2VecVisionConfig", "Data2VecVisionOnnxConfig"]
