from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader

# MNIST 데이터셋 로드
mnist_dataset = MNIST(
    root='mnist_offline',         # mnist_offline 폴더를 지정
    train=True,
    download=False,               # 데이터셋이 없으면 자동 다운로드
    transform=transforms.ToTensor()
)

# 데이터 로더
loader = DataLoader(mnist_dataset, batch_size=64, shuffle=True)

# 사용 예시
for images, labels in loader:
    print(images.shape, labels.shape)
    break