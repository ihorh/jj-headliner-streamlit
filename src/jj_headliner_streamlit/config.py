from pathlib import Path
from typing import Final

import jj_headliner_streamlit

PROJECT_ROOT: Final[Path] = Path(jj_headliner_streamlit.__file__).parent.parent.parent
DD: Final[Path] = PROJECT_ROOT / ".datarepo"

DVC_IMPORT_REPO: Final[str] = "https://github.com/ihorh/jj-headliner.git"
DVC_IMPORT_PATH: Final[str] = ".datarepo/99_test"

GOOGLE_APPLICATION_CREDENTIALS_SECRET_KEY: Final[str] = "GOOGLE_APPLICATION_CREDENTIALS"  # noqa: S105
GOOGLE_APPLICATION_CREDENTIALS: Final[Path] = PROJECT_ROOT / "config" / "jj-headliner-dvc-registry-read.secret.json"
