from onnxruntime.quantization import (
    quantize_dynamic,
    QuantType
)

quantize_dynamic(
    model_input="yolov8m-seg.onnx",
    model_output="yolov8m-seg-int8.onnx",
    weight_type=QuantType.QInt8
)

print("INT8 model saved")