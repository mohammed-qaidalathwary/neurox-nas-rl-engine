 %%writefile train.py
from config import Config
from training.cifar10_loader import get_cifar10_loaders

def main():

    print("NeuroX initialized")
    print("Dataset:", Config.dataset)
    print("Device:", Config.device)

    trainloader, testloader = get_cifar10_loaders(Config.batch_size)

    print("Data loaders ready")
    print("Train batches:", len(trainloader))
    print("Test batches:", len(testloader))

if __name__ == "__main__":
    main()
