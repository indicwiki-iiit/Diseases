from re import template
from tokenize import Name
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from genXML import tewiki, writePage


def getImage(url):
    return url.rsplit('/', 1)[-1]


def getData(datarow):
    data = {
        'Name': datarow[0],
        'info_Specialty': datarow[11],
        'info_Symptoms': datarow[12],
        'info_Usual_onset': datarow[13],
        'info_Duration': datarow[14],
        'info_Causes': datarow[15],
        'info_Risk_factors': datarow[16],
        'info_Diagnostic_method': datarow[17],
        'info_Prevention': datarow[18],
        'info_Treatment': datarow[19],
        'info_Prognosis': datarow[20],
        'info_Frequency': datarow[21],
        'info_Medication': datarow[22],
        'imageURL': getImage(datarow[23]),
        'Overview': datarow[4],
        'Symptoms': datarow[3],
        'Causes': datarow[5],
        'Risk_factors': datarow[6],
        'Diagnosis': datarow[7],
        'Treatment': datarow[8],
        'Remedies': datarow[9],
        'Medication': datarow[10],
        'link': datarow[1],
        'link2': datarow[2]
    }
    return data


def main():
    fileLoader = FileSystemLoader('./')
    env = Environment(loader=fileLoader)
    template = env.get_template('Template/template.j2')
    df = pd.read_csv(open('Datasets/FinalDiseasesHindi.csv', 'rb'))
    df = df.fillna('NaN')

    xmlDump = open('diseases.xml', 'w')
    xmlDump.write(tewiki+'\n')

    # file = open('test.txt', 'w')

    initial_page_id = 900000
    # print(len(df))

    for i in range(1157):
        row = df.iloc[i]
        text = template.render(getData(row))
        title = df.loc[i, 'Name']
        writePage(initial_page_id, title, text, xmlDump)
        initial_page_id += 1
        # file.write(text)

    xmlDump.write('</mediawiki>')
    xmlDump.close()


if __name__ == '__main__':
    main()
