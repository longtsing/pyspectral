# -*- coding: utf-8 -*-
"""Sphinx 文档配置文件（中文版）。"""

import os
import sys

# 将仓库根加入 sys.path 以便 autodoc 能找到模块
DOC_SOURCES_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath('../'))

# 尝试导入版本号，如果失败则使用默认值
try:
    from pyspectral import __version__ as release  # noqa
    version = '.'.join(release.split('.')[:2])
except (ImportError, ModuleNotFoundError):
    release = '0.0.1'
    version = '0.0'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.todo', 'sphinx.ext.coverage',
              'sphinx.ext.intersphinx', 'sphinx.ext.napoleon',
              'sphinx.ext.imgmath']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Pyspectral'
copyright = u'2013-2021, Pytroll'

# 指定中文（简体）
language = 'zh_CN'

exclude_patterns = ['_build']
pygments_style = 'sphinx'

# 使用原始 doc 下的静态资源（避免重复二进制复制）。
# 如果你希望完全将静态资源拷贝到 docs_zh/_static，
# 可将 html_static_path 设置为 ['_static'] 并手动将文件复制到 docs_zh/_static。
html_static_path = ['../doc/_static']

html_theme = 'default'
htmlhelp_basename = 'Pyspectraldoc'

latex_documents = [
    ('index', 'Pyspectral.tex', u'Pyspectral 文档',
     u'Adam Dybbroe', 'manual'),
]

man_pages = [
    ('index', 'pyspectral', u'Pyspectral 文档',
     [u'Adam Dybbroe'], 1)
]
