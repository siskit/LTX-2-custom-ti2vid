"""
Shim module so that `python -m ltx_pipelines.ti2vid_onestage`
and `import ltx_pipelines.ti2vid_onestage` work for CI and Modal.

Здесь мы просто прокидываем вызов в реальный TI2Vid CLI/функцию.
"""

from __future__ import annotations

import sys


def main() -> None:
    """
    Основной entrypoint для `python -m ltx_pipelines.ti2vid_onestage`.
    Подключи здесь реальную функцию/CLI из пакета.
    """
    # TODO: подстрой этот импорт под реальный модуль в твоём репо.
    # Примеры:
    #   from ltx_pipelines.cli import ti2vid_onestage_main
    #   ti2vid_onestage_main()
    #
    #   или
    #   from ltx_pipelines.video import main as ti2vid_main
    #   ti2vid_main()
    #
    # Временно сделаем заглушку, чтобы CI хотя бы проходил импорт.
    print("ti2vid_onestage shim main() called", file=sys.stderr)


if __name__ == "__main__":
    main()
