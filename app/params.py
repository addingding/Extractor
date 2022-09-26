from ecosys import *

def get_path(*dirs):
    _path = os.path.join(*dirs)
    path = _path.replace("\\","/")
    return path

app_src = os.path.join(BASE_DIR,'app','settings','imgs')
ico_file = get_path(app_src,'favicon.ico')
logo_file = get_path(app_src,'logo.png')
opening_gif = get_path(app_src,'open.gif')
background_png = get_path(app_src,'background.png')

program_file = get_path(BASE_DIR,'app','data','programs.json')
operation_file = get_path(BASE_DIR,'app','data','operations.json')


default_config_file = os.path.join(BASE_DIR,"app/settings/defaults.json")
def read_defaults():
    with open(default_config_file,'r') as f:
        defaults = json.load(f)
    return defaults

defaults = read_defaults()

def update_defaults(cate=None,item:dict=None):
    if cate is None:
        defaults.update(item)
    else:
        _item = defaults.get(cate)
        _item.update(item)
        defaults.update({cate:_item})
    with open(default_config_file,'w') as f:
        json.dump(defaults,f)