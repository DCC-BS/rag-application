"""
This type stub file was generated by pyright.
"""

from ...tokenization_utils_fast import PreTrainedTokenizerFast

"""Tokenization classes for OpenAI GPT."""
logger = ...
VOCAB_FILES_NAMES = ...

class GPT2TokenizerFast(PreTrainedTokenizerFast):
    """
    Construct a "fast" GPT-2 tokenizer (backed by HuggingFace's *tokenizers* library). Based on byte-level
    Byte-Pair-Encoding.

    This tokenizer has been trained to treat spaces like parts of the tokens (a bit like sentencepiece) so a word will
    be encoded differently whether it is at the beginning of the sentence (without space) or not:

    ```python
    >>> from transformers import GPT2TokenizerFast

    >>> tokenizer = GPT2TokenizerFast.from_pretrained("openai-community/gpt2")
    >>> tokenizer("Hello world")["input_ids"]
    [15496, 995]

    >>> tokenizer(" Hello world")["input_ids"]
    [18435, 995]
    ```

    You can get around that behavior by passing `add_prefix_space=True` when instantiating this tokenizer, but since
    the model was not pretrained this way, it might yield a decrease in performance.

    <Tip>

    When used with `is_split_into_words=True`, this tokenizer needs to be instantiated with `add_prefix_space=True`.

    </Tip>

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`, *optional*):
            Path to the vocabulary file.
        merges_file (`str`, *optional*):
            Path to the merges file.
        tokenizer_file (`str`, *optional*):
            Path to [tokenizers](https://github.com/huggingface/tokenizers) file (generally has a .json extension) that
            contains everything needed to load the tokenizer.
        unk_token (`str`, *optional*, defaults to `"<|endoftext|>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        bos_token (`str`, *optional*, defaults to `"<|endoftext|>"`):
            The beginning of sequence token.
        eos_token (`str`, *optional*, defaults to `"<|endoftext|>"`):
            The end of sequence token.
        add_prefix_space (`bool`, *optional*, defaults to `False`):
            Whether or not to add an initial space to the input. This allows to treat the leading word just as any
            other word. (GPT2 tokenizer detect beginning of words by the preceding space).
    """

    vocab_files_names = ...
    model_input_names = ...
    slow_tokenizer_class = ...
    def __init__(
        self,
        vocab_file=...,
        merges_file=...,
        tokenizer_file=...,
        unk_token=...,
        bos_token=...,
        eos_token=...,
        add_prefix_space=...,
        **kwargs,
    ) -> None: ...
    def save_vocabulary(self, save_directory: str, filename_prefix: str | None = ...) -> tuple[str]: ...

__all__ = ["GPT2TokenizerFast"]
