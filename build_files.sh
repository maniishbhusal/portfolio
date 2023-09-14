# build_files.sh

echo " BUILD START"
python3.11.4 -m pip install -r requirements.txt
python3.11.4 manage.py collectstatic --no-input --clear
echo " BUILD END"