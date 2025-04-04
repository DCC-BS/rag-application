"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

import torch
from torch import nn

from ....modeling_outputs import SequenceClassifierOutput
from ....modeling_utils import PreTrainedModel
from ....utils import (
    ModelOutput,
    add_start_docstrings,
    add_start_docstrings_to_model_forward,
    replace_return_docstrings,
)
from .configuration_tvlt import TvltConfig

"""PyTorch TVLT model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...

@dataclass
class TvltModelOutput(ModelOutput):
    """
    Class for TvltModel's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        last_pixel_hidden_state (`torch.FloatTensor` of shape `(batch_size, pixel_sequence_length, hidden_size)`):
            Pixel sequence of hidden-states at the output of the last layer of the model.
        last_audio_hidden_state (`torch.FloatTensor` of shape `(batch_size, audio_sequence_length, hidden_size)`):
            Audio sequence of hidden-states at the output of the last layer of the model.
        pixel_label_masks (`torch.FloatTensor` of shape `(batch_size, pixel_patch_length)`):
            Tensor indicating which pixel patches are masked (1) and which are not (0).
        audio_label_masks (`torch.FloatTensor` of shape `(batch_size, audio_patch_length)`):
            Tensor indicating which audio patches are masked (1) and which are not (0).
        pixel_ids_restore (`torch.LongTensor` of shape `(batch_size, pixel_patch_length)`):
            Tensor containing the ids permutation of pixel masking.
        audio_ids_restore (`torch.LongTensor` of shape `(batch_size, audio_patch_length)`):
            Tensor containing the ids permutation of audio masking.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings and one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """

    last_hidden_state: torch.FloatTensor = ...
    last_pixel_hidden_state: torch.FloatTensor = ...
    last_audio_hidden_state: torch.FloatTensor = ...
    pixel_label_masks: torch.LongTensor = ...
    audio_label_masks: torch.LongTensor = ...
    pixel_ids_restore: torch.LongTensor = ...
    audio_ids_restore: torch.LongTensor = ...
    hidden_states: tuple[torch.FloatTensor, ...] | None = ...
    attentions: tuple[torch.FloatTensor, ...] | None = ...

@dataclass
class TvltDecoderOutput(ModelOutput):
    """
    Class for TvltDecoder's outputs, with potential hidden states and attentions.

    Args:
        logits (`torch.FloatTensor` of shape `(batch_size, patch_size ** 2 * num_channels)`):
            Pixel reconstruction logits.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings and one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """

    logits: torch.FloatTensor = ...
    hidden_states: tuple[torch.FloatTensor, ...] | None = ...
    attentions: tuple[torch.FloatTensor, ...] | None = ...

@dataclass
class TvltForPreTrainingOutput(ModelOutput):
    """
    Class for TvltForPreTraining's outputs, with potential hidden states and attentions.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`):
            Pixel reconstruction loss.
        matching_logits (`torch.FloatTensor` of shape `(batch_size, 1)`):
            Matching objective logits.
        pixel_logits (`torch.FloatTensor` of shape
            `(batch_size, pixel_patch_length, image_patch_size ** 3 * pixel_num_channels)`): Pixel reconstruction
            logits.
        audio_logits (`torch.FloatTensor` of shape
            `(batch_size, audio_patch_length, image_patch_size[0] * image_patch_size[1])`): Audio reconstruction
            logits.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings and one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """

    loss: torch.FloatTensor | None = ...
    matching_logits: torch.FloatTensor = ...
    pixel_logits: torch.FloatTensor = ...
    audio_logits: torch.FloatTensor = ...
    hidden_states: tuple[torch.FloatTensor, ...] | None = ...
    attentions: tuple[torch.FloatTensor, ...] | None = ...

def generate_pixel_mask_noise(pixel_values, pixel_mask=..., mask_ratio=...):  # -> tuple[Tensor, int]:
    """Generate noise for audio masking."""
    ...

def generate_audio_mask_noise(
    audio_values, audio_mask=..., mask_ratio=..., mask_type=..., freq_len=...
):  # -> tuple[Tensor | Any, int]:
    """Generate noise for audio masking."""
    ...

def random_masking(
    sequence, noise, len_keep, attention_masks=...
):  # -> tuple[Tensor, Tensor | None, Any | Tensor, Tensor]:
    """
    Perform random masking by per-sample shuffling on frame-level. Per-sample shuffling is done by argsort random
    noise. sequence: [batch_size, seq_len, hidden_dim], sequence
    """
    ...

class TvltPixelEmbeddings(nn.Module):
    """Construct the patch and position embeddings."""
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values, attention_masks=...):  # -> tuple[Any, Any | None]:
        ...

class TvltAudioEmbeddings(nn.Module):
    """Construct the patch and position embeddings."""
    def __init__(self, config) -> None: ...
    def forward(self, audio_values, attention_masks=...):  # -> tuple[Any, Any | None]:
        ...

class TvltPixelPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor: ...

class TvltAudioPatchEmbeddings(nn.Module):
    """
    This class turns `audio_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    def __init__(self, config) -> None: ...
    def forward(self, audio_values: torch.Tensor) -> torch.Tensor: ...

class TvltSelfAttention(nn.Module):
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(
        self, hidden_states, attention_mask=..., head_mask=..., output_attentions=...
    ):  # -> tuple[Tensor, Any] | tuple[Tensor]:
        ...

class TvltSelfOutput(nn.Module):
    """
    The residual connection is defined in TvltLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    def __init__(self, config: TvltConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class TvltAttention(nn.Module):
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads):  # -> None:
        ...
    def forward(self, hidden_states, attention_mask=..., head_mask=..., output_attentions=...):  # -> Any:
        ...

class TvltIntermediate(nn.Module):
    def __init__(self, config: TvltConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TvltOutput(nn.Module):
    def __init__(self, config: TvltConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class TvltLayer(nn.Module):
    """This corresponds to the Block class in the timm implementation."""
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask=..., head_mask=..., output_attentions=...):  # -> Any:
        ...

class TvltEncoder(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(
        self,
        hidden_states,
        attention_mask=...,
        head_mask=...,
        output_attentions=...,
        output_hidden_states=...,
        return_dict=...,
    ):  # -> tuple[Any | tuple[Any, ...] | tuple[()], ...] | BaseModelOutput:
        ...

class TvltPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = TvltConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...

TVLT_START_DOCSTRING = ...
TVLT_INPUTS_DOCSTRING = ...

@add_start_docstrings(
    "The bare TVLT Model transformer outputting raw hidden-states without any specific head on top.",
    TVLT_START_DOCSTRING,
)
class TvltModel(TvltPreTrainedModel):
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self):  # -> tuple[TvltPixelPatchEmbeddings, TvltAudioPatchEmbeddings]:
        ...
    @add_start_docstrings_to_model_forward(TVLT_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TvltModelOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        pixel_values: torch.FloatTensor,
        audio_values: torch.FloatTensor,
        pixel_mask: torch.FloatTensor | None = ...,
        audio_mask: torch.FloatTensor | None = ...,
        mask_pixel: bool = ...,
        mask_audio: bool = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple[torch.FloatTensor] | TvltModelOutput:
        r"""
        Returns:

        Examples:

        ```python
        >>> from transformers import TvltProcessor, TvltModel
        >>> import numpy as np
        >>> import torch

        >>> num_frames = 8
        >>> images = list(np.random.randn(num_frames, 3, 224, 224))
        >>> audio = list(np.random.randn(10000))

        >>> processor = TvltProcessor.from_pretrained("ZinengTang/tvlt-base")
        >>> model = TvltModel.from_pretrained("ZinengTang/tvlt-base")

        >>> input_dict = processor(images, audio, sampling_rate=44100, return_tensors="pt")

        >>> outputs = model(**input_dict)
        >>> loss = outputs.loss
        ```"""
        ...

class TvltDecoder(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(
        self, hidden_states, output_attentions=..., output_hidden_states=..., return_dict=...
    ):  # -> tuple[Any | tuple[Any, ...] | tuple[()], ...] | TvltDecoderOutput:
        ...

@add_start_docstrings(
    "The TVLT Model transformer with the decoder on top for self-supervised pre-training.", TVLT_START_DOCSTRING
)
class TvltForPreTraining(TvltPreTrainedModel):
    def __init__(self, config) -> None: ...
    def patchify_pixel(self, pixel_values):  # -> Tensor:
        """
        pixel_values: [batch_size, num_frames, 3, height, width]
        """
        ...

    def patchify_audio(self, audio_values):  # -> Tensor:
        """
        audio_values: [batch_size, 1, height, width]
        """
        ...

    def pixel_mae_loss(self, pixel_values, pixel_predictions, mask): ...
    def audio_mae_loss(self, audio_values, audio_predictions, mask): ...
    def concatenate_mask(self, mask_token, sequence, ids_restore):  # -> Tensor:
        ...
    @add_start_docstrings_to_model_forward(TVLT_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TvltForPreTrainingOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        pixel_values: torch.FloatTensor,
        audio_values: torch.FloatTensor,
        pixel_mask: torch.FloatTensor | None = ...,
        audio_mask: torch.FloatTensor | None = ...,
        labels: torch.LongTensor | None = ...,
        pixel_values_mixed: torch.FloatTensor | None = ...,
        pixel_mask_mixed: torch.FloatTensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple[torch.FloatTensor] | TvltForPreTrainingOutput:
        r"""
        pixel_values_mixed (`torch.FloatTensor` of shape `(batch_size, num_frames, num_channels, height, width)`):
            Pixel values that mix positive and negative samples in Tvlt vision-audio matching. Audio values can be
            obtained using [`TvltProcessor`]. See [`TvltProcessor.__call__`] for details.

        pixel_mask_mixed (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`):
            Pixel masks of pixel_values_mixed. Pixel values mixed can be obtained using [`TvltProcessor`]. See
            [`TvltProcessor.__call__`] for details.

        labels (`torch.LongTensor` of shape `(batch_size, num_labels)`, *optional*):
            Labels for computing the vision audio matching loss. Indices should be in `[0, 1]`. num_labels has to be 1.

        Return:

        Examples:

        ```python
        >>> from transformers import TvltProcessor, TvltForPreTraining
        >>> import numpy as np
        >>> import torch

        >>> num_frames = 8
        >>> images = list(np.random.randn(num_frames, 3, 224, 224))
        >>> images_mixed = list(np.random.randn(num_frames, 3, 224, 224))
        >>> audio = list(np.random.randn(10000))
        >>> processor = TvltProcessor.from_pretrained("ZinengTang/tvlt-base")
        >>> model = TvltForPreTraining.from_pretrained("ZinengTang/tvlt-base")
        >>> input_dict = processor(
        ...     images, audio, images_mixed, sampling_rate=44100, mask_pixel=True, mask_audio=True, return_tensors="pt"
        ... )

        >>> outputs = model(**input_dict)
        >>> loss = outputs.loss
        ```"""
        ...

class TvltPooler(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states):  # -> Any:
        ...

class TvltMatchingHead(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states):  # -> Any:
        ...

class TvltMAEHead(nn.Module):
    def __init__(self, config, output_dim=...) -> None: ...
    def forward(self, hidden_states):  # -> Any:
        ...

@add_start_docstrings(
    """
    Tvlt Model transformer with a classifier head on top (an MLP on top of the final hidden state of the [CLS] token)
    for audiovisual classification tasks, e.g. CMU-MOSEI Sentiment Analysis and Audio to Video Retrieval.
    """,
    TVLT_START_DOCSTRING,
)
class TvltForAudioVisualClassification(TvltPreTrainedModel):
    def __init__(self, config) -> None: ...
    @add_start_docstrings_to_model_forward(TVLT_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=SequenceClassifierOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        pixel_values: torch.FloatTensor,
        audio_values: torch.FloatTensor,
        pixel_mask: torch.FloatTensor | None = ...,
        audio_mask: torch.FloatTensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        labels: torch.LongTensor | None = ...,
    ) -> tuple[torch.FloatTensor] | SequenceClassifierOutput:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, num_labels)`, *optional*):
            Labels for computing the audiovisual loss. Indices should be in `[0, ..., num_classes-1]` where num_classes
            refers to the number of classes in audiovisual tasks.

        Return:

        Examples:
        ```python
        >>> from transformers import TvltProcessor, TvltForAudioVisualClassification
        >>> import numpy as np
        >>> import torch

        >>> num_frames = 8
        >>> images = list(np.random.randn(num_frames, 3, 224, 224))
        >>> audio = list(np.random.randn(10000))
        >>> processor = TvltProcessor.from_pretrained("ZinengTang/tvlt-base")
        >>> model = TvltForAudioVisualClassification.from_pretrained("ZinengTang/tvlt-base")
        >>> input_dict = processor(images, audio, sampling_rate=44100, return_tensors="pt")

        >>> outputs = model(**input_dict)
        >>> loss = outputs.loss
        ```"""
        ...
