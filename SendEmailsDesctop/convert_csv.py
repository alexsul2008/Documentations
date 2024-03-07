import os
from io import StringIO


from pandas import read_csv, Series, DataFrame, unique, read_excel, read_json



from models.models import PATH_DATA
from utils import find_emails_in_str





def csvListOperatorsORM(path):
    data_csv = read_csv(path, delimiter = ';')
    csv_list_oper = Series(data_csv['Оператор'], index = data_csv.index).unique().tolist()
    csv_list_oper.sort()
    list_operators = []
    for item in csv_list_oper:
        item = item.replace('""', '"')
        list_operators.append({"name": item})


    return list_operators




def uploadDataSpInPandas(path):
    data_csv = read_csv(path, delimiter = ';')
    groups = data_csv.groupby(['Оператор'])['Декадный'].apply(
        lambda Декадный: ''.join(Декадный.to_string(index = False))).str.replace('(\\n)', ',',
                                                                                 regex = True).reset_index()

    locations = DataFrame(unique(data_csv[['Место установки']].values.ravel('K')))
    locations_DPC = DataFrame(data_csv, columns = ['Декадный', 'Оператор', 'Место установки', 'АВС/ DEF', 'Структурный', 'Зона обслуживания'])

    list_locations = []
    for _, row in locations.iterrows():
        item = '{}'.format(row[0])
        list_locations.append({"name": item})

    return list_locations, locations_DPC

def savePandasMgmn(path):
    df = read_excel(path, sheet_name = 1, skiprows = 4, engine='openpyxl')

    path_for_csv = path.rsplit("/", 1)[0] + '/pandas_mgmn.csv'

    df.to_csv(path_for_csv, index = False, sep = ';')
    df_mgmn = read_csv(path_for_csv, sep = ';')
    df_mgmn.rename(columns = {'Коммутатор': 'Kommutator',
                              'Транк': 'Trank',
                              'Название транка': 'NameTrank',
                              'ts': 'Ts',
                              'DPC/IP': 'DPCIP',
                              'OPC': 'OPC',
                              'Назначение транка': 'AssignmentTrank',
                              'Регион коммутатора': 'RegionKommutatora',
                              'Регион шлюза': 'RegionShluza',
                              'Уровень присоед.': 'UrovenPrisoedineniya',
                              'Тип': 'Type',
                              'Напр.': 'Napravlenie',
                              'Тип ТГ': 'TypeTG',
                              'Примечание': 'Primechanie'
                        }, inplace = True)
    df_mgmn.to_csv(path_for_csv, index = False, sep = ';')
    df_mgmn = read_csv(path_for_csv, sep = ';')

    data_in_mgmn = DataFrame(df_mgmn, columns = ['Kommutator', 'NameTrank', 'DPCIP', 'OPC', 'AssignmentTrank',
                                                    'RegionKommutatora', 'RegionShluza', 'UrovenPrisoedineniya',
                                                    'Primechanie'])
    list_emails = data_in_mgmn.groupby(['AssignmentTrank'])['Primechanie'].apply(
        lambda Primechanie: ''.join(str(Primechanie.values.ravel('K')))).str.replace('(\\n)', ',', regex = True).reset_index().to_dict('records')

    list_operators_to_emails = []
    for _, item in enumerate(list_emails):
        # emails = find_emails_in_str(item['Primechanie'])
        emails = "; ".join(find_emails_in_str(item['Primechanie'])) + ";"
        data = {
            "name": str(item["AssignmentTrank"]).strip(),
            "emails": emails
        }
        list_operators_to_emails.append(data)

    csv_list_oper_mgmn = DataFrame(list_operators_to_emails, columns = ['name', 'emails']).drop_duplicates(subset = ['name'])
    list_emails_operators = csv_list_oper_mgmn[csv_list_oper_mgmn.astype(str)['emails'] != ';'].to_dict('records')


    operators_unique = Series(df_mgmn['AssignmentTrank'], index = df_mgmn.index).unique().tolist()



    list_operators = []
    for item in operators_unique:
        if str(item) != 'nan':
            list_operators.append({"name": str(item).strip()})


    data = {
        'listOperatorsToEmails': list_emails_operators,
        'list_operators': list_operators,
        'path_for_csv': path_for_csv,
        'data_in_mgmn': data_in_mgmn,

    }
    # print(f'{data=}')
    os.remove(path_for_csv)
    return data




def downloadEmailsAllOperatorsJson(from_db, from_file):
    df_db = read_json(StringIO(from_db), orient = 'columns')
    df_file = read_json(from_file, orient = 'columns')

    update_df = (df_db.merge(df_file, how = 'outer', on = ['operator_name'], suffixes = ['', '_new'], indicator = True))
    update_df[['email']] = (update_df[['email']].apply(lambda c: c.combine_first(update_df[f'{c.name}_new'])))
    # update_df = update_df.drop(update_df.loc[update_df["email"] == update_df["email_new"]].index)
    update_df = update_df.drop(columns = ["email", "_merge"])
    update_df = update_df.rename(columns = {"email_new": "email"})

   
    # delete_dict = delete_df.to_dict(orient = "list")
    new_dict = update_df.to_dict(orient = "records")

   

    # df_db = df_file = update_df = delete_df = ''
    df_db = df_file = update_df = ''

   
    return {
        # 'delete_email': delete_dict,
        'new_email': new_dict
    }




def downloadEmailsAllOperatorsInDb():
    df_emails = read_csv(os.path.join(PATH_DATA, 'emails_operators.csv'), sep = ';')
    # data_emails = pd.DataFrame(df_emails, columns = ['Email', 'Operator'])

    groups_emails_for_operator = df_emails.groupby(['Operator'])['Email'].apply(
        lambda Email: ''.join(Email.to_string(index = False).strip())).str.replace('(\\n)', ',', regex = True).reset_index()

    return groups_emails_for_operator


def downloadEmailsAllRegionsInDb(path):
    df_emails = read_excel(path, header=None)
    emails_regions = DataFrame(df_emails)
    emails_regions.rename(columns = {0: 'region', 1: 'email'}, inplace = True)
    emails_regions['region'] = emails_regions['region'].apply(lambda x: x.strip())
    emails_regions['email'] = emails_regions['email'].apply(lambda y: y.strip().lower())

    groups = emails_regions.groupby(['region'])['email'].unique().apply(
        lambda email: ';'.join(email) + ';').reset_index().to_dict('records')

    # print(f'{groups=}')

    return groups









