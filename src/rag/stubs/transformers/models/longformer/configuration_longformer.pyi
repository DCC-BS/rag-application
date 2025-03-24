"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from ...configuration_utils import PretrainedConfig
from ...onnx import OnnxConfig
from ...onnx.config import PatchingSpec
from ...tokenization_utils_base import PreTrainedTokenizerBase
from ...utils import TensorType

"""Longformer configuration"""
if TYPE_CHECKING: ...
logger = ...

class LongformerConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`LongformerModel`] or a [`TFLongformerModel`]. It
    is used to instantiate a Longformer model according to the specified arguments, defining the model architecture.

    This is the configuration class to store the configuration of a [`LongformerModel`]. It is used to instantiate an
    Longformer model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the LongFormer
    [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) architecture with a sequence
    length 4,096.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the Longformer model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`LongformerModel`] or [`TFLongformerModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`LongformerModel`] or
            [`TFLongformerModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        attention_window (`int` or `List[int]`, *optional*, defaults to 512):
            Size of an attention window around each token. If an `int`, use the same size for all layers. To specify a
            different window size for each layer, use a `List[int]` where `len(attention_window) == num_hidden_layers`.

    Example:

    ```python
    >>> from transformers import LongformerConfig, LongformerModel

    >>> # Initializing a Longformer configuration
    >>> configuration = LongformerConfig()

    >>> # Initializing a model from the configuration
    >>> model = LongformerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = ...
    def __init__(
        self,
        attention_window: list[int] | int = ...,
        sep_token_id: int = ...,
        pad_token_id: int = ...,
        bos_token_id: int = ...,
        eos_token_id: int = ...,
        vocab_size: int = ...,
        hidden_size: int = ...,
        num_hidden_layers: int = ...,
        num_attention_heads: int = ...,
        intermediate_size: int = ...,
        hidden_act: str = ...,
        hidden_dropout_prob: float = ...,
        attention_probs_dropout_prob: float = ...,
        max_position_embeddings: int = ...,
        type_vocab_size: int = ...,
        initializer_range: float = ...,
        layer_norm_eps: float = ...,
        onnx_export: bool = ...,
        **kwargs,
    ) -> None:
        """Constructs LongformerConfig."""
        ...

class LongformerOnnxConfig(OnnxConfig):
    def __init__(self, config: PretrainedConfig, task: str = ..., patching_specs: list[PatchingSpec] = ...) -> None: ...
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float:
        """
        What absolute tolerance value to use during model conversion validation.

        Returns:
            Float absolute tolerance value.
        """
        ...

    @property
    def default_onnx_opset(self) -> int: ...
    def generate_dummy_inputs(
        self,
        tokenizer: PreTrainedTokenizerBase,
        batch_size: int = ...,
        seq_length: int = ...,
        is_pair: bool = ...,
        framework: TensorType | None = ...,
    ) -> Mapping[str, Any]: ...

__all__ = ["LongformerConfig", "LongformerOnnxConfig"]
