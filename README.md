# CRP_data_mining
Final Year Project on mining cysteine-rich peptide from various protein database

Remember to "pip install pyperclip" if you wish to use the pyperclip function.

Search.py takes input of a long string of protein sequence ( new lines, whitespaces, "-" are acceptable and will be cleaned up) and return Cysteine rich peptides according to parameters : Cysteine_amount(cysteine density) and max_length(maximm length of CRP desired), together with copying the cleaned full sequence to your clipboard automatically using pyperclip function
Search_loop.py performs the same function as Search.py with non-stop executing Search.py after the first search.
Check_duplicates.py takes input of the name of the FASTA file downloaded from the internet and check with the parameter EXCEL_file, returning a new file parameter non_duplicates, do change the filenames of your interest before using.
