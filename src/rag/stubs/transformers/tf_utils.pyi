"""
This type stub file was generated by pyright.
"""

import numpy as np
import tensorflow as tf

logger = ...

def shape_list(tensor: tf.Tensor | np.ndarray) -> list[int]:
    """
    Deal with dynamic shape in tensorflow cleanly.

    Args:
        tensor (`tf.Tensor` or `np.ndarray`): The tensor we want the shape of.

    Returns:
        `List[int]`: The shape of the tensor as a list.
    """
    ...

def stable_softmax(logits: tf.Tensor, axis: int | None = ..., name: str | None = ...) -> tf.Tensor:
    """
    Stable wrapper that returns the same output as `tf.nn.softmax`, but that works reliably with XLA on CPU. It is
    meant as a workaround for the [following issue](https://github.com/tensorflow/tensorflow/issues/55682), and will be
    removed after it gets fixed. The arguments and outputs are the same as `tf.nn.softmax`, and relies on the fact that
    `softmax(x) = softmax(x + c)` (see https://ogunlao.github.io/2020/04/26/you_dont_really_know_softmax.html).

    Args:
        logits (`tf.Tensor`):
            Must be one of the following types: half, float32, float64.
        axis (`int`, *optional*):
            The dimension softmax would be performed on. The default is -1 which indicates the last dimension.
        name (`str`, *optional*):
            A name for the operation.

    Returns:
        `tf.Tensor`:
            A Tensor. Has the same type and shape as logits.
    """
    ...

def functional_layernorm(inputs, weight, bias, epsilon=..., axis=...): ...
def scaled_dot_product_attention(query, key, value, attn_mask=..., dropout_p=..., is_causal=..., scale: float = ...):
    """TF equivalent for torch's nn.functional.scaled_dot_product_attention"""
    ...

def flatten(input, start_dim=..., end_dim=...): ...
def invert_attention_mask(encoder_attention_mask: tf.Tensor) -> tf.Tensor:
    """
    Invert an attention mask (e.g., switches 0. and 1.).

    Args:
        encoder_attention_mask (`torch.Tensor`): An attention mask.

    Returns:
        `tf.Tensor`: The inverted attention mask.
    """
    ...

def check_embeddings_within_bounds(tensor: tf.Tensor, embed_dim: int, tensor_name: str = ...) -> None:
    """
    `tf.gather`, on which TF embedding layers are based, won't check positive out of bound indices on GPU, returning
    zeros instead. This function adds a check against that dangerous silent behavior.

    Args:
        tensor (`tf.Tensor`): The tensor of indices to check.
        embed_dim (`int`): The embedding dimension.
        tensor_name (`str`, *optional*): The name of the tensor to use in the error message.
    """
    ...

def save_attributes_to_hdf5_group(group, name, data):  # -> None:
    """Saves attributes (data) of the specified name into the HDF5 group.

    This method deals with an inherent problem of HDF5 file which is not able to store data larger than
    HDF5_OBJECT_HEADER_LIMIT bytes.

    Args:
        group: A pointer to a HDF5 group.
        name: A name of the attributes to save.
        data: Attributes data to store.

    Raises:
      RuntimeError: If any single attribute is too large to be saved.

    Copied from Keras to Transformers to avoid versioning issues.
    """
    ...

def load_attributes_from_hdf5_group(group, name):  # -> list[Any]:
    """Loads attributes of the specified name from the HDF5 group.

    This method deals with an inherent problem of HDF5 file which is not able to store data larger than
    HDF5_OBJECT_HEADER_LIMIT bytes.

    Args:
        group: A pointer to a HDF5 group.
        name: A name of the attributes to load.

    Returns:
        data: Attributes data.

    Copied from Keras to Transformers to avoid versioning issues.
    """
    ...

def expand_1d(data):
    """Expands 1-dimensional `Tensor`s into 2-dimensional `Tensor`s.
    Copied from Keras to here to avoid versioning issues."""
    ...

def convert_batch_encoding(*args, **kwargs):  # -> tuple[list[Any] | tuple[Any, ...], dict[str, Any]]:
    ...
