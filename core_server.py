import os
def run_server():
    project_path = os.path.dirname(os.path.realpath(__file__))
    credentials_file = os.path.join(project_path, 'credentials.yml')
    model_path = os.path.join(project_path, 'models', 'default', 'current')
    dialogue_path = os.path.join(project_path, 'models', 'default', 'current', 'dialogue')
    endpoints_file = os.path.join(project_path, 'endpoints.yml')
    f = os.popen(r"python -m rasa_core.run -d %s -u %s --credentials %s --cors * --endpoints %s" % (
        dialogue_path, model_path, credentials_file,endpoints_file,), "r")

    d = f.read()  # 读文件
    print(d)
    print(type(d))
    f.close()

if __name__ == '__main__':
    run_server()