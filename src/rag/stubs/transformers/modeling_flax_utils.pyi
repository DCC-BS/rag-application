"""
This type stub file was generated by pyright.
"""

import os
from typing import Any

import flax.linen as nn
import jax
import jax.numpy as jnp
from flax.core.frozen_dict import FrozenDict

from .configuration_utils import PretrainedConfig
from .generation import FlaxGenerationMixin
from .utils import PushToHubMixin
from .utils.import_utils import is_safetensors_available

if is_safetensors_available(): ...
logger = ...

def quick_gelu(x): ...

ACT2FN = ...

def dtype_byte_size(dtype):  # -> float | int:
    """
    Returns the size (in bytes) occupied by one parameter of type `dtype`. Example:
    ```py
    >>> dtype_byte_size(np.float32)
    4
    ```
    """
    ...

def flax_shard_checkpoint(
    params, max_shard_size=...
):  # -> tuple[dict[str, Any], None] | tuple[dict[Any, Any], dict[str, dict[str, Any | int]]]:
    """
    Splits a model state dictionary in sub-checkpoints so that the final size of each sub-checkpoint does not exceed a
    given size. The sub-checkpoints are determined by iterating through the `state_dict` in the order of its keys, so
    there is no optimization made to make each sub-checkpoint as close as possible to the maximum size passed. For
    example, if the limit is 10GB and we have weights of sizes [6GB, 6GB, 2GB, 6GB, 2GB, 2GB] they will get sharded as
    [6GB], [6+2GB], [6+2+2GB] and not [6+2+2GB], [6+2GB], [6GB].

    <Tip warning={true}>

    If one of the model's weight is bigger that `max_shard_size`, it will end up in its own sub-checkpoint which will
    have a size greater than `max_shard_size`.

    </Tip>

    Args:
        params (`Union[Dict, FrozenDict]`): A `PyTree` of model parameters.
        max_shard_size (`int` or `str`, *optional*, defaults to `"10GB"`):
            The maximum size of each sub-checkpoint. If expressed as a string, needs to be digits followed by a unit
            (like `"5MB"`).
    """
    ...

