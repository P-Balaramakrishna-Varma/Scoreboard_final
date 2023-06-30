import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available. PyTorch can access the GPU.")
    
    # Get the count of CUDA devices
    cuda_device_count = torch.cuda.device_count()
    print(f"Number of CUDA Devices: {cuda_device_count}")
    
    # Get the name of CUDA devices
    for i in range(cuda_device_count):
        device_name = torch.cuda.get_device_name(i)
        print(f"Device {i}: {device_name}")

else:
    print("CUDA is not available. PyTorch cannot access the GPU.")
