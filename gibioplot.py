import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display,Image
import plotly.graph_objects as go
from kaleido.scopes.plotly import PlotlyScope
import plotly.io as pio




# Colores
ORANGE = '#ffa100'
L_BLUE_DOTS = '#00a5ff'
L_BLUE_BOX = '#00a2a5'
L_YELOW = '#ffffa5'
L_GREEN = '#9ade00'
BLACK_GRID = '#2f2933'
PLOT_BKGROUND = '#364e59'
COLAB_BKGROUND = '#383838'
TRANSPARENT = '#00000000'


def boxplot(dataset, title, render="colab", filename='figure.png'):
    fig = go.Figure()
    fig.add_trace(go.Box(x=dataset,
                         name=str(title),
                         fillcolor=L_BLUE_BOX,
                         marker_color=L_YELOW,
                         marker_size=10,
                         line_width=1.5,
                         boxmean=True))
    fig.update_layout(height=250,
                      paper_bgcolor=COLAB_BKGROUND,
                      font={'color': ORANGE},
                      margin={'l': 50,
                              't': 5,
                              'b': 30},
                      plot_bgcolor=PLOT_BKGROUND,
                      xaxis={'gridcolor': BLACK_GRID,
                             'zerolinecolor': BLACK_GRID},
                      yaxis={'autorange': True,
                             'showgrid': True,
                             'zeroline': True,
                             'dtick': 5,
                             'gridcolor': BLACK_GRID,
                             'gridwidth': 1,
                             'zerolinecolor': BLACK_GRID,
                             'zerolinewidth': 4},
                      showlegend=False,
                      hovermode='x',
                      hoverlabel=dict(
                          bgcolor=PLOT_BKGROUND,
                          font_size=14,
                          font_family="verdana")
                      )
    if render == 'png':
        scope = PlotlyScope()
        with open(filename, "wb") as f:
            f.write(scope.transform(fig, format="png"))
        display(Image(filename=filename))
    else:
        fig.show()

def plot_dot_line(dot_x, dox_y, y_hat, title="Precio por m2", y_label="Precio [miles de pesos]", x_label='m2', legend_x='Predicción', legend_y='Precio publicado'):
    '''Graficador de tendencia'''
    # Inicializamos el gráfico
    fig = plt.figure(figsize=(16, 9))
    sns.set_style("darkgrid", {'grid.linestyle': '--'})
    # Color en los axis
    mpl.rcParams['text.color'] = ORANGE
    mpl.rcParams['axes.labelcolor'] = ORANGE
    mpl.rcParams['xtick.color'] = ORANGE
    mpl.rcParams['ytick.color'] = ORANGE
    mpl.rcParams["legend.facecolor"] = PLOT_BKGROUND + 'aa'
    fig.patch.set_facecolor(TRANSPARENT)
    # Información del gráfico
    ax1 = fig.add_subplot()
    ax = sns.scatterplot(dot_x, dox_y/1000, color=L_BLUE_DOTS, ax=ax1)
    ax = sns.lineplot(dot_x, y_hat/1000, color=L_GREEN, linewidth=3, ax=ax1)
    ax.set_title(title, fontsize=20)
    ax.set_ylabel(y_label, fontsize=18)
    ax.set_xlabel(x_label, fontsize=18)
    ax.set_facecolor(PLOT_BKGROUND + 'aa')
    plt.legend((legend_x, legend_y), prop={'size': 15})


def plot_meter(value, reference=10, render="colab", filename='figure.png',title='Error medio'):
    '''Medidor tipo `barra horizontal` de una sola magnitud'''
    fig = go.Figure(go.Indicator(
        mode="number+gauge+delta",
        gauge={'shape': "bullet",
               'bgcolor': PLOT_BKGROUND,
               'bar': {'color': L_GREEN}},
        align='center',
        value=value,
        delta={'reference': reference},
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "<b style = 'color: "+ORANGE+";'>"+ title +"</b>",
               'font': {"size": 18}}))
    fig.update_layout(height=50,
                      paper_bgcolor=COLAB_BKGROUND,
                      font={'color': ORANGE},
                      margin={'l': 150,
                              't': 0,
                              'b': 0})
    if render == 'png':
        scope = PlotlyScope()
        with open(filename, "wb") as f:
            f.write(scope.transform(fig, format="png"))
        display(Image(filename=filename))
    else:
        fig.show()


