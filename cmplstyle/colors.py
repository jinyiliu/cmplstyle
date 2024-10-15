import os
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mpc
from matplotlib.typing import ColorType
from matplotlib.patches import Rectangle
from matplotlib.font_manager import FontProperties
from ._color_data import BASE_COLORS_EN_TO_CH, TRAD_COLORS_EN_TO_CH
from .utils import cm2inch

COLORS_EN_TO_CH = BASE_COLORS_EN_TO_CH.update(TRAD_COLORS_EN_TO_CH)

def register_colors(*color_dicts: dict[str, ColorType]) -> None:
    for color_dict in color_dicts:
        mpc._colors_full_map.update(color_dict)


def get_chinese_name(*en_color_names: str) -> tuple[str, ...]:
    ret = []
    for en_color_name in en_color_names:
        if en_color_name in COLORS_EN_TO_CH.keys():
            ret.append(COLORS_EN_TO_CH[en_color_name])
        else:
            raise ValueError(f"Unknown color name: {en_color_name}")
    return tuple(ret)


def make_colorcard(colors: dict[str, str], textcolor: ColorType='#1a0404', ncols: int=12, sort_colors=True):
    cell_width = 1.0 # cm
    cell_height = 3.0
    gap = 0.2
    margin = 0.5

    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mpc.rgb_to_hsv(mpc.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin - gap
    height = cell_height * nrows + 2 * margin - gap

    fig, ax = plt.subplots(figsize=cm2inch(width, height))
    fig.subplots_adjust(left=margin/width, right=(width-margin+gap)/width,
                        bottom=margin/height, top=(height-margin+gap)/height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(0, cell_height * nrows)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i // ncols
        col = i % ncols

        x = cell_width * col
        y = cell_height * (nrows - row - 1)

        x_text = x + (cell_width - gap) / 2
        y_text = cell_height * (nrows - row) - gap - 0.25

        ax.add_patch(
            Rectangle(xy=(x, y), width=cell_width-gap,
                      height=cell_height-gap, facecolor=colors[name])
        )

        ax.text(x_text, y_text, '\n'.join(name), fontsize=10,
                color=textcolor,
                horizontalalignment='center',
                verticalalignment='top',
                fontproperties=FontProperties(
                    fname=os.path.join(os.path.dirname(__file__),
                                       "fonts/SourceHanSerifSC-SemiBold.otf"))
        )

    return fig