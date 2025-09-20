import subprocess




def git_root():
    """Return the git repo root (raises RuntimeError if not a repo)."""
    res = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError("Not in a git repository (run this inside a git repo).")
    return res.stdout.strip()




def git_commit_from_file(msgfile: str) -> bool:
    """Run: git commit -F <msgfile> and return True on success."""
    res = subprocess.run(["git", "commit", "-F", msgfile])
    return res.returncode == 0




def get_head_commit() -> str | None:
    res = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True)
    if res.returncode == 0:
        return res.stdout.strip()
    return None