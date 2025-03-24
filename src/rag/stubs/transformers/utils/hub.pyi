"""
This type stub file was generated by pyright.
"""

import os
from concurrent import futures
from pathlib import Path

"""
Hub utilities: utilities related to download and cache models
"""
logger = ...
_is_offline_mode = ...

def is_offline_mode():  # -> bool:
    ...

torch_cache_home = ...
default_cache_path = ...
PYTORCH_PRETRAINED_BERT_CACHE = ...
PYTORCH_TRANSFORMERS_CACHE = ...
TRANSFORMERS_CACHE = ...
HF_MODULES_CACHE = ...
TRANSFORMERS_DYNAMIC_MODULE_NAME = ...
SESSION_ID = ...
S3_BUCKET_PREFIX = ...
CLOUDFRONT_DISTRIB_PREFIX = ...
_staging_mode = ...
_default_endpoint = ...
HUGGINGFACE_CO_RESOLVE_ENDPOINT = ...
if os.environ.get("HUGGINGFACE_CO_RESOLVE_ENDPOINT", None) is not None:
    HUGGINGFACE_CO_RESOLVE_ENDPOINT = ...
HUGGINGFACE_CO_RESOLVE_ENDPOINT = ...
HUGGINGFACE_CO_PREFIX = ...
HUGGINGFACE_CO_EXAMPLES_TELEMETRY = ...

def is_remote_url(url_or_filename):  # -> bool:
    ...
def define_sagemaker_information():  # -> dict[str, str | int | bool | Any | None]:
    ...
def http_user_agent(user_agent: dict | str | None = ...) -> str:
    """
    Formats a user-agent string with basic info about a request.
    """
    ...

def extract_commit_hash(resolved_file: str | None, commit_hash: str | None) -> str | None:
    """
    Extracts the commit hash from a resolved filename toward a cache file.
    """
    ...

def cached_file(path_or_repo_id: str | os.PathLike, filename: str, **kwargs) -> str | None:
    """
    Tries to locate a file in a local folder and repo, downloads and cache it if necessary.

    Args:
        path_or_repo_id (`str` or `os.PathLike`):
            This can be either:
            - a string, the *model id* of a model repo on huggingface.co.
            - a path to a *directory* potentially containing the file.
        filename (`str`):
            The name of the file to locate in `path_or_repo`.
        cache_dir (`str` or `os.PathLike`, *optional*):
            Path to a directory in which a downloaded pretrained model configuration should be cached if the standard
            cache should not be used.
        force_download (`bool`, *optional*, defaults to `False`):
            Whether or not to force to (re-)download the configuration files and override the cached versions if they
            exist.
        resume_download:
            Deprecated and ignored. All downloads are now resumed by default when possible.
            Will be removed in v5 of Transformers.
        proxies (`Dict[str, str]`, *optional*):
            A dictionary of proxy servers to use by protocol or endpoint, e.g., `{'http': 'foo.bar:3128',
            'http://hostname': 'foo.bar:4012'}.` The proxies are used on each request.
        token (`str` or *bool*, *optional*):
            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
            when running `huggingface-cli login` (stored in `~/.huggingface`).
        revision (`str`, *optional*, defaults to `"main"`):
            The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
            git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
            identifier allowed by git.
        local_files_only (`bool`, *optional*, defaults to `False`):
            If `True`, will only try to load the tokenizer configuration from local files.
        subfolder (`str`, *optional*, defaults to `""`):
            In case the relevant files are located inside a subfolder of the model repo on huggingface.co, you can
            specify the folder name here.
        repo_type (`str`, *optional*):
            Specify the repo type (useful when downloading from a space for instance).

    <Tip>

    Passing `token=True` is required when you want to use a private model.

    </Tip>

    Returns:
        `Optional[str]`: Returns the resolved file (to the cache folder if downloaded from a repo).

    Examples:

    ```python
    # Download a model weight from the Hub and cache it.
    model_weights_file = cached_file("google-bert/bert-base-uncased", "pytorch_model.bin")
    ```
    """
    ...

