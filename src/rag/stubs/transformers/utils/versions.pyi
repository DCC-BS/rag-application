"""
This type stub file was generated by pyright.
"""

"""
Utilities for working with package versions
"""
ops = ...

def require_version(requirement: str, hint: str | None = ...) -> None:
    """
    Perform a runtime check of the dependency versions, using the exact same syntax used by pip.

    The installed module version comes from the *site-packages* dir via *importlib.metadata*.

    Args:
        requirement (`str`): pip style definition, e.g.,  "tokenizers==0.9.4", "tqdm>=4.27", "numpy"
        hint (`str`, *optional*): what suggestion to print in case of requirements not being met

    Example:

    ```python
    require_version("pandas>1.1.2")
    require_version("numpy>1.18.5", "this is important to have for whatever reason")
    ```"""
    ...

def require_version_core(requirement):  # -> None:
    """require_version wrapper which emits a core-specific hint on failure"""
    ...
