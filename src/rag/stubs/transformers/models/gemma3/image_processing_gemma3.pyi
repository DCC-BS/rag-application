"""
This type stub file was generated by pyright.
"""

import numpy as np
import PIL

from ...image_processing_utils import BaseImageProcessor
from ...image_utils import ChannelDimension, ImageInput, PILImageResampling
from ...utils import TensorType, filter_out_non_signature_kwargs, is_vision_available

"""Image processor class for Gemma3."""
logger = ...
if is_vision_available(): ...

class Gemma3ImageProcessor(BaseImageProcessor):
    r"""
    Constructs a SigLIP image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image's (height, width) dimensions to the specified `size`. Can be overridden by
            `do_resize` in the `preprocess` method.
        size (`Dict[str, int]` *optional*, defaults to `{"height": 224, "width": 224}`):
            Size of the image after resizing. Can be overridden by `size` in the `preprocess` method.
        resample (`PILImageResampling`, *optional*, defaults to `Resampling.BILINEAR`):
            Resampling filter to use if resizing the image. Can be overridden by `resample` in the `preprocess` method.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by `do_rescale` in
            the `preprocess` method.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Can be overridden by `rescale_factor` in the `preprocess`
            method.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image by the specified mean and standard deviation. Can be overridden by
            `do_normalize` in the `preprocess` method.
        image_mean (`float` or `List[float]`, *optional*, defaults to `[0.5, 0.5, 0.5]`):
            Mean to use if normalizing the image. This is a float or list of floats the length of the number of
            channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `[0.5, 0.5, 0.5]`):
            Standard deviation to use if normalizing the image. This is a float or list of floats the length of the
            number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
            Can be overridden by the `image_std` parameter in the `preprocess` method.
        do_convert_rgb (`bool`, *optional*, defaults to `True`):
            Whether to convert the image to RGB.
        do_pan_and_scan (`bool`, *optional*):
            Whether to apply `pan_and_scan` to images.
        pan_and_scan_min_crop_size (`int`, *optional*):
            Minimum size of each crop in pan and scan.
        pan_and_scan_max_num_crops (`int`, *optional*):
            Maximum number of crops per image in pan and scan.
        pan_and_scan_min_ratio_to_activate (`float`, *optional*):
            Minimum aspect ratio to activate pan and scan.
    """

    model_input_names = ...
    def __init__(
        self,
        do_resize: bool = ...,
        size: dict[str, int] = ...,
        resample: PILImageResampling = ...,
        do_rescale: bool = ...,
        rescale_factor: int | float = ...,
        do_normalize: bool = ...,
        image_mean: float | list[float] | None = ...,
        image_std: float | list[float] | None = ...,
        do_convert_rgb: bool = ...,
        do_pan_and_scan: bool = ...,
        pan_and_scan_min_crop_size: int = ...,
        pan_and_scan_max_num_crops: int = ...,
        pan_and_scan_min_ratio_to_activate: float = ...,
        **kwargs,
    ) -> None: ...
    def pan_and_scan(
        self,
        image: np.ndarray,
        pan_and_scan_min_crop_size: int,
        pan_and_scan_max_num_crops: int,
        pan_and_scan_min_ratio_to_activate: float,
        data_format: str | ChannelDimension | None = ...,
        input_data_format: str | ChannelDimension | None = ...,
    ):  # -> list[Any] | list[ndarray[_Shape, Any]]:
        """
        Pan and Scan and image, by cropping into smaller images when the aspect ratio exceeds
        minumum allowed ratio.

        Args:
            image (`np.ndarray`):
                Image to resize.
            pan_and_scan_min_crop_size (`int`, *optional*):
                Minimum size of each crop in pan and scan.
            pan_and_scan_max_num_crops (`int`, *optional*):
                Maximum number of crops per image in pan and scan.
            pan_and_scan_min_ratio_to_activate (`float`, *optional*):
                Minimum aspect ratio to activate pan and scan.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format of the input image. If not provided, it will be inferred.
        """
        ...

    @filter_out_non_signature_kwargs()
    def preprocess(
        self,
        images: ImageInput,
        do_resize: bool = ...,
        size: dict[str, int] = ...,
        resample: PILImageResampling = ...,
        do_rescale: bool = ...,
        rescale_factor: float = ...,
        do_normalize: bool = ...,
        image_mean: float | list[float] | None = ...,
        image_std: float | list[float] | None = ...,
        return_tensors: str | TensorType | None = ...,
        data_format: ChannelDimension | None = ...,
        input_data_format: str | ChannelDimension | None = ...,
        do_convert_rgb: bool = ...,
        do_pan_and_scan: bool = ...,
        pan_and_scan_min_crop_size: int = ...,
        pan_and_scan_max_num_crops: int = ...,
        pan_and_scan_min_ratio_to_activate: float = ...,
    ) -> PIL.Image.Image:
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
                passing in images with pixel values between 0 and 1, set `do_rescale=False`.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Size of the image after resizing.
            resample (`int`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`. Only
                has an effect if `do_resize` is set to `True`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image.
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
                Image mean to use for normalization. Only has an effect if `do_normalize` is set to `True`.
            image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
                Image standard deviation to use for normalization. Only has an effect if `do_normalize` is set to
                `True`.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                - Unset: Return a list of `np.ndarray`.
                - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - Unset: Use the channel dimension format of the input image.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
            do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`):
                Whether to convert the image to RGB.
            do_pan_and_scan (`bool`, *optional*, defaults to `self.do_convert_rgb`):
                Whether to apply `pan_and_scan` to images.
            pan_and_scan_min_crop_size (`int`, *optional*, defaults to `self.pan_and_scan_min_crop_size`):
                Minimum size of each crop in pan and scan.
            pan_and_scan_max_num_crops (`int`, *optional*, defaults to `self.pan_and_scan_max_num_crops`):
                Maximum number of crops per image in pan and scan.
            pan_and_scan_min_ratio_to_activate (`float`, *optional*, defaults to `self.pan_and_scan_min_ratio_to_activate`):
                Minimum aspect ratio to activate pan and scan.
        """
        ...

__all__ = ["Gemma3ImageProcessor"]
