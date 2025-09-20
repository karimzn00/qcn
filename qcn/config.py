from pathlib import Path
import toml


DEFAULT_CONFIG = {
    "types": [
        "feat","fix","docs","style","refactor","perf","test","chore","ci"
    ],
    "max_summary_length": 72,
    "history_file": ".qcn_history.json"
}




def find_repo_root():
    # lazy import to avoid requiring git during import-time
    from .git_utils import git_root
    return git_root()




def load_config(repo_root: str | Path):
    repo_root = Path(repo_root)
    cfg_path = repo_root / ".qcnrc"
    if cfg_path.exists():
        try:
            return toml.loads(cfg_path.read_text())
        except Exception:
            return DEFAULT_CONFIG
    return DEFAULT_CONFIG




def write_default_config(repo_root: str | Path):
    cfg_path = Path(repo_root) / ".qcnrc"
    if cfg_path.exists():
        return False
    cfg_path.write_text(toml.dumps(DEFAULT_CONFIG))
    return True
