# eiics.spec
block_cipher = None

a = Analysis(
    ['src/eiics/main_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/eiics/default_images/*.png', 'eiics/default_images'),
        ('src/eiics/default_images/*.jpg', 'eiics/default_images'),
        ('src/eiics/default_images/*.jpeg', 'eiics/default_images'),
        ('src/eiics/help_content.py', 'eiics'),
        ('src/eiics/crypto_engine.py', 'eiics'),
        ('src/eiics/stego_engine.py', 'eiics'),
        ('assets/icon.ico', 'assets'),
        ('assets/icon.png', 'assets'),
        ('assets/icon.icns', 'assets'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='eiics',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico',  # This sets the executable icon on Windows
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='eiics',
)