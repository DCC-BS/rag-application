"""
This type stub file was generated by pyright.
"""

import numpy as np

from ...feature_extraction_sequence_utils import SequenceFeatureExtractor
from ...feature_extraction_utils import BatchFeature
from ...utils import PaddingStrategy, TensorType, is_torch_available

"""
Feature extractor class for SeamlessM4T
"""
if is_torch_available(): ...
logger = ...

class SeamlessM4TFeatureExtractor(SequenceFeatureExtractor):
    r"""
    Constructs a SeamlessM4T feature extractor.

    This feature extractor inherits from [`SequenceFeatureExtractor`] which contains most of the main methods. Users
    should refer to this superclass for more information regarding those methods.

    This class extracts mel-filter bank features from raw speech.

    Args:
        feature_size (`int`, *optional*, defaults to 80):
            The feature dimension of the extracted features.
        sampling_rate (`int`, *optional*, defaults to 16000):
            The sampling rate at which the audio files should be digitalized expressed in hertz (Hz).
        num_mel_bins (`int`, *optional*, defaults to 80):
            Number of Mel-frequency bins.
        padding_value (`float`, *optional*, defaults to 0.0):
            The value that is used to fill the padding vectors.
        stride (`int`, *optional*, defaults to 2):
            Stride used to reshape audios from shape (batch_size,num_frames,num_mel_bins) to
            (batch_size,num_frames//stride,num_mel_bins*stride).
    """

    model_input_names = ...
    def __init__(
        self, feature_size=..., sampling_rate=..., num_mel_bins=..., padding_value=..., stride=..., **kwargs
    ) -> None: ...
    @staticmethod
    def zero_mean_unit_var_norm(
        input_values: list[np.ndarray], attention_mask: list[np.ndarray], padding_value: float = ...
    ) -> list[np.ndarray]:
        """
        Every array in the list is normalized to have zero mean and unit variance
        """
        ...

    def __call__(
        self,
        raw_speech: np.ndarray | list[float] | list[np.ndarray] | list[list[float]],
        padding: bool | str | PaddingStrategy = ...,
        pad_to_multiple_of: int | None = ...,
        max_length: int | None = ...,
        truncation: bool = ...,
        return_tensors: str | TensorType | None = ...,
        sampling_rate: int | None = ...,
        return_attention_mask: bool | None = ...,
        do_normalize_per_mel_bins: bool | None = ...,
        **kwargs,
    ) -> BatchFeature:
        """
        Main method to featurize and prepare for the model one or several sequence(s).

        Args:
            raw_speech (`np.ndarray`, `torch.Tensor`, `List[float]`, `List[np.ndarray]`, `List[torch.Tensor]`,
            `List[List[float]]`, `List[List[List[float]]]`):
                The sequence or batch of sequences to be padded. Each sequence can be a numpy array,
                a torch tensor, a list of float values, a list of numpy arrays, a list of torch tensors,
                a list of list of float values or a list of a list of list of float values.
                If `raw_speech` is a one-dimensional `np.ndarray`, `torch.Tensor` or a `List[float]`, `raw_speech` is
                considered a single-channel, single-sample sound. In all other cases, the first dimension of
                `raw_speech`, whether from an `np.ndarray`, a `torch.Tensor` or a `List[...]`,
                corresponds to the number of samples in the batch, and the number of channels
                (i.e. mono or stereo character) is derived from the other dimensions
                (1D -> single-channel waveform batches; 2D-> stereo-channel waveform batches).
            padding (`bool`, `str` or [`~utils.PaddingStrategy`], *optional*, defaults to `True`):
                Select a strategy to pad the returned sequences (according to the model's padding side and padding
                index) among:

                - `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
                  sequence if provided).
                - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum
                  acceptable input length for the model if that argument is not provided.
                - `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different
                  lengths).
            pad_to_multiple_of (`int`, *optional*, defaults to 2):
                If set will pad the sequence to a multiple of the provided value.

                This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability
                `>= 7.5` (Volta), or on TPUs which benefit from having sequence lengths be a multiple of 128.
            max_length (`int`, *optional*):
                Maximum length of the returned list and optionally padding length (see above).
            truncation (`bool`):
                Activates truncation to cut input sequences longer than *max_length* to *max_length*.
            return_attention_mask (`bool`, *optional*):
                Whether to return the attention mask. If left to the default, will return the attention mask according
                to the specific feature_extractor's default.

                [What are attention masks?](../glossary#attention-mask)

                <Tip>

                For SeamlessM4T models, `attention_mask` should always be passed for batched inference, to avoid subtle
                bugs.

                </Tip>

            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors instead of list of python integers. Acceptable values are:

                - `'tf'`: Return TensorFlow `tf.constant` objects.
                - `'pt'`: Return PyTorch `torch.Tensor` objects.
                - `'np'`: Return Numpy `np.ndarray` objects.
            sampling_rate (`int`, *optional*):
                The sampling rate at which the `raw_speech` input was sampled. It is strongly recommended to pass
                `sampling_rate` at the forward call to prevent silent errors.
            do_normalize_per_mel_bins (`bool`, *optional*, defaults to `True`):
                Whether or not to zero-mean unit-variance normalize the input per mel-channel.
            kwargs (*optional*):
                Remaining dictionary of keyword arguments that will be passed to the tokenizer or the feature
                extractor.
        """
        ...

__all__ = ["SeamlessM4TFeatureExtractor"]
