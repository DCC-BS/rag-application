"""
This type stub file was generated by pyright.
"""

import torch
from torch import nn

from ...modeling_outputs import BaseModelOutput, CausalLMOutput, SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel
from ...utils import (
    add_code_sample_docstrings,
    add_start_docstrings,
    add_start_docstrings_to_model_forward,
    is_flash_attn_2_available,
    replace_return_docstrings,
)
from .configuration_hubert import HubertConfig

"""PyTorch Hubert model."""
if is_flash_attn_2_available(): ...
logger = ...
_HIDDEN_STATES_START_POSITION = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_CTC_EXPECTED_OUTPUT = ...
_CTC_EXPECTED_LOSS = ...
_SEQ_CLASS_CHECKPOINT = ...
_SEQ_CLASS_EXPECTED_OUTPUT = ...
_SEQ_CLASS_EXPECTED_LOSS = ...

class HubertNoLayerNormConvLayer(nn.Module):
    def __init__(self, config, layer_id=...) -> None: ...
    def forward(self, hidden_states): ...

class HubertLayerNormConvLayer(nn.Module):
    def __init__(self, config, layer_id=...) -> None: ...
    def forward(self, hidden_states): ...

class HubertGroupNormConvLayer(nn.Module):
    def __init__(self, config, layer_id=...) -> None: ...
    def forward(self, hidden_states): ...

class HubertPositionalConvEmbedding(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class HubertSamePadLayer(nn.Module):
    def __init__(self, num_conv_pos_embeddings) -> None: ...
    def forward(self, hidden_states): ...

class HubertFeatureEncoder(nn.Module):
    """Construct the features from raw audio waveform"""
    def __init__(self, config) -> None: ...
    def forward(self, input_values):  # -> Any:
        ...

class HubertFeatureExtractor(HubertFeatureEncoder):
    def __init__(self, config) -> None: ...

class HubertFeatureProjection(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states):  # -> Any:
        ...

class HubertAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        dropout: float = ...,
        is_decoder: bool = ...,
        bias: bool = ...,
        is_causal: bool = ...,
        config: HubertConfig | None = ...,
    ) -> None: ...
    def forward(
        self,
        hidden_states: torch.Tensor,
        key_value_states: torch.Tensor | None = ...,
        past_key_value: tuple[torch.Tensor] | None = ...,
        attention_mask: torch.Tensor | None = ...,
        layer_head_mask: torch.Tensor | None = ...,
        output_attentions: bool = ...,
    ) -> tuple[torch.Tensor, torch.Tensor | None, tuple[torch.Tensor] | None]:
        """Input shape: Batch x Time x Channel"""
        ...

