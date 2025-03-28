"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

import numpy as np
import PIL.Image

from .utils import ExplicitEnum, is_vision_available

if is_vision_available(): ...
if TYPE_CHECKING: ...
logger = ...
ImageInput = Union[
    "PIL.Image.Image", np.ndarray, "torch.Tensor", list["PIL.Image.Image"], list[np.ndarray], list["torch.Tensor"]
]
VideoInput = Union[
    list["PIL.Image.Image"],
    "np.ndarray",
    "torch.Tensor",
    list["np.ndarray"],
    list["torch.Tensor"],
    list[list["PIL.Image.Image"]],
    list[list["np.ndarrray"]],
    list[list["torch.Tensor"]],
]

class ChannelDimension(ExplicitEnum):
    FIRST = ...
    LAST = ...

class AnnotationFormat(ExplicitEnum):
    COCO_DETECTION = ...
    COCO_PANOPTIC = ...

class AnnotionFormat(ExplicitEnum):
    COCO_DETECTION = ...
    COCO_PANOPTIC = ...

@dataclass
class VideoMetadata:
    total_num_frames: int
    fps: float
    duration: float
    video_backend: str
    ...

AnnotationType = dict[str, int | str | list[dict]]

def is_pil_image(img):  # -> bool:
    ...

class ImageType(ExplicitEnum):
    PIL = ...
    TORCH = ...
    NUMPY = ...
    TENSORFLOW = ...
    JAX = ...

def get_image_type(
    image,
):  # -> Literal[ImageType.PIL, ImageType.TORCH, ImageType.NUMPY, ImageType.TENSORFLOW, ImageType.JAX]:
    ...
def is_valid_image(img):  # -> bool:
    ...
def is_valid_list_of_images(images: list):  # -> list[Any] | bool:
    ...
def valid_images(imgs):  # -> bool:
    ...
def is_batched(img):  # -> bool:
    ...
def is_scaled_image(image: np.ndarray) -> bool:
    """
    Checks to see whether the pixel values have already been rescaled to [0, 1].
    """
    ...

def make_list_of_images(images, expected_ndims: int = ...) -> list[ImageInput]:
    """
    Ensure that the output is a list of images. If the input is a single image, it is converted to a list of length 1.
    If the input is a batch of images, it is converted to a list of images.

    Args:
        images (`ImageInput`):
            Image of images to turn into a list of images.
        expected_ndims (`int`, *optional*, defaults to 3):
            Expected number of dimensions for a single input image. If the input image has a different number of
            dimensions, an error is raised.
    """
    ...

def make_flat_list_of_images(images: list[ImageInput] | ImageInput) -> ImageInput:
    """
    Ensure that the output is a flat list of images. If the input is a single image, it is converted to a list of length 1.
    If the input is a nested list of images, it is converted to a flat list of images.
    Args:
        images (`Union[List[ImageInput], ImageInput]`):
            The input image.
    Returns:
        list: A list of images or a 4d array of images.
    """
    ...

def make_nested_list_of_images(images: list[ImageInput] | ImageInput) -> ImageInput:
    """
    Ensure that the output is a nested list of images.
    Args:
        images (`Union[List[ImageInput], ImageInput]`):
            The input image.
    Returns:
        list: A list of list of images or a list of 4d array of images.
    """
    ...

def make_batched_videos(videos) -> VideoInput:
    """
    Ensure that the input is a list of videos.
    Args:
        videos (`VideoInput`):
            Video or videos to turn into a list of videos.
    Returns:
        list: A list of videos.
    """
    ...

def to_numpy_array(img) -> np.ndarray: ...
def infer_channel_dimension_format(
    image: np.ndarray, num_channels: int | tuple[int, ...] | None = ...
) -> ChannelDimension:
    """
    Infers the channel dimension format of `image`.

    Args:
        image (`np.ndarray`):
            The image to infer the channel dimension of.
        num_channels (`int` or `Tuple[int, ...]`, *optional*, defaults to `(1, 3)`):
            The number of channels of the image.

    Returns:
        The channel dimension of the image.
    """
    ...

def get_channel_dimension_axis(image: np.ndarray, input_data_format: ChannelDimension | str | None = ...) -> int:
    """
    Returns the channel dimension axis of the image.

    Args:
        image (`np.ndarray`):
            The image to get the channel dimension axis of.
        input_data_format (`ChannelDimension` or `str`, *optional*):
            The channel dimension format of the image. If `None`, will infer the channel dimension from the image.

    Returns:
        The channel dimension axis of the image.
    """
    ...

def get_image_size(image: np.ndarray, channel_dim: ChannelDimension = ...) -> tuple[int, int]:
    """
    Returns the (height, width) dimensions of the image.

    Args:
        image (`np.ndarray`):
            The image to get the dimensions of.
        channel_dim (`ChannelDimension`, *optional*):
            Which dimension the channel dimension is in. If `None`, will infer the channel dimension from the image.

    Returns:
        A tuple of the image's height and width.
    """
    ...

def get_image_size_for_max_height_width(
    image_size: tuple[int, int], max_height: int, max_width: int
) -> tuple[int, int]:
    """
    Computes the output image size given the input image and the maximum allowed height and width. Keep aspect ratio.
    Important, even if image_height < max_height and image_width < max_width, the image will be resized
    to at least one of the edges be equal to max_height or max_width.

    For example:
        - input_size: (100, 200), max_height: 50, max_width: 50 -> output_size: (25, 50)
        - input_size: (100, 200), max_height: 200, max_width: 500 -> output_size: (200, 400)

    Args:
        image_size (`Tuple[int, int]`):
            The image to resize.
        max_height (`int`):
            The maximum allowed height.
        max_width (`int`):
            The maximum allowed width.
    """
    ...

def is_valid_annotation_coco_detection(annotation: dict[str, list | tuple]) -> bool: ...
def is_valid_annotation_coco_panoptic(annotation: dict[str, list | tuple]) -> bool: ...
def valid_coco_detection_annotations(annotations: Iterable[dict[str, list | tuple]]) -> bool: ...
def valid_coco_panoptic_annotations(annotations: Iterable[dict[str, list | tuple]]) -> bool: ...
def load_image(image: str | PIL.Image.Image, timeout: float | None = ...) -> PIL.Image.Image:
    """
    Loads `image` to a PIL Image.

    Args:
        image (`str` or `PIL.Image.Image`):
            The image to convert to the PIL Image format.
        timeout (`float`, *optional*):
            The timeout value in seconds for the URL request.

    Returns:
        `PIL.Image.Image`: A PIL Image.
    """
    ...

def default_sample_indices_fn(metadata: VideoMetadata, num_frames=..., fps=..., **kwargs):  # -> _Array1D[Any]:
    """
    A default sampling function that replicates the logic used in get_uniform_frame_indices,
    while optionally handling `fps` if `num_frames` is not provided.

    Args:
        metadata (`VideoMetadata`):
            `VideoMetadata` object containing metadata about the video, such as "total_num_frames" or "fps".
        num_frames (`int`, *optional*):
            Number of frames to sample uniformly.
        fps (`int`, *optional*):
            Desired frames per second. Takes priority over num_frames if both are provided.

    Returns:
        `np.ndarray`: Array of frame indices to sample.
    """
    ...

def read_video_opencv(video_path: str, sample_indices_fn: Callable, **kwargs):  # -> tuple[NDArray[Any], VideoMetadata]:
    """
    Decode a video using the OpenCV backend.

    Args:
        video_path (`str`):
            Path to the video file.
        sample_indices_fn (`Callable`):
            A callable function that will return indices at which the video should be sampled. If the video has to be loaded using
            by a different sampling technique than provided by `num_frames` or `fps` arguments, one should provide their own `sample_indices_fn`.
            If not provided, simple uniform sampling with fps is performed.
            Example:
            def sample_indices_fn(metadata, **kwargs):
                return np.linspace(0, metadata.total_num_frames - 1, num_frames, dtype=int)

    Returns:
        Tuple[`np.array`, `VideoMetadata`]: A tuple containing:
            - Numpy array of frames in RGB (shape: [num_frames, height, width, 3]).
            - `VideoMetadata` object.
    """
    ...

