import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

import plotly.io as pio
pio.renderers.default = "browser"


# Veri
df_gap = px.data.gapminder()
df_bar = df_gap.query("year==1997").groupby("continent", as_index=False)["pop"].sum()


# 2x2 Dashboard
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("GSYİH vs Yaşam Süresi",
                    "Kıta Bazlı Nüfus (1997)",
                    "Yaşam Süresi Dağılımı (1997)",
                    "Yaşam Süresi & GSYİH (Nüfus Boyutlu)"),
    vertical_spacing=0.15,
    horizontal_spacing=0.1
)

# 1) Scatter Plot: GDP vs LifeExp
fig.add_trace(
    go.Scatter(
        x=df_gap.query("year==1997")["pop"],
        y=df_gap.query("year==1997")["lifeExp"],
        mode='markers',
        marker=dict(color='violet', size=10),
        name='Nüfus...'
    ),
    row=1, col=1
)


# 2) Bar Plot: Kıta Bazlı Nüfus
fig.add_trace(
    go.Bar(
        x=df_bar["continent"],
        y=df_bar["pop"],
        marker_color='orange',
        name='Kıta Nüfusu'
    ),
    row=1, col=2
)


# 3) Histogram: Yaşam Süresi
fig.add_trace(
    go.Histogram(
        x=df_gap.query("year==1997")["lifeExp"],
        nbinsx=40,
        marker_color='magenta',
        name='Yaşam Süresi Dağılımı'
    ),
    row=2, col=1
)



# 4) Scatter + Size: Popülasyon
fig.add_trace(
    go.Scatter(
        x=df_gap.query("year==1997")["gdpPercap"],
        y=df_gap.query("year==1997")["lifeExp"],
        mode='markers',
        marker=dict(
            color='violet',
            size=df_gap.query("year==1997")["pop"]/500000,
            sizemode='area',
            sizeref=2.*max(df_gap.query("year==1997")["pop"]/500000)/(50.**2),
            sizemin=6
        ),
        name='Yaşam Süresi & GDP (Nüfus)'
    ),
    row=2, col=2
)

# Layout
fig.update_layout(
    showlegend=False,
    title_text="Gapminder Veri Görselleştirme",
    height=900, width=1100
)



# Eksen başlıkları
fig.update_xaxes(title_text="Nüfus", row=1, col=1)
fig.update_yaxes(title_text="Yaşam Süresi", row=1, col=1)

fig.update_xaxes(title_text="Kıta", row=1, col=2)
fig.update_yaxes(title_text="Toplam Nüfus", row=1, col=2)

fig.update_xaxes(title_text="Yaşam Süresi", row=2, col=1)
fig.update_yaxes(title_text="Sıklık", row=2, col=1)

fig.update_xaxes(title_text="Kişi Başına GSYİH", row=2, col=2)
fig.update_yaxes(title_text="Yaşam Süresi", row=2, col=2)


fig.show()