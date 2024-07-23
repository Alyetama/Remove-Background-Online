# -*- coding: utf-8 -*-

from pathlib import Path
from urllib import request

# Đường dẫn đến thư mục và tệp mô hình
model_dir = Path('/.u2net')
model_path = model_dir / 'u2net.onnx'

# Tạo thư mục nếu chưa tồn tại
model_dir.mkdir(parents=True, exist_ok=True)

# URL của mô hình
model_url = 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_human_seg.onnx'

# Tải xuống mô hình
request.urlretrieve(model_url, model_path)