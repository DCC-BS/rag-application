"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

import tensorflow as tf

from ... import TFPreTrainedModel
from ...modeling_tf_outputs import ModelOutput
from ...modeling_tf_utils import TFCausalLanguageModelingLoss, TFModelInputType, keras_serializable, unpack_inputs
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_idefics import IdeficsConfig

"""TF 2.0 Idefics model."""
logger = ...
_CONFIG_FOR_DOC = ...

@dataclass
class TFIdeficsBaseModelOutputWithPast(ModelOutput):
    """
    Base class for Idefics model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.

            If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
            hidden_size)` is output.
        past_key_values (`tuple(tuple(tf.Tensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of `tuple(tf.Tensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
            `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and optionally if
            `config.is_encoder_decoder=True` 2 additional tensors of shape `(batch_size, num_heads,
            encoder_sequence_length, embed_size_per_head)`.

            Contains pre-computed hidden-states (key and values in the self-attention blocks and optionally if
            `config.is_encoder_decoder=True` in the cross-attention blocks) that can be used (see `past_key_values`
            input) to speed up sequential decoding.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        image_hidden_states (`tuple(tf.Tensor)`, *optional*):
            Tuple of `tf.Tensor` (one for the output of the image embeddings, `(batch_size, num_images,
            sequence_length, hidden_size)`.

            image_hidden_states of the model produced by the vision encoder, and optionally by the perceiver
    """

    last_hidden_state: tf.Tensor = ...
    past_key_values: tuple[tuple[tf.Tensor]] | None = ...
    hidden_states: tuple[tf.Tensor] | None = ...
    attentions: tuple[tf.Tensor] | None = ...
    image_hidden_states: tuple[tf.Tensor] | None = ...

@dataclass
class TFIdeficsCausalLMOutputWithPast(ModelOutput):
    """
    Base class for Idefics causal language model (or autoregressive) outputs.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss (for next-token prediction).
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        past_key_values (`tuple(tuple(tf.Tensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of `tuple(tf.Tensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
            `(batch_size, num_heads, sequence_length, embed_size_per_head)`)

            Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
            `past_key_values` input) to speed up sequential decoding.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        image_hidden_states (`tuple(tf.Tensor)`, *optional*):
            Tuple of `tf.Tensor` (one for the output of the image embeddings, `(batch_size, num_images,
            sequence_length, hidden_size)`.

            image_hidden_states of the model produced by the vision encoder, and optionally by the perceiver
    """

    loss: tf.Tensor | None = ...
    logits: tf.Tensor = ...
    past_key_values: list[tf.Tensor] | None = ...
    hidden_states: tuple[tf.Tensor] | None = ...
    attentions: tuple[tf.Tensor] | None = ...
    image_hidden_states: tuple[tf.Tensor] | None = ...

def expand_inputs_for_generation(
    input_ids, expand_size=..., is_encoder_decoder=..., attention_mask=..., encoder_outputs=..., **model_kwargs
):  # -> tuple[Any, dict[str, Any]]:
    ...
def update_model_kwargs_for_generation(outputs, model_kwargs): ...
def prepare_inputs_for_generation(input_ids, past_key_values=..., **kwargs):  # -> dict[str, Any | None]:
    ...
def freeze_model(model, module_exceptions=...): ...

