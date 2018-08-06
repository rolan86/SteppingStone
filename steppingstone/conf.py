import os
import sys
import subprocess


p = subprocess.Popen(['echo', '$PYTHONPATH'], stdout=subprocess.PIPE)
python_path, err = p.communicate()
dir_path = os.path.dirname(os.path.realpath(__file__))
os.environ['PYTHONPATH'] = ':'.join([python_path, dir_path])
sys.path.append(dir_path)

