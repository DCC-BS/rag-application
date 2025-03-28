"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING

from ...image_processing_utils import BatchFeature
from ...image_utils import ImageInput
from ...processing_utils import ImagesKwargs, ProcessingKwargs, ProcessorMixin, Unpack
from ...tokenization_utils_base import PreTokenizedInput, TextInput
from ...utils import TensorType
from .modeling_owlv2 import Owlv2ImageGuidedObjectDetectionOutput, Owlv2ObjectDetectionOutput

"""
Image/Text processor class for OWLv2
"""
if TYPE_CHECKING: ...

class Owlv2ImagesKwargs(ImagesKwargs, total=False):
    query_images: ImageInput | None
    ...

class Owlv2ProcessorKwargs(ProcessingKwargs, total=False):
    images_kwargs: Owlv2ImagesKwargs
    _defaults = ...

class Owlv2Processor(ProcessorMixin):
    r"""
    Constructs an Owlv2 processor which wraps [`Owlv2ImageProcessor`] and [`CLIPTokenizer`]/[`CLIPTokenizerFast`] into
    a single processor that interits both the image processor and tokenizer functionalities. See the
    [`~OwlViTProcessor.__call__`] and [`~OwlViTProcessor.decode`] for more information.

    Args:
        image_processor ([`Owlv2ImageProcessor`]):
            The image processor is a required input.
        tokenizer ([`CLIPTokenizer`, `CLIPTokenizerFast`]):
            The tokenizer is a required input.
    """

    attributes = ...
    image_processor_class = ...
    tokenizer_class = ...
    optional_call_args = ...
    def __init__(self, image_processor, tokenizer, **kwargs) -> None: ...
    def __call__(
        self,
        images: ImageInput | None = ...,
        text: TextInput | PreTokenizedInput | list[TextInput] | list[PreTokenizedInput] = ...,
        *args,
        audio=...,
        videos=...,
        **kwargs: Unpack[Owlv2ProcessorKwargs],
    ) -> BatchFeature:
        """
        Main method to prepare for the model one or several text(s) and image(s). This method forwards the `text` and
        `kwargs` arguments to CLIPTokenizerFast's [`~CLIPTokenizerFast.__call__`] if `text` is not `None` to encode:
        the text. To prepare the image(s), this method forwards the `images` and `kwrags` arguments to
        CLIPImageProcessor's [`~CLIPImageProcessor.__call__`] if `images` is not `None`. Please refer to the doctsring
        of the above two methods for more information.

        Args:
            images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`,
            `List[torch.Tensor]`):
                The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
                tensor. Both channels-first and channels-last formats are supported.
            text (`str`, `List[str]`, `List[List[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
                (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
                `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
            query_images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`, `List[torch.Tensor]`):
                The query image to be prepared, one query image is expected per target image to be queried. Each image
                can be a PIL image, NumPy array or PyTorch tensor. In case of a NumPy array/PyTorch tensor, each image
                should be of shape (C, H, W), where C is a number of channels, H and W are image height and width.
            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors of a particular framework. Acceptable values are:
                - `'tf'`: Return TensorFlow `tf.constant` objects.
                - `'pt'`: Return PyTorch `torch.Tensor` objects.
                - `'np'`: Return NumPy `np.ndarray` objects.
                - `'jax'`: Return JAX `jnp.ndarray` objects.

        Returns:
            [`BatchFeature`]: A [`BatchFeature`] with the following fields:
            - **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
            - **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
              `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
              `None`).
            - **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
            - **query_pixel_values** -- Pixel values of the query images to be fed to a model. Returned when `query_images` is not `None`.
        """
        ...

    def post_process_object_detection(self, *args, **kwargs):
        """
        This method forwards all its arguments to [`Owlv2ImageProcessor.post_process_object_detection`]. Please refer
        to the docstring of this method for more information.
        """
        ...

    def post_process_grounded_object_detection(
        self,
        outputs: Owlv2ObjectDetectionOutput,
        threshold: float = ...,
        target_sizes: TensorType | list[tuple] | None = ...,
        text_labels: list[list[str]] | None = ...,
    ):
        """
        Converts the raw output of [`Owlv2ForObjectDetection`] into final bounding boxes in (top_left_x, top_left_y,
        bottom_right_x, bottom_right_y) format.

        Args:
            outputs ([`Owlv2ObjectDetectionOutput`]):
                Raw outputs of the model.
            threshold (`float`, *optional*, defaults to 0.1):
                Score threshold to keep object detection predictions.
            target_sizes (`torch.Tensor` or `List[Tuple[int, int]]`, *optional*):
                Tensor of shape `(batch_size, 2)` or list of tuples (`Tuple[int, int]`) containing the target size
                `(height, width)` of each image in the batch. If unset, predictions will not be resized.
            text_labels (`List[List[str]]`, *optional*):
                List of lists of text labels for each image in the batch. If unset, "text_labels" in output will be
                set to `None`.

        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the following keys:
            - "scores": The confidence scores for each predicted box on the image.
            - "labels": Indexes of the classes predicted by the model on the image.
            - "boxes": Image bounding boxes in (top_left_x, top_left_y, bottom_right_x, bottom_right_y) format.
            - "text_labels": The text labels for each predicted bounding box on the image.
        """
        ...

    def post_process_image_guided_detection(
        self,
        outputs: Owlv2ImageGuidedObjectDetectionOutput,
        threshold: float = ...,
        nms_threshold: float = ...,
        target_sizes: TensorType | list[tuple] | None = ...,
    ):
        """
        Converts the output of [`Owlv2ForObjectDetection.image_guided_detection`] into the format expected by the COCO
        api.

        Args:
            outputs ([`Owlv2ImageGuidedObjectDetectionOutput`]):
                Raw outputs of the model.
            threshold (`float`, *optional*, defaults to 0.0):
                Minimum confidence threshold to use to filter out predicted boxes.
            nms_threshold (`float`, *optional*, defaults to 0.3):
                IoU threshold for non-maximum suppression of overlapping boxes.
            target_sizes (`torch.Tensor`, *optional*):
                Tensor of shape (batch_size, 2) where each entry is the (height, width) of the corresponding image in
                the batch. If set, predicted normalized bounding boxes are rescaled to the target sizes. If left to
                None, predictions will not be unnormalized.

        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the following keys:
            - "scores": The confidence scores for each predicted box on the image.
            - "boxes": Image bounding boxes in (top_left_x, top_left_y, bottom_right_x, bottom_right_y) format.
            - "labels": Set to `None`.
        """
        ...

    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to CLIPTokenizerFast's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
        ...

    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to CLIPTokenizerFast's [`~PreTrainedTokenizer.decode`]. Please refer to
        the docstring of this method for more information.
        """
        ...

__all__ = ["Owlv2Processor"]
