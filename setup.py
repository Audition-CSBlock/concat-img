from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('PyQt/GUI.py', base=base, targetName = 'MergeGUI')
]

setup(name='concat-img',
      version = '1.0',
      description = 'concat images with opencv',
      options = dict(build_exe = buildOptions),
      executables = executables)
