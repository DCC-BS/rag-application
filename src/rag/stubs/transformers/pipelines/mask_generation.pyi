"""
This type stub file was generated by pyright.
"""

from ..utils import add_end_docstrings, is_torch_available
from .base import ChunkPipeline, build_pipeline_init_args

if is_torch_available(): ...
logger = ...

@add_end_docstrings(
    build_pipeline_init_args(has_image_processor=True),
    r"""
        points_per_batch (*optional*, int, default to 64):
            Sets the number of points run simultaneously by the model. Higher numbers may be faster but use more GPU
            memory.
        output_bboxes_mask (`bool`, *optional*, default to `False`):
            Whether or not to output the bounding box predictions.
        output_rle_masks (`bool`, *optional*, default to `False`):
            Whether or not to output the masks in `RLE` format""",
)
class MaskGenerationPipeline(ChunkPipeline):
    """
    Automatic mask generation for images using `SamForMaskGeneration`. This pipeline predicts binary masks for an
    image, given an image. It is a `ChunkPipeline` because you can seperate the points in a mini-batch in order to
    avoid OOM issues. Use the `points_per_batch` argument to control the number of points that will be processed at the
    same time. Default is `64`.

    The pipeline works in 3 steps:
        1. `preprocess`: A grid of 1024 points evenly separated is generated along with bounding boxes and point
           labels.
            For more details on how the points and bounding boxes are created, check the `_generate_crop_boxes`
            function. The image is also preprocessed using the `image_processor`. This function `yields` a minibatch of
            `points_per_batch`.

        2. `forward`: feeds the outputs of `preprocess` to the model. The image embedding is computed only once.
            Calls both `self.model.get_image_embeddings` and makes sure that the gradients are not computed, and the
            tensors and models are on the same device.

        3. `postprocess`: The most important part of the automatic mask generation happens here. Three steps
            are induced:
                - image_processor.postprocess_masks (run on each minibatch loop): takes in the raw output masks,
                  resizes them according
                to the image size, and transforms there to binary masks.
                - image_processor.filter_masks (on each minibatch loop): uses both `pred_iou_thresh` and
                  `stability_scores`. Also
                applies a variety of filters based on non maximum suppression to remove bad masks.
                - image_processor.postprocess_masks_for_amg applies the NSM on the mask to only keep relevant ones.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> generator = pipeline(model="facebook/sam-vit-base", task="mask-generation")
    >>> outputs = generator(
    ...     "http://images.cocodataset.org/val2017/000000039769.jpg",
    ... )

    >>> outputs = generator(
    ...     "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png", points_per_batch=128
    ... )
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This segmentation pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"mask-generation"`.

    See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=mask-generation).
    """
    def __init__(self, **kwargs) -> None: ...
    def __call__(
        self, image, *args, num_workers=..., batch_size=..., **kwargs
    ):  # -> list[Any] | PipelineIterator | Generator[Any, Any, None] | Tensor | Any | None:
        """
        Generates binary segmentation masks

        Args:
            inputs (`np.ndarray` or `bytes` or `str` or `dict`):
                Image or list of images.
            mask_threshold (`float`, *optional*, defaults to 0.0):
                Threshold to use when turning the predicted masks into binary values.
            pred_iou_thresh (`float`, *optional*, defaults to 0.88):
                A filtering threshold in `[0,1]` applied on the model's predicted mask quality.
            stability_score_thresh (`float`, *optional*, defaults to 0.95):
                A filtering threshold in `[0,1]`, using the stability of the mask under changes to the cutoff used to
                binarize the model's mask predictions.
            stability_score_offset (`int`, *optional*, defaults to 1):
                The amount to shift the cutoff when calculated the stability score.
            crops_nms_thresh (`float`, *optional*, defaults to 0.7):
                The box IoU cutoff used by non-maximal suppression to filter duplicate masks.
            crops_n_layers (`int`, *optional*, defaults to 0):
                If `crops_n_layers>0`, mask prediction will be run again on crops of the image. Sets the number of
                layers to run, where each layer has 2**i_layer number of image crops.
            crop_overlap_ratio (`float`, *optional*, defaults to `512 / 1500`):
                Sets the degree to which crops overlap. In the first crop layer, crops will overlap by this fraction of
                the image length. Later layers with more crops scale down this overlap.
            crop_n_points_downscale_factor (`int`, *optional*, defaults to `1`):
                The number of points-per-side sampled in layer n is scaled down by crop_n_points_downscale_factor**n.
            timeout (`float`, *optional*, defaults to None):
                The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and
                the call may block forever.

        Return:
            `Dict`: A dictionary with the following keys:
                - **mask** (`PIL.Image`) -- A binary mask of the detected object as a PIL Image of shape `(width,
                  height)` of the original image. Returns a mask filled with zeros if no object is found.
                - **score** (*optional* `float`) -- Optionally, when the model is capable of estimating a confidence of
                  the "object" described by the label and the mask.

        """
        ...

    def preprocess(
        self,
        image,
        points_per_batch=...,
        crops_n_layers: int = ...,
        crop_overlap_ratio: float = ...,
        points_per_crop: int | None = ...,
        crop_n_points_downscale_factor: int | None = ...,
        timeout: float | None = ...,
    ):  # -> Generator[dict[str | Any, Any], Any, None]:
        ...
    def postprocess(
        self, model_outputs, output_rle_mask=..., output_bboxes_mask=..., crops_nms_thresh=...
    ):  # -> dict[str | Any, Any | list[Any]]:
        ...
