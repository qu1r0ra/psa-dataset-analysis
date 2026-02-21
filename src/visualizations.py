import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from IPython.display import display

from src.constants import (
    major_expenditure_categories,
    socio_demo_factors_list,
    socio_demo_factors,
)


def generate_stacked_bar(
    df, groupby_col, category_dict, reindex=False, title=None, figsize=(10, 6)
):
    category_labels = category_dict.keys()
    category_values = category_dict.values()

    df_grouped_summed = df.groupby(groupby_col)[list(category_values)].sum()
    df_grouped_normalized = df_grouped_summed.div(
        df_grouped_summed.sum(axis=1), axis=0
    )  # normalize values to proportions

    if isinstance(reindex, list):
        df_grouped_normalized = df_grouped_normalized.reindex(reindex)
    elif reindex:
        df_grouped_normalized = df_grouped_normalized.sort_index()

    ax = df_grouped_normalized.plot(
        kind="bar", stacked=True, figsize=figsize, colormap="tab20"
    )

    ax.set_title(title or f"Stacked Bar Chart by {groupby_col}")
    ax.set_xlabel(groupby_col)
    ax.set_ylabel("Proportion")
    ax.legend(
        title="Expenditure Category", labels=category_labels, bbox_to_anchor=(1.05, 1)
    )

    plt.tight_layout()
    plt.show()


def generate_summary_table(df, factor_title, factor_col):
    df_grouped_summed = df.groupby(factor_col)[
        list(major_expenditure_categories.values())
    ].sum()
    df_grouped_normalized = df_grouped_summed.div(
        df_grouped_summed.sum(axis=1), axis=0
    )  # normalize values to proportions

    summary_df = pd.DataFrame()

    for category_title, category_col in major_expenditure_categories.items():
        col_vals = df_grouped_normalized[category_col]

        summary_df.loc[category_title, "Mean"] = col_vals.mean()
        summary_df.loc[category_title, "Std. Dev."] = col_vals.std()
        summary_df.loc[category_title, "Group with Min %"] = col_vals.idxmin()
        summary_df.loc[category_title, "Min %"] = col_vals.min()
        summary_df.loc[category_title, "Group with Max %"] = col_vals.idxmax()
        summary_df.loc[category_title, "Max %"] = col_vals.max()
        summary_df.loc[category_title, "Range"] = col_vals.max() - col_vals.min()

    summary_df = summary_df[
        [
            "Mean",
            "Std. Dev.",
            "Group with Min %",
            "Min %",
            "Group with Max %",
            "Max %",
            "Range",
        ]
    ]

    try:
        display(
            summary_df.style.set_caption(
                f"Numerical Summaries of Major Expenditure Categories Across '{factor_title}' Groups"
            ).format(
                {
                    "Mean": "{:.2%}",
                    "Std. Dev.": "{:.2%}",
                    "Min %": "{:.2%}",
                    "Max %": "{:.2%}",
                    "Range": "{:.2%}",
                }
            )
        )
    except NameError:
        print(summary_df)


def generate_stacked_bar_summary_table(df, n, reindex=False):
    if n >= len(socio_demo_factors):
        raise ValueError(
            f"Value must be in the range [0, {len(socio_demo_factors) - 1}]"
        )

    factor_title = socio_demo_factors_list[n][0]
    factor_col = socio_demo_factors_list[n][1]

    # visualization
    generate_stacked_bar(
        df,
        groupby_col=factor_col,
        category_dict=major_expenditure_categories,
        reindex=reindex,
        title=f"Proportional Breakdown of Spending by {factor_title}",
    )

    # numerical summaries
    generate_summary_table(df, factor_title=factor_title, factor_col=factor_col)


def generate_scatter(data, x, y, log_x=False, log_y=False, title=None):
    sns.scatterplot(data=data, x=x, y=y)

    if log_x:
        plt.xscale("log")
    if log_y:
        plt.yscale("log")

    plt.title(title or f"{x} vs. {y}")
    plt.xlabel(x)
    plt.ylabel(y)

    plt.tight_layout()
    plt.show()


def generate_numeric_col_summary(series, title=None):
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=series)
    plt.title(title or f"Boxplot of '{series.name}'")
    plt.xlabel(series.name)
    plt.tight_layout()
    plt.show()

    print(f"----- Numerical summaries of column '{series.name}' -----")
    print(f"Mean    : {series.mean():.2f}")
    print(f"Median  : {series.median():.2f}")
    print(f"Std Dev : {series.std():.2f}")


def visualize_crosstab_by_cluster(df, grouping, reindex=None):
    code_to_label = {v: k for k, v in socio_demo_factors.items()}
    crosstab = (
        pd.crosstab(df["Cluster"], df[grouping], normalize="index").reindex(
            columns=reindex
        )
        * 100
    )
    x_label = code_to_label.get(grouping, grouping)

    # Display heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(crosstab, annot=True, fmt=".2f", cmap="Blues")
    plt.title(f"Cluster vs. {x_label}")
    plt.ylabel("Cluster")
    plt.xlabel(x_label)
    plt.show()
