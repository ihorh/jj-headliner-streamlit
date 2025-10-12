from __future__ import annotations

import logging
import shutil
from typing import TYPE_CHECKING, Final

import dvc
import dvc.api
import pandas as pd
import streamlit as st

from jj_headliner_streamlit.config import (
    DD,
    DVC_IMPORT_PATH,
    GITHUB_TOKEN_SECRET_KEY,
    GOOGLE_APPLICATION_CREDENTIALS,
    GOOGLE_APPLICATION_CREDENTIALS_SECRET_KEY,
    get_github_repo_url,
)

if TYPE_CHECKING:
    from pathlib import Path

LOG = logging.getLogger(__name__)

REMOTE_FILE: Final[str] = f"{DVC_IMPORT_PATH}/headlines/test-data-set.parquet"
DATA_FILE: Final[Path] = DD / "99_test" / "headlines" / "test-data-set.parquet"

if not DATA_FILE.exists():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not GOOGLE_APPLICATION_CREDENTIALS.exists():
        GOOGLE_APPLICATION_CREDENTIALS.parent.mkdir(parents=True, exist_ok=True)
        with GOOGLE_APPLICATION_CREDENTIALS.open("w") as f:
            f.write(st.secrets[GOOGLE_APPLICATION_CREDENTIALS_SECRET_KEY])
    github_token = st.secrets[GITHUB_TOKEN_SECRET_KEY]
    with (
        dvc.api.open(
            REMOTE_FILE,
            get_github_repo_url(github_token),
            remote_config={
                "credentialpath": GOOGLE_APPLICATION_CREDENTIALS.as_posix(),
            },
        ) as src,
        DATA_FILE.open("wb") as dst,
    ):
        shutil.copyfileobj(src, dst)

st.title("Hello Streamlit!")

df = pd.read_parquet(DATA_FILE)

st.dataframe(df.head(32))
