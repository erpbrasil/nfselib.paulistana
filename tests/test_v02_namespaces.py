"""Namespaces do v02 escritos como na 0.3.0.

A 0.4.0 regenerou o v02 com o generateDS 2.44.3, cujo import absoluto de
``generatedsnamespaces`` falha em silencio dentro do pacote e deixava o ``export`` sem o
``xmlns`` padrao da prefeitura, sem o ``xmlns=""`` dos filhos e sem ``xmlns:xsi`` e
``xmlns:xsd``, trocando-os por ``xmlns:tipos`` e ``xmlns:ds``. O XML de referencia em
tests/data foi gerado pela 0.3.0 (lido da mesma fixture e escrito com ``export`` sem
``namespacedef_``, como o erpbrasil.edoc faz).
"""
import importlib
import io
import os

import pytest

from nfselib.paulistana.v02 import PedidoEnvioLoteRPS

DATA = os.path.join(os.path.dirname(__file__), "data")


def _export(obj, **kwargs):
    buf = io.StringIO()
    obj.export(buf, 0, **kwargs)
    return buf.getvalue()


def test_envio_lote_rps_matches_0_3_0_output():
    path = os.path.join(DATA, "v02_pedido_envio_lote_rps_0.3.0.xml")
    with open(path, encoding="utf-8") as fp:
        expected = fp.read()
    obj = PedidoEnvioLoteRPS.parse(path, silence=True)
    assert _export(obj, pretty_print=True) == expected


@pytest.mark.parametrize(
    "module,expected",
    [
        ("PedidoConsultaLote", '<PedidoConsultaLote xmlns="http://www.prefeitura.sp.gov.br/nfe"/>'),
        ("PedidoConsultaNFe", '<PedidoConsultaNFe xmlns="http://www.prefeitura.sp.gov.br/nfe"/>'),
        (
            "PedidoCancelamentoNFe",
            '<PedidoCancelamentoNFe xmlns="http://www.prefeitura.sp.gov.br/nfe"/>',
        ),
        ("PedidoCancelamentoLote", "<PedidoCancelamentoLote/>"),
        ("RetornoConsulta", "<RetornoConsulta/>"),
        ("RetornoEnvioLoteRPS", "<RetornoEnvioLoteRPS/>"),
        ("RetornoCancelamentoNFe", "<RetornoCancelamentoNFe/>"),
        ("RetornoInformacoesLote", "<RetornoInformacoesLote/>"),
    ],
)
def test_root_element_declarations_match_0_3_0(module, expected):
    mod = importlib.import_module("nfselib.paulistana.v02." + module)
    obj = getattr(mod, module)()
    assert _export(obj, pretty_print=False) == expected


def test_namespace_defs_are_loaded():
    # se o import do generatedsnamespaces voltar a falhar, o dicionario fica vazio
    assert PedidoEnvioLoteRPS.GenerateDSNamespaceDefs_.get("PedidoEnvioLoteRPS")
