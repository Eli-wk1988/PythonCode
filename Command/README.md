<h1 align = center> Python/VS Code 相关指令收集 </h1>
注：如无特殊说明，本文档所列指令基于Windows平台。

### VSCODE虚拟环境激活及设置

在vscode中新建终端，在终端中输入以下指令：<br>
创建虚拟环境：python -m venv .venv <br>
激活虚拟环境：.venv\scripts\activate  <br>

### pip更新
python - m pip install --upgrade pip

### 清华大学PyPi镜像站
单次使用：python -m pip install [待安装库名称] -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

### 查看已安装库
cmd（管理员模式）：pip list

### 生成pyi（已安装mypy库）
stubgen [文件名或路径]

### 生成pyd（已安装cython）
python 路径]setup.py build_ext --inplace