def cached_files(
    path_or_repo_id: str | os.PathLike,
    filenames: list[str],
    cache_dir: str | os.PathLike | None = ...,
    force_download: bool = ...,
    resume_download: bool | None = ...,
    proxies: dict[str, str] | None = ...,
    token: bool | str | None = ...,
    revision: str | None = ...,
    local_files_only: bool = ...,
    subfolder: str = ...,
    repo_type: str | None = ...,
    user_agent: str | dict[str, str] | None = ...,
    _raise_exceptions_for_gated_repo: bool = ...,
    _raise_exceptions_for_missing_entries: bool = ...,
    _raise_exceptions_for_connection_errors: bool = ...,
    _commit_hash: str | None = ...,
    **deprecated_kwargs,
) -> str | None:
    """
    Tries to locate several files in a local folder and repo, downloads and cache them if necessary.

    Args:
        path_or_repo_id (`str` or `os.PathLike`):
            This can be either:
            - a string, the *model id* of a model repo on huggingface.co.
            - a path to a *directory* potentially containing the file.
        filenames (`List[str]`):
            The name of all the files to locate in `path_or_repo`.
        cache_dir (`str` or `os.PathLike`, *optional*):
            Path to a directory in which a downloaded pretrained model configuration should be cached if the standard
            cache should not be used.
        force_download (`bool`, *optional*, defaults to `False`):
            Whether or not to force to (re-)download the configuration files and override the cached versions if they
            exist.
        resume_download:
            Deprecated and ignored. All downloads are now resumed by default when possible.
            Will be removed in v5 of Transformers.
        proxies (`Dict[str, str]`, *optional*):
            A dictionary of proxy servers to use by protocol or endpoint, e.g., `{'http': 'foo.bar:3128',
            'http://hostname': 'foo.bar:4012'}.` The proxies are used on each request.
        token (`str` or *bool*, *optional*):
            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
            when running `huggingface-cli login` (stored in `~/.huggingface`).
        revision (`str`, *optional*, defaults to `"main"`):
            The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
            git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
            identifier allowed by git.
        local_files_only (`bool`, *optional*, defaults to `False`):
            If `True`, will only try to load the tokenizer configuration from local files.
        subfolder (`str`, *optional*, defaults to `""`):
            In case the relevant files are located inside a subfolder of the model repo on huggingface.co, you can
            specify the folder name here.
        repo_type (`str`, *optional*):
            Specify the repo type (useful when downloading from a space for instance).

    Private args:
        _raise_exceptions_for_gated_repo (`bool`):
            if False, do not raise an exception for gated repo error but return None.
        _raise_exceptions_for_missing_entries (`bool`):
            if False, do not raise an exception for missing entries but return None.
        _raise_exceptions_for_connection_errors (`bool`):
            if False, do not raise an exception for connection errors but return None.
        _commit_hash (`str`, *optional*):
            passed when we are chaining several calls to various files (e.g. when loading a tokenizer or
            a pipeline). If files are cached for this commit hash, avoid calls to head and get from the cache.

    <Tip>

    Passing `token=True` is required when you want to use a private model.

    </Tip>

    Returns:
        `Optional[str]`: Returns the resolved file (to the cache folder if downloaded from a repo).

    Examples:

    ```python
    # Download a model weight from the Hub and cache it.
    model_weights_file = cached_file("google-bert/bert-base-uncased", "pytorch_model.bin")
    ```
    """
    ...

