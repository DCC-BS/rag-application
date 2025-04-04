"""
This type stub file was generated by pyright.
"""

import os

import flax.linen as nn
import jax
import jax.numpy as jnp
from flax.core.frozen_dict import FrozenDict
from jax.random import PRNGKey

from ...modeling_flax_outputs import FlaxBaseModelOutput, FlaxCausalLMOutputWithCrossAttentions, FlaxSeq2SeqLMOutput
from ...modeling_flax_utils import FlaxPreTrainedModel
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_speech_encoder_decoder import SpeechEncoderDecoderConfig

"""Classes to support Flax Speech-Encoder-Decoder architectures"""
logger = ...
_CONFIG_FOR_DOC = ...
SPEECH_ENCODER_DECODER_START_DOCSTRING = ...
SPEECH_ENCODER_DECODER_INPUTS_DOCSTRING = ...
SPEECH_ENCODER_DECODER_ENCODE_INPUTS_DOCSTRING = ...
SPEECH_ENCODER_DECODER_DECODE_INPUTS_DOCSTRING = ...

class FlaxSpeechEncoderDecoderModule(nn.Module):
    config: SpeechEncoderDecoderConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        inputs,
        attention_mask,
        decoder_input_ids,
        decoder_attention_mask,
        decoder_position_ids,
        encoder_outputs=...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
        deterministic: bool = ...,
        freeze_feature_encoder: bool = ...,
    ):  # -> Any | FlaxSeq2SeqLMOutput:
        ...

