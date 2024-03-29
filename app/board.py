from ecosys import *

e_work = Event()
e_mt = Event()
e_uv = Event()
e_stop = Event()

disk_1_temperature_ok = Event()
disk_8_temperature_ok = Event()

info = dict(
    pg_idx = None,
    pg_name = None,
    disk_1_preset = 25,
    disk_8_preset = 25,
    pg_total_time = 0,
    pg_worked_time = 0,
    pg_start_time = time.time(),

    step_idx = 1,
    op_name= "----",
    disk = 1,
    sec_wait= 50,
    sec_mix= 60,
    sec_mag= 6,
    ul_volumn= 700,
    speed_mix= 2,
    temperature= 0,
    step_total_time = 0,
    step_worked_time = 0,
    step_start_time = time.time(),
    
    disk_1_temperature = 25,
    disk_8_temperature = 25,
    disk_1_temperature_ok = disk_1_temperature_ok,
    disk_8_temperature_ok = disk_8_temperature_ok,
    disk_pos = 1,
    led_is_on = False,
    fan_is_on = False,
    uv_is_on = False,
    door_at_spot = False,
    sheath_at_spot = False,
    disk_info = [""]*8,
    extract_pausing = False,
)

class Updater:
    ...


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
        logger.info(f"{list(item.keys())} updated and saved")