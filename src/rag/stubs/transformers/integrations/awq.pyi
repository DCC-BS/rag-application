"""
This type stub file was generated by pyright.
"""

from ..utils import is_torch_available

"AWQ (Activation aware Weight Quantization) integration file"
if is_torch_available(): ...
logger = ...
AWQ_FUSED_MAPPINGS = ...
AWQ_SCALES_MAPPINGS = ...

def replace_quantization_scales(model, model_type): ...
def replace_with_awq_linear(
    model, modules_to_not_convert=..., quantization_config=..., current_key_name=..., has_been_replaced=...
) -> bool:
    """
    Public method that recursively replaces the Linear layers of the given model with AWQ quantized layers.
    `accelerate` is needed to use this method. Returns the converted model and a boolean that indicates if the
    conversion has been successfull or not.

    During the module replacement, we also infer the backend to use through the `quantization_config` object.

    Args:
        model (`torch.nn.Module`):
            The model to convert, can be any `torch.nn.Module` instance.
        quantization_config (`AwqConfig`):
            The quantization config object that contains the quantization parameters.
        modules_to_not_convert (`list`, *optional*):
            A list of modules to not convert. If a module name is in the list (e.g. `lm_head`), it will not be
            converted.
        current_key_name (`list`, *optional*):
            A list that contains the current key name. This is used for recursion and should not be passed by the user.
        has_been_replaced (`bool`, *optional*):
            A boolean that indicates if the conversion has been successful or not. This is used for recursion and
            should not be passed by the user.
    """
    ...

def get_modules_to_fuse(
    model, quantization_config
):  # -> dict[str, list[str] | bool] | dict[str, list[str] | bool | float]:
    """
    Returns the fusing mapping given the quantization config and the model

    Args:
        model (`~PreTrainedModel`):
            The model to fuse - note this model should have been converted into AWQ format beforehand.
        quantization_config (`~transformers.quantization_config.AWQConfig`):
            The quantization configuration to use.
    """
    ...

def fuse_awq_modules(model, quantization_config):
    """
    Optionally fuse some modules in the model to speedup inference.

    Args:
        model (`~PreTrainedModel`):
            The model to fuse - note this model should have been converted into AWQ format beforehand.
        quantization_config (`Union[AwqConfig, dict]`):
            The quantization configuration to use.
    """
    ...

def post_init_awq_exllama_modules(model, exllama_config):
    """
    Runs post init for Exllama layers which performs:
        - Weights unpacking, reordering and repacking
        - Devices scratch space allocation
    """
    ...

def post_init_awq_ipex_modules(model):
    """
    Runs post init for IPEX layers which performs:
        - Weights packing, reordering and repacking
    """
    ...
