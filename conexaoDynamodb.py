
"""
EXEMPLO DE CONEXÃO COM O DYNAMODB
"""
import boto3
from boto3.dynamodb.conditions import Key, Attr

#Ou então configure suas chaves no user/.aws/config
dynamodb = boto3.resource('dynamodb',region_name='sua_regiao',  aws_access_key_id='seu_acess_user_key_iam',
     aws_secret_access_key='seu_acess_user_secrete_key_iam')

#Tabela que quer referenciar
table = dynamodb.Table('Rfid_IoT')


print(table.creation_date_time)

#Filtro de consulta
filter_expression = Key('thing').eq('raspberry')

response = []

response = table.scan(
    FilterExpression=filter_expression
 )
dados = []
for i in response['Items']:
    print(json.dumps(i,default=decimal_default),i["payload"])
    print(i["payload"].get("rfid"))
    dados.append(i["payload"].get("rfid"))

if len(dados)>0:
     rfids = dados[-1]