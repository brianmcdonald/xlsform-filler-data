import pandas as pd
import random
import click
import warnings
from lorem_text import lorem
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
from pandas.io.formats import excel
excel.ExcelFormatter.header_style = None

@click.command()
@click.argument("filename", required=True)
@click.option("--rows", "-r", default=100, type=int, required=False, help="the number of records required")
@click.option("--output", "-o", default="./filler-data.xlsx", type=str, required=False, help="the output directory")

def cli(filename, rows, output):
    survey = pd.read_excel(filename, sheet_name='survey')
    survey = survey[survey['type']!='calculate']
    choices = pd.read_excel(filename, sheet_name='choices')

    for index, row in survey.iterrows():
        if 'select_one' in row['type']:
            choice_name = row['type'].split(' ')[1]
            choices_list = choices[choices['list_name'] == choice_name]['name']
            temp = choices_list.sample(n=rows, replace=True)
            df[row['name']] = temp.values
        if 'select_multiple' in row['type']: # adding multiple answers not working yet
            choice_name = row['type'].split(' ')[1]
            choices_list = choices[choices['list_name'] == choice_name]['name']
            choices_count = len(choices_list)
            choices_num = random.randint(choices_count, choices_count)
            temp = choices_list.sample(n=rows, replace=True)
            df[row['name']] = temp.values
        if 'text' in row['type']:
            words = random.randint(1,5)
            #lorem.words(words)
            df[row['name']] = lorem.words(words)
        if 'integer' in row['type']:
            df[row['name']] = random.randint(0,100)
        if 'date' in row['type']:
            dates = ['2022-04-20','2022-04-21','2022-04-22','2022-04-23','2022-04-24']
            df[row['name']]  = random.choice(dates)

    df.to_excel(output, index=None)
    print('Sucessfully saved to: '+ output)

df = pd.DataFrame()

if __name__ == "__main__":
    cli()