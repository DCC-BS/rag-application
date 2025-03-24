"""
This type stub file was generated by pyright.
"""

import torch

from ....modeling_utils import PreTrainedModel
from ....utils import add_start_docstrings
from .configuration_retribert import RetriBertConfig

"""
RetriBERT model
"""
logger = ...

class RetriBertPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """

    config_class = RetriBertConfig
    load_tf_weights = ...
    base_model_prefix = ...

RETRIBERT_START_DOCSTRING = ...

@add_start_docstrings(
    """Bert Based model to embed queries or document for document retrieval.""", RETRIBERT_START_DOCSTRING
)
class RetriBertModel(RetriBertPreTrainedModel):
    def __init__(self, config: RetriBertConfig) -> None: ...
    def embed_sentences_checkpointed(
        self, input_ids, attention_mask, sent_encoder, checkpoint_batch_size=...
    ):  # -> Tensor:
        ...
    def embed_questions(self, input_ids, attention_mask=..., checkpoint_batch_size=...):  # -> Any:
        ...
    def embed_answers(self, input_ids, attention_mask=..., checkpoint_batch_size=...):  # -> Any:
        ...
    def forward(
        self,
        input_ids_query: torch.LongTensor,
        attention_mask_query: torch.FloatTensor | None,
        input_ids_doc: torch.LongTensor,
        attention_mask_doc: torch.FloatTensor | None,
        checkpoint_batch_size: int = ...,
    ) -> torch.FloatTensor:
        r"""
        Args:
            input_ids_query (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary for the queries in a batch.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask_query (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            input_ids_doc (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary for the documents in a batch.
            attention_mask_doc (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on documents padding token indices.
            checkpoint_batch_size (`int`, *optional*, defaults to `-1`):
                If greater than 0, uses gradient checkpointing to only compute sequence representation on
                `checkpoint_batch_size` examples at a time on the GPU. All query representations are still compared to
                all document representations in the batch.

        Return:
            `torch.FloatTensor``: The bidirectional cross-entropy loss obtained while trying to match each query to its
            corresponding document and each document to its corresponding query in the batch
        """
        ...
