from __future__ import annotations

from typing import TYPE_CHECKING, Final

import pandas as pd
import streamlit as st

from jj_headliner_streamlit.config import (
    DD,
    DVC_IMPORT_PATH,
)
from jj_headliner_streamlit.data import dvc_import_data_file

if TYPE_CHECKING:
    from pathlib import Path


DATA_FILE: Final[Path] = dvc_import_data_file(
    DD / "99_test" / "headlines" / "test-data-set.parquet",
    f"{DVC_IMPORT_PATH}/headlines/test-data-set.parquet",
)

st.title("Hello Streamlit!")

df = pd.read_parquet(DATA_FILE)

st.dataframe(df.head(32))
