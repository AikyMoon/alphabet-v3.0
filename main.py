
def g():
    return [
        '   ggggg  ',
        '  ggggggg ',
        ' gg     gg',
        'gg      gg',
        'gg        ',
        'gg        ',
        'gg        ',
        'gg   ggggg',
        'gg      gg',
        ' gg     gg',
        '  ggggggg ',
        '   ggggg  ',
    ]
def f():
    return [
        'ffffffffff',
        'ffffffffff',
        'ff        ',
        'ff        ',
        'ff        ',
        'fffffff   ',
        'fffffff   ',
        'ff        ',
        'ff        ',
        'ff        ',
        'ff        ',
        'ff        '
    ]
def e():
    return [
        'eeeeeeeeee',
        'eeeeeeeeee',
        'ee     eee',
        'ee        ',
        'ee        ',
        'eeeeeee   ',
        'eeeeeee   ',
        'ee        ',
        'ee        ',
        'ee     eee',
        'eeeeeeeeee',
        'eeeeeeeeee',
    ]
def d():
    return [
        'ddddd     ',
        'dddddd    ',
        'dd   dd   ',
        'dd    dd  ',
        'dd    dd  ',
        'dd    dd  ',
        'dd    dd  ',
        'dd    dd  ',
        'dd    dd  ',
        'dd   dd   ',
        'dddddd    ',
        'ddddd     ',
    ]

def c():
    return [
        '   cccc   ',
        '  cc  cc  ',
        ' cc    cc ',
        'cc     cc ',
        'cc        ',
        'cc        ',
        'cc        ',
        'cc        ',
        'cc     cc ',
        ' cc    cc ',
        '  cc  cc  ',
        '   cccc   ',
    ]


def b():
    return [
'bbbb      ',
'b   b     ',
'b    b    ',
'b   b     ',
'bbbb      ',
'bbbbb     ',
'b    b    ',
'b    b    ',
'b     b   ',
'b    b    ',
'b    b    ',
'bbbbb     '
    ]


def a():
    return[
        '    aa    ',
        '    aa    ',
        '   a  a   ',
        '   a  a   ',
        '   a  a   ',
        '  a    a  ',
        '  a    a  ',
        '  aaaaaa  ',
        ' a      a ',
        ' a      a ',
        'a        a',
        'a        a'
    ]
letters_dict = {
    'a' : a,
    'b' : b,
    'c' : c,
    'd' : d,
    'e' : e,
    'f' : f,
    'g' : g,
    'h' : h,
    'i' : i,
    'j' : j,
    'k' : k,
    'l' : l,
    'm' : m,
    'n' : n,
    'o' : o,
    'p' : p,
    'q' : q,
    'r' : r,
    's' : s,
    't' : t,
    'u' : u,
    'v' : v,
    'w' : w,
    'x' : x,
    'y' : y,
    'z' : z,
    ' ' : void,
    ',' : comma,
    '?' : question,
    '!' : exclamation,
    '.' : dot
}

def parser(text):
    parse_text = []
    for let in text.lower():
        parse_text.append(let)
    return parse_text

def print_letters(parse:list, lets:dict):
    word = []
    for let in parse:
        word.append(lets[let]())

    for i in range(12):
        for j in range(len(word)):
            print(word[j][i], end = '  ')
        print()

text = input()

lst = parser(text)
print_letters(lst, let_dict)

