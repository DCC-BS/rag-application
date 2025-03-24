"""
This type stub file was generated by pyright.
"""

import torch

from ...image_processing_utils import BatchFeature
from ...image_processing_utils_fast import (
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING,
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING_PREPROCESS,
    BaseImageProcessorFast,
    DefaultFastImageProcessorKwargs,
)
from ...image_utils import ImageInput, PILImageResampling
from ...processing_utils import Unpack
from ...utils import add_start_docstrings, is_torch_available, is_torchvision_available

"""Fast Image processor class for ConvNeXT."""
if is_torch_available(): ...
if is_torchvision_available(): ...

class ConvNextFastImageProcessorKwargs(DefaultFastImageProcessorKwargs):
    crop_pct: float | None
    ...

@add_start_docstrings(
    r"Constructs a fast ConvNeXT image processor.",
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING,
    """
        crop_pct (`float`, *optional*):
            Percentage of the image to crop. Only has an effect if size < 384. Can be
            overridden by `crop_pct` in the`preprocess` method.
    """,
)
class ConvNextImageProcessorFast(BaseImageProcessorFast):
    resample = ...
    image_mean = ...
    image_std = ...
    size = ...
    default_to_square = ...
    do_resize = ...
    do_rescale = ...
    do_normalize = ...
    crop_pct = ...
    valid_kwargs = ConvNextFastImageProcessorKwargs
    def __init__(self, **kwargs: Unpack[ConvNextFastImageProcessorKwargs]) -> None: ...
    @add_start_docstrings(
        BASE_IMAGE_PROCESSOR_FAST_DOCSTRING_PREPROCESS,
        """
        crop_pct (`float`, *optional*):
            Percentage of the image to crop. Only has an effect if size < 384. Can be
            overridden by `crop_pct` in the`preprocess` method.
        """,
    )
    def preprocess(self, images: ImageInput, **kwargs: Unpack[ConvNextFastImageProcessorKwargs]) -> BatchFeature: ...
    def resize(
        self,
        image: torch.Tensor,
        size: dict[str, int],
        crop_pct: float,
        interpolation: PILImageResampling = ...,
        **kwargs,
    ) -> torch.Tensor:
        """
        Resize an image.

        Args:
            image (`torch.Tensor`):
                Image to resize.
            size (`Dict[str, int]`):
                Dictionary of the form `{"shortest_edge": int}`, specifying the size of the output image. If
                `size["shortest_edge"]` >= 384 image is resized to `(size["shortest_edge"], size["shortest_edge"])`.
                Otherwise, the smaller edge of the image will be matched to `int(size["shortest_edge"] / crop_pct)`,
                after which the image is cropped to `(size["shortest_edge"], size["shortest_edge"])`.
            crop_pct (`float`):
                Percentage of the image to crop. Only has an effect if size < 384.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
                Resampling filter to use when resizing the image.

        Returns:
            `torch.Tensor`: Resized image.
        """
        ...

__all__ = ["ConvNextImageProcessorFast"]
