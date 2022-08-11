
from DREEM_Herschlag.resources import __file__ as resources_file
from DREEM_Herschlag import __file__ as DREEM_Herschlag_file
import yaml, os

class Path(object):
    def __init__(self) -> None:    
        self.resources_file = '/'.join(resources_file.split('/')[:-1])
        self.DREEM_Herschlag_file = '/'.join(DREEM_Herschlag_file.split('/')[:-1])
        self.sample_attribute_path = self.resources_file+'/sample_attributes.yml'
        self.library_attributes_path = self.resources_file+'/library_attributes.yml'
        self.config_template = self.resources_file+'/config-template.yml'

def get_attributes(file, type='txt'):
    path = Path()

    def open_fun(f,type):
        if type == 'txt':
            return f.read()
        if type == 'yml':
            return yaml.safe_load(f)

    if file == 'samples.csv':
        with open(path.sample_attribute_path, 'r') as f:
            attributes = open_fun(f,type)
        f.close()

    if file == 'library.csv':
        with open(path.library_attributes_path, 'r') as f:
            attributes = open_fun(f,type)
        f.close()

    return attributes

def echo_attributes(file):
    attributes = get_attributes(file)
    print(attributes)

def echo_attributes_samples():
    echo_attributes('samples.csv')

def echo_attributes_library():
    echo_attributes('library.csv')

def _write_cols_to_csv(file,all_cols):
    chain = ''
    for col in all_cols:
        chain = chain+ col+','
    with open(file,'w') as f:
        f.write(chain[:-1]+'\n'*3)
        f.close()

def generate_template_samples(exp_env):
    attributes = get_attributes('samples.csv','yml')
    assert exp_env in ['in_vivo','in_vitro'], "exp_env must be 'in_vivo' or 'in_vitro'"
    all_cols = [attributes[a][b] for a in ['mandatory','optional'] for b in ['all',exp_env]][:-1]
    all_cols = [item for sublist in all_cols for item in sublist if item is not None]
    _write_cols_to_csv(f"template_samples_{exp_env}.csv",all_cols)

def generate_template_library():
    attributes = get_attributes('library.csv','yml')
    all_cols = attributes['mandatory']+attributes['optional']
    _write_cols_to_csv(f"template_library.csv",all_cols)

def generate_config_template():
    path = Path()
    with open(path.config_template,'r') as f:
        temp = f.read()
        f.close()
    with open('template_config.yml','w') as f:
        f.write(temp)
        f.close()

def generate_templates():
    generate_template_samples('in_vivo')
    print('template_samples_in_vivo.csv    generated')
    generate_template_samples('in_vitro')
    print('template_samples_in_vitro.csv   generated')
    generate_template_library()
    print('template_library.csv            generated')
    generate_config_template()
    print('template_config.csv             generated')

def generate_mh_only_folder(samples):
    if not os.path.exists('mh_only'):
        os.mkdir('mh_only')
    for s in samples:
        if not os.path.exists('mh_only/'+s):
            os.mkdir('mh_only/'+s)
            os.system(f"cp output/{s}/BitVector_Files/mh.p mh_only/{s}/mh.p")
        print(f"transfered mh.p to mh_only/{s}")