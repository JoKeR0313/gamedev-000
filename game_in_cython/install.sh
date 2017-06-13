cp -rf ../game/. ./bin/
cp -rf bin/tests/* ./bin/
rm -r bin/tests
find . -name "*.py" -exec bash -c 'mv "$1" "${1%.py}".pyx' - '{}' \;
find . -name "setup.pyx" -exec bash -c 'mv "$1" "${1%.pyx}".py' - '{}' \;

python3 bin/setup.py build_ext --inplace

mv *.so ./bin/
rm -r build
