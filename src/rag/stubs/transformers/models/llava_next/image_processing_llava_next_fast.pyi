"""
This type stub file was generated by pyright.
"""

from ...image_processing_utils import BatchFeature
from ...image_processing_utils_fast import (
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING,
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING_PREPROCESS,
    BaseImageProcessorFast,
    DefaultFastImageProcessorKwargs,
)
from ...image_utils import ImageInput
from ...processing_utils import Unpack
from ...utils import add_start_docstrings, is_torch_available, is_torchvision_available

"""Fast Image processor class for LLaVa-NeXT."""
if is_torch_available(): ...
if is_torchvision_available(): ...

class LlavaNextFastImageProcessorKwargs(DefaultFastImageProcessorKwargs):
    image_grid_pinpoints: list[list[int]] | None
    do_pad: bool | None
    ...

@add_start_docstrings(
    "Constructs a fast ConvNeXT image processor.",
    BASE_IMAGE_PROCESSOR_FAST_DOCSTRING,
    """
        image_grid_pinpoints (`List[List[int]]`, *optional*):
            A list of possible resolutions to use for processing high resolution images. The best resolution is selected
            based on the original size of the image. Can be overridden by `image_grid_pinpoints` in the `preprocess`
            method.
        do_pad (`bool`, *optional*):
            Whether to pad the image. If `True`, will pad the patch dimension of the images in the batch to the largest
            number of patches in the batch. Padding will be applied to the bottom and right with zeros.
    """,
)
class LlavaNextImageProcessorFast(BaseImageProcessorFast):
    resample = ...
    image_mean = ...
    image_std = ...
    size = ...
    default_to_square = ...
    crop_size = ...
    do_resize = ...
    do_center_crop = ...
    do_rescale = ...
    do_normalize = ...
    do_convert_rgb = ...
    do_pad = ...
    image_grid_pinpoints = ...
    valid_kwargs = LlavaNextFastImageProcessorKwargs
    def __init__(self, **kwargs: Unpack[LlavaNextFastImageProcessorKwargs]) -> None: ...
    @add_start_docstrings(
        BASE_IMAGE_PROCESSOR_FAST_DOCSTRING_PREPROCESS,
        """
            image_grid_pinpoints (`List`, *optional*):
                A list of possible resolutions to use for processing high resolution images. Each item in the list should be a tuple or list
                of the form `(height, width)`.
            do_pad (`bool`, *optional*):
                    Whether to pad the image. If `True`, will pad the patch dimension of the images in the batch to the largest
                    number of patches in the batch. Padding will be applied to the bottom and right with zeros.
        """,
    )
    def preprocess(self, images: ImageInput, **kwargs: Unpack[LlavaNextFastImageProcessorKwargs]) -> BatchFeature: ...

__all__ = ["LlavaNextImageProcessorFast"]
