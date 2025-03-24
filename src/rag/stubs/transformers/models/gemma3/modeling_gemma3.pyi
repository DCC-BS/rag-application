"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

import torch
import torch.nn as nn

from ...cache_utils import Cache, HybridCache
from ...generation import GenerationMixin
from ...modeling_flash_attention_utils import FlashAttentionKwargs
from ...modeling_outputs import BaseModelOutputWithPast, CausalLMOutputWithPast, ModelOutput
from ...modeling_utils import PreTrainedModel
from ...processing_utils import Unpack
from ...utils import add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from ...utils.deprecation import deprecate_kwarg
from .configuration_gemma3 import Gemma3Config, Gemma3TextConfig

logger = ...
_CONFIG_FOR_DOC = ...

@dataclass
class Gemma3CausalLMOutputWithPast(ModelOutput):
    """
    Base class for Gemma3 causal language model (or autoregressive) outputs.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss (for next-token prediction).
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.text_config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
            `(batch_size, num_heads, sequence_length, embed_size_per_head)`)

            Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
            `past_key_values` input) to speed up sequential decoding.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        image_hidden_states (`torch.FloatTensor`, *optional*):
            A `torch.FloatTensor` of size `(batch_size, sequence_length, hidden_size)`.
            image_hidden_states of the model produced by the vision encoder after projecting last hidden state.
    """

    loss: torch.FloatTensor | None = ...
    logits: torch.FloatTensor = ...
    past_key_values: list[torch.FloatTensor] | Cache | None = ...
    hidden_states: tuple[torch.FloatTensor] | None = ...
    attentions: tuple[torch.FloatTensor] | None = ...
    image_hidden_states: torch.FloatTensor | None = ...

class Gemma3TextScaledWordEmbedding(nn.Embedding):
    """
    This module overrides nn.Embeddings' forward by multiplying with embeddings scale.
    """
    def __init__(
        self, num_embeddings: int, embedding_dim: int, padding_idx: int, embed_scale: float | None = ...
    ) -> None: ...
    def forward(self, input_ids: torch.Tensor):  # -> Tensor:
        ...

class Gemma3MLP(nn.Module):
    def __init__(self, config: Gemma3TextConfig) -> None: ...
    def forward(self, x):  # -> Any:
        ...

class Gemma3RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = ...) -> None: ...
    def forward(self, x): ...
    def extra_repr(self):  # -> str:
        ...

class Gemma3RotaryEmbedding(nn.Module):
    def __init__(self, config: Gemma3TextConfig, device=...) -> None: ...
    @torch.no_grad()
    def forward(self, x, position_ids):  # -> tuple[Tensor, Tensor]:
        ...

def rotate_half(x):  # -> Tensor:
    """Rotates half the hidden dims of the input."""
    ...

def apply_rotary_pos_emb(q, k, cos, sin, position_ids=..., unsqueeze_dim=...):  # -> tuple[Any, Any]:
    """Applies Rotary Position Embedding to the query and key tensors.

    Args:
        q (`torch.Tensor`): The query tensor.
        k (`torch.Tensor`): The key tensor.
        cos (`torch.Tensor`): The cosine part of the rotary embedding.
        sin (`torch.Tensor`): The sine part of the rotary embedding.
        position_ids (`torch.Tensor`, *optional*):
            Deprecated and unused.
        unsqueeze_dim (`int`, *optional*, defaults to 1):
            The 'unsqueeze_dim' argument specifies the dimension along which to unsqueeze cos[position_ids] and
            sin[position_ids] so that they can be properly broadcasted to the dimensions of q and k. For example, note
            that cos[position_ids] and sin[position_ids] have the shape [batch_size, seq_len, head_dim]. Then, if q and
            k have the shape [batch_size, heads, seq_len, head_dim], then setting unsqueeze_dim=1 makes
            cos[position_ids] and sin[position_ids] broadcastable to the shapes of q and k. Similarly, if q and k have
            the shape [batch_size, seq_len, heads, head_dim], then set unsqueeze_dim=2.
    Returns:
        `tuple(torch.Tensor)` comprising of the query and key tensors rotated using the Rotary Position Embedding.
    """
    ...

def repeat_kv(hidden_states: torch.Tensor, n_rep: int) -> torch.Tensor:
    """
    This is the equivalent of torch.repeat_interleave(x, dim=1, repeats=n_rep). The hidden states go from (batch,
    num_key_value_heads, seqlen, head_dim) to (batch, num_attention_heads, seqlen, head_dim)
    """
    ...

def eager_attention_forward(
    module: nn.Module,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attention_mask: torch.Tensor | None,
    dropout: float = ...,
    scaling: float | None = ...,
    softcap: float | None = ...,
    **kwargs,
) -> tuple[torch.Tensor, torch.Tensor]: ...

