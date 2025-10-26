安装
----

安装最新稳定版的最简单方法是使用 pip::

  $> pip install pyspectral

部分静态数据包含在包中。当需要这些数据时，软件会自动下载。但也可以在一次性手动下载这些数据，这在生产环境中比较有用。下面会说明静态数据的获取方式。

也可以从 github_ 克隆源码::

  $> git clone git://github.com/pytroll/pyspectral.git

然后运行::

  $> python setup.py install

如果要以开发模式安装以便修改源码::

  $> python setup.py develop


静态数据
--------

PySpectral 使用两类静态辅助数据：一是许多卫星传感器的相对光谱响应（统一为 HDF5 格式），二是用于短波段大气校正的查找表（LUTs）。

这些数据通常会在需要时从 `zenodo.org`_ 自动下载，默认放在平台特定的用户数据目录（通过 platformdirs_）。在 Linux 下通常是 ``~/.local/share/pyspectral`` 。


光谱响应数据
^^^^^^^^^^^^^

PySpectral 为多种卫星传感器提供相对光谱响应函数。原始数据来源与格式各异，项目将其统一为内部 HDF5 格式，便于添加新仪器支持。数据也可通过随包提供的脚本手动下载（示例命令见原文）。


大气校正 LUTs
^^^^^^^^^^^^^

用于可见光谱（约 400-600 nm) 的大气校正查找表可在 `zenodo.org`_ 上获得，软件会在需要时下载并放在与光谱响应数据相同的目录结构中。也可用脚本手动下载（示例命令见原文）。


配置文件
^^^^^^^^

包内包含默认的 ``pyspectral.yaml`` （位于 ``etc`` 目录）。你可以通过设置环境变量让程序使用自定义配置文件，例如：:::

  $> PSP_CONFIG_FILE=/path/to/pyspectral.yaml; export PSP_CONFIG_FILE

在配置中可以指定 rsr 和 rayleigh 数据的目录以及是否从网络下载等选项（示例请参见原文）。

.. _zenodo.org: https://zenodo.org
.. _platformdirs: https://github.com/platformdirs/platformdirs
.. _github: http://github.com/pytroll/pyspectral
