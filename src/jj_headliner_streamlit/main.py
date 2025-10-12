from __future__ import annotations

import logging
import subprocess
from typing import TYPE_CHECKING, Final

import pandas as pd
import streamlit as st

from jj_headliner_streamlit.config import (
    DD,
    DVC_IMPORT_PATH,
    GOOGLE_APPLICATION_CREDENTIALS,
    GOOGLE_APPLICATION_CREDENTIALS_SECRET_KEY,
)

if TYPE_CHECKING:
    from pathlib import Path

LOG = logging.getLogger(__name__)


DATA_FILE: Final[Path] = DD / "99_test" / "headlines" / "test-data-set.parquet"

if not DATA_FILE.exists():
    if not GOOGLE_APPLICATION_CREDENTIALS.exists():
        with GOOGLE_APPLICATION_CREDENTIALS.open("w") as f:
            f.write(st.secrets[GOOGLE_APPLICATION_CREDENTIALS_SECRET_KEY])
    subprocess.run(["uv", "run", "dvc", "update", DVC_IMPORT_PATH], check=True)  # noqa: S603, S607

st.title("Hello Streamlit!")

df = pd.read_parquet(DATA_FILE)

st.dataframe(df.head(32))
