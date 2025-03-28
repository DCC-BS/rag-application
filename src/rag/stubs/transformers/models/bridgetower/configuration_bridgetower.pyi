"""
This type stub file was generated by pyright.
"""

from ...configuration_utils import PretrainedConfig

"""BridgeTower model configuration"""
logger = ...

class BridgeTowerVisionConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the vision configuration of a [`BridgeTowerModel`]. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the bridgetower-base
    [BridgeTower/bridgetower-base](https://huggingface.co/BridgeTower/bridgetower-base/) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in visual encoder model.
        patch_size (`int`, *optional*, defaults to 16):
            The size (resolution) of each patch.
        image_size (`int`, *optional*, defaults to 288):
            The size (resolution) of each image.
        initializer_factor (`float`, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).
        layer_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon used by the layer normalization layers.
        stop_gradient (`bool`, *optional*, defaults to `False`):
            Whether to stop gradient for training.
        share_layernorm (`bool`, *optional*, defaults to `True`):
            Whether LayerNorm layers are shared.
        remove_last_layer (`bool`, *optional*, defaults to `False`):
            Whether to remove the last layer from the vision encoder.


    Example:

    ```python
    >>> from transformers import BridgeTowerVisionConfig

    >>> # Initializing a BridgeTower BridgeTower/bridgetower-base style configuration for the vision model
    >>> configuration = BridgeTowerVisionConfig()

    >>> # Accessing the configuration
    >>> configuration
    ```"""

    model_type = ...
    base_config_key = ...
    def __init__(
        self,
        hidden_size=...,
        num_hidden_layers=...,
        num_channels=...,
        patch_size=...,
        image_size=...,
        initializer_factor=...,
        layer_norm_eps=...,
        stop_gradient=...,
        share_layernorm=...,
        remove_last_layer=...,
        **kwargs,
    ) -> None: ...

class BridgeTowerTextConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the text configuration of a [`BridgeTowerModel`]. The default values here
    are copied from RoBERTa. Instantiating a configuration with the defaults will yield a similar configuration to that
    of the bridgetower-base [BridegTower/bridgetower-base](https://huggingface.co/BridgeTower/bridgetower-base/)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 50265):
            Vocabulary size of the text part of the model. Defines the number of different tokens that can be
            represented by the `inputs_ids` passed when calling [`BridgeTowerModel`].
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
        max_position_embeddings (`int`, *optional*, defaults to 514):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids`.
        initializer_factor (`float`, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).
        layer_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon used by the layer normalization layers.
        position_embedding_type (`str`, *optional*, defaults to `"absolute"`):
            Type of position embedding. Choose one of `"absolute"`, `"relative_key"`, `"relative_key_query"`. For
            positional embeddings use `"absolute"`. For more information on `"relative_key"`, please refer to
            [Self-Attention with Relative Position Representations (Shaw et al.)](https://arxiv.org/abs/1803.02155).
            For more information on `"relative_key_query"`, please refer to *Method 4* in [Improve Transformer Models
            with Better Relative Position Embeddings (Huang et al.)](https://arxiv.org/abs/2009.13658).
        is_decoder (`bool`, *optional*, defaults to `False`):
            Whether the model is used as a decoder or not. If `False`, the model is used as an encoder.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.

    Example:

    ```python
    >>> from transformers import BridgeTowerTextConfig

    >>> # Initializing a BridgeTower BridgeTower/bridgetower-base style configuration for the text model
    >>> configuration = BridgeTowerTextConfig()

    >>> # Accessing the configuration
    >>> configuration
    ```"""

    model_type = ...
    base_config_key = ...
    def __init__(
        self,
        vocab_size=...,
        hidden_size=...,
        num_hidden_layers=...,
        num_attention_heads=...,
        initializer_factor=...,
        intermediate_size=...,
        hidden_act=...,
        hidden_dropout_prob=...,
        attention_probs_dropout_prob=...,
        max_position_embeddings=...,
        type_vocab_size=...,
        layer_norm_eps=...,
        pad_token_id=...,
        bos_token_id=...,
        eos_token_id=...,
        position_embedding_type=...,
        use_cache=...,
        **kwargs,
    ) -> None: ...

class BridgeTowerConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`BridgeTowerModel`]. It is used to instantiate a
    BridgeTower model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the bridgetower-base
    [BridgeTower/bridgetower-base](https://huggingface.co/BridgeTower/bridgetower-base/) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        share_cross_modal_transformer_layers (`bool`, *optional*, defaults to `True`):
            Whether cross modal transformer layers are shared.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler.
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        initializer_factor (`float`, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).
        layer_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon used by the layer normalization layers.
        share_link_tower_layers (`bool`, *optional*, defaults to `False`):
            Whether the bride/link tower layers are shared.
        link_tower_type (`str`, *optional*, defaults to `"add"`):
            Type of the bridge/link layer.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        num_hidden_layers (`int`, *optional*, defaults to 6):
            Number of hidden layers in the Transformer encoder.
        tie_word_embeddings (`bool`, *optional*, defaults to `False`):
            Whether to tie input and output embeddings.
        init_layernorm_from_vision_encoder (`bool`, *optional*, defaults to `False`):
            Whether to init LayerNorm from the vision encoder.
        text_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`BridgeTowerTextConfig`].
        vision_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`BridgeTowerVisionConfig`].

    Example:

    ```python
    >>> from transformers import BridgeTowerModel, BridgeTowerConfig

    >>> # Initializing a BridgeTower BridgeTower/bridgetower-base style configuration
    >>> configuration = BridgeTowerConfig()

    >>> # Initializing a model from the BridgeTower/bridgetower-base style configuration
    >>> model = BridgeTowerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = ...
    sub_configs = ...
    def __init__(
        self,
        share_cross_modal_transformer_layers=...,
        hidden_act=...,
        hidden_size=...,
        initializer_factor=...,
        layer_norm_eps=...,
        share_link_tower_layers=...,
        link_tower_type=...,
        num_attention_heads=...,
        num_hidden_layers=...,
        tie_word_embeddings=...,
        init_layernorm_from_vision_encoder=...,
        text_config=...,
        vision_config=...,
        **kwargs,
    ) -> None: ...
    @classmethod
    def from_text_vision_configs(
        cls, text_config: BridgeTowerTextConfig, vision_config: BridgeTowerVisionConfig, **kwargs
    ):  # -> Self:
        r"""
        Instantiate a [`BridgeTowerConfig`] (or a derived class) from BridgeTower text model configuration. Returns:
            [`BridgeTowerConfig`]: An instance of a configuration object
        """
        ...

__all__ = ["BridgeTowerConfig", "BridgeTowerTextConfig", "BridgeTowerVisionConfig"]
