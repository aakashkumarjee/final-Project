from startSqlConversion import main as __main__
import re
import os


def startSql(query, sqlDump, outputFile=None):

    args = ['-d', sqlDump,
            '-l', os.path.dirname(os.path.abspath(__file__)
                                  ) + '/lang/english.csv',
            '-i', query,
            '-j', outputFile]

    generatedSql = __main__(args)

    return str(generatedSql)


# def getSql_like(query, sqlDump, outputFile=None):
#     sql = startSql(query, sqlDump, outputFile)
#
#     sql = re.sub("(WHERE \S+ )=", r'\g<1>LIKE', sql)
#     sql = re.sub("(AND \S+ )=", r'\g<1>LIKE', sql)
#     sql = re.sub("(OR \S+ )=", r'\g<1>LIKE', sql)
#
#     # 'abc def' -> '%abc%def%'
#     for i in re.findall("'(.*?)'", sql):
#         sql = sql.replace(i, "%" + i + "%")
#         sql = sql.replace(i, i.replace(' ', '%'))
#     return sql
