"""
This type stub file was generated by pyright.
"""

import torch
from torch import nn

from ...modeling_outputs import BackboneOutput, BaseModelOutput, BaseModelOutputWithPooling, ImageClassifierOutput
from ...modeling_utils import PreTrainedModel
from ...utils import (
    add_code_sample_docstrings,
    add_start_docstrings,
    add_start_docstrings_to_model_forward,
    replace_return_docstrings,
)
from ...utils.backbone_utils import BackboneMixin
from .configuration_dinov2 import Dinov2Config

"""PyTorch DINOv2 model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_IMAGE_CLASS_CHECKPOINT = ...
_IMAGE_CLASS_EXPECTED_OUTPUT = ...

class Dinov2Embeddings(nn.Module):
    """
    Construct the CLS token, mask token, position and patch embeddings.
    """
    def __init__(self, config: Dinov2Config) -> None: ...
    def interpolate_pos_encoding(self, embeddings: torch.Tensor, height: int, width: int) -> torch.Tensor:
        """
        This method allows to interpolate the pre-trained position encodings, to be able to use the model on higher resolution
        images. This method is also adapted to support torch.jit tracing and interpolation at torch.float32 precision.

        Adapted from:
        - https://github.com/facebookresearch/dino/blob/de9ee3df6cf39fac952ab558447af1fa1365362a/vision_transformer.py#L174-L194, and
        - https://github.com/facebookresearch/dinov2/blob/e1277af2ba9496fbadf7aec6eba56e8d882d1e35/dinov2/models/vision_transformer.py#L179-L211
        """
        ...

    def forward(self, pixel_values: torch.Tensor, bool_masked_pos: torch.Tensor | None = ...) -> torch.Tensor: ...

class Dinov2PatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor: ...

def eager_attention_forward(
    module: nn.Module,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attention_mask: torch.Tensor | None,
    scaling: float,
    dropout: float = ...,
    **kwargs,
):  # -> tuple[Tensor, Tensor]:
    ...

class Dinov2SelfAttention(nn.Module):
    def __init__(self, config: Dinov2Config) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(
        self, hidden_states, head_mask: torch.Tensor | None = ..., output_attentions: bool = ...
    ) -> tuple[torch.Tensor, torch.Tensor] | tuple[torch.Tensor]: ...

class Dinov2SelfOutput(nn.Module):
    """
    The residual connection is defined in Dinov2Layer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    def __init__(self, config: Dinov2Config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class Dinov2Attention(nn.Module):
    def __init__(self, config: Dinov2Config) -> None: ...
    def prune_heads(self, heads: set[int]) -> None: ...
    def forward(
        self, hidden_states: torch.Tensor, head_mask: torch.Tensor | None = ..., output_attentions: bool = ...
    ) -> tuple[torch.Tensor, torch.Tensor] | tuple[torch.Tensor]: ...

class Dinov2LayerScale(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

def drop_path(input: torch.Tensor, drop_prob: float = ..., training: bool = ...) -> torch.Tensor:
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """
    ...

class Dinov2DropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    def __init__(self, drop_prob: float | None = ...) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class Dinov2MLP(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class Dinov2SwiGLUFFN(nn.Module):
    def __init__(self, config) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class Dinov2Layer(nn.Module):
    """This corresponds to the Block class in the original implementation."""
    def __init__(self, config: Dinov2Config) -> None: ...
    def forward(
        self, hidden_states: torch.Tensor, head_mask: torch.Tensor | None = ..., output_attentions: bool = ...
    ) -> tuple[torch.Tensor, torch.Tensor] | tuple[torch.Tensor]: ...

class Dinov2Encoder(nn.Module):
    def __init__(self, config: Dinov2Config) -> None: ...
    def forward(
        self,
        hidden_states: torch.Tensor,
        head_mask: torch.Tensor | None = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ) -> tuple | BaseModelOutput: ...

class Dinov2PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = Dinov2Config
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...
    _supports_sdpa = ...
    _supports_flash_attn_2 = ...

DINOV2_START_DOCSTRING = ...
DINOV2_BASE_INPUTS_DOCSTRING = ...
DINOV2_INPUTS_DOCSTRING = ...

@add_start_docstrings(
    "The bare DINOv2 Model transformer outputting raw hidden-states without any specific head on top.",
    DINOV2_START_DOCSTRING,
)
class Dinov2Model(Dinov2PreTrainedModel):
    def __init__(self, config: Dinov2Config) -> None: ...
    def get_input_embeddings(self) -> Dinov2PatchEmbeddings: ...
    @add_start_docstrings_to_model_forward(DINOV2_BASE_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=BaseModelOutputWithPooling,
        config_class=_CONFIG_FOR_DOC,
        modality="vision",
        expected_output=_EXPECTED_OUTPUT_SHAPE,
    )
    def forward(
        self,
        pixel_values: torch.Tensor | None = ...,
        bool_masked_pos: torch.Tensor | None = ...,
        head_mask: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | BaseModelOutputWithPooling: ...

@add_start_docstrings(
    """
    Dinov2 Model transformer with an image classification head on top (a linear layer on top of the final hidden state
    of the [CLS] token) e.g. for ImageNet.
    """,
    DINOV2_START_DOCSTRING,
)
class Dinov2ForImageClassification(Dinov2PreTrainedModel):
    def __init__(self, config: Dinov2Config) -> None: ...
    @add_start_docstrings_to_model_forward(DINOV2_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_IMAGE_CLASS_CHECKPOINT,
        output_type=ImageClassifierOutput,
        config_class=_CONFIG_FOR_DOC,
        expected_output=_IMAGE_CLASS_EXPECTED_OUTPUT,
    )
    def forward(
        self,
        pixel_values: torch.Tensor | None = ...,
        head_mask: torch.Tensor | None = ...,
        labels: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | ImageClassifierOutput:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...

@add_start_docstrings(
    """
    Dinov2 backbone, to be used with frameworks like DETR and MaskFormer.
    """,
    DINOV2_START_DOCSTRING,
)
class Dinov2Backbone(Dinov2PreTrainedModel, BackboneMixin):
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self) -> Dinov2PatchEmbeddings: ...
    @add_start_docstrings_to_model_forward(DINOV2_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=BackboneOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        pixel_values: torch.Tensor,
        output_hidden_states: bool | None = ...,
        output_attentions: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> BackboneOutput:
        """
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, AutoBackbone
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> processor = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
        >>> model = AutoBackbone.from_pretrained(
        ...     "facebook/dinov2-base", out_features=["stage2", "stage5", "stage8", "stage11"]
        ... )

        >>> inputs = processor(image, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> feature_maps = outputs.feature_maps
        >>> list(feature_maps[-1].shape)
        [1, 768, 16, 16]
        ```"""
        ...

__all__ = ["Dinov2ForImageClassification", "Dinov2Model", "Dinov2PreTrainedModel", "Dinov2Backbone"]