class TFIdeficsDecoupledEmbedding(tf.keras.layers.Embedding):
    """
    Implements a decoupling of parameters to allow freezing (or not) a subset of the embeddings. In practise, the
    regular `weight` can be trained or frozen (i.e. `partially_freeze=True`), and if `num_additional_embeddings` > 0,
    then it will create `num_additional_embeddings` additional parameters that are always trained. If
    `num_additional_embeddings=0`, then the module defaults back to the regular behavior of `tf.keras.layers.Embedding`.
    """
    def __init__(
        self,
        num_embeddings,
        num_additional_embeddings,
        embedding_dim,
        partially_freeze: bool | None = ...,
        dtype=...,
        **kwargs,
    ) -> None:
        """
        Args:
            num_embeddings (`int`):
                Size of the dictionary of embeddings
            num_additional_embeddings (`int`):
                Number of additional embeddings. Only useful when you `partially_freeze=True`.
            embedding_dim (`int`):
                The size of each embedding vector
            partially_freeze: (`bool`, *optional*, defaults to `False`):
                If `True`, the regular `weight` will be frozen. `additional_weight` is never frozen.

        Note: there are a lot of other parameters to initialize a standard `tf.keras.layers.Embedding` such as `mask_zero`,
        `input_length` or `embeddings_initializer`. We are not supporting these.
        """
        ...

    def call(self, input_ids):
        """
        we have 2 embeddings, with different indices - one pretrained self.weight and another
        self.additional_embedding.weight that is being trained.

        in order to make a lookup of the input ids, we:
        1. find out the indices of the entries belonging to the 2nd embedding
        2. extract those values while subtracting the size of the first embedding (num_embeddings), since the 2nd
           embedding starts from 0 and not num_embeddings
        3. perform the 2nd embedding lookup
        4. now we handle the 1st embedding, we overwrite indices belonging to the 2nd embedding with a padding index
        5. perform the 1st embedding lookup
        6. now we overwrite the values in the 1st embedding lookup with the values of the 2nd embedding lookup

        note: for the 1st embedding lookup we could have looked up only the low indices and not do the padding, but
        then we have to create a new tensor and populate it with 2 tensors that are spread out across various indices -
        i.e. not a simple concat - I haven't benchmarked the complex case if it's any faster, given that seqlens are
        usually relatively short it's probably not faster or if faster not by much - but might be a good idea to
        measure.

        """
        ...

    def extra_repr(self) -> str: ...

class TFIdeficsDecoupledLinear(tf.keras.layers.Layer):
    """
    Implements a decoupling of parameters to allow freezing (or not) a subset of the parameters. In practise, the
    regular `weight` can be trained or frozen (i.e. `partially_freeze=True`), and if `out_additional_features` > 0,
    then it will create `out_additional_features * in_features` additional parameters that are always trained. If
    `out_additional_features=0`, then the module defaults back to the regular behavior of `tf.keras.layers.Dense`.
    """
    def __init__(
        self,
        in_features: int,
        out_features: int,
        out_additional_features: int = ...,
        bias: bool = ...,
        partially_freeze: bool = ...,
        **kwargs,
    ) -> None:
        """
        out_additional_features: int. Number of additional trainable dimensions. Only makes sense when
        `partially_freeze=True`. partially_freeze: bool. If True, the regular `weight` will be frozen and extra
        parameters (if any) will be trainable. If False, default to the regular behavior of tf.keras.layers.Dense.
        """
        ...

    def call(self, inputs: tf.Tensor) -> tf.Tensor: ...
    def get_config(self): ...
    def extra_repr(self) -> str:
        """Overwriting `nn.Linear.extra_repr` to include new parameters."""
        ...

    @classmethod
    def from_config(cls, config):  # -> Self:
        ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFIdeficsRMSNorm(tf.keras.layers.Layer):
    def __init__(self, hidden_size, eps=..., **kwargs) -> None:
        """
        TFIdeficsRMSNorm is equivalent to T5LayerNorm
        """
        ...

    def build(self, input_shape):  # -> None:
        ...
    def call(self, hidden_states): ...

class TFIdeficsEmbedding(tf.keras.layers.Layer):
    def __init__(self, dim, max_position_embeddings=..., base=..., **kwargs) -> None: ...
    def call(self, x, seq_len=...):  # -> tuple[Any, Any]:
        ...

def rotate_half(x):
    """Rotates half the hidden dims of the input."""
    ...

def apply_rotary_pos_emb(q, k, cos, sin, position_ids):  # -> tuple[Any, Any]:
    ...

