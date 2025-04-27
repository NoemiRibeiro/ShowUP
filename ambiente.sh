
pip install --user pipx 
#sudo apt install pipx
pipx ensurepath
pipx install poetry

poetry self add poetry-plugin-shell
#sudo apt install python3-poetry

#poetry python install 3.13
poetry env use 3.13
poetry install
poetry add 'fastapi[standard]'

poetry run fastapi dev fast_zero/app.py