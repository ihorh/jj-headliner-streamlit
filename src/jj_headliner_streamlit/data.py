from __future__ import annotations

from shutil import copyfileobj
from typing import TYPE_CHECKING

import dvc.api
import streamlit as st

from jj_headliner_streamlit.config import GITHUB_TOKEN_SECRET_KEY, GOOGLE_APPLICATION_CREDENTIALS, get_github_repo_url

if TYPE_CHECKING:
    from pathlib import Path


@st.cache_resource
def dvc_import_data_file(data_file: Path, remote_path: str) -> Path:
    if data_file.exists():
        return data_file
    data_file.parent.mkdir(parents=True, exist_ok=True)
    github_token = st.secrets[GITHUB_TOKEN_SECRET_KEY]
    with (
        dvc.api.open(
            remote_path,
            get_github_repo_url(github_token),
            mode="rb",
            remote_config={
                "credentialpath": GOOGLE_APPLICATION_CREDENTIALS.as_posix(),
            },
        ) as src,
        data_file.open("wb") as dst,
    ):
        copyfileobj(src, dst)
    return data_file
