import click
import tempfile
import sys
from pathlib import Path
from .config import load_config, write_default_config, find_repo_root
from .git_utils import git_root, git_commit_from_file, get_head_commit
from .storage import append_history, read_history
from .validators import validate_commit_message


@click.group()
def main():
    """Quick Commit Note - interactive commit builder and linter."""
    pass




@main.command()
def init():
    """Create a default .qcnrc in the repo root."""
    repo_root = git_root()
    ok = write_default_config(repo_root)
    if ok:
        click.echo("Created .qcnrc with defaults.")
    else:
        click.echo(".qcnrc already exists.")

@main.command()
def new():
    """Interactive commit builder. Optionally runs git commit for you."""
    repo_root = git_root()
    cfg = load_config(repo_root)
    types = cfg.get("types", [])


    # choose type
    type_choice = click.prompt("Select type", type=click.Choice(types))


    scope = click.prompt("Scope (optional)", default="", show_default=False)


    subject = click.prompt("Short description (subject)")


    click.echo("\n(Edit an extended body in your $EDITOR if you want. Close editor to continue.)")
    body = click.edit()
    if body is None:
        body = ""


    summary = f"{type_choice}{f'({scope})' if scope else ''}: {subject}"
    full_msg = summary + ("\n\n" + body.strip() if body.strip() else "")


    ok, errors = validate_commit_message(full_msg, cfg)
    if not ok:
        click.echo("Commit message failed lint:\n", err=True)
        for e in errors:
            click.echo(f" - {e}")
        if not click.confirm("Proceed anyway? (force commit)"):
            sys.exit(1)


    click.echo("\n---\nCommit message preview:\n")
    click.echo(full_msg)
    click.echo("\n---")


    if click.confirm("Run git commit now with this message?", default=True):
        tf = tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".msg")
        tf.write(full_msg)
        tf.flush()
        tf.close()
        ok = git_commit_from_file(tf.name)
        if ok:
            commit = get_head_commit()
            append_history(repo_root, full_msg, commit)
            click.echo(f"Committed: {commit}")
        else:
            click.echo("Git commit failed", err=True)
            sys.exit(1)
    else:
        click.echo("Commit cancelled. Message saved to clipboard? (not implemented)\n")


@main.command()
@click.argument("path_or_message", required=False)
def lint(path_or_message):
    """Lint a commit message. If argument is a path, read the file; if omitted read stdin."""
    repo_root = git_root()
    cfg = load_config(repo_root)


    if path_or_message:
        p = Path(path_or_message)
        if p.exists():
            content = p.read_text()
        else:
            content = path_or_message
    else:
        content = sys.stdin.read()


    ok, errors = validate_commit_message(content, cfg)
    if not ok:
        for e in errors:
            click.echo(f"ERROR: {e}")
        sys.exit(1)
    click.echo("OK")

@main.command()
def history():
    """Show recorded commit messages (the history file)."""
    repo_root = git_root()
    entries = read_history(repo_root)
    if not entries:
        click.echo("No history yet.")
        return
    for e in entries:
        click.echo(f"- {e.get('timestamp')} {e.get('commit')}: {e.get('message').splitlines()[0]}")


@main.command()
def install_hook():
    """Install a commit-msg git hook that blocks commits with bad messages."""
    repo_root = git_root()
    hook_path = Path(repo_root) / ".git" / "hooks" / "commit-msg"
    hook_script = """#!/bin/sh
# commit-msg hook for qcn: runs `qcn lint <commit-msg-file>` and returns non-zero on failure
exec qcn lint "$1"
"""
    hook_path.write_text(hook_script)
    hook_path.chmod(0o755)
    click.echo(f"Installed commit-msg hook at {hook_path}")




if __name__ == "__main__":
    main()