@add_start_docstrings(SPEECH_ENCODER_DECODER_START_DOCSTRING)
class FlaxSpeechEncoderDecoderModel(FlaxPreTrainedModel):
    r"""
    [`FlaxSpeechEncoderDecoderModel`] is a generic model class that will be instantiated as a transformer architecture
    with the module (flax.nn.Module) of one of the base model classes of the library as encoder module and another one
    as decoder module when created with the :meth*~transformers.FlaxAutoModel.from_pretrained* class method for the
    encoder and :meth*~transformers.FlaxAutoModelForCausalLM.from_pretrained* class method for the decoder.
    """

    config_class = SpeechEncoderDecoderConfig
    base_model_prefix: str = ...
    module_class = FlaxSpeechEncoderDecoderModule
    def __init__(
        self,
        config: SpeechEncoderDecoderConfig,
        input_shape: tuple | None = ...,
        seed: int = ...,
        dtype: jnp.dtype = ...,
        _do_init: bool = ...,
        **kwargs,
    ) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: tuple, params: FrozenDict = ...) -> FrozenDict: ...
    def init_cache(self, batch_size, max_length, encoder_outputs):
        r"""
        Args:
            batch_size (`int`):
                batch_size used for fast auto-regressive decoding. Defines the batch size of the initialized cache.
            max_length (`int`):
                maximum possible length for auto-regressive decoding. Defines the sequence length of the initialized
                cache.
            encoder_outputs (`Union[FlaxBaseModelOutput, tuple(tuple(jnp.ndarray)]`):
                `encoder_outputs` consists of (`last_hidden_state`, *optional*: `hidden_states`, *optional*:
                `attentions`). `last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, *optional*)
                is a sequence of hidden-states at the output of the last layer of the encoder. Used in the
                cross-attention of the decoder.
        """
        ...

    @add_start_docstrings(SPEECH_ENCODER_DECODER_ENCODE_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=FlaxBaseModelOutput, config_class=_CONFIG_FOR_DOC)
    def encode(
        self,
        inputs: jnp.ndarray,
        attention_mask: jnp.ndarray | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        train: bool = ...,
        freeze_feature_encoder: bool = ...,
        params: dict = ...,
        dropout_rng: PRNGKey = ...,
    ):  # -> FlaxBaseModelOutput:
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import FlaxSpeechEncoderDecoderModel

        >>> # initialize a wav2vec2-2-bart from pretrained wav2vec2 and bart models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxSpeechEncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "facebook/wav2vec2-large-lv60", "facebook/bart-large"
        ... )

        >>> inputs = jnp.ones((2, 5000), dtype=jnp.float32)
        >>> encoder_outputs = model.encode(inputs)
        ```"""
        ...

    @add_start_docstrings(SPEECH_ENCODER_DECODER_DECODE_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=FlaxCausalLMOutputWithCrossAttentions, config_class=_CONFIG_FOR_DOC)
    def decode(
        self,
        decoder_input_ids,
        encoder_outputs,
        encoder_attention_mask: jnp.ndarray | None = ...,
        decoder_attention_mask: jnp.ndarray | None = ...,
        decoder_position_ids: jnp.ndarray | None = ...,
        past_key_values: dict = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        train: bool = ...,
        params: dict = ...,
        dropout_rng: PRNGKey = ...,
    ):
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import FlaxSpeechEncoderDecoderModel
        >>> import jax.numpy as jnp

        >>> # initialize a wav2vec2-2-bart from pretrained wav2vec2 and bart models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxSpeechEncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "facebook/wav2vec2-large-lv60", "facebook/bart-large"
        ... )

        >>> inputs = jnp.ones((2, 5000), dtype=jnp.float32)
        >>> encoder_outputs = model.encode(inputs)

        >>> decoder_start_token_id = model.config.decoder.bos_token_id
        >>> decoder_input_ids = jnp.ones((inputs.shape[0], 1), dtype="i4") * decoder_start_token_id

        >>> outputs = model.decode(decoder_input_ids, encoder_outputs)
        >>> logits = outputs.logits
        ```"""
        ...

    @add_start_docstrings_to_model_forward(SPEECH_ENCODER_DECODER_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=FlaxSeq2SeqLMOutput, config_class=_CONFIG_FOR_DOC)
    def __call__(
        self,
        inputs: jnp.ndarray,
        attention_mask: jnp.ndarray | None = ...,
        decoder_input_ids: jnp.ndarray | None = ...,
        decoder_attention_mask: jnp.ndarray | None = ...,
        decoder_position_ids: jnp.ndarray | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        train: bool = ...,
        freeze_feature_encoder: bool = ...,
        params: dict = ...,
        dropout_rng: PRNGKey = ...,
    ):
        r"""
        Returns:

        Examples:

        ```python
        >>> from transformers import FlaxSpeechEncoderDecoderModel, AutoTokenizer

        >>> # load a fine-tuned wav2vec2-2-bart model
        >>> model = FlaxSpeechEncoderDecoderModel.from_pretrained("patrickvonplaten/wav2vec2-2-bart-large")
        >>> # load output tokenizer
        >>> tokenizer_output = AutoTokenizer.from_pretrained("facebook/bart-large")

        >>> inputs = jnp.ones((2, 5000), dtype=jnp.float32)

        >>> # use bart's special bos, pad and eos tokens
        >>> model.config.decoder_start_token_id = model.decoder.config.bos_token_id
        >>> model.config.pad_token_id = model.decoder.config.pad_token_id
        >>> model.config.eos_token_id = model.decoder.config.eos_token_id

        >>> outputs = model.generate(inputs)
        # Assert something? More interesting input? dtype correct?
        ```
        """
        ...

    def prepare_inputs_for_generation(
        self,
        decoder_input_ids,
        max_length,
        attention_mask: jax.Array | None = ...,
        decoder_attention_mask: jax.Array | None = ...,
        encoder_outputs=...,
        **kwargs,
    ):  # -> dict[str, Any | None]:
        ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
    @classmethod
    def from_encoder_decoder_pretrained(
        cls,
        encoder_pretrained_model_name_or_path: str | os.PathLike | None = ...,
        decoder_pretrained_model_name_or_path: str | os.PathLike | None = ...,
        *model_args,
        **kwargs,
    ) -> FlaxPreTrainedModel:
        r"""
        Instantiate an encoder and a decoder from one or two base classes of the library from pretrained model
        checkpoints.

        Params:
            encoder_pretrained_model_name_or_path (`Union[str, os.PathLike]`, *optional*):
                Information necessary to initiate the encoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.

            decoder_pretrained_model_name_or_path (`Union[str, os.PathLike]`, *optional*, defaults to `None`):
                Information necessary to initiate the decoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.

            model_args (remaining positional arguments, *optional*):
                All remaning positional arguments will be passed to the underlying model's `__init__` method.

            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`).

                - To update the encoder configuration, use the prefix *encoder_* for each configuration parameter.
                - To update the decoder configuration, use the prefix *decoder_* for each configuration parameter.
                - To update the parent model configuration, do not use a prefix for each configuration parameter.

                Behaves differently depending on whether a `config` is provided or automatically loaded.

        Example:

        ```python
        >>> from transformers import FlaxSpeechEncoderDecoderModel

        >>> # initialize a wav2vec2-2-bart from pretrained wav2vec2 and bart models. Note that the cross-attention layers will be randomly initialized
        >>> model = FlaxSpeechEncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "facebook/wav2vec2-large-lv60", "facebook/bart-large"
        ... )
        >>> # saving model after fine-tuning
        >>> model.save_pretrained("./wav2vec2-2-bart-large")
        >>> # load fine-tuned model
        >>> model = FlaxSpeechEncoderDecoderModel.from_pretrained("./wav2vec2-2-bart-large")
        ```"""
        ...

__all__ = ["FlaxSpeechEncoderDecoderModel"]
