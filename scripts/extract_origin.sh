echo 'Iniciando download de arquivos da origem'

cd ./raw_data
wget -nc https://caelum-online-public.s3.amazonaws.com/3062-pipeline-dados/dados/dados_empresaB.csv
wget -nc https://caelum-online-public.s3.amazonaws.com/3062-pipeline-dados/dados/dados_empresaA.json

echo 'Finalizado o download de arquivos da origem'