.PHONY: clean ita eng all

all: ita eng

# Sugar recipes
ita: cv_ita.pdf

eng: cv_eng.pdf

# Working recipes
%.pdf: %.tex publications.bib
	latexmk -interaction=nonstopmode $<
	@latexmk -c $<

cv_ita.tex: createcv.py cvtemplate.tex private.json cvcompiler.py
	python createcv.py ita

cv_eng.tex: createcv.py cvtemplate.tex private.json cvcompiler.py
	python createcv.py eng

clean:
	@latexmk -C cv_ita.tex
	@latexmk -C cv_eng.tex
	@rm cv_ita.tex cv_eng.tex
