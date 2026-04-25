from __future__ import annotations

"""
TI2Vid-only init for ltx_pipelines.

Оставляем только то, что реально нужно для TI2Vid пайплайнов и shim-модуля ti2vid_onestage.
Никаких импортов a2vid / Gemma / audio здесь быть не должно.
"""

# ЕслиDistilledPipeline действительно нужен для твоего кода – можно оставить.
# Но для чистого TI2Vid через CLI это не обязательно.
# from ltx_pipelines.distilled import DistilledPipeline  # noqa: F401

# Обеспечиваем, что подмодуль с CLI существует (мы его уже создали).
from ltx_pipelines import ti2vid_onestage  # noqa: F401

__all__ = [
    # "DistilledPipeline",
    "ti2vid_onestage",
]
