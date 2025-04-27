@echo off
echo Iniciando Redis Server...

start "" "C:\Redis-x64-3.0.504 (1)\redis-server.exe"

timeout /t 3

echo Gerando o arquivo data.txt...
start cmd /k "py generate_data.py"

timeout /t 5

echo Iniciando Mapper...
start cmd /k "py mapper.py"

timeout /t 2

echo Iniciando Reducer...
start cmd /k "py reducer.py"

timeout /t 2

echo Iniciando main...
start cmd /k "py main.py"