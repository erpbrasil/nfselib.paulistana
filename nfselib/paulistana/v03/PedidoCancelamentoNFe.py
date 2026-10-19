"""Compatibilidade: este modulo foi renomeado para ``PedidoCancelamentoNFe_v02``.

O nome sem sufixo continua importavel (``from nfselib.paulistana.v03 import PedidoCancelamentoNFe``)
e aponta para o mesmo modulo, para nao quebrar quem importava a versao 0.3.0.
"""
import sys

from . import PedidoCancelamentoNFe_v02 as _impl

sys.modules[__name__] = _impl
