"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable

import flax
import flax.linen as nn
import jax
import jax.numpy as jnp
from flax.core.frozen_dict import FrozenDict

from ...modeling_flax_utils import FlaxPreTrainedModel
from ...utils import ModelOutput, add_start_docstrings, add_start_docstrings_to_model_forward
from .configuration_big_bird import BigBirdConfig

logger = ...
_CHECKPOINT_FOR_DOC = ...
_CONFIG_FOR_DOC = ...
remat = ...

@flax.struct.dataclass
class FlaxBigBirdForPreTrainingOutput(ModelOutput):
    """
    Output type of [`BigBirdForPreTraining`].

    Args:
        prediction_logits (`jnp.ndarray` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        seq_relationship_logits (`jnp.ndarray` of shape `(batch_size, 2)`):
            Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
            before SoftMax).
        hidden_states (`tuple(jnp.ndarray)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `jnp.ndarray` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(jnp.ndarray)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `jnp.ndarray` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """

    prediction_logits: jnp.ndarray = ...
    seq_relationship_logits: jnp.ndarray = ...
    hidden_states: tuple[jnp.ndarray] | None = ...
    attentions: tuple[jnp.ndarray] | None = ...

@flax.struct.dataclass
class FlaxBigBirdForQuestionAnsweringModelOutput(ModelOutput):
    """
    Base class for outputs of question answering models.

    Args:
        start_logits (`jnp.ndarray` of shape `(batch_size, sequence_length)`):
            Span-start scores (before SoftMax).
        end_logits (`jnp.ndarray` of shape `(batch_size, sequence_length)`):
            Span-end scores (before SoftMax).
        pooled_output (`jnp.ndarray` of shape `(batch_size, hidden_size)`):
            pooled_output returned by FlaxBigBirdModel.
        hidden_states (`tuple(jnp.ndarray)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `jnp.ndarray` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(jnp.ndarray)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `jnp.ndarray` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """

    start_logits: jnp.ndarray = ...
    end_logits: jnp.ndarray = ...
    pooled_output: jnp.ndarray = ...
    hidden_states: tuple[jnp.ndarray] | None = ...
    attentions: tuple[jnp.ndarray] | None = ...

BIG_BIRD_START_DOCSTRING = ...
BIG_BIRD_INPUTS_DOCSTRING = ...

class FlaxBigBirdEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""

    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, input_ids, token_type_ids, position_ids, attention_mask, deterministic: bool = ...): ...

class FlaxBigBirdSelfAttention(nn.Module):
    config: BigBirdConfig
    causal: bool = ...
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        hidden_states,
        attention_mask,
        layer_head_mask,
        key_value_states: jnp.ndarray | None = ...,
        init_cache: bool = ...,
        deterministic=...,
        output_attentions: bool = ...,
    ):  # -> tuple[Any, Any] | tuple[Any]:
        ...

class FlaxBigBirdBlockSparseAttention(nn.Module):
    config: BigBirdConfig
    block_sparse_seed: int = ...
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    @staticmethod
    def transpose_for_scores(x, n_heads, head_size): ...
    def __call__(
        self, hidden_states, attention_mask, deterministic=..., output_attentions=...
    ):  # -> tuple[Any, None] | tuple[Any]:
        ...
    @staticmethod
    def create_masks_for_block_sparse_attn(attention_mask, block_size: int):  # -> tuple[Any, Any, Any, Any]:
        ...
    def bigbird_block_sparse_attention(
        self,
        query_layer,
        key_layer,
        value_layer,
        band_mask,
        from_mask,
        to_mask,
        from_blocked_mask,
        to_blocked_mask,
        n_heads,
        head_size,
        indices_prng_key: jax.random.PRNGKey | None = ...,
        deterministic: bool | None = ...,
        plan_from_length=...,
        plan_num_rand_blocks=...,
        output_attentions=...,
    ):  # -> tuple[Any, None]:
        ...
    @staticmethod
    def jax_gather(params, indices, batch_dims=...):
        """
        Gather the indices from params correctly (equivalent to tf.gather but with modifications)

        Args:
            params: (bsz, n_heads, num_blocks, block_size, head_dim)
            indices: (<num_blocks, 1)
        """
        ...

class FlaxBigBirdSelfOutput(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, hidden_states, input_tensor, deterministic: bool = ...): ...

class FlaxBigBirdAttention(nn.Module):
    config: BigBirdConfig
    layer_id: int = ...
    causal: bool = ...
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        hidden_states,
        attention_mask,
        layer_head_mask,
        key_value_states=...,
        init_cache=...,
        deterministic=...,
        output_attentions: bool = ...,
    ):  # -> tuple[Any, Any | None] | tuple[Any]:
        ...

class FlaxBigBirdIntermediate(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, hidden_states): ...

class FlaxBigBirdOutput(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, hidden_states, attention_output, deterministic: bool = ...): ...

