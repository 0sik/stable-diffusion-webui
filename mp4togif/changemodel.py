import torch

model = torch.load('majicmixRealistic_v6.safetensors')

torch.save(model.state_dict(), 'Realistic.ckpt')
