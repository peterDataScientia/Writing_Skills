#!/usr/bin/env python3
"""Render a premium, reproducible academic Gantt chart from a CSV schedule."""
import argparse
import calendar
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
import pandas as pd

PALETTE = ["#123B5D", "#1E5A8A", "#2B79B7", "#3C8DAD",
           "#4A6FA5", "#256D85", "#1B4965"]

def read_schedule(path):
    df = pd.read_csv(path)
    required = {"Task", "StartMonthIndex", "DurationMonths"}
    if not required.issubset(df):
        raise ValueError("Missing required columns: " + ", ".join(sorted(required - set(df))))
    if df.empty or df["Task"].isna().any() or not df["Task"].astype(str).str.strip().all():
        raise ValueError("Every activity needs a non-empty name")
    for col in ("StartMonthIndex", "DurationMonths"):
        num = pd.to_numeric(df[col], errors="raise")
        if num.isna().any() or (num % 1 != 0).any():
            raise ValueError(col + " must contain integers")
        df[col] = num.astype(int)
    if (df.StartMonthIndex < 0).any() or (df.DurationMonths < 1).any():
        raise ValueError("StartMonthIndex >= 0; DurationMonths >= 1")
    return df

def get_months(start, count):
    try:
        year, month = map(int, start.split("-"))
        if len(start) != 7 or month < 1 or month > 12:
            raise ValueError
    except ValueError:
        raise ValueError("Start must be YYYY-MM") from None
    return [f"{calendar.month_abbr[(month - 1 + i) % 12 + 1]} {year + (month - 1 + i)//12}" for i in range(count)]

def draw(df, labels, destination):
    if ((df.StartMonthIndex + df.DurationMonths) > len(labels)).any():
        raise ValueError("An activity extends outside the selected months")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                         "axes.linewidth": 2, "pdf.fonttype": 42,
                         "svg.fonttype": "none", "axes.facecolor": "white",
                         "figure.facecolor": "white", "savefig.facecolor": "white"})
    n = len(df)
    fig, ax = plt.subplots(figsize=(285/25.4, max(102, 42+n*12)/25.4))
    ax.set_xlim(0, len(labels))
    ax.set_ylim(-.5, n-.5)
    for c in range(len(labels)):
        ax.axvspan(c, c+1, color="#EEF4FB" if c % 2 == 0 else "white", zorder=0)
    for c in range(len(labels)+1):
        ax.axvline(c, color="#DCE5F0", linewidth=1.2, zorder=1)
    for idx, row in df.iterrows():
        y = n-idx-1
        if idx % 2 == 0:
            ax.axhspan(y-.5, y+.5, color="#F7FAFC", alpha=.65, zorder=0)
        bar = FancyBboxPatch((int(row.StartMonthIndex)+.1, y-.28),
                             int(row.DurationMonths)-.2, .56,
                             boxstyle="round,pad=0.02,rounding_size=0.08",
                             linewidth=0, facecolor=PALETTE[idx % len(PALETTE)],
                             zorder=4)
        bar.set_path_effects([pe.SimplePatchShadow(offset=(1.2,-1.2), alpha=.13),
                              pe.Normal()])
        ax.add_patch(bar)
    ax.set_xticks([i+.5 for i in range(len(labels))], labels=labels)
    ax.xaxis.tick_top()
    ax.set_yticks(range(n), labels=list(reversed(df.Task.astype(str).tolist())))
    ax.tick_params(axis="both", width=2, length=6, direction="out", pad=9,
                   labelsize=12)
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontweight("bold")
    for side in ("left", "top"):
        ax.spines[side].set_visible(True)
        ax.spines[side].set_linewidth(2)
        ax.spines[side].set_color("black")
    for side in ("right", "bottom"):
        ax.spines[side].set_visible(False)
    ax.grid(False)
    ax.set_xlabel("")
    ax.set_ylabel("")
    fig.subplots_adjust(left=.46, right=.985, top=.79, bottom=.08)
    dest = Path(destination)
    dest.parent.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf", "svg"):
        fig.savefig(dest.with_suffix("."+ext), dpi=600,
                    bbox_inches="tight", pad_inches=.08)
    plt.close(fig)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--start", default="2026-10")
    p.add_argument("--months", type=int, default=6)
    p.add_argument("--out", default="research_timeline")
    args = p.parse_args()
    if not 1 <= args.months <= 24:
        p.error("--months must be 1–24")
    draw(read_schedule(args.csv), get_months(args.start, args.months), args.out)
