import yaml
def read_yaml(filename):
    with open(filename,'r',encoding='utf-8')as f:
        data = yaml.safe_load(f)
        return data