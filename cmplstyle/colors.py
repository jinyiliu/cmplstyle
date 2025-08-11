import os
from matplotlib.typing import ColorType

def register_colors(*color_dicts: dict[str, ColorType]):
    """Register custom colors to matplotlib's color map."""
    from matplotlib import colors
    for color_dict in color_dicts:
        colors._colors_full_map.update(color_dict)


def plot_colortable(
        colors_dict: dict[str, ColorType],
        ncols: int=5,
        savepath: str | None=None,
):
    """Plot a color table for the given colors."""
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    from matplotlib.patches import FancyBboxPatch, BoxStyle
    from cmplstyle.utils import cm2inch

    plt.rcParams["text.usetex"] = False

    names = list(colors_dict.keys())

    cell_width = 2.6 # cm
    cell_height = 1.0
    swatch_width = 0.6
    swatch_height = 0.6
    gap_swatch_text = 0.15
    x_offset = 0.1
    y_offset = 0.1
    margin = 0.5

    n = len(colors_dict)
    nrows = n // ncols + (n % ncols > 0)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin

    fig, ax = plt.subplots(figsize=cm2inch(width, height))
    fig.subplots_adjust(
        left=margin / width,
        bottom=margin / height,
        right=1 - margin / width,
        top=1 - margin / height,
    )
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(0, cell_height * nrows)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_axis_off()
    ax.invert_yaxis()

    for i, name in enumerate(names):
        row = i // ncols
        col = i % ncols

        swatch_start_x = cell_width * col + x_offset
        swatch_start_y = cell_height * row + y_offset
        text_pos_x = cell_width * col + swatch_width + gap_swatch_text + x_offset
        text_pos_y = swatch_start_y + y_offset + 0.24

        ax.text(
            x=text_pos_x,
            y=text_pos_y,
            s=name,
            fontsize=11,
            horizontalalignment="left",
            verticalalignment="center",
            fontproperties=FontProperties(
                fname=os.path.join(
                    os.path.dirname(__file__),
                    "fonts/SourceHanSerifSC-Medium.otf")
                ),
            )

        ax.add_patch(
            FancyBboxPatch(
                xy=(swatch_start_x, swatch_start_y),
                width=swatch_width,
                height=swatch_height,
                facecolor=colors_dict[name],
                edgecolor="0.7",
                boxstyle=BoxStyle(
                    stylename="Round",
                    pad=0.0,
                    rounding_size=0.1,
                )
            )
        )

        if savepath:
            fig.savefig(savepath, bbox_inches="tight")