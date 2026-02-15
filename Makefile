.PHONY: clean

cv.pdf: cv.tex publications.bib
	latexmk -interaction=nonstopmode $<
	@latexmk -c $<

cv.tex: createcv.py cvtemplate.tex private.json cvcompiler.py
	python createcv.py

clean:
	latexmk -C cv.tex
