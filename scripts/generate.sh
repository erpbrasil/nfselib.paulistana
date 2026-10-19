# FONTE DOS SCHEMAS (schemas/nfse/): pacotes oficiais da Prefeitura de Sao Paulo, em
# https://notadomilhao.sf.prefeitura.sp.gov.br/desenvolvedor/ . Nao editar os XSDs a mao: para
# atualizar, baixar o pacote novo e copiar por cima. Pacotes usados na versao atual:
#   schemas-v01-2.zip (13/05/2026)                  sha256 2771f66408dc4bfa6a17c20cb14f6f98c89c63cc1be567264ee48945a62d6167
#     https://notadomilhao.sf.prefeitura.sp.gov.br/wp-content/uploads/2026/05/schemas-v01-2.zip
#   schemas-reformatributaria-v02-5.zip (11/05/2026) sha256 1726c42a9fb6d238ea98262a5f05ba960989824553a36975f37a7827485368e3
#     https://notadomilhao.sf.prefeitura.sp.gov.br/wp-content/uploads/2026/05/schemas-reformatributaria-v02-5.zip
# Referencia normativa: Manual de Utilizacao do Web Service de NFS-e v3.3.9 (01/10/2026).
# Os bindings v02 e v03 foram gerados com generateDS 2.44.3 (ver cabecalho de cada arquivo).
erpbrasil-edoc-gen-download-schema -n paulistana -v v02 -u http://notadomilhao.prefeitura.sp.gov.br/arquivos/schemasv02.zip/@@download/file/schemasv02.zip
erpbrasil-edoc-gen-generate-python -m nfse -n paulistana -v v02 -i "PedidoEnvioLoteRPS_v01|PedidoConsultaLote_v01|RetornoEnvioLoteRPS_v01|RetornoConsulta_v01|RetornoInformacoesLote_v01|PedidoConsultaNFe_v01|PedidoCancelamentoLote_v01|RetornoCancelamentoNFe_v01|PedidoCancelamentoNFe_v01" -d .
# O servico_enviar_lote_rps_envio_v03 foi necessário pois a classe EnviarLoteRpsEnvio
# não estava no arquivo de retorno.

# v03: schemas da reforma tributária (NT-007), gerados diretamente com generateDS
# a partir dos XSDs *_v02.xsd já versionados em schemas/nfse/. Os módulos gerados
# mantêm o sufixo _v02 (nfselib/paulistana/v03/<Nome>_v02.py); os nomes sem sufixo
# são módulos de compatibilidade escritos à mão (nfselib/paulistana/v03/<Nome>.py).
# Requer: pip install generateDS lxml six
V03_MODULES="PedidoCancelamentoLote PedidoCancelamentoNFe PedidoConsultaCNPJ PedidoConsultaLote PedidoConsultaNFe PedidoConsultaNFePeriodo PedidoEnvioLoteRPS PedidoEnvioRPS PedidoInformacoesLote RetornoCancelamentoNFe RetornoConsulta RetornoConsultaCNPJ RetornoEnvioLoteRPS RetornoEnvioRPS RetornoInformacoesLote ConsultaGuia ConsultaSituacaoGuiaAsync ConsultaSituacaoLoteAsync EmissaoGuiaAsync PedidoEnvioLoteRPSAsync RetornoEnvioLoteRPSAsync"
for module in $V03_MODULES; do
    generateDS --no-namespace-defs --no-dates --member-specs="list" --use-getter-setter="none" -f \
        -o "nfselib/paulistana/v03/${module}_v02.py" \
        "schemas/nfse/${module}_v02.xsd"

    # generateDS importa o módulo irmão generatedsnamespaces de forma absoluta
    # ("from generatedsnamespaces import ..."), o que falha dentro do pacote
    # nfselib.paulistana.v03. Isso não quebra a importação do módulo porque o
    # ImportError resultante é um ModuleNotFoundError, capturado pelo próprio
    # generateDS com um fallback silencioso (GenerateDSNamespaceDefs_ = {}).
    # Só corrigimos a importação de GenerateDSNamespaceDefs para relativa,
    # pois é o único dicionário que de fato existe em generatedsnamespaces.py
    # e é necessário para exportar os namespaces corretos no XML gerado.
    # NÃO usar --import-path="." no generateDS acima: isso tornaria também
    # relativa a importação de GenerateDSNamespaceTypePrefixes (que não existe
    # em generatedsnamespaces.py) e geraria um ImportError (não um
    # ModuleNotFoundError) não capturado, quebrando o import do módulo.
    sed -i \
        's/^    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_$/    from .generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_/' \
        "nfselib/paulistana/v03/${module}_v02.py"
done
