import configparser
CFpraser = configparser.ConfigParser()

def save_data():
    CFpraser.read('user_config.cfg')
    return CFpraser

def syncConfig(Var,Config,input):
    if input == 'box':
        var = CFpraser.get('User',Config)
        if var == 'True':
            Var.select()
        else:
            Var.deselect()

    # resolusi input

    if input == 'Option':
        Var.set(CFpraser.get('User',Config))

# def load_data():