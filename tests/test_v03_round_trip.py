import io

import pytest
from lxml import etree

from nfselib.paulistana.v03.PedidoCancelamentoNFe_v02 import (
    tpCPFCNPJNIF,
    tpEnderecoNacional,
)

TIPOS_NS = 'xmlns:tipos="http://www.prefeitura.sp.gov.br/nfe/tipos"'


def _round_trip(obj, name):
    buf = io.StringIO()
    obj.export(buf, 0, name_=name, namespacedef_=TIPOS_NS, pretty_print=False)
    node = etree.fromstring(buf.getvalue().encode('utf-8'))
    rebuilt = obj.__class__.factory()
    rebuilt.build(node)
    return rebuilt


@pytest.mark.parametrize(
    'fields',
    [
        {'cMun': 3550308, 'CEP': 1310100},
        {'cMun': 3304557, 'CEP': 20021130},
    ],
)
def test_tpEnderecoNacional_round_trip(fields):
    original = tpEnderecoNacional(**fields)
    rebuilt = _round_trip(original, 'EnderecoNacional')

    assert rebuilt.cMun == original.cMun
    assert rebuilt.CEP == original.CEP


@pytest.mark.parametrize(
    'fields',
    [
        {'CNPJ': '12345678000195'},
        {'CPF': '12345678901'},
        {'NIF': 'ABC123456'},
    ],
)
def test_tpCPFCNPJNIF_round_trip(fields):
    original = tpCPFCNPJNIF(**fields)
    rebuilt = _round_trip(original, 'CPFCNPJNIF')

    assert rebuilt.CPF == original.CPF
    assert rebuilt.CNPJ == original.CNPJ
    assert rebuilt.NIF == original.NIF
    assert rebuilt.NaoNIF == original.NaoNIF
