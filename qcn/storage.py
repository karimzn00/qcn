from pathlib import Path
import json
from datetime import datetime




def history_path(repo_root: str | Path):
    return Path(repo_root) / ".qcn_history.json"




def append_history(repo_root: str | Path, message: str, commit_hash: str | None = None):
    p = history_path(repo_root)
    if p.exists():
        try:
            data = json.loads(p.read_text())
        except Exception:
            data = []
    else:
        data = []
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "message": message,
        "commit": commit_hash,
    }
    data.append(entry)
    p.write_text(json.dumps(data, indent=2))

def read_history(repo_root: str | Path):
    p = history_path(repo_root)
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text())
    except Exception:
        return []