class TFIdeficsMLP(tf.keras.layers.Layer):
    def __init__(self, hidden_size: int, intermediate_size: int, hidden_act: str, **kwargs) -> None: ...
    def call(self, x): ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFIdeficsAttention(tf.keras.layers.Layer):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(
        self,
        hidden_size: int,
        num_heads: int,
        dropout: float = ...,
        is_cross_attention: bool = ...,
        config: IdeficsConfig = ...,
        qk_layer_norms: bool = ...,
        **kwargs,
    ) -> None: ...
    def call(
        self,
        hidden_states: tf.Tensor,
        key_value_states: tf.Tensor | None = ...,
        attention_mask: tf.Tensor | None = ...,
        position_ids: tf.Tensor | None = ...,
        past_key_value: tuple[tf.Tensor] | None = ...,
        output_attentions: bool = ...,
        use_cache: bool = ...,
    ) -> tuple[tf.Tensor, tf.Tensor | None, tuple[tf.Tensor] | None]: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFIdeficsDecoderLayer(tf.keras.layers.Layer):
    def __init__(self, config: IdeficsConfig, **kwargs) -> None: ...
    def call(
        self,
        hidden_states: tf.Tensor,
        attention_mask: tf.Tensor | None = ...,
        position_ids: tf.Tensor | None = ...,
        past_key_value: tuple[tf.Tensor] | None = ...,
        output_attentions: bool | None = ...,
        use_cache: bool | None = ...,
        training=...,
    ) -> tuple[tf.Tensor, tuple[tf.Tensor, tf.Tensor] | None]:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`tf.Tensor`, *optional*): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            use_cache (`bool`, *optional*):
                If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding
                (see `past_key_values`).
            past_key_value (`Tuple(tf.Tensor)`, *optional*): cached past key and value projection states
        """
        ...

    def build(self, input_shape=...):  # -> None:
        ...

class TFIdeficsGatedCrossAttentionLayer(tf.keras.layers.Layer):
    def __init__(self, config: IdeficsConfig, **kwargs) -> None: ...
    def build(self, input_shape):  # -> None:
        ...
    def call(
        self,
        hidden_states: tf.Tensor,
        attention_mask: tf.Tensor | None = ...,
        image_hidden_states: tf.Tensor | None = ...,
        image_attention_mask: tf.Tensor | None = ...,
        cross_attention_gate: tf.Tensor | None = ...,
        output_attentions: bool | None = ...,
        use_cache: bool | None = ...,
        past_key_value: tuple[tf.Tensor] | None = ...,
    ) -> tuple[tf.Tensor, tuple[tf.Tensor, tf.Tensor] | None]:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`tf.Tensor`, *optional*): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            use_cache (`bool`, *optional*):
                If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding
                (see `past_key_values`).
            past_key_value (`Tuple(tf.Tensor)`, *optional*): cached past key and value projection states
            no_images (`bool`, *optional*, defaults to `False`): If `True` the vision part is ignored
        """
        ...

LLAMA_START_DOCSTRING = ...

@add_start_docstrings(
    "The bare LLaMA Model outputting raw hidden-states without any specific head on top.", LLAMA_START_DOCSTRING
)
class TFIdeficsPreTrainedModel(TFPreTrainedModel):
    config_class = IdeficsConfig
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...

LLAMA_INPUTS_DOCSTRING = ...

