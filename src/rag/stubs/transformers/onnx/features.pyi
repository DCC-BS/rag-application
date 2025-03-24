"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable
from typing import TYPE_CHECKING

from transformers import PreTrainedModel, TFPreTrainedModel

from .. import PretrainedConfig, is_tf_available, is_torch_available
from .config import OnnxConfig

if TYPE_CHECKING: ...
logger = ...
if is_torch_available(): ...
if is_tf_available(): ...
if not is_torch_available() and not is_tf_available(): ...

def supported_features_mapping(
    *supported_features: str, onnx_config_cls: str = ...
) -> dict[str, Callable[[PretrainedConfig], OnnxConfig]]:
    """
    Generate the mapping between supported the features and their corresponding OnnxConfig for a given model.

    Args:
        *supported_features: The names of the supported features.
        onnx_config_cls: The OnnxConfig full name corresponding to the model.

    Returns:
        The dictionary mapping a feature to an OnnxConfig constructor.
    """
    ...

class FeaturesManager:
    _TASKS_TO_AUTOMODELS = ...
    _TASKS_TO_TF_AUTOMODELS = ...
    if is_torch_available():
        _TASKS_TO_AUTOMODELS = ...
    if is_tf_available():
        _TASKS_TO_TF_AUTOMODELS = ...
    _SUPPORTED_MODEL_TYPE = ...
    AVAILABLE_FEATURES = ...
    @staticmethod
    def get_supported_features_for_model_type(
        model_type: str, model_name: str | None = ...
    ) -> dict[str, Callable[[PretrainedConfig], OnnxConfig]]:
        """
        Tries to retrieve the feature -> OnnxConfig constructor map from the model type.

        Args:
            model_type (`str`):
                The model type to retrieve the supported features for.
            model_name (`str`, *optional*):
                The name attribute of the model object, only used for the exception message.

        Returns:
            The dictionary mapping each feature to a corresponding OnnxConfig constructor.
        """
        ...

    @staticmethod
    def feature_to_task(feature: str) -> str: ...
    @staticmethod
    def get_model_class_for_feature(feature: str, framework: str = ...) -> type:
        """
        Attempts to retrieve an AutoModel class from a feature name.

        Args:
            feature (`str`):
                The feature required.
            framework (`str`, *optional*, defaults to `"pt"`):
                The framework to use for the export.

        Returns:
            The AutoModel class corresponding to the feature.
        """
        ...

    @staticmethod
    def determine_framework(model: str, framework: str = ...) -> str:
        """
        Determines the framework to use for the export.

        The priority is in the following order:
            1. User input via `framework`.
            2. If local checkpoint is provided, use the same framework as the checkpoint.
            3. Available framework in environment, with priority given to PyTorch

        Args:
            model (`str`):
                The name of the model to export.
            framework (`str`, *optional*, defaults to `None`):
                The framework to use for the export. See above for priority if none provided.

        Returns:
            The framework to use for the export.

        """
        ...

    @staticmethod
    def get_model_from_feature(
        feature: str, model: str, framework: str = ..., cache_dir: str = ...
    ) -> PreTrainedModel | TFPreTrainedModel:
        """
        Attempts to retrieve a model from a model's name and the feature to be enabled.

        Args:
            feature (`str`):
                The feature required.
            model (`str`):
                The name of the model to export.
            framework (`str`, *optional*, defaults to `None`):
                The framework to use for the export. See `FeaturesManager.determine_framework` for the priority should
                none be provided.

        Returns:
            The instance of the model.

        """
        ...

    @staticmethod
    def check_supported_model_or_raise(
        model: PreTrainedModel | TFPreTrainedModel, feature: str = ...
    ) -> tuple[str, Callable]:
        """
        Check whether or not the model has the requested features.

        Args:
            model: The model to export.
            feature: The name of the feature to check if it is available.

        Returns:
            (str) The type of the model (OnnxConfig) The OnnxConfig instance holding the model export properties.

        """
        ...

    def get_config(model_type: str, feature: str) -> OnnxConfig:
        """
        Gets the OnnxConfig for a model_type and feature combination.

        Args:
            model_type (`str`):
                The model type to retrieve the config for.
            feature (`str`):
                The feature to retrieve the config for.

        Returns:
            `OnnxConfig`: config for the combination
        """
        ...
