<details>
    <summary> CLIK FOR ENGLISH DESCRIPTION</summary>

# Introduction

This directory contains scripts necessary for interacting with Supabase using Python. The aim of this directory is to provide examples and helpful tools to efficiently use Supabase within your project.

Before running the scripts, ensure you have the Supabase URL and API key. These can be set as environment variables or defined directly in your script for simplicity.

I have shared the `URL` and `PUBLIC_KEY` information required for this project in `SupaBase/.env`. These are restricted to `SELECT` only. However, for performing various operations in your own project, you will need to obtain the `SERVICE_KEY` from the API or disable RLS (Row Level Security).

## Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Examples](#examples)
  - [Connecting to Supabase](#connecting-to-supabase)
  - [CRUD Operations](#crud-operations)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
- [Conclusion](#conclusion)

## Installation
To use the scripts in this directory, you need to install the necessary dependencies. You can do this using `pip`:

```bash
pip install supabase
```

## Configuration

To perform operations on Supabase, you first need to create a Supabase client.

```python
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL", "your-supabase-url")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "your-supabase-key")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
```

## Examples

### Connecting to Supabase

Here's how to connect to Supabase:

```python
from supabase import create_client, Client

SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
print("Connected to Supabase")
```

### CRUD Operations

#### Create

Adding a new record to a table:

```python
data = {"name": "John Doe", "email": "john.doe@example.com"}
response = supabase.table("users").insert(data).execute()
print(response.data)
```

#### Read

Fetching records from a table:

```python
response = supabase.table("users").select("*").execute()
print(response.data)
```

#### Update

Updating a record in a table:

```python
updates = {"email": "john.newemail@example.com"}
response = supabase.table("users").update(updates).eq("name", "John Doe").execute()
print(response.data)
```

#### Delete

Deleting a record from a table:

```python
response = supabase.table("users").delete().eq("name", "John Doe").execute()
print(response.data)
```

### Example Outputs

| Operation | Description                | Example Code                                             | Expected Output                                            |
|-----------|----------------------------|----------------------------------------------------------|------------------------------------------------------------|
| Create    | Add a new user             | `supabase.table("users").insert(data).execute()`         | `{"name": "John Doe", "email": "john.doe@example.com"}`    |
| Read      | Fetch all users            | `supabase.table("users").select("*").execute()`          | `[{"name": "John Doe", "email": "john.doe@example.com"}]`  |
| Update    | Update user email          | `supabase.table("users").update(updates).eq("name", "John Doe").execute()` | `[{"name": "John Doe", "email": "john.newemail@example.com"}]` |
| Delete    | Delete user by name        | `supabase.table("users").delete().eq("name", "John Doe").execute()` | `[]`                                                       |

For more information, visit the [Supabase Documentation](https://supabase.io/docs). Feel free to ask me directly if you have any questions.

</details>

---

# Giriş

Bu dizin, Python kullanarak Supabase ile etkileşime geçmek için gerekli betikleri içerir. Bu dizinin amacı, projeniz içinde Supabase'i verimli bir şekilde kullanmak için örnekler ve yardımcı araçlar sağlamaktır.

Betikleri çalıştırmadan önce, Supabase URL ve API anahtarına sahip olduğunuzdan emin olun. Bunları ortam değişkenleri olarak ayarlayabilir veya basitlik açısından doğrudan betiğinizde tanımlayabilirsiniz. 

Ben `SupaBase/.env` içerisinde bu proje için gerekli olan `URL` ve `PUBLIC_KEY` bilgilerini paylaştım. Bunları sadece `SELECT` edebilecek şekilde restrict ettim. Ancak kendi projenizde pek çok operations yapabilmeniz için API içerisindeki `SERVICE_KEY`'ini almanız ya da RLS (Row Level Security) kaldırmanız gerekecek.

## İçindekiler

- [Kurulum](#kurulum)
- [Yapılandırma](#yapılandırma)
- [Örnekler](#örnekler)
  - [Supabase'e Bağlanma](#supabasee-bağlanma)
  - [CRUD İşlemleri](#crud-işlemleri)
    - [Ekleme (Create)](#ekleme-create)
    - [Okuma (Read)](#okuma-read)
    - [Güncelleme (Update)](#güncelleme-update)
    - [Silme (Delete)](#silme-delete)
- [Sonuç](#sonuç)

## Kurulum
Bu dizindeki betikleri kullanabilmek için gerekli bağımlılıkları yüklemeniz gerekmektedir. Bunu `pip` kullanarak yapabilirsiniz:

```bash
pip install supabase
```

## Yapılandırma

Supabase üzerinde operations yapabilmek için öncelikle supabase client'ını oluşturmak gerekecek.

```python
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL", "your-supabase-url")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "your-supabase-key")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
```

## Örnekler

### Supabase'e Bağlanma

Supabase'e nasıl bağlanacağınız aşağıda gösterilmiştir:

```python
from supabase import create_client, Client

SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
print("Supabase'e bağlanıldı")
```

### CRUD İşlemleri

#### Ekleme (Create)

Bir tabloya yeni bir kayıt eklemek:

```python
data = {"name": "John Doe", "email": "john.doe@example.com"}
response = supabase.table("users").insert(data).execute()
print(response.data)
```

#### Okuma (Read)

Bir tablodan kayıtları çekmek:

```python
response = supabase.table("users").select("*").execute()
print(response.data)
```

#### Güncelleme (Update)

Bir tablodaki kaydı güncellemek:

```python
updates = {"email": "john.newemail@example.com"}
response = supabase.table("users").update(updates).eq("name", "John Doe").execute()
print(response.data)
```

#### Silme (Delete)

Bir tablodan kaydı silmek:

```python
response = supabase.table("users").delete().eq("name", "John Doe").execute()
print(response.data)
```

### Örnek Çıktılar

| İşlem    | Açıklama                   | Örnek Kod                                               | Beklenen Çıktı                                          |
|----------|----------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Ekleme   | Yeni bir kullanıcı eklemek | `supabase.table("users").insert(data).execute()`        | `{"name": "John Doe", "email": "john.doe@example.com"}` |
| Okuma    | Tüm kullanıcıları çekmek   | `supabase.table("users").select("*").execute()`         | `[{"name": "John Doe", "email": "john.doe@example.com"}]` |
| Güncelleme| Kullanıcı e-posta güncelle | `supabase.table("users").update(updates).eq("name", "John Doe").execute()` | `[{"name": "John Doe", "email": "john.newemail@example.com"}]` |
| Silme    | Kullanıcıyı isme göre sil   | `supabase.table("users").delete().eq("name", "John Doe").execute()` | `[]`                                                    |


Daha fazla bilgi için [Supabase Dokümantasyonu](https://supabase.io/docs) adresini ziyaret edebilirsiniz. Ayrıca direkt bana sormaktan da çekinmeyin.