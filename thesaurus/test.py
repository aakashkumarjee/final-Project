path = "test.dat"
import unicodedata
def remove_accents(string):
    nkfd_form = unicodedata.normalize('NFKD', unicode(string))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

with open(path) as f:
    content = f.readlines()
    print(content)
    # we jump content[0] because it is the encoding-type line : useless to parse
    for line_id in range(1, len(content)):
        if '(' not in content[line_id]:
            line = content[line_id].split("|")
            word = remove_accents(line[0])
            print(line, line_id)
            synonyms = remove_accents(content[line_id + 1]).split("|")
            synonyms.pop(0)
            print(word, synonyms)
            print(str(word))
            # modword = []
            # for j in word:
            #     modword.append(j)
            # print(modword)
