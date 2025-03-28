"""
This type stub file was generated by pyright.
"""

from ....tokenization_utils import PreTrainedTokenizer

"""Tokenization class for Speech2Text2."""
logger = ...
VOCAB_FILES_NAMES = ...
BPE_TOKEN_MERGES = ...
BPE_TOKEN_VOCAB = ...

def get_pairs(word):  # -> set[Any]:
    """
    Return set of symbol pairs in a word. word is represented as tuple of symbols (symbols being variable-length
    strings)
    """
    ...

class Speech2Text2Tokenizer(PreTrainedTokenizer):
    """
    Constructs a Speech2Text2Tokenizer.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains some of the main methods. Users should refer to
    the superclass for more information regarding such methods.

    Args:
        vocab_file (`str`):
            File containing the vocabulary.
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sentence token.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sentence token.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.

        **kwargs
            Additional keyword arguments passed along to [`PreTrainedTokenizer`]
    """

    vocab_files_names = ...
    model_input_names = ...
    def __init__(
        self,
        vocab_file,
        bos_token=...,
        pad_token=...,
        eos_token=...,
        unk_token=...,
        do_lower_case=...,
        merges_file=...,
        **kwargs,
    ) -> None: ...
    @property
    def vocab_size(self) -> int: ...
    def get_vocab(self) -> dict: ...
    def bpe(self, token):  # -> LiteralString:
        ...
    def convert_tokens_to_string(self, tokens: list[str]) -> str:
        """
        Converts a list of output tokens into a single string.
        """
        ...

    def save_vocabulary(self, save_directory: str, filename_prefix: str | None = ...) -> tuple[str]: ...
