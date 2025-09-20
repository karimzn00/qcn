from qcn.validators import validate_commit_message




def test_valid_message():
    cfg = {"types": ["feat", "fix"], "max_summary_length": 72}
    ok, errs = validate_commit_message("feat: add new feature", cfg)
    assert ok




def test_invalid_type():
    cfg = {"types": ["feat"], "max_summary_length": 72}
    ok, errs = validate_commit_message("fix: broken", cfg)
    assert not ok




def test_long_summary():
    cfg = {"types": ["feat"], "max_summary_length": 5}