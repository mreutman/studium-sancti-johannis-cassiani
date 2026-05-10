all: latex pdf

latex:
	./psalms/psalms-basic.py > psalms-all.tex

pdf:
	xelatex -halt-on-error ./psalter.tex

clean:
	rm -fv psalter.aux
	rm -fv psalter.log
	rm -fv psalter.pdf
	rm -fv psalter.log