@add_start_docstrings(
    "The bare LLaMA Model outputting raw hidden-states without any specific head on top.", LLAMA_START_DOCSTRING
)
@keras_serializable
class TFIdeficsMainLayer(tf.keras.layers.Layer):
    """
    Transformer decoder consisting of `config.num_hidden_layers` layers. Each layer is a [`IdeficsDecoderLayer`]

    Args:
        config: IdeficsConfig
    """

    config_class = IdeficsConfig
    def __init__(self, config: IdeficsConfig, add_pooling_year: bool = ..., **kwargs) -> None: ...
    def freeze_relevant_params(self, config=...):  # -> None:
        ...
    def freeze_text_layers(self, module_exceptions=...):  # -> None:
        ...
    def freeze_vision_layers(self, module_exceptions=...):  # -> None:
        ...
    def get_input_embeddings(self):  # -> TFIdeficsDecoupledEmbedding:
        ...
    def set_input_embeddings(self, value):  # -> None:
        ...
    @unpack_inputs
    @add_start_docstrings_to_model_forward(LLAMA_INPUTS_DOCSTRING)
    def call(
        self,
        input_ids: TFModelInputType | None = ...,
        attention_mask: tf.Tensor | None = ...,
        position_ids: tf.Tensor | None = ...,
        past_key_values: list[tf.Tensor] | None = ...,
        inputs_embeds: tf.Tensor | None = ...,
        pixel_values: tf.Tensor | None = ...,
        image_encoder_embeddings: tf.Tensor | None = ...,
        perceiver_embeddings: tf.Tensor | None = ...,
        image_attention_mask: tf.Tensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        interpolate_pos_encoding: bool | None = ...,
        return_dict: bool | None = ...,
        training: bool | None = ...,
    ) -> TFIdeficsBaseModelOutputWithPast | tuple[tf.Tensor]: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFIdeficsModel(TFIdeficsPreTrainedModel):
    def __init__(self, config: IdeficsConfig, *inputs, **kwargs) -> None: ...
    def call(
        self,
        input_ids: TFModelInputType | None = ...,
        attention_mask: tf.Tensor | None = ...,
        position_ids: tf.Tensor | None = ...,
        past_key_values: list[tf.Tensor] | None = ...,
        inputs_embeds: tf.Tensor | None = ...,
        pixel_values: tf.Tensor | None = ...,
        image_encoder_embeddings: tf.Tensor | None = ...,
        perceiver_embeddings: tf.Tensor | None = ...,
        image_attention_mask: tf.Tensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        interpolate_pos_encoding: bool | None = ...,
        return_dict: bool | None = ...,
        training: bool | None = ...,
    ) -> TFIdeficsBaseModelOutputWithPast | tuple[tf.Tensor]: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFIdeficsForVisionText2Text(TFPreTrainedModel, TFCausalLanguageModelingLoss):
    _keys_to_ignore_on_load_missing = ...
    _tied_weights_keys = ...
    config_class = IdeficsConfig
    def __init__(self, config, vision_model=..., **kwargs) -> None: ...
    def get_input_embeddings(self):  # -> TFIdeficsDecoupledEmbedding:
        ...
    def set_input_embeddings(self, value):  # -> None:
        ...
    def get_output_embeddings(self):  # -> TFIdeficsDecoupledLinear:
        ...
    def set_output_embeddings(self, new_embeddings):  # -> None:
        ...
    def set_decoder(self, decoder):  # -> None:
        ...
    def get_decoder(self):  # -> TFIdeficsMainLayer:
        ...
    def tie_weights(self):  # -> None:
        """
        Overwrite `transformers.modeling_utils.PreTrainedModel.tie_weights` to handle the case of
        IdeficsDecoupledLinear and IdeficsDecoupledEmbedding.
        """
        ...

    @unpack_inputs
    @add_start_docstrings_to_model_forward(LLAMA_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TFIdeficsCausalLMOutputWithPast, config_class=_CONFIG_FOR_DOC)
    def call(
        self,
        input_ids: TFModelInputType | None = ...,
        attention_mask: tf.Tensor | None = ...,
        position_ids: tf.Tensor | None = ...,
        past_key_values: list[tf.Tensor] | None = ...,
        inputs_embeds: tf.Tensor | None = ...,
        pixel_values: tf.Tensor | None = ...,
        image_encoder_embeddings: tf.Tensor | None = ...,
        perceiver_embeddings: tf.Tensor | None = ...,
        image_attention_mask: tf.Tensor | None = ...,
        labels: tf.Tensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        interpolate_pos_encoding: bool | None = ...,
        return_dict: bool | None = ...,
        training=...,
    ) -> TFIdeficsCausalLMOutputWithPast | tuple[tf.Tensor]:
        r"""
            labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
                config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
                (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

        Returns:

        Example:

        ```python
        >> from transformers import AutoTokenizer, TFIdeficsForVisionText2Text

        >> model = TFIdeficsForVisionText2Text.from_pretrained("HuggingFaceM4/idefics-9b")
        >> tokenizer = AutoTokenizer.from_pretrained("HuggingFaceM4/idefics-9b")

        >> prompt = "Hey, are you consciours? Can you talk to me?"
        >> inputs = tokenizer(prompt, return_tensors="tf")

        >> # Generate
        >> generate_ids = model.generate(inputs.input_ids, max_length=30)
        >> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        "Hey, are you consciours? Can you talk to me?\nI'm not consciours, but I can talk to you."
        ```"""
        ...

    def prepare_inputs_for_generation(self, input_ids, past=..., **kwargs):  # -> dict[str, Any | None]:
        ...
    def build(self, input_shape=...):  # -> None:
        ...

__all__ = ["TFIdeficsForVisionText2Text", "TFIdeficsModel", "TFIdeficsPreTrainedModel"]
