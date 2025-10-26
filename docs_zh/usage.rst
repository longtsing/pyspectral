使用说明
--------

获取 Sentinel-3A OLCI 的光谱响应并打开调试信息：

  >>> from pyspectral.rsr_reader import RelativeSpectralResponse
  >>> from pyspectral.utils import debug_on
  >>> debug_on()
  >>> olci = RelativeSpectralResponse('Sentinel-3A', 'olci')

如果之前未下载过相应数据，pyspectral 会从 Zenodo 自动下载这些光谱响应数据。

示例：简单绘图与带内太阳通量的计算（示例代码与原文一致，注释为中文）。

更多用例包括如何用 3.7 μm 波段计算太阳反射率、如何获取并应用 Rayleigh 校正等（详见原文示例）。
