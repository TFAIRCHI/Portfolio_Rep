import plotly.express as px

fig = px.bar(x=["A", "B", "C"], y=[4, 7, 1], title="Bar Chart")
fig.write_html("plot.html")