def get_file_from_repo(*args, **kwargs):  # -> str | None:
    """
    Tries to locate a file in a local folder and repo, downloads and cache it if necessary.

    Args:
        path_or_repo (`str` or `os.PathLike`):
            This can be either:

            - a string, the *model id* of a model repo on huggingface.co.
            - a path to a *directory* potentially containing the file.
        filename (`str`):
            The name of the file to locate in `path_or_repo`.
        cache_dir (`str` or `os.PathLike`, *optional*):
            Path to a directory in which a downloaded pretrained model configuration should be cached if the standard
            cache should not be used.
        force_download (`bool`, *optional*, defaults to `False`):
            Whether or not to force to (re-)download the configuration files and override the cached versions if they
            exist.
        resume_download:
            Deprecated and ignored. All downloads are now resumed by default when possible.
            Will be removed in v5 of Transformers.
        proxies (`Dict[str, str]`, *optional*):
            A dictionary of proxy servers to use by protocol or endpoint, e.g., `{'http': 'foo.bar:3128',
            'http://hostname': 'foo.bar:4012'}.` The proxies are used on each request.
        token (`str` or *bool*, *optional*):
            The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
            when running `huggingface-cli login` (stored in `~/.huggingface`).
        revision (`str`, *optional*, defaults to `"main"`):
            The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
            git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
            identifier allowed by git.
        local_files_only (`bool`, *optional*, defaults to `False`):
            If `True`, will only try to load the tokenizer configuration from local files.
        subfolder (`str`, *optional*, defaults to `""`):
            In case the relevant files are located inside a subfolder of the model repo on huggingface.co, you can
            specify the folder name here.

    <Tip>

    Passing `token=True` is required when you want to use a private model.

    </Tip>

    Returns:
        `Optional[str]`: Returns the resolved file (to the cache folder if downloaded from a repo) or `None` if the
        file does not exist.

    Examples:

    ```python
    # Download a tokenizer configuration from huggingface.co and cache.
    tokenizer_config = get_file_from_repo("google-bert/bert-base-uncased", "tokenizer_config.json")
    # This model does not have a tokenizer config so the result will be None.
    tokenizer_config = get_file_from_repo("FacebookAI/xlm-roberta-base", "tokenizer_config.json")
    ```
    """
    ...

def download_url(url, proxies=...):  # -> str:
    """
    Downloads a given url in a temporary file. This function is not safe to use in multiple processes. Its only use is
    for deprecated behavior allowing to download config/models with a single url instead of using the Hub.

    Args:
        url (`str`): The url of the file to download.
        proxies (`Dict[str, str]`, *optional*):
            A dictionary of proxy servers to use by protocol or endpoint, e.g., `{'http': 'foo.bar:3128',
            'http://hostname': 'foo.bar:4012'}.` The proxies are used on each request.

    Returns:
        `str`: The location of the temporary file where the url was downloaded.
    """
    ...

def has_file(
    path_or_repo: str | os.PathLike,
    filename: str,
    revision: str | None = ...,
    proxies: dict[str, str] | None = ...,
    token: bool | str | None = ...,
    *,
    local_files_only: bool = ...,
    cache_dir: str | Path | None = ...,
    repo_type: str | None = ...,
    **deprecated_kwargs,
):  # -> bool:
    """
    Checks if a repo contains a given file without downloading it. Works for remote repos and local folders.

    If offline mode is enabled, checks if the file exists in the cache.

    <Tip warning={false}>

    This function will raise an error if the repository `path_or_repo` is not valid or if `revision` does not exist for
    this repo, but will return False for regular connection errors.

    </Tip>
    """
    ...

