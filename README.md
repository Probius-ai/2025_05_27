# MNIST 오프라인 데이터셋 PyTorch & TensorFlow 예제

이 저장소는 오프라인 MNIST 데이터셋을 PyTorch와 TensorFlow에서 불러오는 예제 코드를 제공합니다.

## 권장 Python 버전
- Python 3.9 ~ 3.11 버전을 권장합니다. (최신 macOS/Windows 및 주요 딥러닝 프레임워크와 호환)

## 폴더 구조
```
2025_05_27/
├── mnist_offline/
│   ├── mnist.npz
│   └── raw/
│       ├── train-images-idx3-ubyte.gz
│       ├── train-labels-idx1-ubyte.gz
│       ├── t10k-images-idx3-ubyte.gz
│       └── t10k-labels-idx1-ubyte.gz
├── pytorch_data_load.py
├── tf_data_load.py
├── requirements.txt           # macOS (Apple Silicon)용
├── requirements_win.txt       # Windows용
```

## 1. 가상환경(.venv) 만들기 및 패키지 설치

### macOS (Apple Silicon, m4/M3/M2/M1)
```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Windows
```cmd
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements_win.txt
```

## 2. 예제 코드 실행

### PyTorch (pytorch_data_load.py)
```sh
python pytorch_data_load.py
```

### TensorFlow (tf_data_load.py)
```sh
python tf_data_load.py
```

## 3. 데이터셋 준비
- `mnist_offline/MNIST/raw/` 폴더에 MNIST의 4개 .gz 파일이 있어야 합니다.
- 또는, `mnist_offline/mnist.npz` 파일이 있어야 합니다.
- PyTorch는 `raw/` 폴더의 .gz 파일을, TensorFlow는 npz 파일을 사용합니다.
- 처음 실행 시 자동 다운로드도 지원합니다.

## 참고
- macOS에서는 `tensorflow-macos`, `tensorflow-metal`을 사용합니다.
- Windows에서는 공식 `tensorflow`만 사용합니다.
- Python 3.9~3.11 버전을 권장합니다.
