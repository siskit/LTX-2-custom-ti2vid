from __future__ import annotations

"""
Entry point shim so that:

    python -m ltx_pipelines.ti2vid_onestage ...

делает то же самое, что и оригинальный TI2Vid one-stage CLI
из ti2vid_one_stage.main(...).
"""

from ltx_pipelines.ti2vid_one_stage import main as _ti2vid_one_stage_main


def main() -> None:
    """
    Делегируем выполнение в реальный one-stage TI2Vid пайплайн.
    Все аргументы командной строки читает сам _ti2vid_one_stage_main.
    """
    _ti2vid_one_stage_main()


if __name__ == "__main__":
    main()