class HubertFlashAttention2(HubertAttention):
    """
    Hubert flash attention module. This module inherits from `HubertAttention` as the weights of the module stays
    untouched. The only required change would be on the forward pass where it needs to correctly call the public API of
    flash attention and deal with padding tokens in case the input contains any of them.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def forward(
        self,
        hidden_states: torch.Tensor,
        key_value_states: torch.Tensor | None = ...,
        past_key_value: tuple[torch.Tensor] | None = ...,
        attention_mask: torch.Tensor | None = ...,
        layer_head_mask: torch.Tensor | None = ...,
        output_attentions: bool = ...,
    ) -> tuple[torch.Tensor, torch.Tensor | None, tuple[torch.Tensor] | None]: ...

class HubertSdpaAttention(HubertAttention):
    def forward(
        self,
        hidden_states: torch.Tensor,
        key_value_states: torch.Tensor | None = ...,
        past_key_value: tuple[torch.Tensor] | None = ...,
        attention_mask: torch.Tensor | None = ...,
        layer_head_mask: torch.Tensor | None = ...,
        output_attentions: bool = ...,
    ) -> tuple[torch.Tensor, torch.Tensor | None, tuple[torch.Tensor] | None]:
        """Input shape: Batch x Time x Channel"""
        ...

HUBERT_ATTENTION_CLASSES = ...

class HubertFeedForward(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states):  # -> Any:
        ...

class HubertEncoderLayer(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask=..., output_attentions=...):  # -> tuple[Any, Any] | tuple[Any]:
        ...

class HubertAttnAdapterLayer(nn.Module):
    def __init__(self, config) -> None:
        """
        Implements adapter modules directly with 3D tensor weight as parameters and without using ModuleList to speed
        up training throughput.
        """
        ...

    def forward(self, hidden_states: torch.FloatTensor):  # -> FloatTensor:
        ...

class HubertEncoderLayerStableLayerNorm(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(
        self, hidden_states: torch.Tensor, attention_mask: torch.Tensor | None = ..., output_attentions: bool = ...
    ):  # -> tuple[Tensor, Any] | tuple[Tensor]:
        ...

class HubertEncoder(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(
        self,
        hidden_states: torch.tensor,
        attention_mask: torch.Tensor | None = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ):  # -> tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...] | BaseModelOutput:
        ...

class HubertEncoderStableLayerNorm(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(
        self, hidden_states, attention_mask=..., output_attentions=..., output_hidden_states=..., return_dict=...
    ):  # -> tuple[Any | tuple[Any, ...] | tuple[()] | tuple[Any | None, ...], ...] | BaseModelOutput:
        ...

class HubertPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = HubertConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...
    _supports_flash_attn_2 = ...
    _supports_sdpa = ...

HUBERT_START_DOCSTRING = ...
HUBERT_INPUTS_DOCSTRING = ...

@add_start_docstrings(
    "The bare Hubert Model transformer outputting raw hidden-states without any specific head on top.",
    HUBERT_START_DOCSTRING,
)
class HubertModel(HubertPreTrainedModel):
    def __init__(self, config: HubertConfig) -> None: ...
    @add_start_docstrings_to_model_forward(HUBERT_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=BaseModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        input_values: torch.Tensor | None,
        attention_mask: torch.Tensor | None = ...,
        mask_time_indices: torch.FloatTensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | BaseModelOutput:
        """

        Returns:

        Example:

        ```python
        >>> from transformers import AutoProcessor, HubertModel
        >>> from datasets import load_dataset
        >>> import soundfile as sf

        >>> processor = AutoProcessor.from_pretrained("facebook/hubert-large-ls960-ft")
        >>> model = HubertModel.from_pretrained("facebook/hubert-large-ls960-ft")


        >>> def map_to_array(batch):
        ...     speech, _ = sf.read(batch["file"])
        ...     batch["speech"] = speech
        ...     return batch


        >>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
        >>> ds = ds.map(map_to_array)

        >>> input_values = processor(ds["speech"][0], return_tensors="pt").input_values  # Batch size 1
        >>> hidden_states = model(input_values).last_hidden_state
        ```"""
        ...

@add_start_docstrings(
    """Hubert Model with a `language modeling` head on top for Connectionist Temporal Classification (CTC).""",
    HUBERT_START_DOCSTRING,
)
class HubertForCTC(HubertPreTrainedModel):
    def __init__(self, config, target_lang: str | None = ...) -> None: ...
    def tie_weights(self):  # -> None:
        """
        This method overwrites [`~PreTrainedModel.tie_weights`] so that adapter weights can be correctly loaded when
        passing `target_lang=...` to `from_pretrained(...)`.

        This method is **not** supposed to be called by the user and is prone to be changed in the future.
        """
        ...

    def freeze_feature_extractor(self):  # -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
        ...

    def freeze_feature_encoder(self):  # -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
        ...

    def freeze_base_model(self):  # -> None:
        """
        Calling this function will disable the gradient computation for the base model so that its parameters will not
        be updated during training. Only the classification head will be updated.
        """
        ...

    @add_start_docstrings_to_model_forward(HUBERT_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=CausalLMOutput,
        config_class=_CONFIG_FOR_DOC,
        expected_output=_CTC_EXPECTED_OUTPUT,
        expected_loss=_CTC_EXPECTED_LOSS,
    )
    def forward(
        self,
        input_values: torch.Tensor | None,
        attention_mask: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        labels: torch.Tensor | None = ...,
    ) -> tuple | CausalLMOutput:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, target_length)`, *optional*):
            Labels for connectionist temporal classification. Note that `target_length` has to be smaller or equal to
            the sequence length of the output logits. Indices are selected in `[-100, 0, ..., config.vocab_size - 1]`.
            All labels set to `-100` are ignored (masked), the loss is only computed for labels in `[0, ...,
            config.vocab_size - 1]`.
        """
        ...

@add_start_docstrings(
    """
    Hubert Model with a sequence classification head on top (a linear layer over the pooled output) for tasks like
    SUPERB Keyword Spotting.
    """,
    HUBERT_START_DOCSTRING,
)
class HubertForSequenceClassification(HubertPreTrainedModel):
    def __init__(self, config) -> None: ...
    def freeze_feature_extractor(self):  # -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameters will
        not be updated during training.
        """
        ...

    def freeze_feature_encoder(self):  # -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
        ...

    def freeze_base_model(self):  # -> None:
        """
        Calling this function will disable the gradient computation for the base model so that its parameters will not
        be updated during training. Only the classification head will be updated.
        """
        ...

    @add_start_docstrings_to_model_forward(HUBERT_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_SEQ_CLASS_CHECKPOINT,
        output_type=SequenceClassifierOutput,
        config_class=_CONFIG_FOR_DOC,
        modality="audio",
        expected_output=_SEQ_CLASS_EXPECTED_OUTPUT,
        expected_loss=_SEQ_CLASS_EXPECTED_LOSS,
    )
    def forward(
        self,
        input_values: torch.Tensor | None,
        attention_mask: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        labels: torch.Tensor | None = ...,
    ) -> tuple | SequenceClassifierOutput:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...

__all__ = ["HubertForCTC", "HubertForSequenceClassification", "HubertModel", "HubertPreTrainedModel"]
