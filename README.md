# cmplstyle

A Python package providing matplotlib style for scientific plotting with traditional Chinese color palette.

## Installation
You can install the package using pip:
```bash
pip install cmplstyle
```

## Features

- A collection of 365 traditional Chinese colors.
- Optmised matplotlib style for scientific plotting.
- Small handy functions for helping scientific plotting.

## Traditional Chinese Colors (TCC)

Our color collection is sourced from the reference [《中国传统色：国民版色卡》](https://www.douban.com/doubanapp/dispatch/book/35951952?dt_dapp=1) by 郭浩, featuring hues widely used in traditional Chinese art and design. See [here](https://jinyiliu.github.io/2025/08/13/cmplstyle/TCC_ncols_5.pdf) for a complete color reference.

The color names are in Chinese and their HEX color values are stored in the `cmplstyle.TCC` dictionary. Once the package is imported, the colors can be accessed easily by their names. For example,
```python
import cmplstyle
import seaborn
seaborn.palplot(["群青", "西子", "胭脂", "桂黄", "苍苍", "青骊", "官绿", "米汤娇", "沧浪", "梅子青", "石榴裙"])
```
will plot a color palette with the specified colors in the list:

![Example TCC Palette](https://raw.githubusercontent.com/jinyiliu/cmplstyle/main/cmplstyle/assets/example_tcc_palette.png)

For readers unfamiliar with Chinese characters, the colors can also be accessed by the numbered indices (`TCC_1` through `TCC_365`). See [here](https://jinyiliu.github.io/2025/08/13/cmplstyle/TCC_indexed_ncols_5.pdf) for a complete indexed color reference.

The package provides conversions between Chinese color names and their `TCC_` indexed names: use `cmplstyle.color_index_to_name` to retrieve the Chinese name for a given `TCC_` index, and `cmplstyle.index_name_to_color` to find the corresponding `TCC_` index for a Chinese color name.

## Built-in Matplotlib style

The package includes a built-in Matplotlib style. Activate it with:
```python
import cmplstyle
cmplstyle.use_builtin_mplstyle()
```

## LICENSE
This package is licensed under the [MIT License](https://github.com/jinyiliu/cmplstyle/blob/main/LICENSE).
