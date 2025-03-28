"""
This type stub file was generated by pyright.
"""

from .utils import ExplicitEnum, is_safetensors_available

"""PyTorch - TF 2.0 general utilities."""
if is_safetensors_available(): ...
logger = ...

class TransposeType(ExplicitEnum):
    """
    Possible ...
    """

    NO = ...
    SIMPLE = ...
    CONV1D = ...
    CONV2D = ...

def convert_tf_weight_name_to_pt_weight_name(
    tf_name, start_prefix_to_remove=..., tf_weight_shape=..., name_scope=...
):  # -> tuple[str, Literal[TransposeType.CONV2D, TransposeType.CONV1D, TransposeType.SIMPLE, TransposeType.NO]]:
    """
    Convert a TF 2.0 model variable name in a pytorch model weight name.

    Conventions for TF2.0 scopes -> PyTorch attribute names conversions:

        - '$1___$2' is replaced by $2 (can be used to duplicate or remove layers in TF2.0 vs PyTorch)
        - '_._' is replaced by a new level separation (can be used to convert TF2.0 lists in PyTorch nn.ModulesList)

    return tuple with:

        - pytorch model weight name
        - transpose: `TransposeType` member indicating whether and how TF2.0 and PyTorch weights matrices should be
          transposed with regards to each other
    """
    ...

def apply_transpose(transpose: TransposeType, weight, match_shape=..., pt_to_tf=...):  # -> NDArray[Any]:
    """
    Apply a transpose to some weight then tries to reshape the weight to the same shape as a given shape, all in a
    framework agnostic way.
    """
    ...

def load_pytorch_checkpoint_in_tf2_model(
    tf_model,
    pytorch_checkpoint_path,
    tf_inputs=...,
    allow_missing_keys=...,
    output_loading_info=...,
    _prefix=...,
    tf_to_pt_weight_rename=...,
):
    """Load pytorch checkpoints in a TF 2.0 model"""
    ...

def load_pytorch_model_in_tf2_model(tf_model, pt_model, tf_inputs=..., allow_missing_keys=...):
    """Load pytorch checkpoints in a TF 2.0 model"""
    ...

def load_pytorch_weights_in_tf2_model(
    tf_model,
    pt_state_dict,
    tf_inputs=...,
    allow_missing_keys=...,
    output_loading_info=...,
    _prefix=...,
    tf_to_pt_weight_rename=...,
):
    """Load pytorch state_dict in a TF 2.0 model."""
    ...

def load_pytorch_state_dict_in_tf2_model(
    tf_model,
    pt_state_dict,
    tf_inputs=...,
    allow_missing_keys=...,
    output_loading_info=...,
    _prefix=...,
    tf_to_pt_weight_rename=...,
    ignore_mismatched_sizes=...,
    skip_logger_warnings=...,
):
    """Load a pytorch state_dict in a TF 2.0 model. pt_state_dict can be either an actual dict or a lazy-loading
    safetensors archive created with the safe_open() function."""
    ...

def load_sharded_pytorch_safetensors_in_tf2_model(
    tf_model,
    safetensors_shards,
    tf_inputs=...,
    allow_missing_keys=...,
    output_loading_info=...,
    _prefix=...,
    tf_to_pt_weight_rename=...,
    ignore_mismatched_sizes=...,
):  # -> tuple[Any, dict[str, list[Any] | Any]]:
    ...
def load_tf2_checkpoint_in_pytorch_model(
    pt_model, tf_checkpoint_path, tf_inputs=..., allow_missing_keys=..., output_loading_info=...
):  # -> tuple[Any, dict[str, Any | list[Any]]]:
    """
    Load TF 2.0 HDF5 checkpoint in a PyTorch model We use HDF5 to easily do transfer learning (see
    https://github.com/tensorflow/tensorflow/blob/ee16fcac960ae660e0e4496658a366e2f745e1f0/tensorflow/python/keras/engine/network.py#L1352-L1357).
    """
    ...

def load_tf2_model_in_pytorch_model(
    pt_model, tf_model, allow_missing_keys=..., output_loading_info=...
):  # -> tuple[Any, dict[str, Any | list[Any]]]:
    """Load TF 2.0 model in a pytorch model"""
    ...

def load_tf2_weights_in_pytorch_model(
    pt_model, tf_weights, allow_missing_keys=..., output_loading_info=...
):  # -> tuple[Any, dict[str, Any | list[Any]]]:
    """Load TF2.0 symbolic weights in a PyTorch model"""
    ...

def load_tf2_state_dict_in_pytorch_model(
    pt_model, tf_state_dict, allow_missing_keys=..., output_loading_info=...
):  # -> tuple[Any, dict[str, Any | list[Any]]]:
    ...
