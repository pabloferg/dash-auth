def prettify(fig):
    fig.update_layout(template="simple_white")

    fig.layout.font = dict(family="Helvetica",
                           size=12,
                           color='rgb(20,20,20)'
                           )
    fig.update_xaxes(tickfont=dict(family='Helvetica',
                                   color='rgb(20,20,20)',
                                   size=12))

    fig.update_xaxes(showline=True, linewidth=0.7, linecolor='rgb(20,20,20)',
                     tickfont=dict(family='Helvetica', color='rgb(20,20,20)', size=12))
    fig.update_yaxes(showline=True, linewidth=0.7, linecolor='rgb(20,20,20)',
                     tickfont=dict(family='Helvetica', color='rgb(20,20,20)', size=12))

    return fig