def read_video_decord(
    video_path: str, sample_indices_fn: Callable | None = ..., **kwargs
):  # -> tuple[Any, VideoMetadata]:
    """
    Decode a video using the Decord backend.

    Args:
        video_path (`str`):
            Path to the video file.
        sample_indices_fn (`Callable`, *optional*):
            A callable function that will return indices at which the video should be sampled. If the video has to be loaded using
            by a different sampling technique than provided by `num_frames` or `fps` arguments, one should provide their own `sample_indices_fn`.
            If not provided, simple uniform sampling with fps is performed.
            Example:
            def sample_indices_fn(metadata, **kwargs):
                return np.linspace(0, metadata.total_num_frames - 1, num_frames, dtype=int)

    Returns:
        Tuple[`np.array`, `VideoMetadata`]: A tuple containing:
            - Numpy array of frames in RGB (shape: [num_frames, height, width, 3]).
            - `VideoMetadata` object.
    """
    ...

def read_video_pyav(video_path: str, sample_indices_fn: Callable, **kwargs):  # -> tuple[NDArray[Any], VideoMetadata]:
    """
    Decode the video with PyAV decoder.

    Args:
        video_path (`str`):
            Path to the video file.
        sample_indices_fn (`Callable`, *optional*):
            A callable function that will return indices at which the video should be sampled. If the video has to be loaded using
            by a different sampling technique than provided by `num_frames` or `fps` arguments, one should provide their own `sample_indices_fn`.
            If not provided, simple uniform sampling with fps is performed.
            Example:
            def sample_indices_fn(metadata, **kwargs):
                return np.linspace(0, metadata.total_num_frames - 1, num_frames, dtype=int)

    Returns:
        Tuple[`np.array`, `VideoMetadata`]: A tuple containing:
            - Numpy array of frames in RGB (shape: [num_frames, height, width, 3]).
            - `VideoMetadata` object.
    """
    ...

def read_video_torchvision(
    video_path: str, sample_indices_fn: Callable, **kwargs
):  # -> tuple[ndarray[Any, Any], VideoMetadata]:
    """
    Decode the video with torchvision decoder.

    Args:
        video_path (`str`):
            Path to the video file.
        sample_indices_fn (`Callable`, *optional*):
            A callable function that will return indices at which the video should be sampled. If the video has to be loaded using
            by a different sampling technique than provided by `num_frames` or `fps` arguments, one should provide their own `sample_indices_fn`.
            If not provided, simple uniform sampling with fps is performed.
            Example:
            def sample_indices_fn(metadata, **kwargs):
                return np.linspace(0, metadata.total_num_frames - 1, num_frames, dtype=int)

    Returns:
        Tuple[`np.array`, `VideoMetadata`]: A tuple containing:
            - Numpy array of frames in RGB (shape: [num_frames, height, width, 3]).
            - `VideoMetadata` object.
    """
    ...

VIDEO_DECODERS = ...

def load_video(
    video: str | VideoInput,
    num_frames: int | None = ...,
    fps: int | None = ...,
    backend: str = ...,
    sample_indices_fn: Callable | None = ...,
    **kwargs,
) -> np.array:
    """
    Loads `video` to a numpy array.

    Args:
        video (`str` or `VideoInput`):
            The video to convert to the numpy array format. Can be a link to video or local path.
        num_frames (`int`, *optional*):
            Number of frames to sample uniformly. If not passed, the whole video is loaded.
        fps (`int`, *optional*):
            Number of frames to sample per second. Should be passed only when `num_frames=None`.
            If not specified and `num_frames==None`, all frames are sampled.
        backend (`str`, *optional*, defaults to `"opencv"`):
            The backend to use when loading the video. Can be any of ["decord", "pyav", "opencv", "torchvision"]. Defaults to "opencv".
        sample_indices_fn (`Callable`, *optional*):
            A callable function that will return indices at which the video should be sampled. If the video has to be loaded using
            by a different sampling technique than provided by `num_frames` or `fps` arguments, one should provide their own `sample_indices_fn`.
            If not provided, simple uniformt sampling with fps is performed, otherwise `sample_indices_fn` has priority over other args.
            The function expects at input the all args along with all kwargs passed to `load_video` and should output valid
            indices at which the video should be sampled. For example:

            Example:
            def sample_indices_fn(metadata, **kwargs):
                return np.linspace(0, metadata.total_num_frames - 1, num_frames, dtype=int)

    Returns:
        Tuple[`np.array`, Dict]: A tuple containing:
            - Numpy array of frames in RGB (shape: [num_frames, height, width, 3]).
            - Metadata dictionary.
    """
    ...

