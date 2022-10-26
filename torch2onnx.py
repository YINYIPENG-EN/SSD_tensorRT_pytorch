import onnx
from nets.ssd import get_ssd
import torch
from onnxsim import simplify
import numpy as np

Simplity = True

output_path = "model_data/ssd.onnx"
num_classes = 21
model = get_ssd('train', num_classes)
model_dict = model.state_dict()
device = torch.device('cuda')
ckpt = torch.load('./model_data/ssd_weights.pth',map_location=device)
ckpt = {k: v for k, v in ckpt.items() if np.shape(model_dict[k]) == np.shape(ckpt[k])}
model_dict.update(ckpt)
model.load_state_dict(model_dict)
model.eval()
model.to(device)
x = torch.zeros(1, 3, 300, 300).to(device)
output_names = ["output0","output1", "output2"]
input_names = ["images"]
torch.onnx.export(model, x, output_path, verbose=True, input_names=input_names,
                  output_names=output_names, do_constant_folding=True, opset_version=12)
if Simplity:
    onnx_model = onnx.load(output_path)  # load onnx model
    model_simp, check = simplify(onnx_model)
    assert check, "Simplified ONNX model could not be validated"
    onnx.save(model_simp, output_path)
    print('finished exporting onnx')