# A builder for curriculum vitae

I set up this script to have a manageable CV. At least, this has less friction than the europass site, at least for my necessity.

If you are brave enough you can read the CV directly in the python script `createcv.py` to check it.
But I recomend to run the `texlive-install.sh` script,and install the python packages wihn `pip install -r requirements.txt` (possibly in a virtual environment), and finally run make.
You will need to have pandas installed, or to adapt the `texlive-install.sh` script to your package manager (it is currently aimed at running on ubuntu with `apt`)
(Or more simply dowload the cv from the release that I setup)

---

###### Note:

I have included the modercv package as a subfolder with its License.
I do not own moderncv. I included it to avoid compatibility problems, my photo occupies more space, so, spacewise should not be a problem.

