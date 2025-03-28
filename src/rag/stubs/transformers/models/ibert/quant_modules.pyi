"""
This type stub file was generated by pyright.
"""

from torch import nn
from torch.autograd import Function

logger = ...

class QuantEmbedding(nn.Module):
    """
    Quantized version of `torch.nn.Embedding`. Adds quantization-specific arguments on top of `torch.nn.Embedding`.

    Args:
        weight_bit (`int`, *optional*, defaults to `8`):
            Bitwidth for the quantized weight.
        momentum (`float`, *optional*, defaults to `0.95`):
            Momentum for updating the activation quantization range.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
    """
    def __init__(
        self,
        num_embeddings,
        embedding_dim,
        padding_idx=...,
        max_norm=...,
        norm_type=...,
        scale_grad_by_freq=...,
        sparse=...,
        _weight=...,
        weight_bit=...,
        momentum=...,
        quant_mode=...,
    ) -> None: ...
    def forward(self, x, positions=..., incremental_state=...):  # -> tuple[Tensor, None] | tuple[Any, Any]:
        ...

class QuantAct(nn.Module):
    """
    Quantizes the given activation.

    Args:
        activation_bit (`int`):
            Bitwidth for the quantized activation.
        act_range_momentum (`float`, *optional*, defaults to `0.95`):
            Momentum for updating the activation quantization range.
        per_channel (`bool`, *optional*, defaults to `False`):
            Whether to or not use channel-wise quantization.
        channel_len (`int`, *optional*):
            Specify the channel length when set the *per_channel* True.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
    """
    def __init__(
        self, activation_bit, act_range_momentum=..., per_channel=..., channel_len=..., quant_mode=...
    ) -> None: ...
    def __repr__(self):  # -> str:
        ...
    def forward(
        self,
        x,
        pre_act_scaling_factor=...,
        identity=...,
        identity_scaling_factor=...,
        specified_min=...,
        specified_max=...,
    ):  # -> tuple[Any, None] | tuple[Any, Any]:
        ...

class QuantLinear(nn.Module):
    """
    Quantized version of `torch.nn.Linear`. Adds quantization-specific arguments on top of `torch.nn.Linear`.

    Args:
        weight_bit (`int`, *optional*, defaults to `8`):
            Bitwidth for the quantized weight.
        bias_bit (`int`, *optional*, defaults to `32`):
            Bitwidth for the quantized bias.
        per_channel (`bool`, *optional*, defaults to `False`):
            Whether or not to use channel-wise quantization.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
    """
    def __init__(
        self, in_features, out_features, bias=..., weight_bit=..., bias_bit=..., per_channel=..., quant_mode=...
    ) -> None: ...
    def __repr__(self):  # -> str:
        ...
    def forward(self, x, prev_act_scaling_factor=...):  # -> tuple[Tensor, None] | tuple[Any, Any]:
        ...

class IntGELU(nn.Module):
    """
    Quantized version of `torch.nn.GELU`. Adds quantization-specific arguments on top of `torch.nn.GELU`.

    Args:
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
        force_dequant (`str`, *optional*, defaults to `"none"`):
            Force dequantize the layer if either "gelu" or "nonlinear" is given.
    """
    def __init__(self, quant_mode=..., force_dequant=...) -> None: ...
    def int_erf(self, x_int, scaling_factor):  # -> tuple[Any | None, Any]:
        ...
    def forward(self, x, scaling_factor=...):  # -> tuple[Any, None] | tuple[Any, Any]:
        ...

class IntSoftmax(nn.Module):
    """
    Quantized version of `torch.nn.Softmax`. Adds quantization-specific arguments on top of `torch.nn.Softmax`.

    Args:
        output_bit (`int`):
            Bitwidth for the layer output activation.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
        force_dequant (`str`, *optional*, defaults to `"none"`):
            Force dequantize the layer if either "softmax" or "nonlinear" is given.
    """
    def __init__(self, output_bit, quant_mode=..., force_dequant=...) -> None: ...
    def int_polynomial(self, x_int, scaling_factor):  # -> tuple[Any, Any]:
        ...
    def int_exp(self, x_int, scaling_factor):  # -> tuple[Any, Any]:
        ...
    def forward(self, x, scaling_factor):  # -> tuple[Tensor, None] | tuple[Any, float]:
        ...

class IntLayerNorm(nn.Module):
    """
    Quantized version of `torch.nn.LayerNorm`. Adds quantization-specific arguments on top of `torch.nn.LayerNorm`.

    Args:
        output_bit (`int`, *optional*, defaults to `8`):
            Bitwidth for the layer output activation.
        quant_mode (`bool`, *optional*, defaults to `False`):
            Whether or not the layer is quantized.
        force_dequant (`str`, *optional*, defaults to `"none"`):
            Force dequantize the layer if either "layernorm" or "nonlinear" is given.
    """
    def __init__(self, normalized_shape, eps, output_bit=..., quant_mode=..., force_dequant=...) -> None: ...
    def set_shift(self, y_int):  # -> None:
        ...
    def overflow_fallback(self, y_int):
        """
        This fallback function is called when overflow is detected during training time, and adjusts the `self.shift`
        to avoid overflow in the subsequent runs.
        """
        ...

    def forward(self, x, scaling_factor=...):  # -> tuple[Any, None] | tuple[Any, Tensor]:
        ...

