import re




COMMIT_RE = re.compile(r"^(?P<type>\w+)(?:\((?P<scope>[^)]+)\))?:\s(?P<subject>.+)$")




def validate_commit_message(message: str, config: dict):
    """Return (ok: bool, errors: list[str]).


    - Checks the first line (summary) against conventional format
    - Ensures type is known, summary not too long, and summary not ending with a dot
    """
    errors = []
    if not message or not message.strip():
        return False, ["Empty commit message"]


    first_line = message.strip().splitlines()[0]
    m = COMMIT_RE.match(first_line)
    if not m:
        errors.append("Summary must follow: type(scope): subject\nExample: feat(api): add pagination")
        return False, errors


    ctype = m.group("type")
    subject = m.group("subject").strip()


    allowed = config.get("types", [])
    if ctype not in allowed:
        errors.append(f"Type '{ctype}' not in allowed types: {allowed}")


    max_len = config.get("max_summary_length", 72)
    if len(subject) > max_len:
        errors.append(f"Summary too long ({len(subject)} > {max_len})")


    if subject.endswith("."):
        errors.append("Summary should not end with a period '.')")


    return (len(errors) == 0), errors