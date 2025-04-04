"""
This type stub file was generated by pyright.
"""

from typing import Any

import torch
import torch.nn as nn
from torch import Tensor
from transformers import PreTrainedModel, add_start_docstrings
from transformers.modeling_outputs import (
    BackboneOutput,
    BaseModelOutputWithNoAttention,
    BaseModelOutputWithPoolingAndNoAttention,
    ImageClassifierOutputWithNoAttention,
)
from transformers.models.textnet.configuration_textnet import TextNetConfig
from transformers.utils import (
    add_code_sample_docstrings,
    add_start_docstrings_to_model_forward,
    replace_return_docstrings,
)
from transformers.utils.backbone_utils import BackboneMixin

"""PyTorch TextNet model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...

class TextNetConvLayer(nn.Module):
    def __init__(self, config: TextNetConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TextNetRepConvLayer(nn.Module):
    r"""
    This layer supports re-parameterization by combining multiple convolutional branches
    (e.g., main convolution, vertical, horizontal, and identity branches) during training.
    At inference time, these branches can be collapsed into a single convolution for
    efficiency, as per the re-parameterization paradigm.

    The "Rep" in the name stands for "re-parameterization" (introduced by RepVGG).
    """
    def __init__(
        self, config: TextNetConfig, in_channels: int, out_channels: int, kernel_size: int, stride: int
    ) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TextNetStage(nn.Module):
    def __init__(self, config: TextNetConfig, depth: int) -> None: ...
    def forward(self, hidden_state):  # -> Any:
        ...

class TextNetEncoder(nn.Module):
    def __init__(self, config: TextNetConfig) -> None: ...
    def forward(
        self, hidden_state: torch.Tensor, output_hidden_states: bool | None = ..., return_dict: bool | None = ...
    ) -> BaseModelOutputWithNoAttention: ...

TEXTNET_START_DOCSTRING = ...
TEXTNET_INPUTS_DOCSTRING = ...

class TextNetPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = TextNetConfig
    base_model_prefix = ...
    main_input_name = ...

@add_start_docstrings(
    "The bare Textnet model outputting raw features without any specific head on top.", TEXTNET_START_DOCSTRING
)
class TextNetModel(TextNetPreTrainedModel):
    def __init__(self, config) -> None: ...
    @add_start_docstrings_to_model_forward(TEXTNET_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=BaseModelOutputWithPoolingAndNoAttention,
        config_class=_CONFIG_FOR_DOC,
        modality="vision",
        expected_output=_EXPECTED_OUTPUT_SHAPE,
    )
    def forward(
        self, pixel_values: Tensor, output_hidden_states: bool | None = ..., return_dict: bool | None = ...
    ) -> tuple[Any, list[Any]] | tuple[Any] | BaseModelOutputWithPoolingAndNoAttention: ...

@add_start_docstrings(
    """
    TextNet Model with an image classification head on top (a linear layer on top of the pooled features), e.g. for
    ImageNet.
    """,
    TEXTNET_START_DOCSTRING,
)
class TextNetForImageClassification(TextNetPreTrainedModel):
    def __init__(self, config) -> None: ...
    @add_start_docstrings_to_model_forward(TEXTNET_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=ImageClassifierOutputWithNoAttention, config_class=_CONFIG_FOR_DOC)
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
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:
        ```python
        >>> import torch
        >>> import requests
        >>> from transformers import TextNetForImageClassification, TextNetImageProcessor
        >>> from PIL import Image

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> processor = TextNetImageProcessor.from_pretrained("czczup/textnet-base")
        >>> model = TextNetForImageClassification.from_pretrained("czczup/textnet-base")

        >>> inputs = processor(images=image, return_tensors="pt")
        >>> with torch.no_grad():
        ...     outputs = model(**inputs)
        >>> outputs.logits.shape
        torch.Size([1, 2])
        ```"""
        ...

@add_start_docstrings(
    """
    TextNet backbone, to be used with frameworks like DETR and MaskFormer.
    """,
    TEXTNET_START_DOCSTRING,
)
class TextNetBackbone(TextNetPreTrainedModel, BackboneMixin):
    def __init__(self, config) -> None: ...
    @add_start_docstrings_to_model_forward(TEXTNET_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=BackboneOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self, pixel_values: Tensor, output_hidden_states: bool | None = ..., return_dict: bool | None = ...
    ) -> tuple[tuple] | BackboneOutput:
        """
        Returns:

        Examples:

        ```python
        >>> import torch
        >>> import requests
        >>> from PIL import Image
        >>> from transformers import AutoImageProcessor, AutoBackbone

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> processor = AutoImageProcessor.from_pretrained("czczup/textnet-base")
        >>> model = AutoBackbone.from_pretrained("czczup/textnet-base")

        >>> inputs = processor(image, return_tensors="pt")
        >>> with torch.no_grad():
        >>>     outputs = model(**inputs)
        ```"""
        ...

__all__ = ["TextNetBackbone", "TextNetModel", "TextNetPreTrainedModel", "TextNetForImageClassification"]