def get_percentile_min_max(
    input, lower_percentile, upper_percentile, output_tensor=...
):  # -> tuple[Number | Tensor, Number | Tensor]:
    """
    Calculate the percentile max and min values in a given tensor

    Args:
        input (`torch.Tensor`):
            The target tensor to calculate percentile max and min.
        lower_percentile (`float`):
            If 0.1, means we return the value of the smallest 0.1% value in the tensor as percentile min.
        upper_percentile (`float`):
            If 99.9, means we return the value of the largest 0.1% value in the tensor as percentile max.
        output_tensor (`bool`, *optional*, defaults to `False`):
            If True, this function returns tensors, otherwise it returns values.

    Returns:
        `Tuple(torch.Tensor, torch.Tensor)`: Percentile min and max value of *input*
    """
    ...

def linear_quantize(input, scale, zero_point, inplace=...):  # -> Tensor:
    """
    Quantize single-precision input tensor to integers with the given scaling factor and zeropoint.

    Args:
        input (`torch.Tensor`):
            Single-precision input tensor to be quantized.
        scale (`torch.Tensor`):
            Scaling factor for quantization.
        zero_pint (`torch.Tensor`):
            Shift for quantization.
        inplace (`bool`, *optional*, defaults to `False`):
            Whether to compute inplace or not.

    Returns:
        `torch.Tensor`: Linearly quantized value of *input* according to *scale* and *zero_point*.
    """
    ...

def symmetric_linear_quantization_params(num_bits, saturation_min, saturation_max, per_channel=...):
    """
    Compute the scaling factor with the given quantization range for symmetric quantization.

    Args:
        saturation_min (`torch.Tensor`):
            Lower bound for quantization range.
        saturation_max (`torch.Tensor`):
            Upper bound for quantization range.
        per_channel (`bool`, *optional*, defaults to `False`):
            Whether to or not use channel-wise quantization.

    Returns:
        `torch.Tensor`: Scaling factor that linearly quantizes the given range between *saturation_min* and
        *saturation_max*.
    """
    ...

class SymmetricQuantFunction(Function):
    """
    Class to quantize the given floating-point values using symmetric quantization with given range and bitwidth.
    """
    @staticmethod
    def forward(ctx, x, k, percentile_mode, scale):  # -> Tensor:
        """
        Args:
            x (`torch.Tensor`):
                Floating point tensor to be quantized.
            k (`int`):
                Quantization bitwidth.
            percentile_mode (`bool`):
                Whether or not to use percentile calibration.
            scale (`torch.Tensor`):
                Pre-calculated scaling factor for *x*. Note that the current implementation of SymmetricQuantFunction
                requires pre-calculated scaling factor.

        Returns:
            `torch.Tensor`: Symmetric-quantized value of *input*.
        """
        ...

    @staticmethod
    def backward(ctx, grad_output):  # -> tuple[Any, None, None, None, None]:
        ...

class floor_ste(Function):
    """
    Straight-through Estimator(STE) for torch.floor()
    """
    @staticmethod
    def forward(ctx, x):  # -> Tensor:
        ...
    @staticmethod
    def backward(ctx, grad_output): ...

class round_ste(Function):
    """
    Straight-through Estimator(STE) for torch.round()
    """
    @staticmethod
    def forward(ctx, x):  # -> Tensor:
        ...
    @staticmethod
    def backward(ctx, grad_output): ...

def batch_frexp(inputs, max_bit=...):  # -> tuple[Tensor, Tensor]:
    """
    Decompose the scaling factor into mantissa and twos exponent.

    Args:
        scaling_factor (`torch.Tensor`):
            Target scaling factor to decompose.

    Returns:
        ``Tuple(torch.Tensor, torch.Tensor)`: mantisa and exponent
    """
    ...

class FixedPointMul(Function):
    """
    Function to perform fixed-point arithmetic that can match integer arithmetic on hardware.

    Args:
        pre_act (`torch.Tensor`):
            Input tensor.
        pre_act_scaling_factor (`torch.Tensor`):
            Scaling factor of the input tensor *pre_act*.
        bit_num (`int`):
            Quantization bitwidth.
        z_scaling_factor (`torch.Tensor`):
            Scaling factor of the output tensor.
        identity (`torch.Tensor`, *optional*):
            Identity tensor, if exists.
        identity_scaling_factor (`torch.Tensor`, *optional*):
            Scaling factor of the identity tensor *identity*, if exists.

    Returns:
        `torch.Tensor`: Output tensor(*pre_act* if *identity* is not given, otherwise the addition of *pre_act* and
        *identity*), whose scale is rescaled to *z_scaling_factor*.
    """
    @staticmethod
    def forward(
        ctx, pre_act, pre_act_scaling_factor, bit_num, z_scaling_factor, identity=..., identity_scaling_factor=...
    ):  # -> Tensor:
        ...
    @staticmethod
    def backward(ctx, grad_output):  # -> tuple[Any, None, None, None, None, Any | None, None]:
        ...
