import os

def train_nlu():
    project_path = os.path.dirname(os.path.realpath(__file__))
    model_file = os.path.join(project_path, 'nlu_model_config.yaml')
    nlu_file = os.path.join(project_path, 'nlu.json')
    output_path = os.path.join(project_path, 'models')
    f = os.popen(r"python -m rasa_nlu.train -c %s -d %s --fixed_model_name current -o %s" % (
        model_file, nlu_file, output_path), "r")

    d = f.read()  # 读文件
    print(d)
    print(type(d))
    f.close()
def train_core():
    project_path = os.path.dirname(os.path.realpath(__file__))
    domain_file = os.path.join(project_path, 'domain.yml')
    stories_file = os.path.join(project_path, 'stories.md')
    output_path = os.path.join(project_path, 'models','default','current', 'dialogue')
    model_file = os.path.join(project_path, 'nlu_model_config.yaml')
    f = os.popen(r"python -m rasa_core.train -d %s -s %s -o %s -c %s" % (
        domain_file, stories_file, output_path,model_file), "r")

    d = f.read()  # 读文件
    print(d)
    print(type(d))
    f.close()
if __name__ == '__main__':
    train_nlu()
    train_core()