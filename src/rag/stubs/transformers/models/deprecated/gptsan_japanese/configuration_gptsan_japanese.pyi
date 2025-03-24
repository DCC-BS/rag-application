"""
This type stub file was generated by pyright.
"""

from ....configuration_utils import PretrainedConfig

"""GPTSAN-japanese model configuration"""
logger = ...

class GPTSanJapaneseConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`GPTSanJapaneseModel`]. It is used to instantiate
    a GPTSANJapanese model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the GPTSANJapanese
    [Tanrei/GPTSAN-japanese](https://huggingface.co/Tanrei/GPTSAN-japanese) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Arguments:
        vocab_size (`int`, *optional*, defaults to 36000):
            Vocabulary size of the GPTSANJapanese model. Defines the number of different tokens that can be represented
            by the `inputs_ids` passed when calling [`GPTSanJapaneseModel`].
        max_position_embeddings (`int`, *optional*, defaults to 1280):
            The maximum sequence length that this model might ever be used with. Defaults set this to 1280.
        d_model (`int`, *optional*, defaults to 1024):
            Size of the encoder layers and the pooler layer.
        d_ff (`int`, *optional*, defaults to 8192):
            Size of the intermediate feed forward layer in each `SwitchTransformersBlock`.
        d_ext (`int`, *optional*, defaults to 4096):
            Size of the intermediate feed forward layer in each Extra-layers.
        d_spout (`int`, *optional*, defaults to 128):
            Size of the `spout` vector.
        num_switch_layers (`int`, *optional*, defaults to 10):
            Number of layers in the Switch Transformer layer.
        num_ext_layers (`int`, *optional*, defaults to 0):
            Number of layers in the Extra-layers.
        num_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        num_experts (`int`, *optional*, defaults to 16):
            Number of experts for each SwitchTransformer layer.
        expert_capacity (`int`, *optional*, defaults to 128):
            Number of tokens that can be stored in each expert. If set to 1, the model will behave like a regular
            Transformer.
        dropout_rate (`float`, *optional*, defaults to 0.0):
            The ratio for all dropout layers.
        layer_norm_eps (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization layers.
        router_bias (`bool`, *optional*, defaults to `False`):
            Whether to add a bias to the router.
        router_jitter_noise (`float`, *optional*, defaults to 0.0):
            Amount of noise to add to the router. Set it to 0.0 during prediction or set small value (usually 1e-2)
            during training.
        router_dtype (`str`, *optional*, default to `"float32"`):
            The `dtype` used for the routers. It is preferable to keep the `dtype` to `"float32"` as specified in the
            *selective precision* discussion in [the paper](https://arxiv.org/abs/2101.03961).
        router_ignore_padding_tokens (`bool`, *optional*, defaults to `False`):
            Whether to ignore padding tokens when routing.
        output_hidden_states (`bool`, *optional*, default to `False`):
            Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors for
            more detail.
        output_attentions (`bool`, *optional*, defaults to `False`):
            Whether or not to return the attentions tensors of all attention layers.
        initializer_factor (`float`, *optional*, defaults to 0.002):
            A factor for initializing all weight matrices.
        output_router_logits (`bool`, *optional*, default to `False`):
            Whether or not to return the router logits of all experts.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models)
    """

    model_type = ...
    keys_to_ignore_at_inference = ...
    attribute_map = ...
    def __init__(
        self,
        vocab_size=...,
        max_position_embeddings=...,
        d_model=...,
        d_ff=...,
        d_ext=...,
        d_spout=...,
        num_switch_layers=...,
        num_ext_layers=...,
        num_heads=...,
        num_experts=...,
        expert_capacity=...,
        dropout_rate=...,
        layer_norm_epsilon=...,
        router_bias=...,
        router_jitter_noise=...,
        router_dtype=...,
        router_ignore_padding_tokens=...,
        output_hidden_states=...,
        output_attentions=...,
        initializer_factor=...,
        output_router_logits=...,
        use_cache=...,
        separator_token_id=...,
        pad_token_id=...,
        eos_token_id=...,
        **kwargs,
    ) -> None: ...
