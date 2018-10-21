def make_password(phrase):
    # Your code here
    dicts = {'o':'0','O':'0',
             'i':'1','I':'1',
             's':'5','S':'5'}
    p_list = [c[0] for c in phrase.split(' ')]
    for i in range(len(p_list)):
        if p_list[i] in dicts.keys():
            p_list[i] = dicts[p_list[i]]
    return ''.join(p_list)


"""
from string import maketrans
def make_password(phrase):
    return ''.join(word[0] for word in phrase.split()).translate(maketrans('iosIOS', '105105'))
"""


"""
def make_password(phrase):
    li = [w[0] for w in phrase.split()]
    dico = {'i': '1', 'o': '0', 's': '5'}
    li = [dico[el.lower()] if el.lower() in dico else el for el in li]
    return "".join(li) 
"""
