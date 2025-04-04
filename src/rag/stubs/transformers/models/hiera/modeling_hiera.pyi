"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

import torch
from torch import nn

from ...modeling_outputs import (
    BackboneOutput,
    BaseModelOutput,
    BaseModelOutputWithPooling,
    ImageClassifierOutput,
    ModelOutput,
)
from ...modeling_utils import PreTrainedModel
from ...utils import (
    add_code_sample_docstrings,
    add_start_docstrings,
    add_start_docstrings_to_model_forward,
    replace_return_docstrings,
)
from ...utils.backbone_utils import BackboneMixin
from .configuration_hiera import HieraConfig

"""PyTorch Hiera model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_IMAGE_CLASS_CHECKPOINT = ...
_IMAGE_CLASS_EXPECTED_OUTPUT = ...

@dataclass
class HieraEncoderOutput(ModelOutput):
    """
    Hiera encoder's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`. Thesre are the unrolled hidden states of the model.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, height, width, hidden_size)`. These are the reshaped and re-rolled hidden states of the model.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """

    last_hidden_state: torch.FloatTensor = ...
    hidden_states: tuple[torch.FloatTensor, ...] | None = ...
    attentions: tuple[torch.FloatTensor, ...] | None = ...
    reshaped_hidden_states: tuple[torch.FloatTensor, ...] | None = ...

@dataclass
class HieraModelOutput(ModelOutput):
    """
    Hiera model's outputs that also contains a pooling of the last hidden states.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`torch.FloatTensor` of shape `(batch_size, hidden_size)`, *optional*, returned when `add_pooling_layer=True` is passed):
            Average pooling of the last layer hidden-state.
        bool_masked_pos (`torch.BoolTensor` of shape `(batch_size, sequence_length)`):
            Tensor indicating which patches are masked (0) and which are not (1).
        ids_restore (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
            Tensor containing the original index of the (shuffled) masked patches.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`. These are the unrolled hidden states of the model.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, height, width, hidden_size)`. These are the reshaped and re-rolled hidden states of the model.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """

    last_hidden_state: torch.FloatTensor = ...
    pooler_output: torch.FloatTensor | None = ...
    bool_masked_pos: torch.BoolTensor = ...
    ids_restore: torch.LongTensor = ...
    hidden_states: tuple[torch.FloatTensor, ...] | None = ...
    attentions: tuple[torch.FloatTensor, ...] | None = ...
    reshaped_hidden_states: tuple[torch.FloatTensor, ...] | None = ...

@dataclass
class HieraForImageClassificationOutput(ImageClassifierOutput):
    """
    Hiera image classification outputs.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, `optional`):
            Loss value for the training task.
        logits (`torch.FloatTensor` of shape `(batch_size, num_labels)`):
            Prediction scores of the classification head (logits of the output layer).
        hidden_states (`tuple(torch.FloatTensor)`, `optional`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`. These are the unrolled hidden states of the model.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, `optional`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, `optional`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, height, width, hidden_size)`. These are the reshaped and re-rolled hidden states of the model.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """

    loss: torch.FloatTensor | None = ...
    logits: torch.FloatTensor = ...
    hidden_states: tuple[torch.FloatTensor, ...] | None = ...
    attentions: tuple[torch.FloatTensor, ...] | None = ...
    reshaped_hidden_states: tuple[torch.FloatTensor, ...] | None = ...

@dataclass
class HieraForPreTrainingOutput(ModelOutput):
    """
    Class for HieraForPreTraining's outputs, with potential hidden states and attentions.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`):
            Pixel reconstruction loss.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, patch_size ** 2 * num_channels)`):
            Pixel reconstruction logits.
        bool_masked_pos (`torch.BoolTensor` of shape `(batch_size, sequence_length)`):
            Tensor indicating which patches are masked (0) and which are not (1).
        ids_restore (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
            Tensor containing the original index of the (shuffled) masked patches.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, height, width, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs reshaped to include the spatial dimensions.
    """

    loss: torch.FloatTensor | None = ...
    logits: torch.FloatTensor = ...
    bool_masked_pos: torch.BoolTensor = ...
    ids_restore: torch.LongTensor = ...
    hidden_states: tuple[torch.FloatTensor] | None = ...
    attentions: tuple[torch.FloatTensor] | None = ...
    reshaped_hidden_states: tuple[torch.FloatTensor] | None = ...

class HieraPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    def __init__(self, config, is_mae: bool = ...) -> None: ...
    def masked_conv(
        self, pixel_values: torch.FloatTensor, bool_masked_pos: torch.BoolTensor | None = ...
    ) -> torch.Tensor:
        """Zero-out the masked regions of the input before conv.
        Prevents leakage of masked regions when using overlapping kernels.
        """
        ...

    def random_masking(
        self, pixel_values: torch.FloatTensor, noise: torch.FloatTensor | None = ...
    ) -> tuple[torch.BoolTensor, torch.LongTensor]:
        """
        Perform per-sample random masking by per-sample shuffling. Per-sample shuffling is done by argsort random
        noise.

        Args:
            pixel_values (`torch.FloatTensor` of shape `(batch_size, num_channels, height, width)`)
            noise (`torch.FloatTensor` of shape `(batch_size, num_mask_units)`, *optional*) which is
                mainly used for testing purposes to control randomness and maintain the reproducibility
        """
        ...

    def forward(
        self, pixel_values: torch.FloatTensor, noise: torch.FloatTensor | None = ...
    ) -> tuple[torch.Tensor, torch.BoolTensor | None, torch.LongTensor | None]: ...

class HieraEmbeddings(nn.Module):
    """
    Construct position and patch embeddings.
    """
    def __init__(self, config: HieraConfig, is_mae: bool = ...) -> None: ...
    def interpolate_pos_encoding(
        self, embeddings: torch.Tensor, pos_embeds: torch.Tensor, height: int, width: int
    ) -> torch.Tensor:
        """
        This method allows to interpolate the pre-trained position encodings, to be able to use the model on higher resolution
        images. This method is also adapted to support torch.jit tracing, no class embeddings, and different patch strides.

        Adapted from:
        - https://github.com/facebookresearch/dino/blob/de9ee3df6cf39fac952ab558447af1fa1365362a/vision_transformer.py#L174-L194, and
        - https://github.com/facebookresearch/dinov2/blob/e1277af2ba9496fbadf7aec6eba56e8d882d1e35/dinov2/models/vision_transformer.py#L179-L211
        """
        ...

    def get_position_embedding(
        self, embeddings: torch.Tensor, height: int, width: int, interpolate_pos_encoding: bool
    ) -> torch.FloatTensor: ...
    def forward(
        self,
        pixel_values: torch.FloatTensor,
        noise: torch.FloatTensor | None = ...,
        interpolate_pos_encoding: bool = ...,
    ) -> tuple[torch.Tensor, torch.BoolTensor | None, torch.LongTensor | None]: ...

