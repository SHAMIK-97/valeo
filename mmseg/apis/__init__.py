# Copyright (c) OpenMMLab. All rights reserved.
from .inference import inference_model, init_model, show_result_pyplot,inference_model_1
from .mmseg_inferencer import MMSegInferencer
from .remote_sense_inferencer import RSImage, RSInferencer

__all__ = [
    'init_model', 'inference_model', 'show_result_pyplot', 'MMSegInferencer',
    'RSInferencer', 'RSImage','inference_model_1'
]