def load_images(
    images: list | tuple | str | PIL.Image.Image, timeout: float | None = ...
) -> PIL.Image.Image | list[PIL.Image.Image] | list[list[PIL.Image.Image]]:
    """Loads images, handling different levels of nesting.

    Args:
      images: A single image, a list of images, or a list of lists of images to load.
      timeout: Timeout for loading images.

    Returns:
      A single image, a list of images, a list of lists of images.
    """
    ...

def validate_preprocess_arguments(
    do_rescale: bool | None = ...,
    rescale_factor: float | None = ...,
    do_normalize: bool | None = ...,
    image_mean: float | list[float] | None = ...,
    image_std: float | list[float] | None = ...,
    do_pad: bool | None = ...,
    size_divisibility: int | None = ...,
    do_center_crop: bool | None = ...,
    crop_size: dict[str, int] | None = ...,
    do_resize: bool | None = ...,
    size: dict[str, int] | None = ...,
    resample: PILImageResampling | None = ...,
):  # -> None:
    """
    Checks validity of typically used arguments in an `ImageProcessor` `preprocess` method.
    Raises `ValueError` if arguments incompatibility is caught.
    Many incompatibilities are model-specific. `do_pad` sometimes needs `size_divisor`,
    sometimes `size_divisibility`, and sometimes `size`. New models and processors added should follow
    existing arguments when possible.

    """
    ...

