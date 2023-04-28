rem https://osdn.net/projects/winmerge-jp/downloads/78448/WinMerge-2.16.28-jp-4-x64-Setup.exe/
rem 上のリンクはwinmargeのDLりんくです。
rem これをインストールすれば以下のテキスト比較コマンド使用できます。

set path1=C:\Users\keita\Downloads\新三芳WCS239\build.inp
set path2=C:\Users\keita\Downloads\新三芳WCS239_125A\build.inp

start WinMergeU %path1% %path2% /or resut.txt


pause