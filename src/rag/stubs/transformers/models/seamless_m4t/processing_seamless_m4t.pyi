"""
This type stub file was generated by pyright.
"""

from ...processing_utils import ProcessorMixin

"""
Audio/Text processor class for SeamlessM4T
"""

class SeamlessM4TProcessor(ProcessorMixin):
    r"""
    Constructs a SeamlessM4T processor which wraps a SeamlessM4T feature extractor and a SeamlessM4T tokenizer into a
    single processor.

    [`SeamlessM4TProcessor`] offers all the functionalities of [`SeamlessM4TFeatureExtractor`] and
    [`SeamlessM4TTokenizerFast`]. See the [`~SeamlessM4TProcessor.__call__`] and [`~SeamlessM4TProcessor.decode`] for
    more information.

    Args:
        feature_extractor ([`SeamlessM4TFeatureExtractor`]):
            The audio processor is a required input.
        tokenizer ([`SeamlessM4TTokenizerFast`]):
            The tokenizer is a required input.
    """

    feature_extractor_class = ...
    tokenizer_class = ...
    def __init__(self, feature_extractor, tokenizer) -> None: ...
    def __call__(self, text=..., audios=..., src_lang=..., tgt_lang=..., **kwargs):
        """
        Main method to prepare for the model one or several sequences(s) and audio(s). This method forwards the `text`
        and `kwargs` arguments to SeamlessM4TTokenizerFast's [`~SeamlessM4TTokenizerFast.__call__`] if `text` is not
        `None` to encode the text. To prepare the audio(s), this method forwards the `audios` and `kwrags` arguments to
        SeamlessM4TFeatureExtractor's [`~SeamlessM4TFeatureExtractor.__call__`] if `audios` is not `None`. Please refer
        to the doctsring of the above two methods for more information.

        Args:
            text (`str`, `List[str]`, `List[List[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
                (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
                `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
            audios (`np.ndarray`, `torch.Tensor`, `List[np.ndarray]`, `List[torch.Tensor]`):
                The audio or batch of audios to be prepared. Each audio can be NumPy array or PyTorch tensor. In case
                of a NumPy array/PyTorch tensor, each audio should be of shape (C, T), where C is a number of channels,
                and T the sample length of the audio.
            src_lang (`str`, *optional*):
                The language code of the input texts/audios. If not specified, the last `src_lang` specified will be
                used.
            tgt_lang (`str`, *optional*):
                The code of the target language. If not specified, the last `tgt_lang` specified will be used.
            kwargs (*optional*):
                Remaining dictionary of keyword arguments that will be passed to the feature extractor and/or the
                tokenizer.
        Returns:
            [`BatchEncoding`]: A [`BatchEncoding`] with the following fields:

            - **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
            - **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
              `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
              `None`).
            - **input_features** -- Audio input features to be fed to a model. Returned when `audios` is not `None`.
        """
        ...

    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to SeamlessM4TTokenizerFast's [`~PreTrainedTokenizer.batch_decode`].
        Please refer to the docstring of this method for more information.
        """
        ...

    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to SeamlessM4TTokenizerFast's [`~PreTrainedTokenizer.decode`]. Please
        refer to the docstring of this method for more information.
        """
        ...

    @property
    def model_input_names(self):  # -> list[Any]:
        ...

__all__ = ["SeamlessM4TProcessor"]
