"""
This type stub file was generated by pyright.
"""

from ..utils import is_torch_available

"AQLM (Additive Quantization of Language Model) integration file"
if is_torch_available(): ...

def replace_with_aqlm_linear(
    model, quantization_config=..., linear_weights_not_to_quantize=..., current_key_name=..., has_been_replaced=...
):  # -> tuple[Any, bool]:
    """
    Public method that recursively replaces the Linear layers of the given model with AQLM quantized layers.
    `accelerate` is needed to use this method. Returns the converted model and a boolean that indicates if the
    conversion has been successfull or not.

    Args:
        model (`torch.nn.Module`):
            The model to convert, can be any `torch.nn.Module` instance.
        quantization_config (`AqlmConfig`):
            The quantization config object that contains the quantization parameters.
        linear_weights_not_to_quantize (`list[str]`, *optional*):
            A list of nn.Linear weights to not convert. If a parameter path is in the list (e.g. `lm_head.weight`), the corresponding module will not be
            converted.
        current_key_name (`list`, *optional*):
            A list that contains the current key name. This is used for recursion and should not be passed by the user.
        has_been_replaced (`bool`, *optional*):
            A boolean that indicates if the conversion has been successful or not. This is used for recursion and
            should not be passed by the user.
    """
    ...
