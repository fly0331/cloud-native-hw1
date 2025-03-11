# cloud-native-hw1

## 📌 System Requirements
請確保您的環境符合以下條件：

- **Python 版本**：Python 3.11+
- **作業系統**：macOS / Windows

### 🔹 確認 Python 版本
```bash
python --version
```
如果 Python 版本 **低於 3.11**，請升級。

---

## 📦 Installation（安裝）
### 1️⃣ 下載專案（從 GitHub 或壓縮包解壓縮）
```bash
git clone https://github.com/fly0331/cloud-native-hw1.git
cd cloud-native-hw1
```

### 2️⃣ 安裝依賴（確保 `pip` 可用）
```bash
pip install -r requirements.txt
```

### 3️⃣ 執行建置（格式化程式碼 & 檢查）
```bash
./build.sh  # Linux/macOS
sh build.sh  # Windows（使用 Git Bash）
```

---

## 🚀 Running the Application（執行專案）
### 1️⃣ 執行 CLI 應用程式
```bash
./run.sh  # Linux/macOS
sh run.sh  # Windows（使用 Git Bash）
```

### 2️⃣ 手動執行（若不使用 `run.sh`）
```bash
python main.py
```

---

## 🛠️ Features（功能列表）
| 指令 | 說明 |
|------|------|
| `REGISTER <username>` | 註冊新使用者 |
| `CREATE_LISTING <username> <title> <description> <price> <category>` | 建立商品 |
| `DELETE_LISTING <username> <listing_id>` | 刪除商品 |
| `GET_LISTING <username> <listing_id>` | 查詢商品資訊 |
| `GET_CATEGORY <username> <category>` | 查詢某分類的商品（時間排序） |
| `GET_TOP_CATEGORY <username>` | 取得最多商品的分類 |
| `EXIT` | 退出程式 |

---

## 📌 指令範例
### 🔹 註冊使用者
```bash
REGISTER user1  
```
### 🔹 創建商品
```bash
CREATE_LISTING user1 'Phone Model 8' 'Brand new, black' 1000 'Electronics'
```
### 🔹 查詢商品
```bash
GET_LISTING user1 100001
```
### 🔹 刪除商品
```bash
DELETE_LISTING user1 100001
```
### 🔹 查詢分類商品
```bash
GET_CATEGORY user1 'Electronics'
```
### 🔹 取得熱門分類
```bash
GET_TOP_CATEGORY user1
```

