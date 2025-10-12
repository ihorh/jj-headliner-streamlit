from __future__ import annotations

from typing import TYPE_CHECKING

import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError

if TYPE_CHECKING:
    from pathlib import Path


@st.cache_resource
def ensure_fresh_gcp_creds_file_exists(path: Path, secrets_dict_key: str) -> Path:
    try:
        gcp_creds = st.secrets.get(secrets_dict_key)
    except StreamlitSecretNotFoundError:
        gcp_creds = None

    if not gcp_creds:
        if path.exists() and not gcp_creds: # ! local environment
            return path
        msg = f"Neither {path} nor {secrets_dict_key} are set"
        raise ValueError(msg)

    if path.exists():
        path.unlink()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        f.write(gcp_creds)
    return path
