"""Garantem que os bindings seguem os XSDs oficiais da prefeitura de Sao Paulo.

Fontes: manual de utilizacao do web service v3.3.9 (tpRetencaoPisCofins, pag. 23) e os
pacotes de schemas v01-2 e reformatributaria v02-5 (ver scripts/generate.sh).
"""
import importlib

import pytest

RETENCAO = {"0", "3", "4", "5", "6", "7", "8", "9"}

NEW_V03_MODULES = [
    "ConsultaGuia_v02",
    "ConsultaSituacaoGuiaAsync_v02",
    "ConsultaSituacaoLoteAsync_v02",
    "EmissaoGuiaAsync_v02",
    "PedidoEnvioLoteRPSAsync_v02",
    "RetornoEnvioLoteRPSAsync_v02",
]


def _values(enum_cls):
    return {member.value for member in enum_cls}


def test_v03_tpRetencaoPisCofins_domain():
    from nfselib.paulistana.v03.PedidoEnvioRPS_v02 import tpRetencaoPisCofins

    assert _values(tpRetencaoPisCofins) == RETENCAO


def test_v02_tpRetencaoPisCofins_domain():
    from nfselib.paulistana.v02.PedidoEnvioLoteRPS import tpRetencaoPisCofins

    assert _values(tpRetencaoPisCofins) == RETENCAO


def test_v03_tpReeRepRes_has_no_leading_zeros():
    from nfselib.paulistana.v03.PedidoEnvioRPS_v02 import tpReeRepRes

    assert _values(tpReeRepRes) == {"1", "2", "3", "4", "99"}


def test_v03_has_no_invented_retencao_group():
    module = importlib.import_module("nfselib.paulistana.v03.PedidoEnvioRPS_v02")
    assert not hasattr(module, "RetencaoPisCofins")


@pytest.mark.parametrize("name", NEW_V03_MODULES)
def test_new_v03_service_modules_import(name):
    module = importlib.import_module("nfselib.paulistana.v03." + name)
    assert module.__name__.endswith(name)
