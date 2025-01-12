# Initial environment.yml from https://github.com/yucenli/bnn-bo could not be utilized. 
# Therefore, all version constraints and some specific packages had to be removed.

#Subsequence of Env_Correction/environment_old.yml
yml_file= """name: bnn-bo
channels:
  - pytorch
  - defaults
  - conda-forge
dependencies:
  - _libgcc_mutex=0.1=main
  - _openmp_mutex=5.1=1_gnu
  - asttokens=2.0.5=pyhd3eb1b0_0
  - backcall=0.2.0=pyhd3eb1b0_0
  - ca-certificates=2023.5.7=hbcca054_0
  - debugpy=1.5.1=py39h295c915_0
  - decorator=5.1.1=pyhd3eb1b0_0
  - entrypoints=0.4=pyhd8ed1ab_0
  - executing=0.8.3=pyhd3eb1b0_0
  - ipykernel=6.15.0=pyh210e3f2_0
  - ipython=8.12.0=py39h06a4308_0
  - jedi=0.18.1=py39h06a4308_1
  - jupyter_client=7.0.6=pyhd8ed1ab_0
  - jupyter_core=4.12.0=py39hf3d152e_0
  - ld_impl_linux-64=2.38=h1181459_1
  - libffi=3.4.4=h6a678d5_0
  - libgcc-ng=11.2.0=h1234567_1
  - libgomp=11.2.0=h1234567_1
  - libsodium=1.0.18=h36c2ea0_1
  - libstdcxx-ng=11.2.0=h1234567_1
  - matplotlib-inline=0.1.6=py39h06a4308_0
  - ncurses=6.4=h6a678d5_0
  - nest-asyncio=1.5.6=pyhd8ed1ab_0
  - openssl=1.1.1t=h7f8727e_0
  - packaging=23.1=pyhd8ed1ab_0
  - parso=0.8.3=pyhd3eb1b0_0
  - pcre=8.45=h295c915_0
  - pexpect=4.8.0=pyhd3eb1b0_3
  - pickleshare=0.7.5=pyhd3eb1b0_1003
  - pip=23.0.1=py39h06a4308_0
  - prompt-toolkit=3.0.36=py39h06a4308_0
  - ptyprocess=0.7.0=pyhd3eb1b0_2
  - pure_eval=0.2.2=pyhd3eb1b0_0
  - pygments=2.15.1=py39h06a4308_1
  - python=3.9.16=h7a1cb2a_2
  - python-dateutil=2.8.2=pyhd8ed1ab_0
  - python_abi=3.9=2_cp39
  - pyzmq=19.0.2=py39hb69f2a1_2
  - readline=8.2=h5eee18b_0
  - setuptools=67.8.0=py39h06a4308_0
  - six=1.16.0=pyhd3eb1b0_1
  - sqlite=3.41.2=h5eee18b_0
  - stack_data=0.2.0=pyhd3eb1b0_0
  - tk=8.6.12=h1ccaba5_0
  - tornado=6.1=py39hb9d737c_3
  - traitlets=5.7.1=py39h06a4308_0
  - typing_extensions=4.5.0=py39h06a4308_0
  - tzdata=2023c=h04d1e81_0
  - wcwidth=0.2.5=pyhd3eb1b0_0
  - wheel=0.38.4=py39h06a4308_0
  - xz=5.4.2=h5eee18b_0
  - zeromq=4.3.4=h9c3ff4c_1
  - zlib=1.2.13=h5eee18b_0
  - pip:
      - --extra-index-url https://download.pytorch.org/whl/cu116
      - asdfghjkl==0.1a2
      - backpack-for-pytorch==1.5.2
      - blessed==1.20.0
      - botorch==0.8.5
      - box2d-py==2.3.5
      - certifi==2023.5.7
      - charset-normalizer==3.1.0
      - cloudpickle==2.2.1
      - cmake==3.26.3
      - contourpy==1.0.7
      - cycler==0.11.0
      - einops==0.6.1
      - emcee==3.1.4
      - filelock==3.12.0
      - fonttools==4.39.4
      - gpustat==1.1
      - gpytorch==1.10
      - gym==0.26.2
      - gym-notices==0.0.8
      - idna==3.4
      - importlib-metadata==6.6.0
      - importlib-resources==5.12.0
      - jinja2==3.1.2
      - joblib==1.2.0
      - kiwisolver==1.4.4
      - laplace-torch==0.1a2
      - linear-operator==0.4.0
      - lit==16.0.5
      - llvmlite==0.40.0
      - markupsafe==2.1.2
      - matplotlib==3.7.1
      - mpmath==1.3.0
      - multipledispatch==0.6.0
      - networkx==3.1
      - numba==0.57.0
      - numpy==1.24.3
      - nvidia-cublas-cu11==11.10.3.66
      - nvidia-cuda-cupti-cu11==11.7.101
      - nvidia-cuda-nvrtc-cu11==11.7.99
      - nvidia-cuda-runtime-cu11==11.7.99
      - nvidia-cudnn-cu11==8.5.0.96
      - nvidia-cufft-cu11==10.9.0.58
      - nvidia-curand-cu11==10.2.10.91
      - nvidia-cusolver-cu11==11.4.0.1
      - nvidia-cusparse-cu11==11.7.4.91
      - nvidia-ml-py==11.525.112
      - nvidia-nccl-cu11==2.14.3
      - nvidia-nvtx-cu11==11.7.91
      - opencv-python==4.7.0.72
      - opt-einsum==3.3.0
      - pillow==9.5.0
      - psutil==5.9.5
      - py-pde==0.31.0
      - pygame==2.1.0
      - pyparsing==3.0.9
      - requests==2.31.0
      - scikit-learn==1.2.2
      - scipy==1.10.1
      - swig==4.1.1
      - sympy==1.12
      - threadpoolctl==3.1.0
      - torch==1.12.0
      - torchaudio==0.12.0+cu116
      - torchvision==0.13.0+cu116
      - tqdm==4.65.0
      - triton==2.0.0
      - urllib3==2.0.2
      - zipp==3.15.0"""

