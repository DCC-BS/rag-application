"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

import numpy as np
import tensorflow as tf

from ...modeling_tf_outputs import (
    TFBaseModelOutput,
    TFBaseModelOutputWithPooling,
    TFSemanticSegmenterOutput,
    TFSequenceClassifierOutput,
)
from ...modeling_tf_utils import (
    TFModelInputType,
    TFPreTrainedModel,
    TFSequenceClassificationLoss,
    keras,
    keras_serializable,
    unpack_inputs,
)
from ...utils import (
    add_code_sample_docstrings,
    add_start_docstrings,
    add_start_docstrings_to_model_forward,
    replace_return_docstrings,
)
from .configuration_data2vec_vision import Data2VecVisionConfig

"""TF 2.0 Data2Vec Vision model."""
logger = ...
_CONFIG_FOR_DOC = ...
_CHECKPOINT_FOR_DOC = ...
_EXPECTED_OUTPUT_SHAPE = ...
_IMAGE_CLASS_CHECKPOINT = ...
_IMAGE_CLASS_EXPECTED_OUTPUT = ...

@dataclass
class TFData2VecVisionModelOutputWithPooling(TFBaseModelOutputWithPooling):
    """
    Class for outputs of [`TFData2VecVisionModel`].

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`tf.Tensor` of shape `(batch_size, hidden_size)`):
            Average of the last layer hidden states of the patch tokens (excluding the *[CLS]* token) if
            *config.use_mean_pooling* is set to True. If set to False, then the final hidden state of the *[CLS]* token
            will be returned.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """

    last_hidden_state: tf.Tensor = ...
    pooler_output: tf.Tensor = ...
    hidden_states: tuple[tf.Tensor] | None = ...
    attentions: tuple[tf.Tensor] | None = ...

