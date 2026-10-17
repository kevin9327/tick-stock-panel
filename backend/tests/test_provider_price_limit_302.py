"""除权因子自检的涨跌停幅度: 创业板 302 号段同为 ±20%。"""
import pytest

from app.plugins.fuyao.provider import _price_limit as fuyao_limit
from app.plugins.tdxquant.provider import _price_limit as tdx_limit


@pytest.mark.parametrize("limit", [tdx_limit, fuyao_limit])
def test_chinext_302_uses_20pct_limit(limit):
    assert limit("302132.SZ") == pytest.approx(0.20)
    assert limit("000001.SZ") == pytest.approx(0.10)
