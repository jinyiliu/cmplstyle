import matplotlib.colors as mpc
from matplotlib.typing import ColorType
from _color_data import BASE_COLORS_EN_TO_CH, TRAD_COLORS_EN_TO_CH

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
