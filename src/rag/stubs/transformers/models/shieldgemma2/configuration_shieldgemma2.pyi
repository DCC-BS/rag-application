"""
This type stub file was generated by pyright.
"""

from ...configuration_utils import PretrainedConfig

logger = ...

class ShieldGemma2Config(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`ShieldGemma2ForImageClassification`]. It is used to instantiate an
    ShieldGemma2ForImageClassification according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the shieldgemma-2-4b-it.

    e.g. [google/gemma-3-4b](https://huggingface.co/google/gemma-3-4b)

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        text_config (`Union[ShieldGemma2TextConfig, dict]`, *optional*):
            The config object of the text backbone.
        vision_config (`Union[AutoConfig, dict]`,  *optional*):
            Custom vision config or dict.
        mm_tokens_per_image (`int`, *optional*, defaults to 256):
            The number of tokens per image embedding.
        boi_token_index (`int`, *optional*, defaults to 255999):
            The begin-of-image token index to wrap the image prompt.
        eoi_token_index (`int`, *optional*, defaults to 256000):
            The end-of-image token index to wrap the image prompt.
        image_token_index (`int`, *optional*, defaults to 262144):
            The image token index to encode the image prompt.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.


    Example:

    ```python
    >>> from transformers import ShieldGemma2ForConditionalGeneration, ShieldGemma2Config, SiglipVisionConfig, ShieldGemma2TextConfig

    >>> # Initializing a Siglip-like vision config
    >>> vision_config = SiglipVisionConfig()

    >>> # Initializing a ShieldGemma2 Text config
    >>> text_config = ShieldGemma2TextConfig()

    >>> # Initializing a ShieldGemma2 gemma-3-4b style configuration
    >>> configuration = ShieldGemma2Config(vision_config, text_config)

    >>> # Initializing a model from the gemma-3-4b style configuration
    >>> model = ShieldGemma2TextConfig(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = ...
    sub_configs = ...
    def __init__(
        self,
        text_config=...,
        vision_config=...,
        mm_tokens_per_image: int = ...,
        boi_token_index: int = ...,
        eoi_token_index: int = ...,
        image_token_index: int = ...,
        initializer_range: float = ...,
        **kwargs,
    ) -> None: ...

__all__ = ["ShieldGemma2Config"]
