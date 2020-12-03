#!/bin/bash
set -e
sudo -u ec2-user -i <<'EOF'

source activate pytorch_p36

curl -sL https://rpm.nodesource.com/setup_12.x | sudo -E bash -
sudo yum install -y nodejs

pip install numpy
pip install pandas
pip install matplotlib
pip install bamboolib
pip install sklearn
pip install sktime

python -m bamboolib install_nbextensions
python -m bamboolib install_labextensions

source deactivate

EOF