class TFData2VecVisionDropPath(keras.layers.Layer):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).
    References:
        (1) github.com:rwightman/pytorch-image-models
    """
    def __init__(self, drop_path, **kwargs) -> None: ...
    def call(self, x, training=...): ...

class TFData2VecVisionEmbeddings(keras.layers.Layer):
    """
    Construct the CLS token, position and patch embeddings. Optionally, also the mask token.

    """
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def build(self, input_shape=...):  # -> None:
        ...
    def call(self, pixel_values: tf.Tensor, bool_masked_pos: tf.Tensor | None = ...) -> tf.Tensor: ...

class TFData2VecVisionPatchEmbeddings(keras.layers.Layer):
    """
    Image to Patch Embedding.
    """
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, training: bool = ...) -> tf.Tensor: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionSelfAttention(keras.layers.Layer):
    def __init__(self, config: Data2VecVisionConfig, window_size: tuple | None = ..., **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(
        self,
        hidden_states: tf.Tensor,
        head_mask: tf.Tensor,
        output_attentions: bool,
        relative_position_bias: TFData2VecVisionRelativePositionBias | None = ...,
        training: bool = ...,
    ) -> tuple[tf.Tensor]: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionSelfOutput(keras.layers.Layer):
    """
    The residual connection is defined in TFData2VecVisionLayer instead of here (as is the case with other models), due
    to the layernorm applied before each block.
    """
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, gamma=..., training: bool = ...) -> tf.Tensor: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionAttention(keras.layers.Layer):
    def __init__(self, config: Data2VecVisionConfig, window_size: tuple | None = ..., **kwargs) -> None: ...
    def prune_heads(self, heads): ...
    def call(
        self,
        input_tensor: tf.Tensor,
        head_mask: tf.Tensor,
        output_attentions: bool,
        relative_position_bias: TFData2VecVisionRelativePositionBias | None = ...,
        training: bool = ...,
    ) -> tuple[tf.Tensor]: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionIntermediate(keras.layers.Layer):
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionOutput(keras.layers.Layer):
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = ...) -> tf.Tensor: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionLayer(keras.layers.Layer):
    """This corresponds to the Block class in the timm implementation."""
    def __init__(
        self, config: Data2VecVisionConfig, window_size: tuple | None = ..., drop_path_rate: float = ..., **kwargs
    ) -> None: ...
    def build(self, input_shape: tf.TensorShape = ...):  # -> None:
        ...
    def call(
        self,
        hidden_states: tf.Tensor,
        head_mask: tf.Tensor,
        output_attentions: bool,
        relative_position_bias: TFData2VecVisionRelativePositionBias | None = ...,
        training: bool = ...,
    ) -> tuple[tf.Tensor]: ...

class TFData2VecVisionRelativePositionBias(keras.layers.Layer):
    def __init__(self, config: Data2VecVisionConfig, window_size: tuple, **kwargs) -> None: ...
    def build(self, input_shape):  # -> None:
        ...
    def get_position_index(self): ...
    def call(self, inputs=...) -> tf.Tensor: ...

class TFData2VecVisionEncoder(keras.layers.Layer):
    def __init__(self, config: Data2VecVisionConfig, window_size: tuple | None = ..., **kwargs) -> None: ...
    def call(
        self,
        hidden_states: tf.Tensor,
        head_mask: tf.Tensor | None = ...,
        output_attentions: bool = ...,
        output_hidden_states: bool = ...,
        return_dict: bool = ...,
    ) -> tuple | TFBaseModelOutput: ...
    def build(self, input_shape=...):  # -> None:
        ...

@keras_serializable
class TFData2VecVisionMainLayer(keras.layers.Layer):
    config_class = Data2VecVisionConfig
    def __init__(self, config: Data2VecVisionConfig, add_pooling_layer: bool = ..., **kwargs) -> None: ...
    def get_input_embeddings(self) -> keras.layers.Layer: ...
    @unpack_inputs
    def call(
        self,
        pixel_values: tf.Tensor | None = ...,
        bool_masked_pos: tf.Tensor | None = ...,
        head_mask: tf.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        training: bool = ...,
    ) -> tuple | TFData2VecVisionModelOutputWithPooling: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionPooler(keras.layers.Layer):
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = Data2VecVisionConfig
    base_model_prefix = ...
    main_input_name = ...
    _keys_to_ignore_on_load_unexpected = ...

DATA2VEC_VISION_START_DOCSTRING = ...
DATA2VEC_VISION_INPUTS_DOCSTRING = ...

@add_start_docstrings(
    "The bare Data2VecVision Model transformer outputting raw hidden-states without any specific head on top.",
    DATA2VEC_VISION_START_DOCSTRING,
)
class TFData2VecVisionModel(TFData2VecVisionPreTrainedModel):
    def __init__(self, config: Data2VecVisionConfig, add_pooling_layer: bool = ..., *inputs, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    @unpack_inputs
    @add_start_docstrings_to_model_forward(DATA2VEC_VISION_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=TFData2VecVisionModelOutputWithPooling,
        config_class=_CONFIG_FOR_DOC,
        modality="vision",
        expected_output=_EXPECTED_OUTPUT_SHAPE,
    )
    def call(
        self,
        pixel_values: TFModelInputType | None = ...,
        bool_masked_pos: tf.Tensor | None = ...,
        head_mask: np.ndarray | tf.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        training: bool = ...,
    ) -> tuple | TFData2VecVisionModelOutputWithPooling:
        r"""
        bool_masked_pos (`tf.Tensor` of shape `(batch_size, num_patches)`, *optional*):
            Boolean masked positions. Indicates which patches are masked (1) and which aren't (0).
        """
        ...

    def build(self, input_shape=...):  # -> None:
        ...

@add_start_docstrings(
    """
    Data2VecVision Model transformer with an image classification head on top (a linear layer on top of the average of
    the final hidden states of the patch tokens) e.g. for ImageNet.
    """,
    DATA2VEC_VISION_START_DOCSTRING,
)
class TFData2VecVisionForImageClassification(TFData2VecVisionPreTrainedModel, TFSequenceClassificationLoss):
    def __init__(self, config: Data2VecVisionConfig, *inputs, **kwargs) -> None: ...
    @unpack_inputs
    @add_start_docstrings_to_model_forward(DATA2VEC_VISION_INPUTS_DOCSTRING)
    @add_code_sample_docstrings(
        checkpoint=_IMAGE_CLASS_CHECKPOINT,
        output_type=TFSequenceClassifierOutput,
        config_class=_CONFIG_FOR_DOC,
        expected_output=_IMAGE_CLASS_EXPECTED_OUTPUT,
    )
    def call(
        self,
        pixel_values: TFModelInputType | None = ...,
        head_mask: np.ndarray | tf.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        labels: np.ndarray | tf.Tensor | None = ...,
        training: bool | None = ...,
    ) -> TFSequenceClassifierOutput | tuple:
        r"""
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
        ...

    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionConvModule(keras.layers.Layer):
    """
    A convolutional block that bundles conv/norm/activation layers. This block simplifies the usage of convolution
    layers, which are commonly used with a norm layer (e.g., BatchNorm) and activation layer (e.g., ReLU).

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int | tuple[int, int],
        padding: str = ...,
        bias: bool = ...,
        dilation: int | tuple[int, int] = ...,
        **kwargs,
    ) -> None: ...
    def call(self, input: tf.Tensor) -> tf.Tensor: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFAdaptiveAvgPool2D(keras.layers.Layer):
    def __init__(self, output_dims: tuple[int, int], input_ordering: str = ..., **kwargs) -> None: ...
    def pseudo_1d_pool(self, inputs: tf.Tensor, h_pooling: bool): ...
    def call(self, inputs: tf.Tensor): ...

class TFData2VecVisionPyramidPoolingModule(keras.layers.Layer):
    """
    Pyramid Pooling Module (PPM) used in PSPNet.

    Args:
        pool_scales (tuple[int]): Pooling scales used in Pooling Pyramid
            Module.
        channels (int): Channels after modules, before conv_seg.

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    def __init__(self, pool_scales: tuple[int, ...], in_channels: int, out_channels: int, **kwargs) -> None: ...
    def call(self, x: tf.Tensor) -> list[tf.Tensor]: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionUperHead(keras.layers.Layer):
    """
    Unified Perceptual Parsing for Scene Understanding. This head is the implementation of
    [UPerNet](https://arxiv.org/abs/1807.10221).

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    def __init__(self, config: Data2VecVisionConfig, **kwargs) -> None: ...
    def psp_forward(self, inputs): ...
    def call(self, encoder_hidden_states: tf.Tensor) -> tf.Tensor: ...
    def build(self, input_shape=...):  # -> None:
        ...

class TFData2VecVisionFCNHead(keras.layers.Layer):
    """
    Fully Convolution Networks for Semantic Segmentation. This head is implemented from
    [FCNNet](https://arxiv.org/abs/1411.4038).

    Args:
        config (Data2VecVisionConfig): Configuration.
        kernel_size (int): The kernel size for convs in the head. Default: 3.
        dilation (int): The dilation rate for convs in the head. Default: 1.


    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    def __init__(
        self,
        config: Data2VecVisionConfig,
        in_index: int = ...,
        kernel_size: int = ...,
        dilation: int | tuple[int, int] = ...,
        **kwargs,
    ) -> None: ...
    def call(self, encoder_hidden_states: tf.Tensor) -> tf.Tensor: ...
    def build(self, input_shape=...):  # -> None:
        ...

@add_start_docstrings(
    """
    Data2VecVision Model transformer with a semantic segmentation head on top e.g. for ADE20k, CityScapes.
    """,
    DATA2VEC_VISION_START_DOCSTRING,
)
class TFData2VecVisionForSemanticSegmentation(TFData2VecVisionPreTrainedModel):
    def __init__(self, config: Data2VecVisionConfig, *inputs, **kwargs) -> None: ...
    def compute_loss(self, logits, auxiliary_logits, labels): ...
    @unpack_inputs
    @add_start_docstrings_to_model_forward(DATA2VEC_VISION_INPUTS_DOCSTRING)
    @replace_return_docstrings(output_type=TFSemanticSegmenterOutput, config_class=_CONFIG_FOR_DOC)
    def call(
        self,
        pixel_values: tf.Tensor | None = ...,
        head_mask: tf.Tensor | None = ...,
        labels: tf.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
    ) -> tuple | TFSemanticSegmenterOutput:
        r"""
        labels (`tf.Tensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFData2VecVisionForSemanticSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/data2vec-vision-base")
        >>> model = TFData2VecVisionForSemanticSegmentation.from_pretrained("facebook/data2vec-vision-base")

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> # logits are of shape (batch_size, num_labels, height, width)
        >>> logits = outputs.logits
        ```"""
        ...

    def build(self, input_shape=...):  # -> None:
        ...

__all__ = [
    "TFData2VecVisionForImageClassification",
    "TFData2VecVisionForSemanticSegmentation",
    "TFData2VecVisionModel",
    "TFData2VecVisionPreTrainedModel",
]
