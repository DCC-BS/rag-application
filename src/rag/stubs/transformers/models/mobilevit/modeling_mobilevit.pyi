"""
This type stub file was generated by pyright.
"""

import torch
from torch import nn

from ...modeling_outputs import (
    BaseModelOutputWithNoAttention,
    BaseModelOutputWithPoolingAndNoAttention,
    ImageClassifierOutputWithNoAttention,
    SemanticSegmenterOutput,
)
from ...modeling_utils import PreTrainedModel
from ...utils import (
    add_code_sample_docstrings,
    add_start_docstrings,
    add_start_docstrings_to_model_forward,
    replace_return_docstrings,
)
from .configuration_mobilevit import MobileViTConfig

"""PyTorch MobileViT model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_IMAGE_CLASS_CHECKPOINT = ...
_IMAGE_CLASS_EXPECTED_OUTPUT = ...

def make_divisible(value: int, divisor: int = ..., min_value: int | None = ...) -> int:
    """
    Ensure that all layers have a channel count that is divisible by `divisor`. This function is taken from the
    original TensorFlow repo. It can be seen here:
    https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py
    """
    ...

class MobileViTConvLayer(nn.Module):
    def __init__(
        self,
        config: MobileViTConfig,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int = ...,
        groups: int = ...,
        bias: bool = ...,
        dilation: int = ...,
        use_normalization: bool = ...,
        use_activation: bool | str = ...,
    ) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTInvertedResidual(nn.Module):
    """
    Inverted residual block (MobileNetv2): https://arxiv.org/abs/1801.04381
    """
    def __init__(
        self, config: MobileViTConfig, in_channels: int, out_channels: int, stride: int, dilation: int = ...
    ) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTMobileNetLayer(nn.Module):
    def __init__(
        self, config: MobileViTConfig, in_channels: int, out_channels: int, stride: int = ..., num_stages: int = ...
    ) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTSelfAttention(nn.Module):
    def __init__(self, config: MobileViTConfig, hidden_size: int) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTSelfOutput(nn.Module):
    def __init__(self, config: MobileViTConfig, hidden_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTAttention(nn.Module):
    def __init__(self, config: MobileViTConfig, hidden_size: int) -> None: ...
    def prune_heads(self, heads: set[int]) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTIntermediate(nn.Module):
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTOutput(nn.Module):
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class MobileViTTransformerLayer(nn.Module):
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTTransformer(nn.Module):
    def __init__(self, config: MobileViTConfig, hidden_size: int, num_stages: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTLayer(nn.Module):
    """
    MobileViT block: https://arxiv.org/abs/2110.02178
    """
    def __init__(
        self,
        config: MobileViTConfig,
        in_channels: int,
        out_channels: int,
        stride: int,
        hidden_size: int,
        num_stages: int,
        dilation: int = ...,
    ) -> None: ...
    def unfolding(self, features: torch.Tensor) -> tuple[torch.Tensor, dict]: ...
    def folding(self, patches: torch.Tensor, info_dict: dict) -> torch.Tensor: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTEncoder(nn.Module):
    def __init__(self, config: MobileViTConfig) -> None: ...
    def forward(
        self, hidden_states: torch.Tensor, output_hidden_states: bool = ..., return_dict: bool = ...
    ) -> tuple | BaseModelOutputWithNoAttention: ...

class MobileViTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = MobileViTConfig
    base_model_prefix = ...
    main_input_name = ...
    supports_gradient_checkpointing = ...
    _no_split_modules = ...

MOBILEVIT_START_DOCSTRING = ...
MOBILEVIT_INPUTS_DOCSTRING = ...

@add_start_docstrings(
    "The bare MobileViT model outputting raw hidden-states without any specific head on top.", MOBILEVIT_START_DOCSTRING
)
class MobileViTModel(MobileViTPreTrainedModel):
    def __init__(self, config: MobileViTConfig, expand_output: bool = ...) -> None: ...
    @add_start_docstrings_to_model_forward(MOBILEVIT_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=BaseModelOutputWithPoolingAndNoAttention,
        config_class=_CONFIG_FOR_DOC,
        modality="vision",
        expected_output=_EXPECTED_OUTPUT_SHAPE,
    )
    def forward(
        self,
        pixel_values: torch.Tensor | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | BaseModelOutputWithPoolingAndNoAttention: ...

@add_start_docstrings(
    """
    MobileViT model with an image classification head on top (a linear layer on top of the pooled features), e.g. for
    ImageNet.
    """,
    MOBILEVIT_START_DOCSTRING,
)
class MobileViTForImageClassification(MobileViTPreTrainedModel):
    def __init__(self, config: MobileViTConfig) -> None: ...
    @add_start_docstrings_to_model_forward(MOBILEVIT_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_IMAGE_CLASS_CHECKPOINT,
        output_type=ImageClassifierOutputWithNoAttention,
        config_class=_CONFIG_FOR_DOC,
        expected_output=_IMAGE_CLASS_EXPECTED_OUTPUT,
    )
    def forward(
        self,
        pixel_values: torch.Tensor | None = ...,
        output_hidden_states: bool | None = ...,
        labels: torch.Tensor | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | ImageClassifierOutputWithNoAttention:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss). If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...

class MobileViTASPPPooling(nn.Module):
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTASPP(nn.Module):
    """
    ASPP module defined in DeepLab papers: https://arxiv.org/abs/1606.00915, https://arxiv.org/abs/1706.05587
    """
    def __init__(self, config: MobileViTConfig) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTDeepLabV3(nn.Module):
    """
    DeepLabv3 architecture: https://arxiv.org/abs/1706.05587
    """
    def __init__(self, config: MobileViTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

@add_start_docstrings(
    """
    MobileViT model with a semantic segmentation head on top, e.g. for Pascal VOC.
    """,
    MOBILEVIT_START_DOCSTRING,
)
class MobileViTForSemanticSegmentation(MobileViTPreTrainedModel):
    def __init__(self, config: MobileViTConfig) -> None: ...
    @add_start_docstrings_to_model_forward(MOBILEVIT_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=SemanticSegmenterOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        pixel_values: torch.Tensor | None = ...,
        labels: torch.Tensor | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | SemanticSegmenterOutput:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> import requests
        >>> import torch
        >>> from PIL import Image
        >>> from transformers import AutoImageProcessor, MobileViTForSemanticSegmentation

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("apple/deeplabv3-mobilevit-small")
        >>> model = MobileViTForSemanticSegmentation.from_pretrained("apple/deeplabv3-mobilevit-small")

        >>> inputs = image_processor(images=image, return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)

        >>> # logits are of shape (batch_size, num_labels, height, width)
        >>> logits = outputs.logits
        ```"""
        ...

__all__ = [
    "MobileViTForImageClassification",
    "MobileViTForSemanticSegmentation",
    "MobileViTModel",
    "MobileViTPreTrainedModel",
]
