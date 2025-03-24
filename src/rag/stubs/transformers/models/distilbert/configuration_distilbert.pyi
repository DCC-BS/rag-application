"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping

from ...configuration_utils import PretrainedConfig
from ...onnx import OnnxConfig

"""DistilBERT model configuration"""
logger = ...

class DistilBertConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`DistilBertModel`] or a [`TFDistilBertModel`]. It
    is used to instantiate a DistilBERT model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the DistilBERT
    [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the DistilBERT model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`DistilBertModel`] or [`TFDistilBertModel`].
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        sinusoidal_pos_embds (`boolean`, *optional*, defaults to `False`):
            Whether to use sinusoidal positional embeddings.
        n_layers (`int`, *optional*, defaults to 6):
            Number of hidden layers in the Transformer encoder.
        n_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        dim (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        hidden_dim (`int`, *optional*, defaults to 3072):
            The size of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        activation (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        qa_dropout (`float`, *optional*, defaults to 0.1):
            The dropout probabilities used in the question answering model [`DistilBertForQuestionAnswering`].
        seq_classif_dropout (`float`, *optional*, defaults to 0.2):
            The dropout probabilities used in the sequence classification and the multiple choice model
            [`DistilBertForSequenceClassification`].

    Examples:

    ```python
    >>> from transformers import DistilBertConfig, DistilBertModel

    >>> # Initializing a DistilBERT configuration
    >>> configuration = DistilBertConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = DistilBertModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = ...
    attribute_map = ...
    def __init__(
        self,
        vocab_size=...,
        max_position_embeddings=...,
        sinusoidal_pos_embds=...,
        n_layers=...,
        n_heads=...,
        dim=...,
        hidden_dim=...,
        dropout=...,
        attention_dropout=...,
        activation=...,
        initializer_range=...,
        qa_dropout=...,
        seq_classif_dropout=...,
        pad_token_id=...,
        **kwargs,
    ) -> None: ...

class DistilBertOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...

__all__ = ["DistilBertConfig", "DistilBertOnnxConfig"]
