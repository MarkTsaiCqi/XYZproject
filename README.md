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

### 安裝相依套件

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 執行測試（本機瀏覽器）

```bash
pytest script/test_cases/
```

### 執行測試（透過 Selenium Grid）

```bash
SELENIUM_REMOTE_URL=http://selenium-hub:4444/wd/hub pytest tests/test_cases/
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

## 🧪 測試說明

| 類別         | 說明                              |
|--------------|-----------------------------------|
| `pages/`     | Page Object 模組                  |
| `components/`| 可重用邏輯（如登入、註冊）       |
| `test_cases/`| 具體測試案例                      |

---

## 💠 CI/CD 集成建議

可透過 Jenkins 使用下列插件實現自動化流程：

- HTML Publisher Plugin
- Email Extension Plugin
- Docker Pipeline Plugin
- Selenium Grid Plugin

---

## 📄 環境變數（.env）

```env
SELENIUM_REMOTE_URL=http://selenium-hub:4444/wd/hub
```

請參考 `.env.example` 並建立 `.env` 作為測試執行時的環境設定。

---

## 📋 授權

MIT License
