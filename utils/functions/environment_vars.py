import os

def print_env_vars():
    print(
        "\n\nTO USE THE PYCHARM DJANGO CONSOLE ON A LOCAL DOCKER CONTAINER, ADD THIS CODE TO THE TOP OF THE STARTING SCRIPT AT: ")
    carrot = '\033[91m' + ">" + '\033[0m'
    print(
    '\033[36m' + "Preferences " + carrot + " Build, Execution, Deployment " + carrot + "  Console " + carrot + "  Django Console" + '\033[0m')

    os.system('sleepm 1')
print('\033[95m' + "GENERATED KROGOTH ENVIRONMENT " + '\033[0m')

red = '\033[31m'
ENDC = '\033[0m'
lightblue = '\033[94m'
print('\033[33m' + "\n\nTO USE THE PYCHARM DJANGO CONSOLE, ADD THIS TO THE TOP OF THE STARTING SCRIPT: \n\n\n" + ENDC)
print("import os")
print("os.environ = {}")
for k, v in os.environ.items():
    os.environ[k] = v
    print("os.environ['" + red + k + "", end=(ENDC + "'] = '" + lightblue + v + ENDC + "'\n"))
