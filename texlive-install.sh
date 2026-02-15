#!/bin/bash
sudo apt install -y latexmk \
  texlive-latex-extra \
  texlive-fonts-extra \
  texlive-lang-italian \
  texlive-luatex \
  cm-super

wget https://mirrors.ctan.org/macros/latex/contrib/moderncv.zip
unzip moderncv.zip

