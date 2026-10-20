"""Assinaturas do v02 escritas como texto ja em base64 (contrato da 0.3.0).

O erpbrasil.edoc entrega no leiaute v01 a assinatura do RPS e a de cancelamento ja em
base64. A 0.4.0 regenerou o v02 com o generateDS 2.44.3, que aplica base64 de novo na
escrita: emissao e cancelamento quebravam com TypeError em base64.b64encode.
"""
import io

from lxml import etree

from nfselib.paulistana.v02 import PedidoCancelamentoNFe, PedidoEnvioLoteRPS

ASSINATURA = "QUJDREVGR0hJSktMTU5PUA=="


def _export(obj, name):
    # sem prefixo, como o elemento pai exporta os filhos dentro do pedido
    buf = io.StringIO()
    obj.export(buf, 0, namespaceprefix_="", name_=name, pretty_print=False)
    return buf.getvalue()


def test_envio_rps_assinatura_is_exported_as_given():
    xml = _export(PedidoEnvioLoteRPS.tpRPS(Assinatura=ASSINATURA), "RPS")
    assert "<Assinatura>%s</Assinatura>" % ASSINATURA in xml


def test_envio_rps_assinatura_is_read_back_as_text():
    xml = _export(PedidoEnvioLoteRPS.tpRPS(Assinatura=ASSINATURA), "RPS")
    rebuilt = PedidoEnvioLoteRPS.tpRPS.factory()
    rebuilt.build(etree.fromstring(xml.encode()))
    assert rebuilt.Assinatura == ASSINATURA


def test_cancelamento_assinatura_is_exported_as_given():
    detalhe = PedidoCancelamentoNFe.DetalheType(AssinaturaCancelamento=ASSINATURA)
    xml = _export(detalhe, "Detalhe")
    assert "<AssinaturaCancelamento>%s</AssinaturaCancelamento>" % ASSINATURA in xml


def test_nfe_assinatura_still_base64_binary():
    # campo que ja era base64Binary na 0.3.0: recebe bytes e escreve base64
    xml = _export(PedidoEnvioLoteRPS.tpNFe(Assinatura=b"abc"), "NFe")
    assert "<Assinatura>YWJj</Assinatura>" in xml
