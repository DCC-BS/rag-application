"""
This type stub file was generated by pyright.
"""

from ...tokenization_utils import PreTrainedTokenizer

"""Tokenization classes for CANINE."""
logger = ...
UNICODE_VOCAB_SIZE = ...
PAD = ...
CLS = ...
SEP = ...
BOS = ...
MASK = ...
RESERVED = ...
SPECIAL_CODEPOINTS: dict[int, str] = ...
SPECIAL_CODEPOINTS_BY_NAME: dict[str, int] = ...

class CanineTokenizer(PreTrainedTokenizer):
    r"""
    Construct a CANINE tokenizer (i.e. a character splitter). It turns text into a sequence of characters, and then
    converts each character into its Unicode code point.

    [`CanineTokenizer`] inherits from [`PreTrainedTokenizer`].

    Refer to superclass [`PreTrainedTokenizer`] for usage examples and documentation concerning parameters.

    Args:
        model_max_length (`int`, *optional*, defaults to 2048):
                The maximum sentence length the model accepts.
    """
    def __init__(
        self,
        bos_token=...,
        eos_token=...,
        sep_token=...,
        cls_token=...,
        pad_token=...,
        mask_token=...,
        add_prefix_space=...,
        model_max_length=...,
        **kwargs,
    ) -> None: ...
    @property
    def vocab_size(self) -> int: ...
    def get_vocab(self):  # -> dict[str, int]:
        ...
    def convert_tokens_to_string(self, tokens):  # -> str:
        ...
    def build_inputs_with_special_tokens(
        self, token_ids_0: list[int], token_ids_1: list[int] | None = ...
    ) -> list[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. A CANINE sequence has the following format:

        - single sequence: `[CLS] X [SEP]`
        - pair of sequences: `[CLS] A [SEP] B [SEP]`

        Args:
            token_ids_0 (`List[int]`):
                List of IDs to which the special tokens will be added.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of [input IDs](../glossary#input-ids) with the appropriate special tokens.
        """
        ...

    def get_special_tokens_mask(
        self, token_ids_0: list[int], token_ids_1: list[int] | None = ..., already_has_special_tokens: bool = ...
    ) -> list[int]:
        """
        Retrieve sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` method.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.
            already_has_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not the token list is already formatted with special tokens for the model.

        Returns:
            `List[int]`: A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
        """
        ...

    def create_token_type_ids_from_sequences(
        self, token_ids_0: list[int], token_ids_1: list[int] | None = ...
    ) -> list[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. A CANINE
        sequence pair mask has the following format:

        ```
        0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1
        | first sequence    | second sequence |
        ```

        If `token_ids_1` is `None`, this method only returns the first portion of the mask (0s).

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of [token type IDs](../glossary#token-type-ids) according to the given sequence(s).
        """
        ...

    def save_vocabulary(self, save_directory: str, filename_prefix: str | None = ...):  # -> tuple[()]:
        ...

__all__ = ["CanineTokenizer"]
