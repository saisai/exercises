
r=$1
python -c "import os; print(os.path.abspath('$r').replace('/d/', '/'))" 
