"""
This type stub file was generated by pyright.
"""

from ..utils import ExplicitEnum, add_end_docstrings, is_tf_available, is_torch_available
from .base import GenericTensor, Pipeline, build_pipeline_init_args

if is_tf_available(): ...
if is_torch_available(): ...

def sigmoid(_outputs):  # -> Any:
    ...
def softmax(_outputs):  # -> Any:
    ...

class ClassificationFunction(ExplicitEnum):
    SIGMOID = ...
    SOFTMAX = ...
    NONE = ...

@add_end_docstrings(
    build_pipeline_init_args(has_tokenizer=True),
    r"""
        return_all_scores (`bool`, *optional*, defaults to `False`):
            Whether to return all prediction scores or just the one of the predicted class.
        function_to_apply (`str`, *optional*, defaults to `"default"`):
            The function to apply to the model outputs in order to retrieve the scores. Accepts four different values:

            - `"default"`: if the model has a single label, will apply the sigmoid function on the output. If the model
              has several labels, will apply the softmax function on the output. In case of regression tasks, will not
              apply any function on the output.
            - `"sigmoid"`: Applies the sigmoid function on the output.
            - `"softmax"`: Applies the softmax function on the output.
            - `"none"`: Does not apply any function on the output.""",
)
class TextClassificationPipeline(Pipeline):
    """
    Text classification pipeline using any `ModelForSequenceClassification`. See the [sequence classification
    examples](../task_summary#sequence-classification) for more information.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> classifier = pipeline(model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    >>> classifier("This movie is disgustingly good !")
    [{'label': 'POSITIVE', 'score': 1.0}]

    >>> classifier("Director tried too much.")
    [{'label': 'NEGATIVE', 'score': 0.996}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This text classification pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"sentiment-analysis"` (for classifying sequences according to positive or negative sentiments).

    If multiple classification labels are available (`model.config.num_labels >= 2`), the pipeline will run a softmax
    over the results. If there is a single label, the pipeline will run a sigmoid over the result. In case of regression
    tasks (`model.config.problem_type == "regression"`), will not apply any function on the output.

    The models that this pipeline can use are models that have been fine-tuned on a sequence classification task. See
    the up-to-date list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=text-classification).
    """

    return_all_scores = ...
    function_to_apply = ...
    def __init__(self, **kwargs) -> None: ...
    def __call__(
        self, inputs, **kwargs
    ):  # -> list[list[Any] | PipelineIterator | Generator[Any, Any, None] | Tensor | Any | None] | list[Any] | PipelineIterator | Generator[Any, Any, None] | Tensor | Any | None:
        """
        Classify the text(s) given as inputs.

        Args:
            inputs (`str` or `List[str]` or `Dict[str]`, or `List[Dict[str]]`):
                One or several texts to classify. In order to use text pairs for your classification, you can send a
                dictionary containing `{"text", "text_pair"}` keys, or a list of those.
            top_k (`int`, *optional*, defaults to `1`):
                How many results to return.
            function_to_apply (`str`, *optional*, defaults to `"default"`):
                The function to apply to the model outputs in order to retrieve the scores. Accepts four different
                values:

                If this argument is not specified, then it will apply the following functions according to the number
                of labels:

                - If problem type is regression, will not apply any function on the output.
                - If the model has a single label, will apply the sigmoid function on the output.
                - If the model has several labels, will apply the softmax function on the output.

                Possible values are:

                - `"sigmoid"`: Applies the sigmoid function on the output.
                - `"softmax"`: Applies the softmax function on the output.
                - `"none"`: Does not apply any function on the output.

        Return:
            A list or a list of list of `dict`: Each result comes as list of dictionaries with the following keys:

            - **label** (`str`) -- The label predicted.
            - **score** (`float`) -- The corresponding probability.

            If `top_k` is used, one such dictionary is returned per label.
        """
        ...

    def preprocess(self, inputs, **tokenizer_kwargs) -> dict[str, GenericTensor]: ...
    def postprocess(
        self, model_outputs, function_to_apply=..., top_k=..., _legacy=...
    ):  # -> dict[str, Any | str] | list[dict[str, Any | str]]:
        ...
