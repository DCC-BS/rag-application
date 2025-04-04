"""
This type stub file was generated by pyright.
"""

from ....processing_utils import ProcessorMixin

"""
Processor class for TVLT.
"""

class TvltProcessor(ProcessorMixin):
    r"""
    Constructs a TVLT processor which wraps a TVLT image processor and TVLT feature extractor into a single processor.

    [`TvltProcessor`] offers all the functionalities of [`TvltImageProcessor`] and [`TvltFeatureExtractor`]. See the
    docstring of [`~TvltProcessor.__call__`] for more information.

    Args:
        image_processor (`TvltImageProcessor`):
            An instance of [`TvltImageProcessor`]. The image processor is a required input.
        feature_extractor (`TvltFeatureExtractor`):
            An instance of [`TvltFeatureExtractor`]. The feature extractor is a required input.
    """

    attributes = ...
    image_processor_class = ...
    feature_extractor_class = ...
    def __init__(self, image_processor, feature_extractor) -> None: ...
    def __call__(
        self,
        images=...,
        audio=...,
        images_mixed=...,
        sampling_rate=...,
        mask_audio=...,
        mask_pixel=...,
        *args,
        **kwargs,
    ):  # -> dict[Any, Any]:
        """
        Forwards the `images` argument to TvltImageProcessor's [`~TvltImageProcessor.preprocess`] and the `audio`
        argument to TvltFeatureExtractor's [`~TvltFeatureExtractor.__call__`]. Please refer to the docstring of the
        above two methods for more information.
        """
        ...

    @property
    def model_input_names(self):  # -> list[Any]:
        ...
