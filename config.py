class Config:

    # Dataset
    dataset = "CIFAR10"

    # Training
    batch_size = 128
    epochs = 10
    learning_rate = 3e-4

    # Reinforcement Learning
    gamma = 0.99
    clip_epsilon = 0.2

    # NAS
    max_layers = 6

    # Device
    device = "cuda"
