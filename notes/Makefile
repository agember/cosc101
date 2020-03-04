


all:
	jupyter nbconvert 2020-03-04.ipynb --TagRemovePreprocessor.remove_cell_tags='["worksheet-only"]' --output='2020-03-04.notes.html'
	jupyter nbconvert 2020-03-04.ipynb --TagRemovePreprocessor.remove_cell_tags='["notes-only"]' --TagRemovePreprocessor.remove_all_outputs_tags='["worksheet-code-only"]' --output='2020-03-04.worksheet.html'
	jupyter nbconvert 2020-03-04.ipynb --TagRemovePreprocessor.remove_all_outputs_tags='["worksheet-code-only"]' --to slides --output='2020-03-04'