class ImageFeatureExtractionMixin:
    """
    Mixin that contain utilities for preparing image features.
    """
    def to_pil_image(self, image, rescale=...):  # -> Image:
        """
        Converts `image` to a PIL Image. Optionally rescales it and puts the channel dimension back as the last axis if
        needed.

        Args:
            image (`PIL.Image.Image` or `numpy.ndarray` or `torch.Tensor`):
                The image to convert to the PIL Image format.
            rescale (`bool`, *optional*):
                Whether or not to apply the scaling factor (to make pixel values integers between 0 and 255). Will
                default to `True` if the image type is a floating type, `False` otherwise.
        """
        ...

    def convert_rgb(self, image):  # -> Image:
        """
        Converts `PIL.Image.Image` to RGB format.

        Args:
            image (`PIL.Image.Image`):
                The image to convert.
        """
        ...

    def rescale(self, image: np.ndarray, scale: float | int) -> np.ndarray:
        """
        Rescale a numpy image by scale amount
        """
        ...

    def to_numpy_array(self, image, rescale=..., channel_first=...):  # -> NDArray[Any] | ndarray[Any, Any]:
        """
        Converts `image` to a numpy array. Optionally rescales it and puts the channel dimension as the first
        dimension.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to convert to a NumPy array.
            rescale (`bool`, *optional*):
                Whether or not to apply the scaling factor (to make pixel values floats between 0. and 1.). Will
                default to `True` if the image is a PIL Image or an array/tensor of integers, `False` otherwise.
            channel_first (`bool`, *optional*, defaults to `True`):
                Whether or not to permute the dimensions of the image to put the channel dimension first.
        """
        ...

    def expand_dims(self, image):  # -> Image | NDArray[Any]:
        """
        Expands 2-dimensional `image` to 3 dimensions.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to expand.
        """
        ...

    def normalize(self, image, mean, std, rescale=...):  # -> NDArray[float64]:
        """
        Normalizes `image` with `mean` and `std`. Note that this will trigger a conversion of `image` to a NumPy array
        if it's a PIL Image.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to normalize.
            mean (`List[float]` or `np.ndarray` or `torch.Tensor`):
                The mean (per channel) to use for normalization.
            std (`List[float]` or `np.ndarray` or `torch.Tensor`):
                The standard deviation (per channel) to use for normalization.
            rescale (`bool`, *optional*, defaults to `False`):
                Whether or not to rescale the image to be between 0 and 1. If a PIL image is provided, scaling will
                happen automatically.
        """
        ...

    def resize(self, image, size, resample=..., default_to_square=..., max_size=...):  # -> Image:
        """
        Resizes `image`. Enforces conversion of input to PIL.Image.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to resize.
            size (`int` or `Tuple[int, int]`):
                The size to use for resizing the image. If `size` is a sequence like (h, w), output size will be
                matched to this.

                If `size` is an int and `default_to_square` is `True`, then image will be resized to (size, size). If
                `size` is an int and `default_to_square` is `False`, then smaller edge of the image will be matched to
                this number. i.e, if height > width, then image will be rescaled to (size * height / width, size).
            resample (`int`, *optional*, defaults to `PILImageResampling.BILINEAR`):
                The filter to user for resampling.
            default_to_square (`bool`, *optional*, defaults to `True`):
                How to convert `size` when it is a single int. If set to `True`, the `size` will be converted to a
                square (`size`,`size`). If set to `False`, will replicate
                [`torchvision.transforms.Resize`](https://pytorch.org/vision/stable/transforms.html#torchvision.transforms.Resize)
                with support for resizing only the smallest edge and providing an optional `max_size`.
            max_size (`int`, *optional*, defaults to `None`):
                The maximum allowed for the longer edge of the resized image: if the longer edge of the image is
                greater than `max_size` after being resized according to `size`, then the image is resized again so
                that the longer edge is equal to `max_size`. As a result, `size` might be overruled, i.e the smaller
                edge may be shorter than `size`. Only used if `default_to_square` is `False`.

        Returns:
            image: A resized `PIL.Image.Image`.
        """
        ...

    def center_crop(self, image, size):  # -> Image | ndarray[_Shape, dtype[Any]] | ndarray[_Shape, Any]:
        """
        Crops `image` to the given size using a center crop. Note that if the image is too small to be cropped to the
        size given, it will be padded (so the returned result has the size asked).

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor` of shape (n_channels, height, width) or (height, width, n_channels)):
                The image to resize.
            size (`int` or `Tuple[int, int]`):
                The size to which crop the image.

        Returns:
            new_image: A center cropped `PIL.Image.Image` or `np.ndarray` or `torch.Tensor` of shape: (n_channels,
            height, width).
        """
        ...

    def flip_channel_order(self, image):  # -> ndarray[_Shape, dtype[Any]] | ndarray[_Shape, Any]:
        """
        Flips the channel order of `image` from RGB to BGR, or vice versa. Note that this will trigger a conversion of
        `image` to a NumPy array if it's a PIL Image.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image whose color channels to flip. If `np.ndarray` or `torch.Tensor`, the channel dimension should
                be first.
        """
        ...

    def rotate(self, image, angle, resample=..., expand=..., center=..., translate=..., fillcolor=...):  # -> Image:
        """
        Returns a rotated copy of `image`. This method returns a copy of `image`, rotated the given number of degrees
        counter clockwise around its centre.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to rotate. If `np.ndarray` or `torch.Tensor`, will be converted to `PIL.Image.Image` before
                rotating.

        Returns:
            image: A rotated `PIL.Image.Image`.
        """
        ...

def validate_annotations(
    annotation_format: AnnotationFormat,
    supported_annotation_formats: tuple[AnnotationFormat, ...],
    annotations: list[dict],
) -> None: ...
def validate_kwargs(valid_processor_keys: list[str], captured_kwargs: list[str]):  # -> None:
    ...
@dataclass(frozen=True)
class SizeDict:
    """
    Hashable dictionary to store image size information.
    """

    height: int = ...
    width: int = ...
    longest_edge: int = ...
    shortest_edge: int = ...
    max_height: int = ...
    max_width: int = ...
    def __getitem__(self, key):  # -> Any:
        ...
