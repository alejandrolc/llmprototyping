import os
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
import sys
sys.path.insert(0,"../src")
import llmprototyping
print(llmprototyping.__file__)
print('-'*20)