class Gemma3Attention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(self, config: Gemma3TextConfig, layer_idx: int) -> None: ...
    def forward(
        self,
        hidden_states: torch.Tensor,
        position_embeddings: torch.Tensor,
        attention_mask: torch.Tensor | None,
        past_key_value: Cache | None = ...,
        cache_position: torch.LongTensor | None = ...,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> tuple[torch.Tensor, torch.Tensor | None, tuple[torch.Tensor] | None]: ...

class Gemma3DecoderLayer(nn.Module):
    def __init__(self, config: Gemma3TextConfig, layer_idx: int) -> None: ...
    def forward(
        self,
        hidden_states: torch.Tensor,
        position_embeddings_global: torch.Tensor,
        position_embeddings_local: torch.Tensor,
        attention_mask: torch.Tensor | None = ...,
        position_ids: torch.LongTensor | None = ...,
        past_key_value: Cache | None = ...,
        output_attentions: bool | None = ...,
        use_cache: bool | None = ...,
        cache_position: torch.LongTensor | None = ...,
        last_cache_position: int = ...,
        **kwargs,
    ) -> tuple[torch.FloatTensor, tuple[torch.FloatTensor, torch.FloatTensor] | None]: ...

GEMMA3_START_DOCSTRING = ...

@add_start_docstrings(
    "The bare Gemma3 Model outputting raw hidden-states without any specific head on top.", GEMMA3_START_DOCSTRING
)
class Gemma3PreTrainedModel(PreTrainedModel):
    config_class = Gemma3Config
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...
    _skip_keys_device_placement = ...
    _supports_flash_attn_2 = ...
    _supports_sdpa = ...
    _supports_flex_attn = ...
    _supports_cache_class = ...
    _supports_quantized_cache = ...
    _supports_static_cache = ...
    _supports_attention_backend = ...

GEMMA3_INPUTS_DOCSTRING = ...

@add_start_docstrings(
    "The bare Gemma3Text Model outputting raw hidden-states without any specific head on top.", GEMMA3_START_DOCSTRING
)
class Gemma3TextModel(Gemma3PreTrainedModel):
    """
    Transformer decoder consisting of *config.num_hidden_layers* layers. Each layer is a [`Gemma3TextDecoderLayer`]

    Args:
        config: Gemma3TextConfig
    """

    config_class = Gemma3TextConfig
    def __init__(self, config: Gemma3TextConfig) -> None: ...
    def get_input_embeddings(self):  # -> Gemma3TextScaledWordEmbedding | Module:
        ...
    def set_input_embeddings(self, value):  # -> None:
        ...
    @add_start_docstrings_to_model_forward(GEMMA3_INPUTS_DOCSTRING)
    def forward(
        self,
        input_ids: torch.LongTensor | None = ...,
        attention_mask: torch.Tensor | None = ...,
        position_ids: torch.LongTensor | None = ...,
        past_key_values: HybridCache | None = ...,
        inputs_embeds: torch.FloatTensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        cache_position: torch.LongTensor | None = ...,
        last_cache_position: int | None = ...,
        **flash_attn_kwargs: Unpack[FlashAttentionKwargs],
    ) -> tuple | BaseModelOutputWithPast: ...

class Gemma3ForCausalLM(Gemma3PreTrainedModel, GenerationMixin):
    _tied_weights_keys = ...
    _tp_plan = ...
    _pp_plan = ...
    config_class = Gemma3TextConfig
    base_model_prefix = ...
    def __init__(self, config: Gemma3TextConfig) -> None: ...
    def get_input_embeddings(self):  # -> Gemma3TextScaledWordEmbedding | Module:
        ...
    def set_input_embeddings(self, value):  # -> None:
        ...
    def get_output_embeddings(self):  # -> Linear:
        ...
    def set_output_embeddings(self, new_embeddings):  # -> None:
        ...
    def set_decoder(self, decoder):  # -> None:
        ...
    def get_decoder(self):  # -> Gemma3TextModel:
        ...
    @deprecate_kwarg("num_logits_to_keep", version="4.50", new_name="logits_to_keep")
    @add_start_docstrings_to_model_forward(GEMMA3_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=CausalLMOutputWithPast, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        input_ids: torch.LongTensor = ...,
        attention_mask: torch.Tensor | None = ...,
        position_ids: torch.LongTensor | None = ...,
        past_key_values: HybridCache | None = ...,
        inputs_embeds: torch.FloatTensor | None = ...,
        labels: torch.LongTensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        cache_position: torch.LongTensor | None = ...,
        logits_to_keep: int | torch.Tensor = ...,
        **loss_kwargs,
    ) -> tuple | CausalLMOutputWithPast:
        r"""
            labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
                config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
                (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

            logits_to_keep (`int` or `torch.Tensor`, *optional*):
                If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
                `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
                token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
                If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
                This is useful when using packed tensor format (single dimension for batch and sequence length).

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, Gemma3ForCausalLM

        >>> model = Gemma3ForCausalLM.from_pretrained("google/gemma-2-9b")
        >>> tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b")

        >>> prompt = "What is your favorite condiment?"
        >>> inputs = tokenizer(prompt, return_tensors="pt")

        >>> # Generate
        >>> generate_ids = model.generate(inputs.input_ids, max_length=30)
        >>> tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        "What is your favorite condiment?"
        ```"""
        ...

    def prepare_inputs_for_generation(
        self,
        input_ids,
        past_key_values=...,
        attention_mask=...,
        inputs_embeds=...,
        cache_position=...,
        position_ids=...,
        use_cache=...,
        logits_to_keep=...,
        **kwargs,
    ):  # -> dict[Any, Any]:
        ...

class Gemma3MultiModalProjector(nn.Module):
    def __init__(self, config: Gemma3Config) -> None: ...
    def forward(self, vision_outputs: torch.Tensor):  # -> Tensor:
        ...

@add_start_docstrings(
    """The GEMMA3 model which consists of a vision backbone and a language model.""", GEMMA3_START_DOCSTRING
)
class Gemma3ForConditionalGeneration(Gemma3PreTrainedModel, GenerationMixin):
    def __init__(self, config: Gemma3Config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value):  # -> None:
        ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings):  # -> None:
        ...
    def set_decoder(self, decoder):  # -> None:
        ...
    def get_decoder(self): ...
    def get_image_features(self, pixel_values: torch.Tensor):  # -> Any:
        """
        Projects the last hidden state from the vision model into language model space.

        Args:
            pixel_values (`torch.FloatTensor]` of shape `(batch_size, channels, height, width)`)
               The tensors corresponding to the input images.
        Returns:
            image_features (`torch.Tensor`): Image feature tensor of shape `(num_images, image_length, embed_dim)`).
        """
        ...

    @deprecate_kwarg("num_logits_to_keep", version="4.50", new_name="logits_to_keep")
    @add_start_docstrings_to_model_forward(GEMMA3_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Gemma3CausalLMOutputWithPast, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        input_ids: torch.LongTensor = ...,
        pixel_values: torch.FloatTensor = ...,
        attention_mask: torch.Tensor | None = ...,
        position_ids: torch.LongTensor | None = ...,
        past_key_values: list[torch.FloatTensor] | Cache | None = ...,
        token_type_ids: torch.LongTensor | None = ...,
        cache_position: torch.LongTensor | None = ...,
        inputs_embeds: torch.FloatTensor | None = ...,
        labels: torch.LongTensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        logits_to_keep: int | torch.Tensor = ...,
        **lm_kwargs,
    ) -> tuple | Gemma3CausalLMOutputWithPast:
        r"""
            labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
                config.text_config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
                (masked), the loss is only computed for the tokens with labels in `[0, ..., config.text_config.vocab_size]`.

            logits_to_keep (`int` or `torch.Tensor`, *optional*):
                If an `int`, compute logits for the last `logits_to_keep` tokens. If `0`, calculate logits for all
                `input_ids` (special case). Only last token logits are needed for generation, and calculating them only for that
                token can save memory, which becomes pretty significant for long sequences or large vocabulary size.
                If a `torch.Tensor`, must be 1D corresponding to the indices to keep in the sequence length dimension.
                This is useful when using packed tensor format (single dimension for batch and sequence length).

        Returns:

        Example:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, Gemma3ForConditionalGeneration

        >>> model = Gemma3ForConditionalGeneration.from_pretrained("google/Gemma3-test-224px-hf")
        >>> processor = AutoProcessor.from_pretrained("google/Gemma3-test-224px-hf")

        >>> prompt = "answer en Where is the cow standing?"
        >>> url = "https://huggingface.co/gv-hf/Gemma3-test-224px-hf/resolve/main/cow_beach_1.png"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, text=prompt,  return_tensors="pt")

        >>> # Generate
        >>> generate_ids = model.generate(**inputs, max_length=30)
        >>> processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        "answer en Where is the cow standing?\nbeach"
        ```"""
        ...

    def prepare_inputs_for_generation(
        self,
        input_ids,
        past_key_values=...,
        inputs_embeds=...,
        cache_position=...,
        position_ids=...,
        pixel_values=...,
        attention_mask=...,
        token_type_ids=...,
        use_cache=...,
        logits_to_keep=...,
        labels=...,
        **kwargs,
    ): ...
    def tie_weights(self): ...

__all__ = ["Gemma3PreTrainedModel", "Gemma3TextModel", "Gemma3ForCausalLM", "Gemma3ForConditionalGeneration"]
