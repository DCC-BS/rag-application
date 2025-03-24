"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping, Sequence

from ...feature_extraction_utils import BatchFeature
from ...image_utils import ImageInput
from ...processing_utils import Unpack
from ..gemma3.processing_gemma3 import Gemma3Processor, Gemma3ProcessorKwargs

logger = ...
DEFAULT_SHIELDGEMMA2_POLICIES: Mapping[str, str] = ...

class ShieldGemma2ProcessorKwargs(Gemma3ProcessorKwargs, total=False):
    policies: Sequence[str] | None
    custom_policies: Mapping[str, str] | None
    _defaults = ...

class ShieldGemma2Processor(Gemma3Processor):
    def __init__(
        self, image_processor, tokenizer, chat_template=..., image_seq_length=..., policy_definitions=..., **kwargs
    ) -> None:
        """A processor for the ShieldGemma 2 model.

        Args:
            image_processor: The image processor to use, typically a `Gemma3ImageProcessorFast` instance.
            tokenizer: The tokenizer to use, typically a `GemmaTokenizerFast` instance.
            chat_template: The chat template to use with this processor. Typically, this is unset as the processor
                configuration on Hugging Face Hub includes this value already.
            image_seq_length: The number of soft tokens per image. Typically, this is unset as the processor
                configuration on Hugging Face Hub includes this value already.
            policy_definitions: A mapping from policy name to its description in text used as the default policies to
                classify images against. The policy descriptions are included in the text of the prompts generated by
                this processor. Typically, this is unset as the processor configuration on Hugging Face Hub includes
                the base policies ShieldGemma was trained on.
        """
        ...

    def __call__(
        self, images: ImageInput = ..., text=..., videos=..., audio=..., **kwargs: Unpack[ShieldGemma2ProcessorKwargs]
    ) -> BatchFeature:
        """Generates a batch of inputs from the provided images.

        ShieldGemma was trained to classify image content for policy compliance using a specific prompt construction.
        This processor generates a batch of such prompts from the provided images by:

        1.  Creating a list of conversations, one for each `<image, policy>` pair;
        2.  Converting these conversations to text using `self.apply_chat_template()`; and
        3.  Encoding the conversations and images using the same techniques as `Gemma3Processor`.

        Args:
            images: A single image or a list of images to include in the batch.
            text: Not supported.
            videos: Not supported.
            audio: Not supported.
            kwargs: An optional dictionary of keyword arguments to configre the
                processor. Possible values include:

                *   `custom_policies`: Additional policy definitions that augment the `self.policy_definitions` passed
                    into the constructor. Note that `custom_policies` that share a key with `self.policy_definitions`
                    will override the policy description
                *   `policies`: (Optional) a list of keys in the joint `self.policy_definitions | custom_policies`
                    dictionary of specific interest for the provided images. If empty or None, prompts will be
                    generated for every key in the joint dictionary.

        Returns:
            A `BatchFeature` continaing `input_ids`, `pixel_values`, etc. where each Tensor is of shape
            `(len(images) * len(policies), )`, and the order within the batch will be
            img1_policy1, ... img1_policyN, ... imgM_policyN.
        """
        ...

    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to GemmaTokenizerFast's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
        ...

    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to GemmaTokenizerFast's [`~PreTrainedTokenizer.decode`]. Please refer to
        the docstring of this method for more information.
        """
        ...

    @property
    def model_input_names(self):  # -> list[Any]:
        ...

__all__ = ["ShieldGemma2Processor"]
