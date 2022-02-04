from podping_hivewatcher import __version__
from podping_hivewatcher.hivewatcher import allowed_op_id, get_allowed_accounts


def test_get_allowed_accounts():
    """Checks the get allowed accounts function"""
    allowed = get_allowed_accounts()
    assert "podping.gittest" in allowed


def test_allowed_op_id():
    ans = allowed_op_id("pp_video_update")
    assert ans

    ans = allowed_op_id("sm_something")
    assert not ans
    