import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
st = px.scatter(df, x = "date", y = "cases", color = "country", size = "cases", size_max = 60)
st.show()