"""
This type stub file was generated by pyright.
"""

from ...tokenization_utils import PreTrainedTokenizer

"""Tokenization class for Perceiver."""
logger = ...

class PerceiverTokenizer(PreTrainedTokenizer):
    """
    Construct a Perceiver tokenizer. The Perceiver simply uses raw bytes utf-8 encoding.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    this superclass for more information regarding those methods.

    Args:
        pad_token (`str`, *optional*, defaults to `"[PAD]"`):
            The token used for padding, for example when batching sequences of different lengths.
        bos_token (`str`, *optional*, defaults to `"[BOS]"`):
            The BOS token (reserved in the vocab, but not actually used).
        eos_token (`str`, *optional*, defaults to `"[EOS]"`):
            The end of sequence token (reserved in the vocab, but not actually used).

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the end of sequence.
            The token used is the `sep_token`.

            </Tip>

        mask_token (`str`, *optional*, defaults to `"[MASK]"`):
            The MASK token, useful for masked language modeling.
        cls_token (`str`, *optional*, defaults to `"[CLS]"`):
            The CLS token (reserved in the vocab, but not actually used).
        sep_token (`str`, *optional*, defaults to `"[SEP]"`):
            The separator token, which is used when building a sequence from two sequences.

    """

    model_input_names = ...
    def __init__(
        self,
        pad_token=...,
        bos_token=...,
        eos_token=...,
        mask_token=...,
        cls_token=...,
        sep_token=...,
        model_max_length=...,
        **kwargs,
    ) -> None: ...
    def get_vocab(self) -> dict[str, int]: ...
    @property
    def vocab_size(self):  # -> int:
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

    def build_inputs_with_special_tokens(
        self, token_ids_0: list[int], token_ids_1: list[int] | None = ...
    ) -> list[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks. A sequence has the
        following format:

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

    def convert_tokens_to_string(self, tokens):  # -> str:
        """Converts a sequence of tokens (string) in a single string."""
        ...

    def save_vocabulary(self, save_directory: str, filename_prefix: str | None = ...) -> tuple[str]: ...

__all__ = ["PerceiverTokenizer"]
