import configparser
CFpraser = configparser.ConfigParser()

def load_data():
    CFpraser.read('user_config.cfg')
    return CFpraser

def syncConfig(Var,Config,input):
    if input == 'box':
        var = CFpraser.get('User',Config)
        if var == 'True':
            Var.select()
        else:
            Var.deselect()
    if input == 'Option':
        Var.set(CFpraser.get('User',Config))


def save_data(cfg):
    with open('user_config.cfg', 'w') as configfile:cfg.write(configfile)