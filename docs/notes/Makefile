NOTEBOOKS = $(wildcard *.ipynb)

HTML = $(NOTEBOOKS:.ipynb=.html)

all: $(HTML)
	python3 index.py

.PRECIOUS: %.notes.html %.slides.html %.worksheet.html

%.html: %.notes.html %.slides.html %.worksheet.html ;

%.notes.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags='["none", "worksheet-only", "colab-only"]' --TagRemovePreprocessor.remove_all_outputs_tags='["notes-code-only"]' --to html --output='$@'

%.slides.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_all_outputs_tags='["none", "worksheet-code-only"]' --to slides --output='$*'

%.worksheet.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags='["none", "notes-only", "colab-only"]' --TagRemovePreprocessor.remove_all_outputs_tags='["worksheet-code-only"]' --output='$@'

%.colab: %.ipynb
	jupyter nbconvert --to notebook $< --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags='["notes-only"]' --output='$@'

clean:
	rm *.html
