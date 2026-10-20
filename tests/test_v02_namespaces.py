"""Namespaces do elemento raiz dos pedidos do v02 (contrato da 0.3.0).

O generateDS gera "from generatedsnamespaces import ..." (absoluto), que falha dentro do
pacote e cai num fallback silencioso com o dicionario vazio. Na 0.4.0 e na 0.4.1 os
pedidos do leiaute v01 sairam sem o namespace http://www.prefeitura.sp.gov.br/nfe no
elemento raiz, e o XML gerado pelo l10n_br_nfse_paulistana deixou de bater com o esperado.
"""
import importlib
import io

import pytest

NFE = 'xmlns="http://www.prefeitura.sp.gov.br/nfe"'

MODULOS = [
    "PedidoCancelamentoLote",
    "PedidoCancelamentoNFe",
    "PedidoConsultaLote",
    "PedidoConsultaNFe",
    "PedidoEnvioLoteRPS",
    "RetornoCancelamentoNFe",
    "RetornoConsulta",
    "RetornoEnvioLoteRPS",
    "RetornoInformacoesLote",
]

RAIZES = {
    "PedidoEnvioLoteRPS": '<PedidoEnvioLoteRPS xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    ' xmlns:xsd="http://www.w3.org/2001/XMLSchema" %s/>' % NFE,
    "PedidoConsultaLote": "<PedidoConsultaLote %s/>" % NFE,
    "PedidoConsultaNFe": "<PedidoConsultaNFe %s/>" % NFE,
    "PedidoCancelamentoNFe": "<PedidoCancelamentoNFe %s/>" % NFE,
}


def _modulo(nome):
    return importlib.import_module("nfselib.paulistana.v02." + nome)


@pytest.mark.parametrize("nome", MODULOS)
def test_generatedsnamespaces_is_loaded(nome):
    assert _modulo(nome).GenerateDSNamespaceDefs_


@pytest.mark.parametrize("nome", sorted(RAIZES))
def test_root_namespace(nome):
    buf = io.StringIO()
    getattr(_modulo(nome), nome)().export(buf, 0, pretty_print=False)
    assert buf.getvalue() == RAIZES[nome]


def test_cabecalho_without_namespace():
    mod = _modulo("PedidoEnvioLoteRPS")
    pedido = mod.PedidoEnvioLoteRPS(Cabecalho=mod.CabecalhoType(Versao="1"))
    buf = io.StringIO()
    pedido.export(buf, 0, pretty_print=False)
    assert '<Cabecalho xmlns="" Versao="1"/>' in buf.getvalue()
