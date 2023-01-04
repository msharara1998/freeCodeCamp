import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")

# changing str to datetime type
df.index = pd.to_datetime(df.index, infer_datetime_format=True)

# Clean data
top_2_5 = df["value"].quantile(1 - 0.025)  # top 2.5 %
bottom_2_5 = df["value"].quantile(0.025)  # bottom 2.5 %
filter_condition = (df["value"] < top_2_5) & (df["value"] > bottom_2_5)
df = df[filter_condition]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 5))
    ax.plot(df.index, df.value)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar["month"] = df_bar.index.month_name()
    df_bar["year"] = df_bar.index.year

    df_bar = pd.DataFrame(
        df_bar.groupby(["year", "month"])
        .mean()
        .round()
        .astype(int)
    )

    # reset index
    df_bar.reset_index(inplace=True)
    df_bar.columns = ["Years", "Months", "Average Page Views"]
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8, 10))
    sns.barplot(data=df_bar,
                x="Years",
                y="Average Page Views",
                hue="Months",
                ci=None,
                ax=ax,
                palette="tab10",
                hue_order=[
                    "January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November",
                    "December"
                ])
    plt.legend(loc=2, prop={'size': 12})

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(22, 8))

    sns.boxplot(data=df_box, x="year", y="value", ax=ax[0])
    sns.boxplot(data=df_box,
                x="month",
                y="value",
                ax=ax[1],
                order=[
                    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                    "Sep", "Oct", "Nov", "Dec"
                ])

    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[0].set_xlabel("Year")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    ax[0].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig