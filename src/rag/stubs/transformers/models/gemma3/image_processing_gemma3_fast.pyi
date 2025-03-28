"""
This type stub file was generated by pyright.
"""

import torch

from ...image_processing_utils_fast import (
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING,
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING_PREPROCESS,
    BaseImageProcessorFast,
    BatchFeature,
    DefaultFastImageProcessorKwargs,
)
from ...image_utils import ImageInput
from ...processing_utils import Unpack
from ...utils import add_start_docstrings, is_torch_available, is_torchvision_available, is_vision_available

"""Fast Image processor class for SigLIP."""
if is_vision_available(): ...
if is_torch_available(): ...
if is_torchvision_available(): ...
logger = ...

class Gemma3FastImageProcessorKwargs(DefaultFastImageProcessorKwargs):
    do_pan_and_scan: bool | None
    pan_and_scan_min_crop_size: int | None
    pan_and_scan_max_num_crops: int | None
    pan_and_scan_min_ratio_to_activate: float | None
    ...

@add_start_docstrings(
    "Constructs a fast ConvNeXT image processor. Based on [`SiglipImageProcessor`] with incorporation of Pan adn Scan cropping method.",
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING,
    """
        do_pan_and_scan (`bool`, *optional*):
            Whether to apply `pan_and_scan` to images.
        pan_and_scan_min_crop_size (`int`, *optional*):
            Minimum size of each crop in pan and scan.
        pan_and_scan_max_num_crops (`int`, *optional*):
            Maximum number of crops per image in pan and scan.
        pan_and_scan_min_ratio_to_activate (`float`, *optional*):
            Minimum aspect ratio to activate pan and scan.
    """,
)
class Gemma3ImageProcessorFast(BaseImageProcessorFast):
    resample = ...
    image_mean = ...
    image_std = ...
    size = ...
    default_to_square = ...
    do_resize = ...
    do_rescale = ...
    do_normalize = ...
    do_pan_and_scan = ...
    pan_and_scan_min_crop_size = ...
    pan_and_scan_max_num_crops = ...
    pan_and_scan_min_ratio_to_activate = ...
    valid_kwargs = Gemma3FastImageProcessorKwargs
    def __init__(self, **kwargs: Unpack[Gemma3FastImageProcessorKwargs]) -> None: ...
    def pan_and_scan(
        self,
        image: torch.Tensor,
        pan_and_scan_min_crop_size: int,
        pan_and_scan_max_num_crops: int,
        pan_and_scan_min_ratio_to_activate: float,
    ):  # -> list[Any] | list[Tensor]:
        """
        Pan and Scan an image, by cropping into smaller images when the aspect ratio exceeds
        minumum allowed ratio.

        Args:
            image (`torch.Tensor`):
                Image to resize.
            pan_and_scan_min_crop_size (`int`, *optional*):
                Minimum size of each crop in pan and scan.
            pan_and_scan_max_num_crops (`int`, *optional*):
                Maximum number of crops per image in pan and scan.
            pan_and_scan_min_ratio_to_activate (`float`, *optional*):
                Minimum aspect ratio to activate pan and scan.
        """
        ...

    @add_start_docstrings(
        BASE_IMAGE_PROCESSOR_FAST_DOCSTRING_PREPROCESS,
        """
            do_pan_and_scan (`bool`, *optional*):
                Whether to apply `pan_and_scan` to images.
            pan_and_scan_min_crop_size (`int`, *optional*):
                Minimum size of each crop in pan and scan.
            pan_and_scan_max_num_crops (`int`, *optional*):
                Maximum number of crops per image in pan and scan.
            pan_and_scan_min_ratio_to_activate (`float`, *optional*):
                Minimum aspect ratio to activate pan and scan.
        """,
    )
    def preprocess(self, images: ImageInput, **kwargs: Unpack[Gemma3FastImageProcessorKwargs]) -> BatchFeature: ...

__all__ = ["Gemma3ImageProcessorFast"]
