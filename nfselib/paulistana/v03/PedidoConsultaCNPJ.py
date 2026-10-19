"""Compatibilidade: este modulo foi renomeado para ``PedidoConsultaCNPJ_v02``.

O nome sem sufixo continua importavel (``from nfselib.paulistana.v03 import PedidoConsultaCNPJ``)
e aponta para o mesmo modulo, para nao quebrar quem importava a versao 0.3.0.
"""
import sys

from . import PedidoConsultaCNPJ_v02 as _impl

sys.modules[__name__] = _impl
