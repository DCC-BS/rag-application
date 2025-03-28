"""
This type stub file was generated by pyright.
"""

from functools import lru_cache

WEIGHTS_NAME = ...
WEIGHTS_INDEX_NAME = ...
TF2_WEIGHTS_NAME = ...
TF2_WEIGHTS_INDEX_NAME = ...
TF_WEIGHTS_NAME = ...
FLAX_WEIGHTS_NAME = ...
FLAX_WEIGHTS_INDEX_NAME = ...
SAFE_WEIGHTS_NAME = ...
SAFE_WEIGHTS_INDEX_NAME = ...
CONFIG_NAME = ...
FEATURE_EXTRACTOR_NAME = ...
IMAGE_PROCESSOR_NAME = ...
PROCESSOR_NAME = ...
CHAT_TEMPLATE_NAME = ...
GENERATION_CONFIG_NAME = ...
MODEL_CARD_NAME = ...
SENTENCEPIECE_UNDERLINE = ...
SPIECE_UNDERLINE = ...
MULTIPLE_CHOICE_DUMMY_INPUTS = ...
DUMMY_INPUTS = ...
DUMMY_MASK = ...

def check_min_version(min_version):  # -> None:
    ...
@lru_cache
def get_available_devices() -> frozenset[str]:
    """
    Returns a frozenset of devices available for the current PyTorch installation.
    """
    ...
