NOTEBOOKS = $(wildcard *.ipynb)

HTML = $(NOTEBOOKS:.ipynb=.html)
MARKDOWN = $(NOTEBOOKS:.ipynb=.md)

all: $(HTML) $(MARKDOWN)
	python3 index.py

.PRECIOUS: %.notes.html %.slides.html %.worksheet.html %.solution.html %.md

%.html: %.slides.html %.notes.html %.worksheet.html %.solution.html ;

%.md: %.ipynb
	jupyter nbconvert $< --to markdown --output='$@'

%.notes.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags "none" --TagRemovePreprocessor.remove_cell_tags  "worksheet-only" --TagRemovePreprocessor.remove_cell_tags  "blank" --TagRemovePreprocessor.remove_cell_tags  "colab-only" --TagRemovePreprocessor.remove_all_outputs_tags "notes-code-only" --no-prompt --to html --output='$@'

%.slides.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_all_outputs_tags "none" --TagRemovePreprocessor.remove_all_outputs_tags "worksheet-code-only" --no-prompt --to slides --output='$*'

%.worksheet.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags "none" --TagRemovePreprocessor.remove_cell_tags "notes-only" --TagRemovePreprocessor.remove_cell_tags "colab-only" --TagRemovePreprocessor.remove_cell_tags "answer" --TagRemovePreprocessor.remove_all_outputs_tags "worksheet-code-only" --no-prompt --to html --output='$@'
    
%.solution.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags "none" --TagRemovePreprocessor.remove_cell_tags  "blank" --TagRemovePreprocessor.remove_cell_tags  "notes-only" --no-prompt --to html --output='$@'

%.colab: %.ipynb
	jupyter nbconvert --to notebook $< --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags "notes-only" --output='$@'

clean:
	rm *.slides.html *.notes.html *.worksheet.html
