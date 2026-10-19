import importlib

import pytest

NAMES = [
    "PedidoCancelamentoLote",
    "PedidoCancelamentoNFe",
    "PedidoConsultaCNPJ",
    "PedidoConsultaLote",
    "PedidoConsultaNFe",
    "PedidoConsultaNFePeriodo",
    "PedidoEnvioLoteRPS",
    "PedidoEnvioRPS",
    "PedidoInformacoesLote",
    "RetornoCancelamentoNFe",
    "RetornoConsulta",
    "RetornoConsultaCNPJ",
    "RetornoEnvioLoteRPS",
    "RetornoEnvioRPS",
    "RetornoInformacoesLote",
]


@pytest.mark.parametrize("name", NAMES)
def test_legacy_module_name_is_the_renamed_module(name):
    legacy = importlib.import_module("nfselib.paulistana.v03." + name)
    renamed = importlib.import_module("nfselib.paulistana.v03." + name + "_v02")
    assert legacy is renamed


def test_from_import_like_erpbrasil_edoc_does_it():
    from nfselib.paulistana.v03 import PedidoConsultaNFe, RetornoConsulta
    from nfselib.paulistana.v03 import PedidoConsultaNFe_v02, RetornoConsulta_v02

    assert PedidoConsultaNFe is PedidoConsultaNFe_v02
    assert RetornoConsulta is RetornoConsulta_v02
    assert hasattr(PedidoConsultaNFe, "PedidoConsultaNFe")
