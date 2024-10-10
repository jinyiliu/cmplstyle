import os
import matplotlib.pyplot as plt
from .utils import onecol_wth, median_wth, fullpg_wth, cm2inch
from .colors import register_colors


def use_style() -> None:
    from _color_data import CH_BASE_COLORS, CH_TRAD_COLORS
    register_colors(CH_BASE_COLORS, CH_TRAD_COLORS)

    pkgpath = os.path.dirname(__file__)
    plt.style.use(os.path.join(pkgpath, 'mplstyle.rc'))
