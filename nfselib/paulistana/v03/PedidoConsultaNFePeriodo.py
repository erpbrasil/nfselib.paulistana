"""Compatibilidade: este modulo foi renomeado para ``PedidoConsultaNFePeriodo_v02``.

O nome sem sufixo continua importavel (``from nfselib.paulistana.v03 import PedidoConsultaNFePeriodo``)
e aponta para o mesmo modulo, para nao quebrar quem importava a versao 0.3.0.
"""
import sys

from . import PedidoConsultaNFePeriodo_v02 as _impl

sys.modules[__name__] = _impl
