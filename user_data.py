import configparser
CFpraser = configparser.ConfigParser()

def load_data():
    CFpraser.read('user_config.cfg')
    return CFpraser

def syncConfig(Var,Config,input):
    match input:
        case 'box':
            var = CFpraser.get('User',Config)
            if var == 'True':
                Var.select()
            else:
                Var.deselect()
        case 'Option':
            Var.set(CFpraser.get('User',Config))
        case 'int_Option':
            value = int(CFpraser.get('User',Config))
            Var.set(value)
            return value


def save_data(cfg):
    with open('user_config.cfg', 'w') as configfile:cfg.write(configfile)