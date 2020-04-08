NOTEBOOKS = $(wildcard *.ipynb)

HTML = $(NOTEBOOKS:.ipynb=.html)

all: $(HTML)
	python3 index.py

.PRECIOUS: %.notes.html %.slides.html %.worksheet.html

%.html: %.notes.html %.slides.html %.worksheet.html ;

%.notes.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags='["worksheet-only"]'  --execute --ExecutePreprocessor.allow_errors=True --TagRemovePreprocessor.remove_all_outputs_tags='["notes-code-only"]' --output='$@'

%.slides.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_all_outputs_tags='["worksheet-code-only"]' --to slides --output='$*'

%.worksheet.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags='["notes-only", "colab-only"]' --TagRemovePreprocessor.remove_all_outputs_tags='["worksheet-code-only"]' --output='$@'

%.colab: %.ipynb
	jupyter nbconvert --to notebook $< --TagRemovePreprocessor.remove_cell_tags='["notes-only"]' --TagRemovePreprocessor.remove_all_outputs_tags='["worksheet-code-only"]' --output='$@'

clean:
	rm *.html