class FlaxPreTrainedModel(PushToHubMixin, FlaxGenerationMixin):
    r"""
    Base class for all models.

    [`FlaxPreTrainedModel`] takes care of storing the configuration of the models and handles methods for loading,
    downloading and saving models.

    Class attributes (overridden by derived classes):

        - **config_class** ([`PretrainedConfig`]) -- A subclass of [`PretrainedConfig`] to use as configuration class
          for this model architecture.
        - **base_model_prefix** (`str`) -- A string indicating the attribute associated to the base model in derived
          classes of the same architecture adding modules on top of the base model.
        - **main_input_name** (`str`) -- The name of the principal input to the model (often `input_ids` for NLP
          models, `pixel_values` for vision models and `input_values` for speech models).
    """

    config_class = ...
    base_model_prefix = ...
    main_input_name = ...
    _auto_class = ...
    _missing_keys = ...
    def __init__(
        self,
        config: PretrainedConfig,
        module: nn.Module,
        input_shape: tuple = ...,
        seed: int = ...,
        dtype: jnp.dtype = ...,
        _do_init: bool = ...,
    ) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: tuple, params: FrozenDict = ...) -> dict: ...
    def enable_gradient_checkpointing(self): ...
    @property
    def framework(self) -> str:
        """
        :str: Identifies that this is a Flax model.
        """
        ...

    @property
    def config(self) -> PretrainedConfig: ...
    @property
    def module(self) -> nn.Module: ...
    @property
    def params(self) -> dict | FrozenDict: ...
    @property
    def required_params(self) -> set: ...
    @property
    def params_shape_tree(self) -> dict: ...
    @params.setter
    def params(self, params: dict | FrozenDict):  # -> None:
        ...
    def to_bf16(self, params: dict | FrozenDict, mask: Any = ...):  # -> Any:
        r"""
        Cast the floating-point `params` to `jax.numpy.bfloat16`. This returns a new `params` tree and does not cast
        the `params` in place.

        This method can be used on TPU to explicitly convert the model parameters to bfloat16 precision to do full
        half-precision training or to save weights in bfloat16 for inference in order to save memory and improve speed.

        Arguments:
            params (`Union[Dict, FrozenDict]`):
                A `PyTree` of model parameters.
            mask (`Union[Dict, FrozenDict]`):
                A `PyTree` with same structure as the `params` tree. The leaves should be booleans, `True` for params
                you want to cast, and should be `False` for those you want to skip.

        Examples:

        ```python
        >>> from transformers import FlaxBertModel

        >>> # load model
        >>> model = FlaxBertModel.from_pretrained("google-bert/bert-base-cased")
        >>> # By default, the model parameters will be in fp32 precision, to cast these to bfloat16 precision
        >>> model.params = model.to_bf16(model.params)
        >>> # If you want don't want to cast certain parameters (for example layer norm bias and scale)
        >>> # then pass the mask as follows
        >>> from flax import traverse_util

        >>> model = FlaxBertModel.from_pretrained("google-bert/bert-base-cased")
        >>> flat_params = traverse_util.flatten_dict(model.params)
        >>> mask = {
        ...     path: (path[-2] != ("LayerNorm", "bias") and path[-2:] != ("LayerNorm", "scale"))
        ...     for path in flat_params
        ... }
        >>> mask = traverse_util.unflatten_dict(mask)
        >>> model.params = model.to_bf16(model.params, mask)
        ```"""
        ...

    def to_fp32(self, params: dict | FrozenDict, mask: Any = ...):  # -> Any:
        r"""
        Cast the floating-point `params` to `jax.numpy.float32`. This method can be used to explicitly convert the
        model parameters to fp32 precision. This returns a new `params` tree and does not cast the `params` in place.

        Arguments:
            params (`Union[Dict, FrozenDict]`):
                A `PyTree` of model parameters.
            mask (`Union[Dict, FrozenDict]`):
                A `PyTree` with same structure as the `params` tree. The leaves should be booleans, `True` for params
                you want to cast, and should be `False` for those you want to skip

        Examples:

        ```python
        >>> from transformers import FlaxBertModel

        >>> # Download model and configuration from huggingface.co
        >>> model = FlaxBertModel.from_pretrained("google-bert/bert-base-cased")
        >>> # By default, the model params will be in fp32, to illustrate the use of this method,
        >>> # we'll first cast to fp16 and back to fp32
        >>> model.params = model.to_f16(model.params)
        >>> # now cast back to fp32
        >>> model.params = model.to_fp32(model.params)
        ```"""
        ...

    def to_fp16(self, params: dict | FrozenDict, mask: Any = ...):  # -> Any:
        r"""
        Cast the floating-point `params` to `jax.numpy.float16`. This returns a new `params` tree and does not cast the
        `params` in place.

        This method can be used on GPU to explicitly convert the model parameters to float16 precision to do full
        half-precision training or to save weights in float16 for inference in order to save memory and improve speed.

        Arguments:
            params (`Union[Dict, FrozenDict]`):
                A `PyTree` of model parameters.
            mask (`Union[Dict, FrozenDict]`):
                A `PyTree` with same structure as the `params` tree. The leaves should be booleans, `True` for params
                you want to cast, and should be `False` for those you want to skip

        Examples:

        ```python
        >>> from transformers import FlaxBertModel

        >>> # load model
        >>> model = FlaxBertModel.from_pretrained("google-bert/bert-base-cased")
        >>> # By default, the model params will be in fp32, to cast these to float16
        >>> model.params = model.to_fp16(model.params)
        >>> # If you want don't want to cast certain parameters (for example layer norm bias and scale)
        >>> # then pass the mask as follows
        >>> from flax import traverse_util

        >>> model = FlaxBertModel.from_pretrained("google-bert/bert-base-cased")
        >>> flat_params = traverse_util.flatten_dict(model.params)
        >>> mask = {
        ...     path: (path[-2] != ("LayerNorm", "bias") and path[-2:] != ("LayerNorm", "scale"))
        ...     for path in flat_params
        ... }
        >>> mask = traverse_util.unflatten_dict(mask)
        >>> model.params = model.to_fp16(model.params, mask)
        ```"""
        ...

    @classmethod
    def load_flax_weights(cls, resolved_archive_file): ...
    @classmethod
    def load_flax_sharded_weights(cls, shard_files):
        """
        This is the same as [`flax.serialization.from_bytes`]
        (https:lax.readthedocs.io/en/latest/_modules/flax/serialization.html#from_bytes) but for a sharded checkpoint.

        This load is performed efficiently: each checkpoint shard is loaded one by one in RAM and deleted after being
        loaded in the model.

        Args:
            shard_files (`List[str]`:
                The list of shard files to load.

        Returns:
            `Dict`: A nested dictionary of the model parameters, in the expected format for flax models : `{'model':
            {'params': {'...'}}}`.
        """
        ...

    @classmethod
    def can_generate(cls) -> bool:
        """
        Returns whether this model can generate sequences with `.generate()`. Returns:
            `bool`: Whether this model can generate sequences with `.generate()`.
        """
        ...

    @classmethod
    def from_pretrained(
        cls,
        pretrained_model_name_or_path: str | os.PathLike,
        dtype: jnp.dtype = ...,
        *model_args,
        config: PretrainedConfig | str | os.PathLike | None = ...,
        cache_dir: str | os.PathLike | None = ...,
        ignore_mismatched_sizes: bool = ...,
        force_download: bool = ...,
        local_files_only: bool = ...,
        token: str | bool | None = ...,
        revision: str = ...,
        **kwargs,
    ):  # -> Self | tuple[Self, Any]:
        r"""
        Instantiate a pretrained flax model from a pre-trained model configuration.

        The warning *Weights from XXX not initialized from pretrained model* means that the weights of XXX do not come
        pretrained with the rest of the model. It is up to you to train those weights with a downstream fine-tuning
        task.

        The warning *Weights from XXX not used in YYY* means that the layer XXX is not used by YYY, therefore those
        weights are discarded.

        Parameters:
            pretrained_model_name_or_path (`str` or `os.PathLike`):
                Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *pt index checkpoint file* (e.g, `./tf_model/model.ckpt.index`). In this case,
                      `from_pt` should be set to `True`.
            dtype (`jax.numpy.dtype`, *optional*, defaults to `jax.numpy.float32`):
                The data type of the computation. Can be one of `jax.numpy.float32`, `jax.numpy.float16` (on GPUs) and
                `jax.numpy.bfloat16` (on TPUs).

                This can be used to enable mixed-precision training or half-precision inference on GPUs or TPUs. If
                specified all the computation will be performed with the given `dtype`.

                **Note that this only specifies the dtype of the computation and does not influence the dtype of model
                parameters.**

                If you wish to change the dtype of the model parameters, see [`~FlaxPreTrainedModel.to_fp16`] and
                [`~FlaxPreTrainedModel.to_bf16`].
            model_args (sequence of positional arguments, *optional*):
                All remaining positional arguments will be passed to the underlying model's `__init__` method.
            config (`Union[PretrainedConfig, str, os.PathLike]`, *optional*):
                Can be either:

                    - an instance of a class derived from [`PretrainedConfig`],
                    - a string or path valid as input to [`~PretrainedConfig.from_pretrained`].

                Configuration for the model to use instead of an automatically loaded configuration. Configuration can
                be automatically loaded when:

                    - The model is a model provided by the library (loaded with the *model id* string of a pretrained
                      model).
                    - The model was saved using [`~PreTrainedModel.save_pretrained`] and is reloaded by supplying the
                      save directory.
                    - The model is loaded by supplying a local directory as `pretrained_model_name_or_path` and a
                      configuration JSON file named *config.json* is found in the directory.
            cache_dir (`Union[str, os.PathLike]`, *optional*):
                Path to a directory in which a downloaded pretrained model configuration should be cached if the
                standard cache should not be used.
            from_pt (`bool`, *optional*, defaults to `False`):
                Load the model weights from a PyTorch checkpoint save file (see docstring of
                `pretrained_model_name_or_path` argument).
            ignore_mismatched_sizes (`bool`, *optional*, defaults to `False`):
                Whether or not to raise an error if some of the weights from the checkpoint do not have the same size
                as the weights of the model (if for instance, you are instantiating a model with 10 labels from a
                checkpoint with 3 labels).
            force_download (`bool`, *optional*, defaults to `False`):
                Whether or not to force the (re-)download of the model weights and configuration files, overriding the
                cached versions if they exist.
            resume_download:
                Deprecated and ignored. All downloads are now resumed by default when possible.
                Will be removed in v5 of Transformers.
            proxies (`Dict[str, str]`, *optional*):
                A dictionary of proxy servers to use by protocol or endpoint, e.g., `{'http': 'foo.bar:3128',
                'http://hostname': 'foo.bar:4012'}`. The proxies are used on each request.
            local_files_only(`bool`, *optional*, defaults to `False`):
                Whether or not to only look at local files (i.e., do not try to download the model).
            token (`str` or `bool`, *optional*):
                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
                the token generated when running `huggingface-cli login` (stored in `~/.huggingface`).
            revision (`str`, *optional*, defaults to `"main"`):
                The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
                git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
                identifier allowed by git.


                <Tip>

                To test a pull request you made on the Hub, you can pass `revision="refs/pr/<pr_number>"`.

                </Tip>

            subfolder (`str`, *optional*, defaults to `""`):
                In case the relevant files are located inside a subfolder of the model repo on huggingface.co, you can
                specify the folder name here.
            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`). Behaves differently depending on whether a `config` is provided or
                automatically loaded:

                    - If a configuration is provided with `config`, `**kwargs` will be directly passed to the
                      underlying model's `__init__` method (we assume all relevant updates to the configuration have
                      already been done)
                    - If a configuration is not provided, `kwargs` will be first passed to the configuration class
                      initialization function ([`~PretrainedConfig.from_pretrained`]). Each key of `kwargs` that
                      corresponds to a configuration attribute will be used to override said attribute with the
                      supplied `kwargs` value. Remaining keys that do not correspond to any configuration attribute
                      will be passed to the underlying model's `__init__` function.

        Examples:

        ```python
        >>> from transformers import BertConfig, FlaxBertModel

        >>> # Download model and configuration from huggingface.co and cache.
        >>> model = FlaxBertModel.from_pretrained("google-bert/bert-base-cased")
        >>> # Model was saved using *save_pretrained('./test/saved_model/')* (for example purposes, not runnable).
        >>> model = FlaxBertModel.from_pretrained("./test/saved_model/")
        >>> # Loading from a PyTorch checkpoint file instead of a PyTorch model (slower, for example purposes, not runnable).
        >>> config = BertConfig.from_json_file("./pt_model/config.json")
        >>> model = FlaxBertModel.from_pretrained("./pt_model/pytorch_model.bin", from_pt=True, config=config)
        ```"""
        ...

    def save_pretrained(
        self,
        save_directory: str | os.PathLike,
        params=...,
        push_to_hub=...,
        max_shard_size=...,
        token: str | bool | None = ...,
        safe_serialization: bool = ...,
        **kwargs,
    ):  # -> None:
        """
        Save a model and its configuration file to a directory, so that it can be re-loaded using the
        `[`~FlaxPreTrainedModel.from_pretrained`]` class method

        Arguments:
            save_directory (`str` or `os.PathLike`):
                Directory to which to save. Will be created if it doesn't exist.
            push_to_hub (`bool`, *optional*, defaults to `False`):
                Whether or not to push your model to the Hugging Face model hub after saving it. You can specify the
                repository you want to push to with `repo_id` (will default to the name of `save_directory` in your
                namespace).
            max_shard_size (`int` or `str`, *optional*, defaults to `"10GB"`):
                The maximum size for a checkpoint before being sharded. Checkpoints shard will then be each of size
                lower than this size. If expressed as a string, needs to be digits followed by a unit (like `"5MB"`).

                <Tip warning={true}>

                If a single weight of the model is bigger than `max_shard_size`, it will be in its own checkpoint shard
                which will be bigger than `max_shard_size`.

                </Tip>

            token (`str` or `bool`, *optional*):
                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
                the token generated when running `huggingface-cli login` (stored in `~/.huggingface`).
            kwargs (`Dict[str, Any]`, *optional*):
                Additional key word arguments passed along to the [`~utils.PushToHubMixin.push_to_hub`] method.
            safe_serialization (`bool`, *optional*, defaults to `False`):
                Whether to save the model using `safetensors` or through msgpack.
        """
        ...

    @classmethod
    def register_for_auto_class(cls, auto_class=...):  # -> None:
        """
        Register this class with a given auto class. This should only be used for custom models as the ones in the
        library are already mapped with an auto class.

        <Tip warning={true}>

        This API is experimental and may have some slight breaking changes in the next releases.

        </Tip>

        Args:
            auto_class (`str` or `type`, *optional*, defaults to `"FlaxAutoModel"`):
                The auto class to register this new model with.
        """
        ...

if FlaxPreTrainedModel.push_to_hub.__doc__ is not None: ...

def overwrite_call_docstring(model_class, docstring):  # -> None:
    ...
def append_call_sample_docstring(
    model_class, checkpoint, output_type, config_class, mask=..., revision=..., real_checkpoint=...
):  # -> None:
    ...
def append_replace_return_docstrings(model_class, output_type, config_class):  # -> None:
    ...
