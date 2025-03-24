"""
This type stub file was generated by pyright.
"""

import torch
from torch import Tensor, nn

from ...file_utils import add_code_sample_docstrings, add_start_docstrings, add_start_docstrings_to_model_forward
from ...modeling_outputs import (
    BaseModelOutputWithNoAttention,
    BaseModelOutputWithPoolingAndNoAttention,
    ImageClassifierOutputWithNoAttention,
)
from ...modeling_utils import PreTrainedModel
from .configuration_regnet import RegNetConfig

"""PyTorch RegNet model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_IMAGE_CLASS_CHECKPOINT = ...
_IMAGE_CLASS_EXPECTED_OUTPUT = ...

class RegNetConvLayer(nn.Module):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int = ...,
        stride: int = ...,
        groups: int = ...,
        activation: str | None = ...,
    ) -> None: ...
    def forward(self, hidden_state):  # -> Any:
        ...

class RegNetEmbeddings(nn.Module):
    """
    RegNet Embedddings (stem) composed of a single aggressive convolution.
    """
    def __init__(self, config: RegNetConfig) -> None: ...
    def forward(self, pixel_values):  # -> Any:
        ...

class RegNetShortCut(nn.Module):
    """
    RegNet shortcut, used to project the residual features to the correct size. If needed, it is also used to
    downsample the input using `stride=2`.
    """
    def __init__(self, in_channels: int, out_channels: int, stride: int = ...) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...

class RegNetSELayer(nn.Module):
    """
    Squeeze and Excitation layer (SE) proposed in [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507).
    """
    def __init__(self, in_channels: int, reduced_channels: int) -> None: ...
    def forward(self, hidden_state): ...

class RegNetXLayer(nn.Module):
    """
    RegNet's layer composed by three `3x3` convolutions, same as a ResNet bottleneck layer with reduction = 1.
    """
    def __init__(self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = ...) -> None: ...
    def forward(self, hidden_state): ...

class RegNetYLayer(nn.Module):
    """
    RegNet's Y layer: an X layer with Squeeze and Excitation.
    """
    def __init__(self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = ...) -> None: ...
    def forward(self, hidden_state): ...

class RegNetStage(nn.Module):
    """
    A RegNet stage composed by stacked layers.
    """
    def __init__(
        self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = ..., depth: int = ...
    ) -> None: ...
    def forward(self, hidden_state):  # -> Any:
        ...

class RegNetEncoder(nn.Module):
    def __init__(self, config: RegNetConfig) -> None: ...
    def forward(
        self, hidden_state: Tensor, output_hidden_states: bool = ..., return_dict: bool = ...
    ) -> BaseModelOutputWithNoAttention: ...

class RegNetPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = RegNetConfig
    base_model_prefix = ...
    main_input_name = ...
    _no_split_modules = ...

REGNET_START_DOCSTRING = ...
REGNET_INPUTS_DOCSTRING = ...

@add_start_docstrings(
    "The bare RegNet model outputting raw features without any specific head on top.", REGNET_START_DOCSTRING
)
class RegNetModel(RegNetPreTrainedModel):
    def __init__(self, config) -> None: ...
    @add_start_docstrings_to_model_forward(REGNET_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=BaseModelOutputWithPoolingAndNoAttention,
        config_class=_CONFIG_FOR_DOC,
        modality="vision",
        expected_output=_EXPECTED_OUTPUT_SHAPE,
    )
    def forward(
        self, pixel_values: Tensor, output_hidden_states: bool | None = ..., return_dict: bool | None = ...
    ) -> BaseModelOutputWithPoolingAndNoAttention: ...

@add_start_docstrings(
    """
    RegNet Model with an image classification head on top (a linear layer on top of the pooled features), e.g. for
    ImageNet.
    """,
    REGNET_START_DOCSTRING,
)
class RegNetForImageClassification(RegNetPreTrainedModel):
    def __init__(self, config) -> None: ...
    @add_start_docstrings_to_model_forward(REGNET_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_IMAGE_CLASS_CHECKPOINT,
        output_type=ImageClassifierOutputWithNoAttention,
        config_class=_CONFIG_FOR_DOC,
        expected_output=_IMAGE_CLASS_EXPECTED_OUTPUT,
    )
    def forward(
        self,
        pixel_values: torch.FloatTensor | None = ...,
        labels: torch.LongTensor | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> ImageClassifierOutputWithNoAttention:
        r"""
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...

__all__ = ["RegNetForImageClassification", "RegNetModel", "RegNetPreTrainedModel"]
