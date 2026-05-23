all: latex pdf

latex:
	./psalms/psalms-basic.py > psalms-all.tex
	./psalms/odes.py > odes-all.tex

pdf:
	xelatex -halt-on-error -shell-escape ./psalter.tex

clean:
	rm -fv psalter.aux
	rm -fv psalter.log
	rm -fv psalter.pdf
	rm -fv psalter.log
