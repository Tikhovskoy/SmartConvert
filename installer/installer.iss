[Setup]
AppName=SmartConvert
AppVersion=1.0
DefaultDirName={pf}\SmartConvert
DefaultGroupName=SmartConvert
OutputDir=.
OutputBaseFilename=SmartConvertSetup
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico

[Files]
Source: "SmartConvert.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "tesseract\*"; DestDir: "{app}\tesseract"; Flags: recursesubdirs ignoreversion
Source: "poppler\*"; DestDir: "{app}\poppler"; Flags: recursesubdirs ignoreversion
Source: "README.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\SmartConvert"; Filename: "{app}\SmartConvert.exe"
Name: "{commondesktop}\SmartConvert"; Filename: "{app}\SmartConvert.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Создать ярлык на рабочем столе"; GroupDescription: "Ярлыки:"; Flags: checkedonce

[Run]
Filename: "{app}\SmartConvert.exe"; Description: "Запустить SmartConvert"; Flags: nowait postinstall skipifsilent
