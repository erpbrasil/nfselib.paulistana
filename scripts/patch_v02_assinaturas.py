"""Mantem no pacote v02 o contrato das assinaturas da 0.3.0.

Ate a 0.3.0 o v02 era gerado pelo generateDS 2.36.6 e tinha dois campos de assinatura
escritos como texto (o chamador entrega a assinatura ja em base64, como o erpbrasil.edoc
faz no leiaute v01). O generateDS 2.44.3 trata esses campos como xs:base64Binary e aplica
base64 de novo na escrita, o que quebra a emissao e o cancelamento. Este script reaplica o
comportamento antigo, so nos dois pontos em que ele existia, e roda no generate.sh.

Uso: python scripts/patch_v02_assinaturas.py nfselib/paulistana/v02
"""
import os
import re
import sys

BUILD_OLD = (
    "                try:\n"
    "                    bval_ = base64.b64decode(sval_)\n"
    "                except (TypeError, ValueError) as exp:\n"
    "                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)\n"
)
BUILD_NEW = "                bval_ = sval_\n"

# (modulo, classe, campo, leitura tambem como texto)
PONTOS = [
    ("PedidoEnvioLoteRPS", "tpRPS", "Assinatura", True),
    ("PedidoCancelamentoNFe", "DetalheType", "AssinaturaCancelamento", False),
]


def _bloco(text, classe):
    start = re.search(r"^class %s\(" % classe, text, re.M)
    end = re.search(r"^class ", text[start.end():], re.M)
    stop = start.end() + end.start() if end else len(text)
    return start.start(), stop


def aplica(pasta):
    alterados = 0
    for modulo, classe, campo, leitura in PONTOS:
        path = os.path.join(pasta, modulo + ".py")
        text = open(path, encoding="utf-8").read()
        ini, fim = _bloco(text, classe)
        bloco = text[ini:fim]
        old = "self.gds_format_base64(self.%s, input_name='%s')" % (campo, campo)
        new = "self.gds_format_string(self.%s, input_name='%s')" % (campo, campo)
        novo = bloco.replace(old, new)
        if leitura:
            i = novo.index("nodeName_ == '%s'" % campo)
            novo = novo[:i] + novo[i:].replace(BUILD_OLD, BUILD_NEW, 1)
        if novo != bloco:
            open(path, "w", encoding="utf-8").write(text[:ini] + novo + text[fim:])
            alterados += 1
    return alterados


if __name__ == "__main__":
    print("assinaturas do v02 ajustadas em %d ponto(s)" % aplica(sys.argv[1]))
