dist: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: dist

clean:
	rm -rf dist
