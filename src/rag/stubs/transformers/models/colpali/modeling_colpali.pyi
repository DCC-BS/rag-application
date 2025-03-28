"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

import torch
from torch import nn

from ...cache_utils import Cache
from ...modeling_utils import PreTrainedModel
from ...utils import ModelOutput, add_start_docstrings, add_start_docstrings_to_model_forward, replace_return_docstrings
from .configuration_colpali import ColPaliConfig

"""PyTorch ColPali model"""
_CONFIG_FOR_DOC = ...
COLPALI_START_DOCSTRING = ...

@add_start_docstrings(
    "The bare ColPali model outputting raw hidden-states without any specific head on top.", COLPALI_START_DOCSTRING
)
class ColPaliPreTrainedModel(PreTrainedModel):
    config_class = ColPaliConfig
    base_model_prefix = ...
    _no_split_modules = ...

@dataclass
class ColPaliForRetrievalOutput(ModelOutput):
    """
    Base class for ColPali embeddings output.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss (for next-token prediction).
        embeddings (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            The embeddings of the model.
        past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
            `(batch_size, num_heads, sequence_length, embed_size_per_head)`)

            Contains pre-computed hidden-states (key and values in the self-attention blocks) that can be used (see
            `past_key_values` input) to speed up sequential decoding.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        image_hidden_states (`torch.FloatTensor`, *optional*):
            A `torch.FloatTensor` of size `(batch_size, num_images, sequence_length, hidden_size)`.
            image_hidden_states of the model produced by the vision encoder after projecting last hidden state.
    """

    loss: torch.FloatTensor | None = ...
    embeddings: torch.Tensor = ...
    past_key_values: list[torch.FloatTensor] | Cache | None = ...
    hidden_states: tuple[torch.FloatTensor] | None = ...
    attentions: tuple[torch.FloatTensor] | None = ...
    image_hidden_states: torch.FloatTensor | None = ...

COLPALI_FOR_RETRIEVAL_INPUT_DOCSTRING = ...

@add_start_docstrings("""
    In our proposed ColPali approach, we leverage VLMs to construct efficient multi-vector embeddings directly
    from document images (“screenshots”) for document retrieval. We train the model to maximize the similarity
    between these document embeddings and the corresponding query embeddings, using the late interaction method
    introduced in ColBERT.

    Using ColPali removes the need for potentially complex and brittle layout recognition and OCR pipelines with a
    single model that can take into account both the textual and visual content (layout, charts, etc.) of a document.
    """)
class ColPaliForRetrieval(ColPaliPreTrainedModel):
    def __init__(self, config: ColPaliConfig) -> None: ...
    @add_start_docstrings_to_model_forward(COLPALI_FOR_RETRIEVAL_INPUT_DOCSTRING)
    @replace_return_docstrings(output_type=ColPaliForRetrievalOutput, config_class=_CONFIG_FOR_DOC)
    def forward(
        self,
        input_ids: torch.LongTensor = ...,
        pixel_values: torch.FloatTensor = ...,
        attention_mask: torch.Tensor | None = ...,
        output_attentions: bool | None = ...,
        output_hidden_states: bool | None = ...,
        return_dict: bool | None = ...,
        **kwargs,
    ) -> tuple | ColPaliForRetrievalOutput:
        r"""
        Returns:
        """
        ...

    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value):  # -> None:
        ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings):  # -> None:
        ...
    def set_decoder(self, decoder):  # -> None:
        ...
    def get_decoder(self): ...
    def tie_weights(self): ...
    def resize_token_embeddings(
        self, new_num_tokens: int | None = ..., pad_to_multiple_of: int | None = ..., mean_resizing: bool = ...
    ) -> nn.Embedding: ...

__all__ = ["ColPaliForRetrieval", "ColPaliForRetrievalOutput", "ColPaliPreTrainedModel"]
