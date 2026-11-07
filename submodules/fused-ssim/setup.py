from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    ext_modules=[CUDAExtension(name="fused_ssim_cuda", sources=["ssim.cu", "ext.cpp"])],
    cmdclass={"build_ext": BuildExtension},
)
