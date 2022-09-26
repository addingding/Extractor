from ecosys import *

# LANGUAGES[0] = 0 #0 English, 1 中文, 2-繁体中文
LANG_FILE = os.path.join(BASE_DIR,'app','settings','lang.json')

with open(LANG_FILE,'r',encoding='utf-8') as f:
    LANGS = json.load(f)

def _lang(*args):
    for arg in args:
        if not isinstance(arg,str):
            _ret =[LANGS[i][LANGUAGES[0]] for i in arg]
        else:
            _ret = LANGS[arg][LANGUAGES[0]]
    return _ret
def lang(*args):
    if len(args)==0:
        return ""
    try:
        return _lang(*args)
    except:
        return args[0]

def test_language_settings(language=1):
    LANGUAGES[0] = language
    print(lang(["op_name","op_name"]))
    print(lang("op_name"))
    print(lang("o_name"))
    print(lang())
    print(lang(""))

if __name__ == "__main__":
    test_language_settings(0)
    test_language_settings(1)