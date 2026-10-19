import io

from lxml import etree

from nfselib.paulistana.v02.PedidoCancelamentoNFe import tpChaveRPS

TIPOS_NS = 'xmlns:tipos="http://www.prefeitura.sp.gov.br/nfe/tipos"'


def test_tpChaveRPS_round_trip():
    original = tpChaveRPS(
        InscricaoPrestador=12345678,
        SerieRPS='001',
        NumeroRPS=42,
    )

    buf = io.StringIO()
    original.export(
        buf, 0, name_='ChaveRPS', namespacedef_=TIPOS_NS, pretty_print=False
    )
    xml = buf.getvalue()

    node = etree.fromstring(xml.encode('utf-8'))
    rebuilt = tpChaveRPS.factory()
    rebuilt.build(node)

    assert rebuilt.InscricaoPrestador == original.InscricaoPrestador
    assert rebuilt.SerieRPS == original.SerieRPS
    assert rebuilt.NumeroRPS == original.NumeroRPS
