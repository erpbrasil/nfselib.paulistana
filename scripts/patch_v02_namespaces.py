"""Mantem no pacote v02 as declaracoes de namespace da 0.3.0.

O generateDS 2.44.3 gera, em cada modulo, ``from generatedsnamespaces import ...`` (import
absoluto). Dentro do pacote ``nfselib.paulistana.v02`` esse import falha com
ModuleNotFoundError, que o proprio modulo captura e troca por ``{}``. Sem o dicionario
``GenerateDSNamespaceDefs`` o ``export`` perde o ``xmlns`` padrao da prefeitura, o
``xmlns=""`` dos filhos e o ``xmlns:xsi``/``xmlns:xsd`` do envio, e cai no ``namespacedef_``
padrao do gerador (``xmlns:tipos`` e ``xmlns:ds``). Ate a 0.3.0 (generateDS 2.36.6) o import
era relativo. Alem disso a 2.44.3 passou a gravar em ``export`` e ``_exportChildren`` um
``namespacedef_`` padrao com ``xmlns:tipos`` e ``xmlns:ds``, enquanto a 0.3.0 usava ``''``
(raizes sem dicionario, como RetornoConsulta, saem sem declaracao). Este script (1) volta o
import de ``GenerateDSNamespaceDefs`` para relativo, so nele: o ``GenerateDSNamespaceTypePrefixes`` nao existe em generatedsnamespaces.py e um import
relativo dele levantaria ImportError, que o modulo nao captura (mesmo cuidado do v03 no
generate.sh); e (2) volta o ``namespacedef_`` padrao dessas assinaturas para ``''``.

Uso: python scripts/patch_v02_namespaces.py nfselib/paulistana/v02
"""
import glob
import re
import os
import sys

OLD = "    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_\n"
NEW = "    from .generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_\n"
# so nas assinaturas de metodo; as chamadas ja passam namespacedef_='' explicitamente
DEFAULT_RE = re.compile(r"^(    def (?:export|_exportChildren)\(.*?)namespacedef_='[^']+'", re.M)


def aplica(pasta):
    alterados = 0
    for path in sorted(glob.glob(os.path.join(pasta, "*.py"))):
        text = open(path, encoding="utf-8").read()
        novo = DEFAULT_RE.sub(r"\1namespacedef_=''", text.replace(OLD, NEW))
        if novo != text:
            open(path, "w", encoding="utf-8").write(novo)
            alterados += 1
    return alterados


if __name__ == "__main__":
    print("namespaces do v02 ajustados em %d modulo(s)" % aplica(sys.argv[1]))
