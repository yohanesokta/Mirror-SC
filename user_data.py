import pickle

def save_data():
    config = {'fullscreen','hidden'}
    cfg_file = open('user_config.cfg','wb')
    pickle.dump(config,cfg_file)
    cfg_file.close()

def load_data():
    cfg_read_file = open('user_config.cfg','rb')
    config  = pickle.load(cfg_read_file)
    cfg_read_file.close()

    cnt = 0
    for item in config:
        print('The data ', cnt, ' is : ', item)
        cnt += 1