#Error message when executing "conda env create -f environment.yml"
error_msg=  """
  - tk==8.6.12=h1ccaba5_0
  - python==3.9.16=h7a1cb2a_2
  - matplotlib-inline==0.1.6=py39h06a4308_0
  - libffi==3.4.4=h6a678d5_0
  - libgcc-ng==11.2.0=h1234567_1
  - sqlite==3.41.2=h5eee18b_0
  - ncurses==6.4=h6a678d5_0
  - ca-certificates==2023.5.7=hbcca054_0
  - _openmp_mutex==5.1=1_gnu
  - pygments==2.15.1=py39h06a4308_1
  - zeromq==4.3.4=h9c3ff4c_1
  - prompt-toolkit==3.0.36=py39h06a4308_0
  - setuptools==67.8.0=py39h06a4308_0
  - tornado==6.1=py39hb9d737c_3
  - pip==23.0.1=py39h06a4308_0
  - debugpy==1.5.1=py39h295c915_0
  - typing_extensions==4.5.0=py39h06a4308_0
  - wheel==0.38.4=py39h06a4308_0
  - pcre==8.45=h295c915_0
  - libgomp==11.2.0=h1234567_1
  - jedi==0.18.1=py39h06a4308_1
  - jupyter_core==4.12.0=py39hf3d152e_0
  - libstdcxx-ng==11.2.0=h1234567_1
  - libsodium==1.0.18=h36c2ea0_1
  - ld_impl_linux-64==2.38=h1181459_1
  - traitlets==5.7.1=py39h06a4308_0
  - readline==8.2=h5eee18b_0
  - zlib==1.2.13=h5eee18b_0
  - xz==5.4.2=h5eee18b_0
  - ipython==8.12.0=py39h06a4308_0
  - pyzmq==19.0.2=py39hb69f2a1_2
  - openssl==1.1.1t=h7f8727e_0
  """

#Setup two lists, tracking the start and end indices of version constraints to be deleted.
start_delete= []
end_delete= []

found_equal= False #After each occurence of an equal sign, the version constraint is has a variable amount of characters and ends with the next occurence of "\n".
for yml_file_index in range(len(yml_file)):
    if not found_equal:
        if yml_file[yml_file_index] == "=":
            start_delete.append(yml_file_index) #including
            found_equal= True

    if found_equal:
        if yml_file[yml_file_index] == "\n":
            end_delete.append(yml_file_index) #excluding
            found_equal= False

end_delete.append(len(yml_file)) #Manually add end of last version constraint sequence (not followed by "\n").

yml_file_new= ""
first= True
for i in range(len(start_delete)):
    if first:
        yml_file_new+= yml_file[:start_delete[i]]
        first= False
    else:
        yml_file_new+= yml_file[(end_delete[i-1]) : start_delete[i]]
print(yml_file_new)