class HieraMaskUnitAttention(nn.Module):
    """
    Computes either Mask Unit or Global Attention. Also is able to perform query pooling.

    Note: this assumes the tokens have already been flattened and unrolled into mask units.
    """
    def __init__(
        self,
        hidden_size: int,
        hidden_size_output: int,
        num_heads: int,
        query_stride: int = ...,
        window_size: int = ...,
        use_mask_unit_attn: bool = ...,
    ) -> None: ...
    def forward(
        self, hidden_states: torch.Tensor, head_mask: torch.FloatTensor | None = ..., output_attentions: bool = ...
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        """Input should be of shape [batch, tokens, channels]."""
        ...

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

class HieraDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    def __init__(self, drop_prob: float | None = ...) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class HieraMlp(nn.Module):
    def __init__(self, config, dim: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class HieraLayer(nn.Module):
    def __init__(
        self,
        config,
        hidden_size: int,
        hidden_size_output: int,
        num_heads: int,
        drop_path: float = ...,
        query_stride: int = ...,
        window_size: int = ...,
        use_mask_unit_attn: bool = ...,
    ) -> None: ...
    def forward(
        self, hidden_states: torch.Tensor, head_mask: torch.FloatTensor | None = ..., output_attentions: bool = ...
    ) -> tuple[torch.Tensor, torch.Tensor | None]: ...

class HieraStage(nn.Module):
    def __init__(
        self,
        config,
        depth: int,
        hidden_size: int,
        hidden_size_output: int,
        num_heads: int,
        drop_path: list[float],
        query_stride: list[int],
        window_size: int,
        use_mask_unit_attn: bool,
        stage_num: int | None = ...,
    ) -> None: ...
    def forward(
        self, hidden_states: torch.Tensor, head_mask: torch.FloatTensor | None, output_attentions: bool = ...
    ) -> tuple[torch.Tensor, torch.Tensor | None]: ...

def undo_windowing(hidden_states: torch.Tensor, shape: list[int], mask_unit_shape: list[int]) -> torch.Tensor:
    """
    Restore spatial organization by undoing windowed organization of mask units.

    Args:
        hidden_states (`torch.Tensor`): The hidden states tensor of shape `[batch_size, num_mask_unit_height*num_mask_unit_width, hidden_size]`.
        shape (`List[int]`): The original shape of the hidden states tensor before windowing.
        mask_unit_shape (`List[int]`): The shape of the mask units used for windowing.

    Returns:
        torch.Tensor: The restored hidden states tensor of shape [batch_size, num_mask_unit_height*mask_unit_height, num_mask_unit_width*mask_unit_width, hidden_size].
    """
    ...

class HieraEncoder(nn.Module):
    def __init__(self, config: HieraConfig) -> None: ...
    def reroll(
        self, hidden_states: torch.Tensor, stage_idx: int, bool_masked_pos: torch.BoolTensor | None = ...
    ) -> torch.Tensor:
        """
        Roll the given tensor back up to spatial order assuming it's from the given block.

        If no bool_masked_pos is provided returns:
            - [batch_size, height, width, hidden_size]
        If a bool_masked_pos is provided returns:
            - [batch_size, num_mask_units, mask_unit_height, mask_unit_width, hidden_size]
        """
        ...

    def forward(
        self,
        hidden_states: torch.Tensor,
        bool_masked_pos: torch.BoolTensor | None = ...,
        head_mask: torch.FloatTensor | None = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ) -> tuple | BaseModelOutput: ...

def unroll(
    hidden_states: torch.Tensor, image_shape: tuple[int, int], patch_stride: tuple[int, int], schedule: list[list[int]]
) -> torch.Tensor:
    """
    Reorders the tokens such that patches are contiguous in memory.
    E.g., given [batch_size, (height, width), hidden_size] and stride of (stride, stride), this will re-order the tokens as
    [batch_size, (stride, stride, height // stride, width // stride), hidden_size]

    This allows operations like Max2d to be computed as x.view(batch_size, stride*stride, -1, hidden_size).max(dim=1).
    Not only is this faster, but it also makes it easy to support inputs of arbitrary
    dimensions in addition to patch-wise sparsity.

    Performing this operation multiple times in sequence puts entire windows as contiguous
    in memory. For instance, if you applied the stride (2, 2) 3 times, entire windows of
    size 8x8 would be contiguous in memory, allowing operations like mask unit attention
    computed easily and efficiently, while also allowing max to be applied sequentially.

    Note: This means that intermediate values of the model are not in height x width order, so they
    need to be re-rolled if you want to use the intermediate values as a height x width feature map.
    The last block of the network is fine though, since by then the strides are all consumed.
    """
    ...

class HieraPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = HieraConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...

HIERA_START_DOCSTRING = ...
HIERA_INPUTS_DOCSTRING = ...

class HieraPooler(nn.Module):
    def __init__(self, config: HieraConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

@add_start_docstrings(
    "The bare Hiera Model transformer outputting raw hidden-states without any specific head on top.",
    HIERA_START_DOCSTRING,
    """
        add_pooling_layer (`bool`, *optional*, defaults to `True`):
                Whether or not to apply pooling layer.
        is_mae (`bool`, *optional*, defaults to `False`):
                Whether or not to run the model on MAE mode.
    """,
)
class HieraModel(HieraPreTrainedModel):
    def __init__(self, config: HieraConfig, add_pooling_layer: bool = ..., is_mae: bool = ...) -> None: ...
    def get_input_embeddings(self) -> HieraPatchEmbeddings: ...
    @add_start_docstrings_to_model_forward(HIERA_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=HieraModelOutput,
        config_class=_CONFIG_FOR_DOC,
        modality="vision",
        expected_output=_EXPECTED_OUTPUT_SHAPE,
    )
    def forward(
        self,
        pixel_values: torch.Tensor | None = ...,
        noise: torch.FloatTensor | None = ...,
        head_mask: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        interpolate_pos_encoding: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | BaseModelOutputWithPooling:
        r"""
        noise (`torch.FloatTensor` of shape `(batch_size, num_mask_units)`, *optional*) which is
                mainly used for testing purposes to control randomness and maintain the reproducibility
                when is_mae is set to True.
        """
        ...

class HieraDecoder(nn.Module):
    def __init__(self, config: HieraConfig) -> None: ...
    def forward(
        self,
        encoder_hidden_states: torch.Tensor,
        bool_masked_pos: torch.BoolTensor,
        head_mask: torch.Tensor | None = ...,
        output_attentions: bool = ...,
    ) -> tuple[torch.Tensor, torch.BoolTensor]: ...

class HieraMultiScaleHead(nn.Module):
    def __init__(self, config: HieraConfig) -> None: ...
    def apply_fusion_head(self, head: nn.Module, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def forward(self, feature_maps: list[torch.Tensor]) -> torch.Tensor: ...

@add_start_docstrings(
    """The Hiera Model transformer with the decoder on top for self-supervised pre-training.

    <Tip>

    Note that we provide a script to pre-train this model on custom data in our [examples
    directory](https://github.com/huggingface/transformers/tree/main/examples/pytorch/image-pretraining).

    </Tip>
    """,
    HIERA_START_DOCSTRING,
)
class HieraForPreTraining(HieraPreTrainedModel):
    def __init__(self, config: HieraConfig) -> None: ...
    def get_pixel_label_2d(self, pixel_values: torch.Tensor, bool_masked_pos: torch.BoolTensor) -> torch.Tensor: ...
    def forward_loss(
        self, pixel_values: torch.Tensor, logits: torch.Tensor, bool_masked_pos: torch.BoolTensor
    ):  # -> Tensor:
        ...
    @add_start_docstrings_to_model_forward(HIERA_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=HieraForPreTrainingOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        pixel_values: torch.Tensor | None = ...,
        noise: torch.FloatTensor | None = ...,
        head_mask: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        interpolate_pos_encoding: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | HieraForPreTrainingOutput:
        r"""
        noise (`torch.FloatTensor` of shape `(batch_size, num_mask_units)`, *optional*) which is
                mainly used for testing purposes to control randomness and maintain the reproducibility
                when is_mae is set to True.

        Returns:

        Examples:
        ```python
        >>> from transformers import AutoImageProcessor, HieraForPreTraining
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/hiera-tiny-224-mae-hf")
        >>> model = HieraForPreTraining.from_pretrained("facebook/hiera-tiny-224-mae-hf")

        >>> inputs = image_processor(images=image, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        >>> loss = outputs.loss
        >>> print(list(logits.shape))
        [1, 196, 768]
        ```"""
        ...

@add_start_docstrings(
    """
    Hiera Model transformer with an image classification head on top (a linear layer on top of the final hidden state with
    average pooling) e.g. for ImageNet.

    <Tip>

        Note that it's possible to fine-tune Hiera on higher resolution images than the ones it has been trained on, by
        setting `interpolate_pos_encoding` to `True` in the forward of the model. This will interpolate the pre-trained
        position embeddings to the higher resolution.

    </Tip>
    """,
    HIERA_START_DOCSTRING,
)
class HieraForImageClassification(HieraPreTrainedModel):
    def __init__(self, config: HieraConfig) -> None: ...
    @add_start_docstrings_to_model_forward(HIERA_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_IMAGE_CLASS_CHECKPOINT,
        output_type=HieraForImageClassificationOutput,
        config_class=_CONFIG_FOR_DOC,
        expected_output=_IMAGE_CLASS_EXPECTED_OUTPUT,
    )
    def forward(
        self,
        pixel_values,
        head_mask: torch.Tensor | None = ...,
        labels: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        interpolate_pos_encoding: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | HieraForImageClassificationOutput:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...

@add_start_docstrings(
    """
    Hiera backbone, to be used with frameworks like DETR and MaskFormer.
    """,
    HIERA_START_DOCSTRING,
)
class HieraBackbone(HieraPreTrainedModel, BackboneMixin):
    def __init__(self, config: HieraConfig) -> None: ...
    def get_input_embeddings(self):  # -> HieraPatchEmbeddings:
        ...
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

        >>> processor = AutoImageProcessor.from_pretrained("facebook/hiera-tiny-224-hf")
        >>> model = AutoBackbone.from_pretrained(
        ...     "facebook/hiera-tiny-224-hf", out_features=["stage1", "stage2", "stage3", "stage4"]
        ... )

        >>> inputs = processor(image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> feature_maps = outputs.feature_maps
        >>> list(feature_maps[-1].shape)
        [1, 768, 7, 7]
        ```"""
        ...

__all__ = ["HieraForImageClassification", "HieraForPreTraining", "HieraBackbone", "HieraModel", "HieraPreTrainedModel"]
