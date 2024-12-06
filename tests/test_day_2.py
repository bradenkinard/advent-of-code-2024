from advent_of_code_2024.day_2 import report_is_safe


def test_increasing_is_safe() -> None:
    report = [0, 1, 3, 6, 7]
    assert report_is_safe(report)


def test_decreasing_is_safe() -> None:
    report = [7, 6, 3, 2, 0]
    assert report_is_safe(report)


def test_increase_too_much() -> None:
    report = [0, 1, 2, 7]
    assert not report_is_safe(report, max_diff=3)


def test_decrease_too_much() -> None:
    report = [7, 6, 1, 0]
    assert not report_is_safe(report, max_diff=3)


def test_unsafe_increase_then_decrease() -> None:
    report = [0, 1, 2, 1]
    assert not report_is_safe(report)


def test_unsafe_decrease_then_increase() -> None:
    report = [2, 1, 0, 1]
    assert not report_is_safe(report)


def test_unsafe_change_by_0() -> None:
    report = [0, 0, 1, 2]
    assert not report_is_safe(report)
