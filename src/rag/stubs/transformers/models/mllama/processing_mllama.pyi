"""
This type stub file was generated by pyright.
"""

import numpy as np

from ...feature_extraction_utils import BatchFeature
from ...image_utils import ImageInput
from ...processing_utils import ImagesKwargs, ProcessingKwargs, ProcessorMixin, Unpack
from ...tokenization_utils_base import PreTokenizedInput, TextInput

"""Processor class for Mllama."""

class MllamaImagesKwargs(ImagesKwargs, total=False):
    max_image_tiles: int | None
    ...

class MllamaProcessorKwargs(ProcessingKwargs, total=False):
    images_kwargs: MllamaImagesKwargs
    _defaults = ...

def get_cross_attention_token_mask(input_ids: list[int], image_token_id: int) -> list[list[int]]:
    """
    Generate a cross-attention token mask for image tokens in the input sequence.

    This function identifies the positions of image tokens in the input sequence and creates
    a mask that defines which subsequent tokens each image token should attend to.

    Args:
        input_ids (List[int]): A list of token ids representing the input sequence.
        image_token_id (int): The id of the token used to represent images in the sequence.

    Returns:
        List[List[int]]: A list of [start, end] pairs, where each pair represents the range
        of tokens an image token should attend to.

    Notes:
        - If no image tokens are present, an empty list is returned.
        - For a single image token, it attends to all subsequent tokens until the end of the sequence.
        - For multiple image tokens, each attends to tokens up to the next image token or the end of the sequence.
        - Consecutive image tokens are treated as a group and attend to all subsequent tokens together.
    """
    ...

def convert_sparse_cross_attention_mask_to_dense(
    cross_attention_token_mask: list[list[list[int]]], num_tiles: list[list[int]], max_num_tiles: int, length: int
) -> np.ndarray:
    """
    Convert the cross attention mask indices to a cross attention mask 4D array.

    This function takes a sparse representation of cross attention masks and converts it to a dense 4D numpy array.
    The sparse representation is a nested list structure that defines attention ranges for each image in each batch item.

    Args:
        cross_attention_token_mask (List[List[List[int]]]): A nested list structure where:
            - The outer list represents the batch dimension.
            - The middle list represents different images within each batch item.
            - The inner list contains pairs of integers [start, end] representing token ranges for each image.
        num_tiles (List[List[int]]): A nested list structure specifying the number of tiles for each image in each batch item.
        max_num_tiles (int): The maximum possible number of tiles.
        length (int): The total sequence length of the input.

    Returns:
        np.ndarray: A 4D numpy array of shape (batch_size, length, max_num_images, max_num_tiles)
            The array contains `1` where attention is allowed and `0` where it is not.

    Note:
        - Special handling is done for cases where the end token is -1, which is interpreted as attending to the end of the sequence.
    """
    ...

def build_string_from_input(prompt: str, bos_token: str, image_token: str) -> str:
    """
    Builds a string from the input prompt by adding `bos_token` if not already present.

    Args:
        prompt (`str`):
            The input prompt string.
        bos_token (`str`):
            The beginning of sentence token to be added.
        image_token (`str`):
            The image token used to identify the start of an image sequence.

    Returns:
        str: The modified prompt string with the `bos_token` added if necessary.

    Examples:
        >>> build_string_from_input("Hello world", "<begin_of_text>", "<|image|>")
        '<begin_of_text>Hello world'

        >>> build_string_from_input("<|image|>Hello world", "<begin_of_text>", "<|image|>")
        '<|image|><begin_of_text>Hello world'

        >>> build_string_from_input("<begin_of_text>Hello world", "<begin_of_text>", "<|image|>")
        '<begin_of_text>Hello world'
    """
    ...

class MllamaProcessor(ProcessorMixin):
    r"""
    Constructs a Mllama processor which wraps [`MllamaImageProcessor`] and
    [`PretrainedTokenizerFast`] into a single processor that inherits both the image processor and
    tokenizer functionalities. See the [`~MllamaProcessor.__call__`] and [`~OwlViTProcessor.decode`] for more
    information.
    The preferred way of passing kwargs is as a dictionary per modality, see usage example below.
        ```python
        from transformers import MllamaProcessor
        from PIL import Image

        processor = MllamaProcessor.from_pretrained("meta-llama/Llama-3.2-11B-Vision")

        processor(
            images=your_pil_image,
            text=["<|image|>If I had to write a haiku for this one"],
            images_kwargs = {"size": {"height": 448, "width": 448}},
            text_kwargs = {"padding": "right"},
            common_kwargs = {"return_tensors": "pt"},
        )
        ```

    Args:
        image_processor ([`MllamaImageProcessor`]):
            The image processor is a required input.
        tokenizer ([`PreTrainedTokenizer`, `PreTrainedTokenizerFast`]):
            The tokenizer is a required input.
        chat_template (`str`, *optional*): A Jinja template which will be used to convert lists of messages
            in a chat into a tokenizable string.

    """

    attributes = ...
    valid_kwargs = ...
    image_processor_class = ...
    tokenizer_class = ...
    def __init__(self, image_processor, tokenizer, chat_template=...) -> None: ...
    def __call__(
        self,
        images: ImageInput | None = ...,
        text: TextInput | PreTokenizedInput | list[TextInput] | list[PreTokenizedInput] | None = ...,
        audio=...,
        videos=...,
        **kwargs: Unpack[MllamaProcessorKwargs],
    ) -> BatchFeature:
        """
        Main method to prepare text(s) and image(s) to be fed as input to the model. This method forwards the `text`
        arguments to PreTrainedTokenizerFast's [`~PreTrainedTokenizerFast.__call__`] if `text` is not `None` to encode
        the text. To prepare the image(s), this method forwards the `images` arguments to
        MllamaImageProcessor's [`~MllamaImageProcessor.__call__`] if `images` is not `None`. Please refer
        to the docstring of the above two methods for more information.

        Args:
            images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`, `List[torch.Tensor]`):
                The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
                tensor. Both channels-first and channels-last formats are supported.
            text (`str`, `List[str]`, `List[List[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
                (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
                `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
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
            TODO: add aspect_ratio_ids and aspect_ratio_mask and cross_attention_mask
        """
        ...

    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to PreTrainedTokenizerFast's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
        ...

    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to PreTrainedTokenizerFast's [`~PreTrainedTokenizer.decode`]. Please refer to
        the docstring of this method for more information.
        """
        ...

    def post_process_image_text_to_text(
        self, generated_outputs, skip_special_tokens=..., clean_up_tokenization_spaces=..., **kwargs
    ):
        """
        Post-process the output of the model to decode the text.

        Args:
            generated_outputs (`torch.Tensor` or `np.ndarray`):
                The output of the model `generate` function. The output is expected to be a tensor of shape `(batch_size, sequence_length)`
                or `(sequence_length,)`.
            skip_special_tokens (`bool`, *optional*, defaults to `True`):
                Whether or not to remove special tokens in the output. Argument passed to the tokenizer's `batch_decode` method.
            Clean_up_tokenization_spaces (`bool`, *optional*, defaults to `False`):
                Whether or not to clean up the tokenization spaces. Argument passed to the tokenizer's `batch_decode` method.
            **kwargs:
                Additional arguments to be passed to the tokenizer's `batch_decode method`.

        Returns:
            `List[str]`: The decoded text.
        """
        ...

    @property
    def model_input_names(self):  # -> list[Any]:
        ...

__all__ = ["MllamaProcessor"]
