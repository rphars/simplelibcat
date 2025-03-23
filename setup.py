from cx_Freeze import setup, Executable 
  
includefiles = ['libdat.csv']
includes = []
excludes = []
packages = []

setup(name = "homelibcat" , 
      version = "0.1" , 
      description = "" ,
      options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},  
      executables = [Executable("lib.py")]) 
