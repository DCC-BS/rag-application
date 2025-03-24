"""
This type stub file was generated by pyright.
"""

from ...feature_extraction_utils import BatchFeature
from ...image_utils import ImageInput, VideoInput
from ...processing_utils import ProcessingKwargs, ProcessorMixin, Unpack
from ...tokenization_utils_base import PreTokenizedInput, TextInput

"""
Processor class for LLaVa-NeXT-Video.
"""
logger = ...

class LlavaNextVideoProcessorKwargs(ProcessingKwargs, total=False):
    _defaults = ...

class LlavaNextVideoProcessor(ProcessorMixin):
    r"""
    Constructs a LLaVa-NeXT-Video processor which wraps a LLaVa-NeXT image processor, LLaVa-NeXT-Video video processor and
    a LLaMa tokenizer into a single processor.

    [`LlavaNextVideoProcessor`] offers all the functionalities of [`LlavaNextImageProcessor`], [`LlavaNextVideoImageProcessor`] and
    [`LlamaTokenizerFast`]. See the [`~LlavaNextVideoProcessor.__call__`] and [`~LlavaNextVideoProcessor.decode`] for more information.

    Args:
        video_processor ([`LlavaNextVideoImageProcessor`], *optional*):
            The video processor is a required input.
        image_processor ([`LlavaNextImageProcessor`], *optional*):
            The image processor is a required input.
        tokenizer ([`LlamaTokenizerFast`], *optional*):
            The tokenizer is a required input.
        chat_template (`str`, *optional*):
            Jinja chat template that will be used in tokenizer's `apply_chat_template`
        patch_size (`int`, *optional*):
            Patch size from the vision tower.
        vision_feature_select_strategy (`str`, *optional*):
            The feature selection strategy used to select the vision feature from the vision backbone.
            Shoudl be same as in model's config
        video_token (`str`, *optional*, defaults to `"<video>"`):
            Special token used to denote video location.
        image_token (`str`, *optional*, defaults to `"<image>"`):
            Special token used to denote image location.
        num_additional_image_tokens (`int`, *optional*, defaults to 0):
            Number of additional tokens added to the image embeddings, such as CLS (+1). If the backbone has no CLS or other
            extra tokens appended, no need to set this arg.
    """

    attributes = ...
    valid_kwargs = ...
    image_processor_class = ...
    video_processor_class = ...
    tokenizer_class = ...
    def __init__(
        self,
        video_processor=...,
        image_processor=...,
        tokenizer=...,
        chat_template=...,
        patch_size=...,
        vision_feature_select_strategy=...,
        video_token=...,
        image_token=...,
        num_additional_image_tokens=...,
        **kwargs,
    ) -> None: ...
    def __call__(
        self,
        images: ImageInput = ...,
        text: TextInput | PreTokenizedInput | list[TextInput] | list[PreTokenizedInput] = ...,
        audio=...,
        videos: VideoInput = ...,
        **kwargs: Unpack[LlavaNextVideoProcessorKwargs],
    ) -> BatchFeature:
        """
        Main method to prepare for the model one or several sequences(s) and image(s). This method forwards the `text`
        and `kwargs` arguments to LlamaTokenizerFast's [`~LlamaTokenizerFast.__call__`] if `text` is not `None` to encode
        the text. To prepare the image(s), this method forwards the `images` and `kwrags` arguments to
        LlavaNextImageProcessor's [`~LlavaNextImageProcessor.__call__`] if `images` is not `None`. To prepare the video(s),
        this method forwards the `videos` and `kwrags` arguments to LlavaNextVideoImageProcessor's
        [`~LlavaNextVideoImageProcessor.__call__`] if `videos` is not `None`. Please refer to the doctsring
        of the above two methods for more information.

        Args:
            text (`str`, `List[str]`, `List[List[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
                (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
                `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
            images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`, `List[torch.Tensor]`):
                The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
                tensor. Both channels-first and channels-last formats are supported.
            videos (`np.ndarray`, `torch.Tensor`, `List[np.ndarray]`, `List[torch.Tensor]`):
                The image or batch of videos to be prepared. Each video can be a 4D NumPy array or PyTorch
                tensor, or a nested list of 3D frames. Both channels-first and channels-last formats are supported.
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
        """
        ...

    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to LlamaTokenizerFast's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
        ...

    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to LlamaTokenizerFast's [`~PreTrainedTokenizer.decode`]. Please refer to
        the docstring of this method for more information.
        """
        ...

    @property
    def model_input_names(self):  # -> list[Any]:
        ...

__all__ = ["LlavaNextVideoProcessor"]
