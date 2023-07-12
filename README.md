python "main.py" --project_name "project" --training_model "/home/softzen/dreambooth/dreambooth/majicmixRealistic_v4.safetensors" --regularization_images "/home/softzen/dreambooth/dreambooth/regularization_images" --training_images "/home/softzen/dreambooth/dreambooth/training-images" --max_training_steps 3000 --class_word "person" --token "zwx" --flip_p 0 --learning_rate 1.0e-06 --save_every_x_steps 0

1.
python 3.10버전 설치
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
pip install -r requirements.txt
2.
vi main.py
sys.path.append('/home/softzen/.local/lib/python3.10/site-packages')
3.
pip install --upgrade setuptools
4.
pip install backports.lzma

cd /usr/local/lib/python3.10
vi lzma.py 
try:
    from _lzma import *
    from _lzma import _encode_filter_properties, _decode_filter_properties
except ImportError:
    from backports.lzma import *
    from backports.lzma import _encode_filter_properties, _decode_filter_properties

5.
pip install taming-transformers-rom1504

6.
pip install git+https://github.com/openai/CLIP.git
