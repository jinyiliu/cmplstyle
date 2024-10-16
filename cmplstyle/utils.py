# Figure widths in cm for A&A journal
# See https://www.aanda.org/for-authors/latex-issues/figures
onecol_wth: float = 8.8
median_wth: float = 12.0
fullpg_wth: float = 18.0

def cm2inch(*args: float | int) -> float | tuple[float, ...]:
    if len(args)==1:
        return args[0] / 2.54
    else:
        return tuple(x / 2.54 for x in args)
