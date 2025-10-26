.. Pyspectral 文档（中文）主文件

欢迎使用 Pyspectral 文档！
===========================

.. figure:: _static/pyspectral_header_montage.png


给定一个气象卫星上的被动传感器，PySpectral 提供相对光谱响应（rsr）函数并提供一些基础操作，例如与太阳谱卷积以推导带内太阳通量。重点为成像传感器（如 AVHRR、VIIRS、MODIS、ABI、AHI 和 SEVIRI），但也包含了更多传感器，且可以轻松添加新的传感器。

使用 PySpectral 可以在 3-4 微米附近的近红外波段分离反射（太阳回散射）和发射（地表热辐射）成分。此外，PySpectral 可用于对真实色彩图像进行背景（气候学）Rayleigh 散射和气溶胶吸收订正。

源代码可在 github_ 页面找到。

借助 PySpectral 与 SatPy_ 的集成（或早期的 mpop_），可以生成诸如 SEVIRI 的 `day solar`_ 或 `day microphysical`_ 等 RGB 合成图像，符合 `MSG Interpretation Guide`_ （EUMETSAT_）。通过 SatPy_ 的集成还可以生成大气校正后的真实色彩图像。

.. _`EUMETSAT`: http://www.eumetsat.int/
.. _`day solar`: _static/msg_daysolar_rgb_20131129_1100_overlay_small.png
.. _`day microphysical`: _static/msg_day_microphysics_summer_rgb_20131129_1100_overlay_small.png
.. _github: http://github.com/pytroll/pyspectral
.. _mpop: http://www.github.com/pytroll/mpop
.. _SatPy: http://www.github.com/pytroll/satpy
.. _MSG Interpretation Guide: https://resources.eumetrain.org/IntGuide/


.. toctree::
   :maxdepth: 2

   platforms_supported
   installation
   usage
   rsr_plotting
   seviri_example
   rad_definitions
   37_reflectance
   rayleigh_correction
   rsr_formatting
   api


索引与表格
===========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
