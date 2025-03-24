"""
This type stub file was generated by pyright.
"""

from tokenizers import Tokenizer

from ..convert_slow_tokenizer import GemmaConverter, GPT2Converter, LlamaConverter, Qwen2Converter, T5Converter

"""
Integration with GGML / The file is copied and adapted from https://github.com/99991/pygguf
with extra methods beings exposed
"""
logger = ...
GGUF_CONFIG_MAPPING = ...
GGUF_TOKENIZER_MAPPING = ...

class GGUFTokenizerSkeleton:
    def __init__(self, dict_) -> None: ...

class GGUFLlamaConverter(LlamaConverter):
    def __init__(self, tokenizer_dict) -> None: ...
    def vocab(self, proto):  # -> list[tuple[Any, Any]]:
        ...
    def merges(self, proto): ...
    def tokenizer(self, proto):  # -> Tokenizer:
        ...
    def decoder(self, replacement, add_prefix_space):  # -> Sequence:
        ...
    def converted(self):  # -> Tokenizer:
        ...

class GGUFQwen2Converter(Qwen2Converter):
    def __init__(self, tokenizer_dict) -> None: ...
    def converted(self) -> Tokenizer: ...

class GGUFPhi3Converter(LlamaConverter):
    def __init__(self, tokenizer_dict) -> None: ...
    def vocab(self, proto):  # -> list[tuple[Any, Any]]:
        ...
    def merges(self, proto): ...
    def tokenizer(self, proto):  # -> Tokenizer:
        ...
    def decoder(self, replacement, add_prefix_space):  # -> Sequence:
        ...
    def converted(self) -> Tokenizer: ...

class GGUFGPTConverter(GPT2Converter):
    def __init__(self, tokenizer_dict) -> None: ...
    def converted(self) -> Tokenizer: ...

class GGUFT5Converter(T5Converter):
    def __init__(self, tokenizer_dict) -> None: ...
    def vocab(self, proto):  # -> list[tuple[Any, Any]]:
        ...
    def normalizer(self, proto):  # -> Sequence | None:
        ...
    def post_processor(self):  # -> TemplateProcessing:
        ...
    def converted(self) -> Tokenizer: ...

class GGUFGemmaConverter(GemmaConverter):
    def __init__(self, tokenizer_dict) -> None: ...
    def vocab(self, proto):  # -> list[Any]:
        ...
    def normalizer(self, proto):  # -> Replace:
        ...
    def decoder(self, replacement, add_prefix_space):  # -> Sequence:
        ...
    def converted(self) -> Tokenizer: ...

GGUF_TO_FAST_CONVERTERS = ...

def convert_gguf_tokenizer(architecture, tokenizer_dict) -> Tokenizer:
    """
    Utilities to convert a slow tokenizer instance in a fast tokenizer instance.

    Args:
        architecture (`str`): The model architecture derived from gguf file.
        transformer_tokenizer ([`~tokenization_utils_base.PreTrainedTokenizer`]):
            Instance of a slow tokenizer to convert in the backend tokenizer for
            [`~tokenization_utils_base.PreTrainedTokenizerFast`].

    Return:
        A instance of [`~tokenizers.Tokenizer`] to be used as the backend tokenizer of a
        [`~tokenization_utils_base.PreTrainedTokenizerFast`]
    """
    ...