class FlaxBigBirdLayer(nn.Module):
    config: BigBirdConfig
    layer_id: int = ...
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        hidden_states,
        attention_mask,
        layer_head_mask,
        encoder_hidden_states: jnp.ndarray | None = ...,
        encoder_attention_mask: jnp.ndarray | None = ...,
        init_cache: bool = ...,
        deterministic: bool = ...,
        output_attentions: bool = ...,
    ):  # -> tuple[Any, Any | None, Any | None] | tuple[Any, Any | None] | tuple[Any]:
        ...

class FlaxBigBirdLayerCollection(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        hidden_states,
        attention_mask,
        head_mask,
        encoder_hidden_states: jnp.ndarray | None = ...,
        encoder_attention_mask: jnp.ndarray | None = ...,
        init_cache: bool = ...,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...] | FlaxBaseModelOutputWithPastAndCrossAttentions:
        ...

class FlaxBigBirdEncoder(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        hidden_states,
        attention_mask,
        head_mask,
        encoder_hidden_states: jnp.ndarray | None = ...,
        encoder_attention_mask: jnp.ndarray | None = ...,
        init_cache: bool = ...,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...] | FlaxBaseModelOutputWithPastAndCrossAttentions:
        ...

class FlaxBigBirdPredictionHeadTransform(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, hidden_states): ...

class FlaxBigBirdLMPredictionHead(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    bias_init: Callable[..., jnp.ndarray] = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, hidden_states, shared_embedding=...): ...

class FlaxBigBirdOnlyMLMHead(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, hidden_states, shared_embedding=...): ...

class FlaxBigBirdPreTrainingHeads(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, hidden_states, pooled_output, shared_embedding=...):  # -> tuple[Any, Any]:
        ...

class FlaxBigBirdPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = BigBirdConfig
    base_model_prefix = ...
    module_class: nn.Module = ...
    def __init__(
        self,
        config: BigBirdConfig,
        input_shape: tuple | None = ...,
        seed: int = ...,
        dtype: jnp.dtype = ...,
        _do_init: bool = ...,
        gradient_checkpointing: bool = ...,
        **kwargs,
    ) -> None: ...
    def enable_gradient_checkpointing(self):  # -> None:
        ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: tuple, params: FrozenDict = ...) -> FrozenDict: ...
    def init_cache(self, batch_size, max_length):
        r"""
        Args:
            batch_size (`int`):
                batch_size used for fast auto-regressive decoding. Defines the batch size of the initialized cache.
            max_length (`int`):
                maximum possible length for auto-regressive decoding. Defines the sequence length of the initialized
                cache.
        """
        ...

    @add_start_docstrings_to_model_forward(BIG_BIRD_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    def __call__(
        self,
        input_ids,
        attention_mask=...,
        token_type_ids=...,
        position_ids=...,
        head_mask=...,
        encoder_hidden_states=...,
        encoder_attention_mask=...,
        params: dict = ...,
        dropout_rng: jax.random.PRNGKey | None = ...,
        indices_rng: jax.random.PRNGKey | None = ...,
        train: bool = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        past_key_values: dict = ...,
    ): ...

class FlaxBigBirdModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    add_pooling_layer: bool = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        input_ids,
        attention_mask,
        token_type_ids,
        position_ids,
        head_mask,
        encoder_hidden_states: jnp.ndarray | None = ...,
        encoder_attention_mask: jnp.ndarray | None = ...,
        init_cache: bool = ...,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | Any | tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | FlaxBaseModelOutputWithPoolingAndCrossAttentions:
        ...

@add_start_docstrings(
    "The bare BigBird Model transformer outputting raw hidden-states without any specific head on top.",
    BIG_BIRD_START_DOCSTRING,
)
class FlaxBigBirdModel(FlaxBigBirdPreTrainedModel):
    module_class = ...

class FlaxBigBirdForPreTrainingModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        input_ids,
        attention_mask,
        token_type_ids,
        position_ids,
        head_mask,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any, Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | Any | FlaxBigBirdForPreTrainingOutput:
        ...

@add_start_docstrings(
    """
    BigBird Model with two heads on top as done during the pretraining: a `masked language modeling` head and a `next
    sentence prediction (classification)` head.
    """,
    BIG_BIRD_START_DOCSTRING,
)
class FlaxBigBirdForPreTraining(FlaxBigBirdPreTrainedModel):
    module_class = ...

FLAX_BIG_BIRD_FOR_PRETRAINING_DOCSTRING = ...

class FlaxBigBirdForMaskedLMModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        input_ids,
        attention_mask,
        token_type_ids,
        position_ids,
        head_mask,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | Any | tuple[Any, Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | FlaxMaskedLMOutput:
        ...

@add_start_docstrings("""BigBird Model with a `language modeling` head on top.""", BIG_BIRD_START_DOCSTRING)
class FlaxBigBirdForMaskedLM(FlaxBigBirdPreTrainedModel):
    module_class = ...

class FlaxBigBirdClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""

    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, features, deterministic=...): ...

class FlaxBigBirdForSequenceClassificationModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        input_ids,
        attention_mask,
        token_type_ids,
        position_ids,
        head_mask,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | Any | FlaxSequenceClassifierOutput:
        ...

@add_start_docstrings(
    """
    BigBird Model transformer with a sequence classification/regression head on top (a linear layer on top of the
    pooled output) e.g. for GLUE tasks.
    """,
    BIG_BIRD_START_DOCSTRING,
)
class FlaxBigBirdForSequenceClassification(FlaxBigBirdPreTrainedModel):
    module_class = ...

class FlaxBigBirdForMultipleChoiceModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        input_ids,
        attention_mask,
        token_type_ids,
        position_ids,
        head_mask,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | Any | FlaxMultipleChoiceModelOutput:
        ...

@add_start_docstrings(
    """
    BigBird Model with a multiple choice classification head on top (a linear layer on top of the pooled output and a
    softmax) e.g. for RocStories/SWAG tasks.
    """,
    BIG_BIRD_START_DOCSTRING,
)
class FlaxBigBirdForMultipleChoice(FlaxBigBirdPreTrainedModel):
    module_class = ...
    def __init__(
        self,
        config: BigBirdConfig,
        input_shape: tuple | None = ...,
        seed: int = ...,
        dtype: jnp.dtype = ...,
        _do_init: bool = ...,
        **kwargs,
    ) -> None: ...

class FlaxBigBirdForTokenClassificationModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        input_ids,
        attention_mask,
        token_type_ids,
        position_ids,
        head_mask,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | Any | tuple[Any, Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | FlaxTokenClassifierOutput:
        ...

@add_start_docstrings(
    """
    BigBird Model with a token classification head on top (a linear layer on top of the hidden-states output) e.g. for
    Named-Entity-Recognition (NER) tasks.
    """,
    BIG_BIRD_START_DOCSTRING,
)
class FlaxBigBirdForTokenClassification(FlaxBigBirdPreTrainedModel):
    module_class = ...

class FlaxBigBirdForQuestionAnsweringHead(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    def setup(self):  # -> None:
        ...
    def __call__(self, encoder_output, deterministic=...): ...

class FlaxBigBirdForQuestionAnsweringModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    add_pooling_layer: bool = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        input_ids,
        attention_mask,
        token_type_ids,
        position_ids,
        head_mask,
        logits_mask=...,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any, Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | Any | tuple[Any, Any, Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | FlaxBigBirdForQuestionAnsweringModelOutput:
        ...

@add_start_docstrings(
    """
    BigBird Model with a span classification head on top for extractive question-answering tasks like SQuAD (a linear
    layers on top of the hidden-states output to compute `span start logits` and `span end logits`).
    """,
    BIG_BIRD_START_DOCSTRING,
)
class FlaxBigBirdForQuestionAnswering(FlaxBigBirdPreTrainedModel):
    module_class = ...
    @add_start_docstrings_to_model_forward(BIG_BIRD_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    def __call__(
        self,
        input_ids,
        attention_mask=...,
        token_type_ids=...,
        position_ids=...,
        head_mask=...,
        question_lengths=...,
        params: dict = ...,
        dropout_rng: jax.random.PRNGKey | None = ...,
        indices_rng: jax.random.PRNGKey | None = ...,
        train: bool = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ): ...
    @staticmethod
    def prepare_question_mask(q_lengths, maxlen: int): ...

class FlaxBigBirdForCausalLMModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype = ...
    gradient_checkpointing: bool = ...
    def setup(self):  # -> None:
        ...
    def __call__(
        self,
        input_ids,
        attention_mask,
        position_ids,
        token_type_ids: jnp.ndarray | None = ...,
        head_mask: jnp.ndarray | None = ...,
        encoder_hidden_states: jnp.ndarray | None = ...,
        encoder_attention_mask: jnp.ndarray | None = ...,
        init_cache: bool = ...,
        deterministic: bool = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | Any | tuple[Any, Any, *tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...]] | FlaxCausalLMOutputWithCrossAttentions:
        ...

@add_start_docstrings(
    """
    BigBird Model with a language modeling head on top (a linear layer on top of the hidden-states output) e.g for
    autoregressive tasks.
    """,
    BIG_BIRD_START_DOCSTRING,
)
class FlaxBigBirdForCausalLM(FlaxBigBirdPreTrainedModel):
    module_class = ...
    def prepare_inputs_for_generation(
        self, input_ids, max_length, attention_mask: jax.Array | None = ...
    ):  # -> dict[str, Any]:
        ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...

__all__ = [
    "FlaxBigBirdForCausalLM",
    "FlaxBigBirdForMaskedLM",
    "FlaxBigBirdForMultipleChoice",
    "FlaxBigBirdForPreTraining",
    "FlaxBigBirdForQuestionAnswering",
    "FlaxBigBirdForSequenceClassification",
    "FlaxBigBirdForTokenClassification",
    "FlaxBigBirdModel",
    "FlaxBigBirdPreTrainedModel",
]
