# -*- mode: python ; coding: utf-8 -*-

datas_list = [ 
    ('Resources/', 'Resources/'), 
    ('Generator/', 'Generator/'), 
    ('prompts.yml', './'),
    ('Help/', 'Help/'),
    ('HDLDesigner/', 'HDLDesigner/')
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas_list,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
	icon='Resources/blue_logo.png',
	name='HDLGen-ChatGPT.exe',
)
