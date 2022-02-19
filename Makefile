pre-build:
	@pip install --upgrade pip
	@pip install --upgrade build
	@pip install --upgrade twine
	echo "Done!"

build:
	python3 -m build
	python3 -m twine upload --repository pypi dist/*

help:
	echo "commands: pre-build\nbuild"
