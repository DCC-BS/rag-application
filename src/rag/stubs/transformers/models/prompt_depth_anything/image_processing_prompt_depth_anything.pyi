"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING

import numpy as np

from ...image_processing_utils import BaseImageProcessor, BatchFeature
from ...image_utils import ChannelDimension, ImageInput, PILImageResampling, is_torch_available
from ...modeling_outputs import DepthEstimatorOutput
from ...utils import TensorType, filter_out_non_signature_kwargs

"""Image processor class for PromptDepthAnything."""
if TYPE_CHECKING: ...
if is_torch_available(): ...
logger = ...

class PromptDepthAnythingImageProcessor(BaseImageProcessor):
    r"""
    Constructs a PromptDepthAnything image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image's (height, width) dimensions. Can be overidden by `do_resize` in `preprocess`.
        size (`Dict[str, int]` *optional*, defaults to `{"height": 384, "width": 384}`):
            Size of the image after resizing. Can be overidden by `size` in `preprocess`.
        resample (`PILImageResampling`, *optional*, defaults to `Resampling.BICUBIC`):
            Defines the resampling filter to use if resizing the image. Can be overidden by `resample` in `preprocess`.
        keep_aspect_ratio (`bool`, *optional*, defaults to `False`):
            If `True`, the image is resized to the largest possible size such that the aspect ratio is preserved. Can
            be overidden by `keep_aspect_ratio` in `preprocess`.
        ensure_multiple_of (`int`, *optional*, defaults to 1):
            If `do_resize` is `True`, the image is resized to a size that is a multiple of this value. Can be overidden
            by `ensure_multiple_of` in `preprocess`.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image by the specified scale `rescale_factor`. Can be overidden by `do_rescale` in
            `preprocess`.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Can be overidden by `rescale_factor` in `preprocess`.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess`
            method.
        image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`):
            Mean to use if normalizing the image. This is a float or list of floats the length of the number of
            channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`):
            Standard deviation to use if normalizing the image. This is a float or list of floats the length of the
            number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
        do_pad (`bool`, *optional*, defaults to `False`):
            Whether to apply center padding. This was introduced in the DINOv2 paper, which uses the model in
            combination with DPT.
        size_divisor (`int`, *optional*):
            If `do_pad` is `True`, pads the image dimensions to be divisible by this value. This was introduced in the
            DINOv2 paper, which uses the model in combination with DPT.
        prompt_scale_to_meter (`float`, *optional*, defaults to 0.001):
            Scale factor to convert the prompt depth to meters.
    """

    model_input_names = ...
    def __init__(
        self,
        do_resize: bool = ...,
        size: dict[str, int] = ...,
        resample: PILImageResampling = ...,
        keep_aspect_ratio: bool = ...,
        ensure_multiple_of: int = ...,
        do_rescale: bool = ...,
        rescale_factor: int | float = ...,
        do_normalize: bool = ...,
        image_mean: float | list[float] | None = ...,
        image_std: float | list[float] | None = ...,
        do_pad: bool = ...,
        size_divisor: int = ...,
        prompt_scale_to_meter: float = ...,
        **kwargs,
    ) -> None: ...
    def resize(
        self,
        image: np.ndarray,
        size: dict[str, int],
        keep_aspect_ratio: bool = ...,
        ensure_multiple_of: int = ...,
        resample: PILImageResampling = ...,
        data_format: str | ChannelDimension | None = ...,
        input_data_format: str | ChannelDimension | None = ...,
        **kwargs,
    ) -> np.ndarray:
        """
        Resize an image to target size `(size["height"], size["width"])`. If `keep_aspect_ratio` is `True`, the image
        is resized to the largest possible size such that the aspect ratio is preserved. If `ensure_multiple_of` is
        set, the image is resized to a size that is a multiple of this value.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Target size of the output image.
            keep_aspect_ratio (`bool`, *optional*, defaults to `False`):
                If `True`, the image is resized to the largest possible size such that the aspect ratio is preserved.
            ensure_multiple_of (`int`, *optional*, defaults to 1):
                The image is resized to a size that is a multiple of this value.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
                Resampling filter to use when resiizing the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
            input_data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the input image. If not provided, it will be inferred.
        """
        ...

    def pad_image(
        self,
        image: np.ndarray,
        size_divisor: int,
        data_format: str | ChannelDimension | None = ...,
        input_data_format: str | ChannelDimension | None = ...,
    ):  # -> ndarray[Any, Any]:
        """
        Center pad an image to be a multiple of `multiple`.

        Args:
            image (`np.ndarray`):
                Image to pad.
            size_divisor (`int`):
                The width and height of the image will be padded to a multiple of this number.
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
        """
        ...

    @filter_out_non_signature_kwargs()
    def preprocess(
        self,
        images: ImageInput,
        prompt_depth: ImageInput | None = ...,
        do_resize: bool | None = ...,
        size: int | None = ...,
        keep_aspect_ratio: bool | None = ...,
        ensure_multiple_of: int | None = ...,
        resample: PILImageResampling | None = ...,
        do_rescale: bool | None = ...,
        rescale_factor: float | None = ...,
        do_normalize: bool | None = ...,
        image_mean: float | list[float] | None = ...,
        image_std: float | list[float] | None = ...,
        do_pad: bool | None = ...,
        size_divisor: int | None = ...,
        prompt_scale_to_meter: float | None = ...,
        return_tensors: str | TensorType | None = ...,
        data_format: ChannelDimension = ...,
        input_data_format: str | ChannelDimension | None = ...,
    ) -> BatchFeature:
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess. Expects a single or batch of images with pixel values ranging from 0 to 255. If
                passing in images with pixel values between 0 and 1, set `do_rescale=False`.
            prompt_depth (`ImageInput`, *optional*):
                Prompt depth to preprocess, which can be sparse depth obtained from multi-view geometry or
                low-resolution depth from a depth sensor. Generally has shape (height, width), where height
                and width can be smaller than those of the images. It's optional and can be None, which means no prompt depth
                is used. If it is None, the output depth will be a monocular relative depth.
                It is recommended to provide a prompt_scale_to_meter value, which is the scale factor to convert the prompt depth
                to meters. This is useful when the prompt depth is not in meters.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Size of the image after resizing. If `keep_aspect_ratio` is `True`, the image is resized to the largest
                possible size such that the aspect ratio is preserved. If `ensure_multiple_of` is set, the image is
                resized to a size that is a multiple of this value.
            keep_aspect_ratio (`bool`, *optional*, defaults to `self.keep_aspect_ratio`):
                Whether to keep the aspect ratio of the image. If False, the image will be resized to (size, size). If
                True, the image will be resized to keep the aspect ratio and the size will be the maximum possible.
            ensure_multiple_of (`int`, *optional*, defaults to `self.ensure_multiple_of`):
                Ensure that the image size is a multiple of this value.
            resample (`int`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`, Only
                has an effect if `do_resize` is set to `True`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image values between [0 - 1].
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
                Image mean.
            image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
                Image standard deviation.
            prompt_scale_to_meter (`float`, *optional*, defaults to `self.prompt_scale_to_meter`):
                Scale factor to convert the prompt depth to meters.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                    - Unset: Return a list of `np.ndarray`.
                    - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                    - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                    - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                    - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                    - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                    - `ChannelDimension.LAST`: image in (height, width, num_channels) format.
            input_data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the input image. If unset, the channel dimension format is inferred
                from the input image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - `"none"` or `ChannelDimension.NONE`: image in (height, width) format.
        """
        ...

    def post_process_depth_estimation(
        self, outputs: DepthEstimatorOutput, target_sizes: TensorType | list[tuple[int, int]] | None | None = ...
    ) -> list[dict[str, TensorType]]:
        """
        Converts the raw output of [`DepthEstimatorOutput`] into final depth predictions and depth PIL images.
        Only supports PyTorch.

        Args:
            outputs ([`DepthEstimatorOutput`]):
                Raw outputs of the model.
            target_sizes (`TensorType` or `List[Tuple[int, int]]`, *optional*):
                Tensor of shape `(batch_size, 2)` or list of tuples (`Tuple[int, int]`) containing the target size
                (height, width) of each image in the batch. If left to None, predictions will not be resized.

        Returns:
            `List[Dict[str, TensorType]]`: A list of dictionaries of tensors representing the processed depth
            predictions.
        """
        ...

__all__ = ["PromptDepthAnythingImageProcessor"]
