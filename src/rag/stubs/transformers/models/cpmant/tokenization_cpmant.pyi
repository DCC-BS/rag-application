"""
This type stub file was generated by pyright.
"""

from transformers.utils import is_jieba_available

from ...tokenization_utils import PreTrainedTokenizer

"""Tokenization classes for CPMAnt."""
if is_jieba_available(): ...
logger = ...
VOCAB_FILES_NAMES = ...

def load_vocab(vocab_file):  # -> OrderedDict[Any, Any]:
    """Loads a vocabulary file into a dictionary."""
    ...

class WordpieceTokenizer:
    def __init__(self, vocab, unk_token=..., max_input_chars_per_word=...) -> None: ...
    def tokenize(self, token):  # -> list[str] | list[Any]:
        ...

class CpmAntTokenizer(PreTrainedTokenizer):
    """
    Construct a CPMAnt tokenizer. Based on byte-level Byte-Pair-Encoding.

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        bod_token (`str`, *optional*, defaults to `"<d>"`):
            The beginning of document token.
        eod_token (`str`, *optional*, defaults to `"</d>"`):
            The end of document token.
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sequence token.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sequence token.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token.
        line_token (`str`, *optional*, defaults to `"</n>"`):
            The line token.
        space_token (`str`, *optional*, defaults to `"</_>"`):
            The space token.
    """

    vocab_files_names = ...
    model_input_names = ...
    add_prefix_space = ...
    def __init__(
        self,
        vocab_file,
        bod_token=...,
        eod_token=...,
        bos_token=...,
        eos_token=...,
        pad_token=...,
        unk_token=...,
        line_token=...,
        space_token=...,
        padding_side=...,
        **kwargs,
    ) -> None: ...
    @property
    def bod_token_id(self): ...
    @property
    def eod_token_id(self): ...
    @property
    def newline_id(self): ...
    @property
    def vocab_size(self) -> int: ...
    def get_vocab(self):  # -> dict[str, int]:
        ...
    def check(self, token):  # -> bool:
        ...
    def convert_tokens_to_string(self, tokens: list[str]) -> str: ...
    def save_vocabulary(self, save_directory: str, filename_prefix: str | None = ...) -> tuple[str]: ...
    def build_inputs_with_special_tokens(self, token_ids_0: list[int], token_ids_1: list[int] = ...) -> list[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. A CPMAnt sequence has the following format:

        - single sequence: `[BOS] Sequence`.

        Args:
            token_ids_0 (`List[int]`): The first tokenized sequence that special tokens will be added.
            token_ids_1 (`List[int]`): The optional second tokenized sequence that special tokens will be added.

        Returns:
            `List[int]`: The model input with special tokens.
        """
        ...

    def get_special_tokens_mask(
        self, token_ids_0: list[int], token_ids_1: list[int] | None = ..., already_has_special_tokens: bool = ...
    ) -> list[int]:
        """
        Retrieve sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` method.

        Args:
            token_ids_0 (`List[int]`): List of IDs.
            token_ids_1 (`List[int]`, *optional*): Optional second list of IDs for sequence pairs.
            already_has_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not the token list is already formatted with special tokens for the model.

        Returns:
            `List[int]`: A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
        """
        ...

__all__ = ["CpmAntTokenizer"]
