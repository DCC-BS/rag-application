"""
This type stub file was generated by pyright.
"""

import torch
import torch.nn as nn

from ...generation import GenerationMixin
from ...modeling_outputs import Seq2SeqMoEModelOutput, Seq2SeqMoEOutput
from ...modeling_utils import PreTrainedModel
from ...utils import (
    add_end_docstrings,
    add_start_docstrings,
    add_start_docstrings_to_model_forward,
    replace_return_docstrings,
)
from .configuration_nllb_moe import NllbMoeConfig

"""PyTorch NLLB-MoE model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_REAL_CHECKPOINT_FOR_DOC = ...

def shift_tokens_right(input_ids: torch.Tensor, pad_token_id: int, decoder_start_token_id: int):  # -> Tensor:
    """
    Shift input ids one token to the right.
    """
    ...

def create_position_ids_from_input_ids(input_ids, padding_idx, past_key_values_length=...):
    """
    Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding symbols
    are ignored. This is modified from fairseq's `utils.make_positions`.

    Args:
        x: torch.Tensor x:

    Returns: torch.Tensor
    """
    ...

def load_balancing_loss_func(router_probs: torch.Tensor, expert_indices: torch.Tensor) -> float:
    r"""
    Computes auxiliary load balancing loss as in Switch Transformer - implemented in Pytorch.

    See Switch Transformer (https://arxiv.org/abs/2101.03961) for more details. This function implements the loss
    function presented in equations (4) - (6) of the paper. It aims at penalizing cases where the routing between
    experts is too unbalanced.

    Args:
        router_probs (`torch.Tensor`):
            Probability assigned to each expert per token. Shape: [batch_size, seqeunce_length, num_experts].
        expert_indices (`torch.Tensor`):
            Indices tensor of shape [batch_size, seqeunce_length] identifying the selected expert for a given token.

    Returns:
        The auxiliary loss.
    """
    ...

class NllbMoeScaledWordEmbedding(nn.Embedding):
    """
    This module overrides nn.Embeddings' forward by multiplying with embeddings scale.
    """
    def __init__(
        self, num_embeddings: int, embedding_dim: int, padding_idx: int, embed_scale: float | None = ...
    ) -> None: ...
    def forward(self, input_ids: torch.Tensor):  # -> Tensor:
        ...

class NllbMoeSinusoidalPositionalEmbedding(nn.Module):
    """This module produces sinusoidal positional embeddings of any length."""
    def __init__(self, num_positions: int, embedding_dim: int, padding_idx: int | None = ...) -> None: ...
    def make_weights(self, num_embeddings: int, embedding_dim: int, padding_idx: int | None = ...):  # -> None:
        ...
    @staticmethod
    def get_embedding(num_embeddings: int, embedding_dim: int, padding_idx: int | None = ...):  # -> Tensor:
        """
        Build sinusoidal embeddings.

        This matches the implementation in tensor2tensor, but differs slightly from the description in Section 3.5 of
        "Attention Is All You Need".
        """
        ...

    @torch.no_grad()
    def forward(
        self, input_ids: torch.Tensor = ..., inputs_embeds: torch.Tensor = ..., past_key_values_length: int = ...
    ):  # -> Tensor | Any:
        ...
    def create_position_ids_from_inputs_embeds(self, inputs_embeds, past_key_values_length):
        """
        We are provided embeddings directly. We cannot infer which are padded so just generate sequential position ids.

        Args:
            inputs_embeds: torch.Tensor

        Returns: torch.Tensor
        """
        ...

class NllbMoeTop2Router(nn.Module):
    """
    Router using tokens choose top-2 experts assignment.

    This router uses the same mechanism as in NLLB-MoE from the fairseq repository. Items are sorted by router_probs
    and then routed to their choice of expert until the expert's expert_capacity is reached. **There is no guarantee
    that each token is processed by an expert**, or that each expert receives at least one token.

    The router combining weights are also returned to make sure that the states that are not updated will be masked.

    """
    def __init__(self, config: NllbMoeConfig) -> None: ...
    def normalize_router_probabilities(self, router_probs, top_1_mask, top_2_mask):  # -> tuple[Any, Any]:
        ...
    def route_tokens(
        self, router_logits: torch.Tensor, input_dtype: torch.dtype = ..., padding_mask: torch.LongTensor | None = ...
    ) -> tuple:
        """
        Computes the `dispatch_mask` and the `dispatch_weights` for each experts. The masks are adapted to the expert
        capacity.
        """
        ...

    def forward(self, hidden_states: torch.Tensor, padding_mask: torch.LongTensor | None = ...) -> tuple:
        r"""
        The hidden states are reshaped to simplify the computation of the router probabilities (combining weights for
        each experts.)

        Args:
            hidden_states (`torch.Tensor`):
                (batch_size, sequence_length, hidden_dim) from which router probabilities are computed.
        Returns:
            top_1_mask (`torch.Tensor` of shape (batch_size, sequence_length)):
                Index tensor of shape [batch_size, sequence_length] corresponding to the expert selected for each token
                using the top1 probabilities of the router.
            router_probabilities (`torch.Tensor` of shape (batch_size, sequence_length, nump_experts)):
                Tensor of shape (batch_size, sequence_length, num_experts) corresponding to the probabilities for each
                token and expert. Used for routing tokens to experts.
            router_logits (`torch.Tensor` of shape (batch_size, sequence_length))):
                Logits tensor of shape (batch_size, sequence_length, num_experts) corresponding to raw router logits.
                This is used later for computing router z-loss.
        """
        ...

class NllbMoeDenseActDense(nn.Module):
    def __init__(self, config: NllbMoeConfig, ffn_dim: int) -> None: ...
    def forward(self, hidden_states):  # -> Any:
        ...

class NllbMoeSparseMLP(nn.Module):
    r"""
    Implementation of the NLLB-MoE sparse MLP module.
    """
    def __init__(self, config: NllbMoeConfig, ffn_dim: int, expert_class: nn.Module = ...) -> None: ...
    def forward(
        self, hidden_states: torch.Tensor, padding_mask: torch.Tensor | None = ...
    ):  # -> tuple[Tensor, tuple[Any, Tensor]]:
        r"""
        The goal of this forward pass is to have the same number of operation as the equivalent `NllbMoeDenseActDense`
        (mlp) layer. This means that all of the hidden states should be processed at most twice ( since we are using a
        top_2 gating mecanism). This means that we keep the complexity to O(batch_size x sequence_length x hidden_dim)
        instead of O(num_experts x batch_size x sequence_length x hidden_dim).

        1- Get the `router_probs` from the `router`. The shape of the `router_mask` is `(batch_size X sequence_length,
        num_expert)` and corresponds to the boolean version of the `router_probs`. The inputs are masked using the
        `router_mask`.

        2- Dispatch the hidden_states to its associated experts. The router probabilities are used to weight the
        contribution of each experts when updating the masked hidden states.

        Args:
            hidden_states (`torch.Tensor` of shape `(batch_size, sequence_length, hidden_dim)`):
                The hidden states
            padding_mask (`torch.Tensor`, *optional*, defaults to `False`):
                Attention mask. Can be in the causal form or not.

        Returns:
            hidden_states (`torch.Tensor` of shape `(batch_size, sequence_length, hidden_dim)`):
                Updated hidden states
            router_logits (`torch.Tensor` of shape `(batch_size, sequence_length, num_experts)`):
                Needed for computing the loss

        """
        ...

class NllbMoeAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        dropout: float = ...,
        is_decoder: bool = ...,
        bias: bool = ...,
        is_causal: bool = ...,
        config: NllbMoeConfig | None = ...,
    ) -> None: ...
    def forward(
        self,
        hidden_states: torch.Tensor,
        encoder_hidden_states: torch.Tensor | None = ...,
        past_key_value: tuple[torch.Tensor] | None = ...,
        attention_mask: torch.Tensor | None = ...,
        layer_head_mask: torch.Tensor | None = ...,
        output_attentions: bool = ...,
    ) -> tuple[torch.Tensor, torch.Tensor | None, tuple[torch.Tensor] | None]:
        """Input shape: Batch x Time x Channel"""
        ...

class NllbMoeEncoderLayer(nn.Module):
    def __init__(self, config: NllbMoeConfig, is_sparse: bool = ...) -> None: ...
    def forward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: torch.Tensor,
        layer_head_mask: torch.Tensor,
        output_attentions: bool = ...,
        output_router_logits: bool = ...,
    ) -> torch.Tensor:
        """
        Args:
            hidden_states (`torch.FloatTensor`):
                input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`):
                attention mask of size `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very
                large negative values.
            layer_head_mask (`torch.FloatTensor`): mask for attention heads in a given layer of size
                `(encoder_attention_heads,)`.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """
        ...

class NllbMoeDecoderLayer(nn.Module):
    def __init__(self, config: NllbMoeConfig, is_sparse: bool = ...) -> None: ...
    def forward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: torch.Tensor | None = ...,
        encoder_hidden_states: torch.Tensor | None = ...,
        encoder_attention_mask: torch.Tensor | None = ...,
        layer_head_mask: torch.Tensor | None = ...,
        cross_attn_layer_head_mask: torch.Tensor | None = ...,
        past_key_value: tuple[torch.Tensor] | None = ...,
        output_attentions: bool | None = ...,
        output_router_logits: bool | None = ...,
        use_cache: bool | None = ...,
    ) -> torch.Tensor:
        """
        Args:
            hidden_states (`torch.FloatTensor`):
                input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`):
                attention mask of size `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very
                large negative values.
            encoder_hidden_states (`torch.FloatTensor`):
                cross attention input to the layer of shape `(batch, seq_len, embed_dim)`
            encoder_attention_mask (`torch.FloatTensor`):
                encoder attention mask of size `(batch, 1, tgt_len, src_len)` where padding elements are indicated by
                very large negative values.
            layer_head_mask (`torch.FloatTensor`):
                mask for attention heads in a given layer of size `(encoder_attention_heads,)`.
            cross_attn_layer_head_mask (`torch.FloatTensor`):
                mask for cross-attention heads in a given layer of size `(decoder_attention_heads,)`.
            past_key_value (`Tuple(torch.FloatTensor)`):
                cached past key and value projection states
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """
        ...

class NllbMoePreTrainedModel(PreTrainedModel):
    config_class = NllbMoeConfig
    base_model_prefix = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...

NLLB_MOE_START_DOCSTRING = ...
NLLB_MOE_GENERATION_EXAMPLE = ...
NLLB_MOE_INPUTS_DOCSTRING = ...

class NllbMoeEncoder(NllbMoePreTrainedModel):
    """
    Transformer encoder consisting of *config.encoder_layers* self attention layers. Each layer is a
    [`NllbMoeEncoderLayer`].

    Args:
        config:
            NllbMoeConfig
        embed_tokens (nn.Embedding):
            output embedding
    """
    def __init__(self, config: NllbMoeConfig, embed_tokens: nn.Embedding | None = ...) -> None: ...
    def forward(
        self,
        input_ids: torch.Tensor | None = ...,
        attention_mask: torch.Tensor | None = ...,
        head_mask: torch.Tensor | None = ...,
        inputs_embeds: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        output_router_logits: bool | None = ...,
        return_dict: bool | None = ...,
    ):  # -> tuple[Any | tuple[Any, ...] | tuple[Tensor | Any, ...] | tuple[()] | tuple[Any | None, ...], ...] | MoEModelOutput:
        r"""
        Args:
            input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`torch.Tensor` of shape `(encoder_layers, encoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            output_router_logits (`bool`, *optional*):
                Whether or not to return the logits of all the routers. They are useful for computing the router loss,
                and should not be returned during inference.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """
        ...

class NllbMoeDecoder(NllbMoePreTrainedModel):
    """
    Transformer decoder consisting of *config.decoder_layers* layers. Each layer is a [`NllbMoeDecoderLayer`]

    Args:
        config:
            NllbMoeConfig
        embed_tokens (nn.Embedding):
            output embedding
    """
    def __init__(self, config: NllbMoeConfig, embed_tokens: nn.Embedding | None = ...) -> None: ...
    def forward(
        self,
        input_ids: torch.Tensor | None = ...,
        attention_mask: torch.Tensor | None = ...,
        encoder_hidden_states: torch.Tensor | None = ...,
        encoder_attention_mask: torch.Tensor | None = ...,
        head_mask: torch.Tensor | None = ...,
        cross_attn_head_mask: torch.Tensor | None = ...,
        past_key_values: list[torch.FloatTensor] | None = ...,
        inputs_embeds: torch.Tensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        output_router_logits: bool | None = ...,
        return_dict: bool | None = ...,
    ):  # -> tuple[Any | tuple[()] | tuple[Any, ...] | tuple[Tensor | Any, ...], ...] | MoEModelOutputWithPastAndCrossAttentions:
        r"""
        Args:
            input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            encoder_hidden_states (`torch.FloatTensor` of shape `(batch_size, encoder_sequence_length, hidden_size)`, *optional*):
                Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention
                of the decoder.
            encoder_attention_mask (`torch.LongTensor` of shape `(batch_size, encoder_sequence_length)`, *optional*):
                Mask to avoid performing cross-attention on padding tokens indices of encoder input_ids. Mask values
                selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            cross_attn_head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the cross-attention modules in the decoder to avoid performing
                cross-attention on hidden heads. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
                Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of
                shape `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of
                shape `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`.

                Contains pre-computed hidden-states (key and values in the self-attention blocks and in the
                cross-attention blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.

                If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those
                that don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of
                all `decoder_input_ids` of shape `(batch_size, sequence_length)`.
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            output_router_logits (`bool`, *optional*):
                Whether or not to return the logits of all the routers. They are useful for computing the router loss,
                and should not be returned during inference.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """
        ...

@add_start_docstrings(
    "The bare NllbMoe Model outputting raw hidden-states without any specific head on top.", NLLB_MOE_START_DOCSTRING
)
class NllbMoeModel(NllbMoePreTrainedModel):
    _tied_weights_keys = ...
    def __init__(self, config: NllbMoeConfig) -> None: ...
    def get_input_embeddings(self):  # -> NllbMoeScaledWordEmbedding | Module:
        ...
    def set_input_embeddings(self, value):  # -> None:
        ...
    def get_encoder(self):  # -> NllbMoeEncoder:
        ...
    def get_decoder(self):  # -> NllbMoeDecoder:
        ...
    @add_start_docstrings_to_model_forward(NLLB_MOE_INPUTS_DOCSTRING)
    @add_start_docstrings_to_model_forward(NLLB_MOE_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqMoEModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        input_ids: torch.LongTensor | None = ...,
        attention_mask: torch.Tensor | None = ...,
        decoder_input_ids: torch.LongTensor | None = ...,
        decoder_attention_mask: torch.LongTensor | None = ...,
        head_mask: torch.Tensor | None = ...,
        decoder_head_mask: torch.Tensor | None = ...,
        cross_attn_head_mask: torch.Tensor | None = ...,
        encoder_outputs: tuple[tuple[torch.FloatTensor]] | None = ...,
        past_key_values: tuple[tuple[torch.FloatTensor]] | None = ...,
        inputs_embeds: torch.FloatTensor | None = ...,
        decoder_inputs_embeds: torch.FloatTensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        output_router_logits: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple[torch.Tensor] | Seq2SeqMoEModelOutput:
        r"""
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, NllbMoeModel

        >>> tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/random-nllb-moe-2-experts")
        >>> model = SwitchTransformersModel.from_pretrained("hf-internal-testing/random-nllb-moe-2-experts")

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1

        >>> # preprocess: Prepend decoder_input_ids with start token which is pad token for NllbMoeModel
        >>> decoder_input_ids = model._shift_right(decoder_input_ids)

        >>> # forward pass
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```"""
        ...

@add_start_docstrings(
    "The NllbMoe Model with a language modeling head. Can be used for summarization.", NLLB_MOE_START_DOCSTRING
)
class NllbMoeForConditionalGeneration(NllbMoePreTrainedModel, GenerationMixin):
    base_model_prefix = ...
    _tied_weights_keys = ...
    def __init__(self, config: NllbMoeConfig) -> None: ...
    def get_encoder(self):  # -> NllbMoeEncoder:
        ...
    def get_decoder(self):  # -> NllbMoeDecoder:
        ...
    def get_output_embeddings(self):  # -> Linear:
        ...
    def set_output_embeddings(self, new_embeddings):  # -> None:
        ...
    @add_start_docstrings_to_model_forward(NLLB_MOE_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=Seq2SeqMoEOutput, config_class=_CONFIG_FOR_DOC)
    @add_end_docstrings(NLLB_MOE_GENERATION_EXAMPLE)
    def forward(
        self,
        input_ids: torch.LongTensor | None = ...,
        attention_mask: torch.Tensor | None = ...,
        decoder_input_ids: torch.LongTensor | None = ...,
        decoder_attention_mask: torch.LongTensor | None = ...,
        head_mask: torch.Tensor | None = ...,
        decoder_head_mask: torch.Tensor | None = ...,
        cross_attn_head_mask: torch.Tensor | None = ...,
        encoder_outputs: tuple[tuple[torch.FloatTensor]] | None = ...,
        past_key_values: tuple[tuple[torch.FloatTensor]] | None = ...,
        inputs_embeds: torch.FloatTensor | None = ...,
        decoder_inputs_embeds: torch.FloatTensor | None = ...,
        labels: torch.LongTensor | None = ...,
        use_cache: bool | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        output_router_logits: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple[torch.Tensor] | Seq2SeqMoEOutput:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
            config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
            (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

        Returns:
        """
        ...

__all__ = [
    "NllbMoeForConditionalGeneration",
    "NllbMoeModel",
    "NllbMoePreTrainedModel",
    "NllbMoeTop2Router",
    "NllbMoeSparseMLP",
]
