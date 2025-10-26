SEVIRI 示例
------------

下面给出一个使用 SEVIRI 数据计算 3.9 μm 反射率的示例：

.. doctest::

  >>> sunz = 80.
  >>> tb3 = 290.0
  >>> tb4 = 282.0
  >>> from pyspectral.near_infrared_reflectance import Calculator
  >>> refl39 = Calculator('Meteosat-10', 'seviri', 'IR3.9')
  >>> print('{refl:4.3f}'.format(refl=refl39.reflectance_from_tbs(sunz, tb3, tb4)[0]))
  0.555

可以将带内太阳通量从外部传入以节省计算时间（示例见原文）。

文末说明了与 SatPy 的集成可以很容易地在 RGB 合成中使用 3.9 μm 反射率。
