"""
This type stub file was generated by pyright.
"""

from ...configuration_utils import PretrainedConfig

"""Switch Transformers model configuration"""
logger = ...

class SwitchTransformersConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`SwitchTransformersModel`]. It is used to
    instantiate a SwitchTransformers model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the
    SwitchTransformers [google/switch-base-8](https://huggingface.co/google/switch-base-8) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Arguments:
        vocab_size (`int`, *optional*, defaults to 32128):
            Vocabulary size of the SwitchTransformers model. Defines the number of different tokens that can be
            represented by the `inputs_ids` passed when calling [`SwitchTransformersModel`].
        d_model (`int`, *optional*, defaults to 768):
            Size of the encoder layers and the pooler layer.
        d_kv (`int`, *optional*, defaults to 64):
            Size of the key, query, value projections per attention head. `d_kv` has to be equal to `d_model //
            num_heads`.
        d_ff (`int`, *optional*, defaults to 2048):
            Size of the intermediate feed forward layer in each `SwitchTransformersBlock`.
        expert_capacity (`int`, *optional*, defaults to 64):
            Number of tokens that can be stored in each expert. If set to 1, the model will behave like a regular
            Transformer.
        num_layers (`int`, *optional*, defaults to 12):
            Number of dense hidden layers in the Transformer encoder layer.
        num_sparse_encoder_layers (`int`, *optional*, defaults to 3):
            Number of sparse (MoE) dense hidden layers in the Transformer encoder layer.
        num_decoder_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer decoder. Will use the same value as `num_layers` if not set.
        num_sparse_decoder_layers (`int`, *optional*, defaults to 3):
            Number of sparse (MoE) dense hidden layers in the Transformer decoder layer.
        num_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        num_experts (`int`, *optional*, defaults to 8):
            Number of experts for each SwitchTransformer layer.
        router_bias (`bool`, *optional*, defaults to `False`):
            Whether to add a bias to the router.
        router_jitter_noise (`float`, *optional*, defaults to 0.01):
            Amount of noise to add to the router.
        router_dtype (`str`, *optional*, default to `"float32"`):
            The `dtype` used for the routers. It is preferable to keep the `dtype` to `"float32"` as specified in the
            *selective precision* discussion in [the paper](https://arxiv.org/abs/2101.03961).
        router_ignore_padding_tokens (`bool`, *optional*, defaults to `False`):
            Whether to ignore padding tokens when routing.
        relative_attention_num_buckets (`int`, *optional*, defaults to 32):
            The number of buckets to use for each attention layer.
        relative_attention_max_distance (`int`, *optional*, defaults to 128):
            The maximum distance of the longer sequences for the bucket separation.
        dropout_rate (`float`, *optional*, defaults to 0.1):
            The ratio for all dropout layers.
        layer_norm_eps (`float`, *optional*, defaults to 1e-6):
            The epsilon used by the layer normalization layers.
        router_z_loss_coef (`float`, *optional*, defaults to 0.001):
            The z loss factor for the total loss.
        router_aux_loss_coef (`float`, *optional*, defaults to 0.001):
            The aux loss factor for the total loss.
        initializer_factor (`float`, *optional*, defaults to 1.0):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).
        dense_act_fn (`string`, *optional*, defaults to `"relu"`):
            Type of feed forward layer to be used. Should be one of `"relu"` or `"gated-gelu"`. SwitchTransformersv1.1
            uses the `"gated-gelu"` feed forward projection. Original SwitchTransformers uses `"relu"`.
        add_router_probs (`bool`, *optional*, defaults to `False`):
            Whether to output router probabilities to compute router auxiliary loss.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
    """

    model_type = ...
    keys_to_ignore_at_inference = ...
    attribute_map = ...
    def __init__(
        self,
        vocab_size=...,
        d_model=...,
        d_kv=...,
        d_ff=...,
        expert_capacity=...,
        num_layers=...,
        num_sparse_encoder_layers=...,
        num_decoder_layers=...,
        num_sparse_decoder_layers=...,
        num_heads=...,
        num_experts=...,
        router_bias=...,
        router_jitter_noise=...,
        router_dtype=...,
        router_ignore_padding_tokens=...,
        relative_attention_num_buckets=...,
        relative_attention_max_distance=...,
        dropout_rate=...,
        layer_norm_epsilon=...,
        router_z_loss_coef=...,
        router_aux_loss_coef=...,
        initializer_factor=...,
        dense_act_fn=...,
        is_encoder_decoder=...,
        add_router_probs=...,
        use_cache=...,
        pad_token_id=...,
        eos_token_id=...,
        **kwargs,
    ) -> None: ...

__all__ = ["SwitchTransformersConfig"]
