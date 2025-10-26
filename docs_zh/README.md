# PySpectral 中文文档

本目录包含 PySpectral 项目的中文翻译文档。

## 快速构建

### Windows 系统

在项目根目录运行：

```cmd
cd docs_zh
python -m sphinx -b html . _build/html
```

或使用提供的批处理文件：

```cmd
cd docs_zh
make.bat html
```

### Linux / macOS 系统

```bash
cd docs_zh
make html
```

构建完成后，HTML 文档位于 `docs_zh/_build/html/index.html`。

## 目录结构

- `conf.py` - Sphinx 配置文件（已设置 `language = 'zh_CN'`）
- `index.rst` - 中文文档主页
- `*.rst` - 各章节的中文翻译文档
- `Makefile` / `make.bat` - 构建脚本
- `_build/` - 构建输出目录（git 忽略）

## 静态资源

静态资源（图片等）当前指向原始 `doc/_static` 目录（通过 `conf.py` 中的 `html_static_path = ['../doc/_static']`）。如需完全独立的中文文档目录，可将 `doc/_static` 复制到 `docs_zh/_static` 并相应修改 `conf.py`。

## API 文档

要生成完整的 API 文档（包含自动生成的模块文档），需要先安装 pyspectral 包：

```bash
pip install -e .
```

然后再运行构建命令。

## 翻译说明

本文档保持了原始英文文档的所有 Sphinx 指令、数学公式、代码示例和交叉引用，仅翻译了说明性文本。如发现翻译错误或建议改进，欢迎提交 PR。

## 相关链接

- 英文文档源：`../doc/`
- PySpectral 项目：https://github.com/pytroll/pyspectral
