from ctypes import *
from ctypes.wintypes import *

user32 = windll.user32

GetForegroundWindow = user32.GetForegroundWindow
GetForegroundWindow.argtypes = ()
GetForegroundWindow.restype = HWND

GetWindowTextLengthA = user32.GetWindowTextLengthA
GetWindowTextLengthA.argtypes = (HWND,)
GetWindowTextLengthA.restype = INT

GetWindowTextA = user32.GetWindowTextA
GetWindowTextA.argtypes = (HWND, LPSTR, INT)
GetWindowTextA.restype = INT


def GetForegroundTitle():
    handle = GetForegroundWindow()
    Length = GetWindowTextLengthA(handle)
    Title = create_string_buffer(Length + 1)
    GetWindowTextA(handle, Title, Length + 1)
    return Title.value


print('--------------- WINDOWS API DEMO ---------------')

while True:
    Title = GetForegroundTitle()

    if Title:
        print(f'Foreground Window: {Title.decode("latin-1")}')

    break
