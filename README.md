# XYZ Web 自動化測試專案

本專案使用 [Selenium WebDriver](https://www.selenium.dev/)、[pytest](https://docs.pytest.org/) 進行網站自動化測試，搭配 Docker-based Selenium Grid 執行於 CI/CD 環境中。

---


## 📁 專案檔案結構

```
XYZproject/
├── page/             # Page頁面目錄
├── script/             # 測試案例目錄
├── run-tests.sh       # 一鍵執行測試腳本
├── requirements.txt   # 測試套件清單
├── .env.example       # 環境變數設定
└── Dockerfile         # 測試容器建立檔
```

### Page Object Model 架構說明

本專案遵循 POM（Page Object Model）設計模式，將網頁中每個頁面封裝為一個對應的 Python 類別，封裝其元素定位與操作邏輯，讓測試案例保持簡潔、可維護。

- `page/`：封裝各頁面操作方法與元素
- `script/`：引用 page object，撰寫實際測試情境

例如：
```python
# 使用 POM：登入測試範例
login_page = LoginPage(driver)
login_page.go_to_login_page()
login_page.enter_credentials("user", "pass")
assert login_page.is_login_successful()
```


---



## 🚀 快速開始

### 啟動 Selenium Grid（第一次使用時）

```bash
docker-compose up -d
```

啟動後可打開 Grid UI 檢查狀態：
[http://localhost:4444/ui](http://localhost:4444/ui)

### 安裝相依套件

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 執行測試（透過 Selenium Grid）

```bash
SELENIUM_REMOTE_URL=http://localhost:4444/wd/hub pytest script/test_xyz_home.py
```

---

## 🐳 與 Selenium Grid 整合

搭配 [selenium-grid-config](https://github.com/MarkTsaiCqi/selenium-grid-config) 專案，快速部署 Selenium 測試環境：

```bash
git clone https://github.com/MarkTsaiCqi/selenium-grid-config
cd selenium-grid-config
docker-compose up -d
```

啟動後即可透過 Grid UI 確認狀態：[http://localhost:4444/ui](http://localhost:4444/ui)

---


## 📄 環境變數（.env）

```env
SELENIUM_REMOTE_URL=http://selenium-hub:4444/wd/hub
```

請參考 `.env.example` 並建立 `.env` 作為測試執行時的環境設定。


---

## 📊 測試報告產出流程

已整合 pytest-html 自動產出測試報告，可透過 nginx 容器瀏覽。

- 測試執行後報告將產生於 `reports/report.html`
- `docker-compose.yml` 包含 `report-server`，對外開啟報告網頁
- 瀏覽：[http://localhost:8080/report.html](http://localhost:8080/report.html)

執行測試並產生報告：

```bash
./run-tests.sh
```


---

## 📈 成功驗證測試跑在 Selenium Grid 上

已完成首次將自動化測試案例成功部署至本機 Selenium Grid 環境：

- 使用 `docker-compose.yml` 啟動 Grid （Hub + Chrome）
- 透過 `pytest` 執行 `test_xyz_home.py`
- 驗證頁面標題包含 "NetMind XYZ"
- 測試經由 `http://localhost:4444/wd/hub` 成功交由 Grid 處理
- 解決 Chrome container crash 問題：

```python
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
```

🔍 執行測試範例：

```bash
SELENIUM_REMOTE_URL=http://localhost:4444/wd/hub pytest script/test_xyz_home.py
```



## 📋 授權

MIT License
