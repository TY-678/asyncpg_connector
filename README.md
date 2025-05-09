# asyncpg_connector

`asyncpg_connector` is a lightweight database connector based on [asyncpg](https://github.com/MagicStack/asyncpg), providing simple configuration and context management for seamless asynchronous interaction with PostgreSQL databases.

[點此閱讀中文版](#asyncpg_connector-中文版)

## Features

- Validates connection configuration using [Pydantic](https://docs.pydantic.dev/).
- Supports context management (`async with`) for automatic connection handling.
- Built-in error handling with clear error messages.

## Installation

Install using `pip`:

```bash
pip install asyncpg-connector
```

Or with Poetry:
```bash
poetry add asyncpg-connector
```

## Usage
Here is a simple example:

```python
import asyncio
from asyncpg_connector import AsyncpgConnector
from asyncpg_connector.model import ConnectorConfig

db_config = ConnectorConfig(
    host="localhost",
    port=5432,
    user="your_username",
    password="your_password",
    database="your_database",
    ssl=False
)

db_connector = AsyncpgConnector(config)

async def main():
    async with db_connector as connector:
        conn = connector.conn
        result = await conn.fetch("SELECT * FROM your_table")
        print(result)

asyncio.run(main())
```


## Error Handling
When the database connection fails, `AsyncpgConnector` raises a `DatabaseConnectionError`:

```python
from asyncpg_connector.error import DatabaseConnectionError

try:
    async with AsyncpgConnector(config) as connector:
        pass
except DatabaseConnectionError as e:
    print(f"Connection failed: {e}")
```

## Requirements
- Python version:`>=3.9,<4.0`
- Dependencies:
    - asyncpg `^0.30.0`
    - Pydantic `^2.11.3`

## Contributing
Contributions are welcome! Please ensure your code adheres to the project's style guidelines and includes relevant tests.

## License
This project is licensed under the MIT License.


# asyncpg_connector (中文版)

`asyncpg_connector` 是一個基於 [asyncpg](https://github.com/MagicStack/asyncpg) 的輕量級資料庫連接器，提供簡單的配置和上下文管理功能，讓您能夠輕鬆地與 PostgreSQL 資料庫進行非同步操作。

## 功能特性

- 使用 [Pydantic](https://docs.pydantic.dev/) 驗證連接配置。
- 支援上下文管理協議 (`async with`)，自動管理連接的建立與關閉。
- 內建錯誤處理，提供清晰的錯誤訊息。

## 安裝

您可以使用 `pip` 安裝：

```bash
pip install asyncpg-connector
```

或使用 Poetry：
```bash
poetry add asyncpg-connector
```

## 使用方式
以下是一個簡單的使用範例：

```python
import asyncio
from asyncpg_connector import AsyncpgConnector
from asyncpg_connector.model import ConnectorConfig

db_config = ConnectorConfig(
    host="localhost",
    port=5432,
    user="your_username",
    password="your_password",
    database="your_database",
    ssl=False
)

db_connector = AsyncpgConnector(config)

async def main():
    async with db_connector as connector:
        conn = connector.conn
        result = await conn.fetch("SELECT * FROM your_table")
        print(result)

asyncio.run(main())
```


## 錯誤處理
當資料庫連接失敗時，AsyncpgConnector 會拋出 DatabaseConnectionError：

```python
from asyncpg_connector.error import DatabaseConnectionError

try:
    async with AsyncpgConnector(config) as connector:
        pass
except DatabaseConnectionError as e:
    print(f"Connection failed: {e}")
```

## 系統需求
- Python 版本：`>=3.9,<4.0`
- 依賴套件：
    - asyncpg `^0.30.0`
    - Pydantic `^2.11.3`

## 貢獻
歡迎提交問題或拉取請求！請確保您的代碼符合專案的風格指南，並附上相關的測試。

## 授權
此專案採用 MIT License 授權。