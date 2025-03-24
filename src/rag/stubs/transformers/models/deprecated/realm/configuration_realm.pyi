"""
This type stub file was generated by pyright.
"""

from ....configuration_utils import PretrainedConfig

"""REALM model configuration."""
logger = ...

class RealmConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of

    1. [`RealmEmbedder`]
    2. [`RealmScorer`]
    3. [`RealmKnowledgeAugEncoder`]
    4. [`RealmRetriever`]
    5. [`RealmReader`]
    6. [`RealmForOpenQA`]

    It is used to instantiate an REALM model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the REALM
    [google/realm-cc-news-pretrained-embedder](https://huggingface.co/google/realm-cc-news-pretrained-embedder)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the REALM model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`RealmEmbedder`], [`RealmScorer`], [`RealmKnowledgeAugEncoder`], or
            [`RealmReader`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimension of the encoder layers and the pooler layer.
        retriever_proj_size (`int`, *optional*, defaults to 128):
            Dimension of the retriever(embedder) projection.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        num_candidates (`int`, *optional*, defaults to 8):
            Number of candidates inputted to the RealmScorer or RealmKnowledgeAugEncoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu_new"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`RealmEmbedder`], [`RealmScorer`],
            [`RealmKnowledgeAugEncoder`], or [`RealmReader`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        span_hidden_size (`int`, *optional*, defaults to 256):
            Dimension of the reader's spans.
        max_span_width (`int`, *optional*, defaults to 10):
            Max span width of the reader.
        reader_layer_norm_eps (`float`, *optional*, defaults to 1e-3):
            The epsilon used by the reader's layer normalization layers.
        reader_beam_size (`int`, *optional*, defaults to 5):
            Beam size of the reader.
        reader_seq_len (`int`, *optional*, defaults to 288+32):
            Maximum sequence length of the reader.
        num_block_records (`int`, *optional*, defaults to 13353718):
            Number of block records.
        searcher_beam_size (`int`, *optional*, defaults to 5000):
            Beam size of the searcher. Note that when eval mode is enabled, *searcher_beam_size* will be the same as
            *reader_beam_size*.

    Example:

    ```python
    >>> from transformers import RealmConfig, RealmEmbedder

    >>> # Initializing a REALM realm-cc-news-pretrained-* style configuration
    >>> configuration = RealmConfig()

    >>> # Initializing a model (with random weights) from the google/realm-cc-news-pretrained-embedder style configuration
    >>> model = RealmEmbedder(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = ...
    def __init__(
        self,
        vocab_size=...,
        hidden_size=...,
        retriever_proj_size=...,
        num_hidden_layers=...,
        num_attention_heads=...,
        num_candidates=...,
        intermediate_size=...,
        hidden_act=...,
        hidden_dropout_prob=...,
        attention_probs_dropout_prob=...,
        max_position_embeddings=...,
        type_vocab_size=...,
        initializer_range=...,
        layer_norm_eps=...,
        span_hidden_size=...,
        max_span_width=...,
        reader_layer_norm_eps=...,
        reader_beam_size=...,
        reader_seq_len=...,
        num_block_records=...,
        searcher_beam_size=...,
        pad_token_id=...,
        bos_token_id=...,
        eos_token_id=...,
        **kwargs,
    ) -> None: ...
