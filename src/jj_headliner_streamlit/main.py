import pandas as pd
import streamlit as st

st.title("Hello Streamlit!")

df = pd.read_parquet(".datarepo/99_test/headlines/test-data-set.parquet")

st.dataframe(df.head(32))
