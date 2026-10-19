
Changelog
=========

0.4.0 (2026-10-19)
~~~~~~~~~~~~~~~~~~

* Schemas sincronizados com os pacotes oficiais da prefeitura: ``schemas-v01-2`` (13/05/2026) e
  ``schemas-reformatributaria-v02-5`` (11/05/2026), conforme o manual do web service v3.3.9. Os
  XSDs que estavam no repositório tinham divergências (por exemplo limite de 50 RPS por lote,
  valores do Simples Nacional ausentes, campos de carga tributária).
* ``tpRetencaoPisCofins`` passa a ter o domínio oficial (0 e 3 a 9, PIS/COFINS/CSLL) nos pacotes
  ``v02`` e ``v03``. O elemento ``RetencaoPisCofins`` de ``tpRPS`` é um valor simples desse tipo
  (a classe-grupo ``RetencaoPisCofins`` com valores 1, 2 e 3 não existe nos layouts oficiais e
  foi removida; ela nunca esteve numa versão publicada).
* ``tpReeRepRes`` (v02): valores ``1``, ``2``, ``3``, ``4`` e ``99``, sem zeros à esquerda.
* Novos módulos do ``v03``: serviço assíncrono (``PedidoEnvioLoteRPSAsync_v02``,
  ``RetornoEnvioLoteRPSAsync_v02``, ``ConsultaSituacaoLoteAsync_v02``) e guias
  (``EmissaoGuiaAsync_v02``, ``ConsultaSituacaoGuiaAsync_v02``, ``ConsultaGuia_v02``).
* Os módulos do pacote ``nfselib.paulistana.v03`` passam a se chamar ``<Nome>_v02``
  (por exemplo ``PedidoCancelamentoNFe_v02``). Os nomes anteriores (``PedidoCancelamentoNFe``
  e demais) continuam importáveis como módulos de compatibilidade.
* Dependências de runtime declaradas (``lxml`` e ``six``), CI no GitHub Actions e publicação no
  PyPI por Trusted Publishing.

0.3.0 (2026-01-11)
~~~~~~~~~~~~~~~~~~

* Corrige o nome do pacote distribuído para ``nfselib_paulistana``,
  necessário para o upload no PyPI.

0.2.0 (2026-01-11)
~~~~~~~~~~~~~~~~~~

* Adiciona o pacote ``nfselib.paulistana.v03``, com as classes geradas
  a partir dos XSDs da Reforma Tributária (NT-007), schemas na versão 3.3.4.

0.1.0 (2020-11-08)
~~~~~~~~~~~~~~~~~~

* First release on PyPI.