class PushToHubMixin:
    """
    A Mixin containing the functionality to push a model or tokenizer to the hub.
    """
    def push_to_hub(
        self,
        repo_id: str,
        use_temp_dir: bool | None = ...,
        commit_message: str | None = ...,
        private: bool | None = ...,
        token: bool | str | None = ...,
        max_shard_size: int | str | None = ...,
        create_pr: bool = ...,
        safe_serialization: bool = ...,
        revision: str = ...,
        commit_description: str = ...,
        tags: list[str] | None = ...,
        **deprecated_kwargs,
    ) -> str:
        """
        Upload the {object_files} to the 🤗 Model Hub.

        Parameters:
            repo_id (`str`):
                The name of the repository you want to push your {object} to. It should contain your organization name
                when pushing to a given organization.
            use_temp_dir (`bool`, *optional*):
                Whether or not to use a temporary directory to store the files saved before they are pushed to the Hub.
                Will default to `True` if there is no directory named like `repo_id`, `False` otherwise.
            commit_message (`str`, *optional*):
                Message to commit while pushing. Will default to `"Upload {object}"`.
            private (`bool`, *optional*):
                Whether to make the repo private. If `None` (default), the repo will be public unless the organization's default is private. This value is ignored if the repo already exists.
            token (`bool` or `str`, *optional*):
                The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated
                when running `huggingface-cli login` (stored in `~/.huggingface`). Will default to `True` if `repo_url`
                is not specified.
            max_shard_size (`int` or `str`, *optional*, defaults to `"5GB"`):
                Only applicable for models. The maximum size for a checkpoint before being sharded. Checkpoints shard
                will then be each of size lower than this size. If expressed as a string, needs to be digits followed
                by a unit (like `"5MB"`). We default it to `"5GB"` so that users can easily load models on free-tier
                Google Colab instances without any CPU OOM issues.
            create_pr (`bool`, *optional*, defaults to `False`):
                Whether or not to create a PR with the uploaded files or directly commit.
            safe_serialization (`bool`, *optional*, defaults to `True`):
                Whether or not to convert the model weights in safetensors format for safer serialization.
            revision (`str`, *optional*):
                Branch to push the uploaded files to.
            commit_description (`str`, *optional*):
                The description of the commit that will be created
            tags (`List[str]`, *optional*):
                List of tags to push on the Hub.

        Examples:

        ```python
        from transformers import {object_class}

        {object} = {object_class}.from_pretrained("google-bert/bert-base-cased")

        # Push the {object} to your namespace with the name "my-finetuned-bert".
        {object}.push_to_hub("my-finetuned-bert")

        # Push the {object} to an organization with the name "my-finetuned-bert".
        {object}.push_to_hub("huggingface/my-finetuned-bert")
        ```
        """
        ...

def send_example_telemetry(example_name, *example_args, framework=...):  # -> None:
    """
    Sends telemetry that helps tracking the examples use.

    Args:
        example_name (`str`): The name of the example.
        *example_args (dataclasses or `argparse.ArgumentParser`): The arguments to the script. This function will only
            try to extract the model and dataset name from those. Nothing else is tracked.
        framework (`str`, *optional*, defaults to `"pytorch"`): The framework for the example.
    """
    ...

def convert_file_size_to_int(size: int | str):  # -> int:
    """
    Converts a size expressed as a string with digits an unit (like `"5MB"`) to an integer (in bytes).

    Args:
        size (`int` or `str`): The size to convert. Will be directly returned if an `int`.

    Example:
    ```py
    >>> convert_file_size_to_int("1MiB")
    1048576
    ```
    """
    ...

def get_checkpoint_shard_files(
    pretrained_model_name_or_path,
    index_filename,
    cache_dir=...,
    force_download=...,
    proxies=...,
    resume_download=...,
    local_files_only=...,
    token=...,
    user_agent=...,
    revision=...,
    subfolder=...,
    _commit_hash=...,
    **deprecated_kwargs,
):  # -> tuple[list[str], Any] | tuple[str | None, Any]:
    """
    For a given model:

    - download and cache all the shards of a sharded checkpoint if `pretrained_model_name_or_path` is a model ID on the
      Hub
    - returns the list of paths to all the shards, as well as some metadata.

    For the description of each arg, see [`PreTrainedModel.from_pretrained`]. `index_filename` is the full path to the
    index (downloaded and cached if `pretrained_model_name_or_path` is a model ID on the Hub).
    """
    ...

def create_and_tag_model_card(
    repo_id: str, tags: list[str] | None = ..., token: str | None = ..., ignore_metadata_errors: bool = ...
):  # -> ModelCard:
    """
    Creates or loads an existing model card and tags it.

    Args:
        repo_id (`str`):
            The repo_id where to look for the model card.
        tags (`List[str]`, *optional*):
            The list of tags to add in the model card
        token (`str`, *optional*):
            Authentication token, obtained with `huggingface_hub.HfApi.login` method. Will default to the stored token.
        ignore_metadata_errors (`str`):
            If True, errors while parsing the metadata section will be ignored. Some information might be lost during
            the process. Use it at your own risk.
    """
    ...

class PushInProgress:
    """
    Internal class to keep track of a push in progress (which might contain multiple `Future` jobs).
    """
    def __init__(self, jobs: futures.Future | None = ...) -> None: ...
    def is_done(self):  # -> bool:
        ...
    def wait_until_done(self):  # -> None:
        ...
    def cancel(self) -> None: ...
