# Make Virtual Environment
virtualenv iposter-env
source iposter-env/Scripts/activate

# Install Dependencies
pip install dash
pip install plotly
pip install pandas
pip install dash-bootstrap-components
pip install pypng
pip install pyqrcode
pip install gunicorn

# Deactivate VE
deactivate
