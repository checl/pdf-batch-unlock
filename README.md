# PDF 批次解鎖工具

一次移除多個 PDF 的密碼，產生沒有密碼的新檔。整個過程都在瀏覽器裡完成，**檔案不會上傳到任何伺服器**，密碼也不會被記錄。

👉 **直接使用：** https://checl.github.io/pdf-batch-unlock/

不想用網路版，也可以下載 [`index.html`](index.html)，存到電腦後用瀏覽器開啟，離線一樣能用。

## 使用方式

1. 點選取區，或把 PDF 拖曳進去，可一次加入多個檔案。
2. 輸入密碼，按「開始解鎖」。
3. 逐一按「下載」，或按「全部下載（ZIP）」一次取回。
4. 下載過的檔案會標成「已下載」，按「移除已下載」清掉它們，接著處理下一批。

解出來的新檔名為 `原檔名_無密碼.pdf`，原始檔案不會被更動。

## 功能

- 多檔批次處理，同一組密碼一次解完
- 密碼不同的檔案會標示出來，換密碼再按一次只重試失敗的檔案
- 只有「權限密碼」（能開啟但禁止列印或複製）的檔案，不需密碼也會自動解除限制
- ZIP 打包下載，支援中文檔名
- 淺色／深色主題，手機瀏覽器也能用

已用 40 位元 RC4、128 位元 RC4、256 位元 AES 等常見加密方式測試，輸出檔確認無密碼且內容完整。

本工具只處理你知道密碼的檔案，不具破解功能。

## 檔案結構

```
index.html      可直接使用的單一檔案（已內嵌解鎖引擎）
template.html   頁面原始碼（版面與程式邏輯）
qpdf.js         qpdf 的 WebAssembly 載入程式
qpdf.wasm       qpdf 的 WebAssembly 引擎
build.py        打包腳本，把上面三個檔案合成 index.html
```

修改 `template.html` 後執行 `python3 build.py` 即可重新產生 `index.html`。

## 技術說明

解鎖引擎是 [qpdf](https://github.com/qpdf/qpdf) 編譯成的 WebAssembly 版本（[@neslinesli93/qpdf-wasm](https://www.npmjs.com/package/@neslinesli93/qpdf-wasm)），以 base64 內嵌於 `index.html`，因此單一檔案即可運作，不需安裝軟體也不需連網。ZIP 打包由頁面內的程式自行產生（不壓縮，使用 UTF-8 檔名旗標）。

## 授權

頁面程式碼採 MIT 授權。qpdf 本身採 Apache-2.0 授權，版權屬原作者。
