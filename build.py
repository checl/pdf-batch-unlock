#!/usr/bin/env python3
"""把 template.html 與 qpdf 引擎打包成單一檔案 index.html。

用法：python3 build.py
產生的 index.html 不需要網路，用瀏覽器開啟即可使用。
"""
import base64, pathlib

root = pathlib.Path(__file__).parent
tpl = (root / "template.html").read_text(encoding="utf-8")
js = (root / "qpdf.js").read_text(encoding="utf-8")
wasm = base64.b64encode((root / "qpdf.wasm").read_bytes()).decode()

# 讓 qpdf 直接使用內嵌的 wasm，不必再從網路或磁碟讀取
js = js.replace(
    "async function Fa(a){var b=Ca;",
    "async function Fa(a){if(f.wasmBinary)return WebAssembly.instantiate(f.wasmBinary,a);var b=Ca;",
).replace('Ca??=Ba("qpdf.wasm")', 'Ca??=f.wasmBinary?"embedded.wasm":Ba("qpdf.wasm")')

body = tpl.replace("/*QPDF_JS*/", js).replace("/*WASM_B64*/", wasm)
page = (
    '<!doctype html>\n<html lang="zh-Hant-TW">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    + body.replace('<div class="wrap">', '</head>\n<body>\n<div class="wrap">', 1)
    + "\n</body>\n</html>\n"
)
(root / "index.html").write_text(page, encoding="utf-8")
print("已產生 index.html，大小 %.1f MB" % (len(page.encode()) / 1048576))
