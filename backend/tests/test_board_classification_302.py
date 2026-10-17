"""创业板 302 号段 (如 302132.SZ) 应归入创业板, 而不是深主板。"""
from app.api.overview import _board as overview_board
from app.services.market_overview_builder import _board as builder_board


def test_overview_board_classifies_302_as_chinext():
    assert overview_board("302132.SZ") == "创业板"
    assert overview_board("000001.SZ") == "深主板"


def test_builder_board_classifies_302_as_chinext():
    assert builder_board("302132.SZ") == "创业板"
    assert builder_board("300750.SZ") == "创业板"
