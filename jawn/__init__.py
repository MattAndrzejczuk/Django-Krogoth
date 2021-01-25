import subprocess
import sys
import django
import rest_framework
try:
    print('\033[35mPython %s\033[0m' % (str(sys.version)[0:6]))
    print('\033[36mInitializing Django \033[1m' +
          str(django.VERSION[0]) + '.' + str(django.VERSION[1]) + '.' + str(django.VERSION[2]) + '\033[0m\033[0m')
    print('\033[94mDjango REST Framework \033[1m' + str(rest_framework.VERSION) + '\033[0m\033[0m')
    bash_cmd = ['git', 'rev-list', '--count', 'HEAD']
    get_build_cmd = str(subprocess.check_output(bash_cmd))
    current_build_1 = ''
    current_build_2 = ''
    v1 = ''
    v2 = ''
    v3 = ''
    total_commits = int(subprocess.check_output(bash_cmd).decode('utf-8').removesuffix('\n'))
    if total_commits >= 1000:
        as_str = str(total_commits)
        v1 = as_str[:1]
        v2 = as_str[1:2]
        v3 = as_str[2:]
    else:
        as_str = str(total_commits)
        v3 = as_str[1:]
        v2 = as_str[:1]
        v1 = '0'
    if v3 == '00':
        v3 = '0'
    else:
        rm_0s = v3.replace('10', '1').replace('20', '2').replace('30', '3').replace('40', '4')
        v3 = rm_0s.replace('50', '5').replace('60', '6').replace('70', '7').replace('80', '8').replace(
            '90', '9')
    APP_VERSION = v1 + '.' + v2 + '.' + v3
    print('\033[1m\033[92mKrogoth ' + v1 + '.' + v2 + '.' + v3 + ' \033[0m\033[0m')
    print()
except:
    print('\033[31mDjango initialized, but the version is unknown...\033[0m')