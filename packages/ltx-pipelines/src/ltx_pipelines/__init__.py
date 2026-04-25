from __future__ import annotations

"""
LTX-2 Pipelines (TI2Vid-only fork).

Оставляем только пайплайны, которые реально нужны для TI2Vid и связанных задач.
Никаких импортов a2vid / audio-пайплайнов отсюда не делаем, чтобы избежать
тяжёлых зависимостей (Gemma/torchvision) в окружении Modal.
"""

from ltx_pipelines.distilled import DistilledPipeline
from ltx_pipelines.ic_lora import ICLoraPipeline
from ltx_pipelines.keyframe_interpolation import KeyframeInterpolationPipeline
from ltx_pipelines.retake import RetakePipeline
from ltx_pipelines.ti2vid_one_stage import TI2VidOneStagePipeline
from ltx_pipelines.ti2vid_two_stages import TI2VidTwoStagesPipeline

# Shim-модуль для CLI: python -m ltx_pipelines.ti2vid_onestage
from ltx_pipelines import ti2vid_onestage  # noqa: F401

__all__ = [
    "DistilledPipeline",
    "ICLoraPipeline",
    "KeyframeInterpolationPipeline",
    "RetakePipeline",
    "TI2VidOneStagePipeline",
    "TI2VidTwoStagesPipeline",
    "ti2vid_onestage",
]
