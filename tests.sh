#!/bin/bash -xe
python -m SimpleHTTPServer 8000 &
FOO_PID=$!

# parametro -s é o diretorio
# parametro -p é uma regex para dizer quais arquivos procurar
python -m unittest discover -s test -p "*Test*"

kill $FOO_PID