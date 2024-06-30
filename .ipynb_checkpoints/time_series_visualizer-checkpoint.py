import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
#df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'])
df.set_index('date')
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]
months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df['date'], df['value'])
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set(xlabel="Date", ylabel="Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig



def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar['date'].dt.month_name(locale='English')
    df_bar['year'] = df_bar['date'].dt.year
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax = sns.barplot(x="year", hue="month", y="value", data=df_bar, hue_order=months, ci=None)
    ax.set(xlabel="Years", ylabel="Average Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

    #fig = sns.catplot(x='Year', y='value', hue='Month', data=df, kind='bar').fig
    #fig = sns.barplot(data=df_bar, x='Year', y='value')
    # Draw bar plot
    # Save image and return fig (don't change this part)
    #fig.savefig('bar_plot.png')
    #return fig
    #df_bar = df.copy()
    #df_bar["year"] = df.index.year.values
    #df_bar["month"] = df.index.month_name()


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
