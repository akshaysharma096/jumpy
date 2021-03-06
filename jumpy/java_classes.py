import jnius_config
import os

jnius_config.add_options('-Dorg.bytedeco.javacpp.nopointergc=true')
jnius_class_path = os.environ.get('JUMPY_CLASS_PATH')
if not jnius_class_path:
	raise Exception('Environment variable JUMPY_CLASS_PATH not set.')
elif not os.path.exists(jnius_class_path):
	raise Exception('File not found : ' + jnius_class_path)
jnius_config.set_classpath(jnius_class_path)

from jnius import autoclass

Nd4j = autoclass('org.nd4j.linalg.factory.Nd4j')
INDArray = autoclass('org.nd4j.linalg.api.ndarray.INDArray')
Transforms = autoclass('org.nd4j.linalg.ops.transforms.Transforms')
NDArrayIndex = autoclass('org.nd4j.linalg.indexing.NDArrayIndex')
DataBuffer = autoclass('org.nd4j.linalg.api.buffer.DataBuffer')
System = autoclass('java.lang.System')
Integer = autoclass('java.lang.Integer')
Float = autoclass('java.lang.Float')
Double = autoclass('java.lang.Double')
Shape = autoclass('org.nd4j.linalg.api.shape.Shape')
BinarySerde = autoclass('org.nd4j.serde.binary.BinarySerde')
NativeOpsHolder = autoclass('org.nd4j.nativeblas.NativeOpsHolder')
DoublePointer = autoclass('org.bytedeco.javacpp.DoublePointer')
FloatPointer = autoclass('org.bytedeco.javacpp.FloatPointer')
IntPointer = autoclass('org.bytedeco.javacpp.IntPointer')
DataTypeUtil = autoclass('org.nd4j.linalg.api.buffer.util.DataTypeUtil')
MemoryManager = autoclass('org.nd4j.linalg.memory.MemoryManager')
SameDiff = autoclass('org.nd4j.autodiff.samediff.SameDiff')
