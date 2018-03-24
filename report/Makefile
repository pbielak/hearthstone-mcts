all: compile clean

compile: document.tex
	pdflatex -shell-escape document.tex
	pdflatex -shell-escape document.tex

clean:
	find . \( -name "*.aux" -or -name "*.bbl" -or \
  	          -name "*.bcf" -or -name "*.blg" -or \
      	          -name "*.lof" -or -name "*.log" -or \
      		  -name "*.lot" -or -name "*.lol" -or \
		  -name "*.nav" -or -name "*.out" -or \
		  -name "*.snm" -or -name "*.toc" -or \
		  -name "*.xml" -or -name "*.vrb" -or \
		  -name "*.pyg" -or -name "*.listing" \) \
		  -type f -delete
	rm -rf _minted-document/

