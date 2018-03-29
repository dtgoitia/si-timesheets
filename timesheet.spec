# -*- mode: python -*-

block_cipher = None


a = Analysis(['src\\timesheet.py'],
             pathex=['C:\\Users\\david-torralba-goiti\\projects\\si-timesheets'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[ 'matplotlib', 'qt5', 'sqlite3', 'numpy', 'pydoc', 'distutils', 'lib2to3', 'pkg_resources', 'pythoncom', 'pytz', 'win32com', 'pywintypes' ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='timesheet',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
