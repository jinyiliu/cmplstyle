# cmplstyle

A Python package providing matplotlib style for scientific plotting with traditional Chinese color palette.

## Installation
You can install the package using pip:
```bash
pip install cmplstyle
```

## Features

- A collection of 365 available traditional Chinese colors.
- Optmised matplotlib style for scientific plotting.

## Traditional Chinese Colors (TCC)

Our color collection is sourced from the reference [《中国传统色：国民版色卡》](https://www.douban.com/doubanapp/dispatch/book/35951952?dt_dapp=1) by 郭浩, featuring hues widely used in traditional Chinese art and design. See [here](https://jinyiliu.github.io/2025/08/13/cmplstyle/TCC_ncols_5.pdf) for a complete color reference.

The color names are in Chinese. Once the package is imported, the colors can be accessed by their names. For example,
```python
import cmplstyle
import seaborn
seaborn.palplot(["群青", "西子", "胭脂", "桂黄", "苍苍", "青骊", "官绿", "米汤娇", "沧浪", "梅子青", "石榴裙"])
```
will plot a color palette with the specified colors in the list:

![Example TCC Palette](./cmplstyle/assets/example_tcc_palette.png)
