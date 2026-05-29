# ⚙️ Installing `protoc` (Protocol Buffer Compiler)

`protoc` is the official **Protocol Buffer compiler**.

It reads `.proto` files and generates code for languages like:

- Python 🐍
- Java ☕
- Go 🐹
- C++ ⚡
- JavaScript 🌐

---

# 🧠 What Does `protoc` Do?

Example:

```proto
message User {
  int32 id = 1;
  string name = 2;
}
```

`protoc` converts this schema into real code.

Example:

```text
user_pb2.py
```

for Python.

---

# 🪟 Windows Setup

---

# 1️⃣ Download Protoc

Go to the official Protocol Buffers releases page:

```text
https://github.com/protocolbuffers/protobuf/releases
```

Download:

```text
protoc-<version>-win64.zip
```

Example:

```text
protoc-31.1-win64.zip
```

---

# 2️⃣ Extract ZIP File

Extract it somewhere like:

```text
C:\protobuf
```

Inside you will see:

```text
bin/
include/
```

---

# 3️⃣ Add `bin` to PATH

Add this folder to PATH:

```text
C:\protobuf\bin
```

---

## 📍 How to Add PATH

- Open Start Menu
- Search:
  
```text
Environment Variables
```

- Open:

```text
Edit the system environment variables
```

- Click:

```text
Environment Variables
```

- Under `System Variables`
- Select `Path`
- Click `Edit`
- Add:

```text
C:\protobuf\bin
```

---

# 4️⃣ Verify Installation

Open terminal:

```bash
protoc --version
```

Expected output:

```text
libprotoc 31.1
```

---

# 🐧 Linux Setup

---

# 1️⃣ Update Packages

```bash
sudo apt update
```

---

# 2️⃣ Install Protoc

```bash
sudo apt install protobuf-compiler
```

---

# 3️⃣ Verify Installation

```bash
protoc --version
```

Expected:

```text
libprotoc 3.x.x
```

---

# 🍎 macOS Setup (Homebrew)

---

# 1️⃣ Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

# 2️⃣ Install Protobuf

```bash
brew install protobuf
```

---

# 3️⃣ Verify Installation

```bash
protoc --version
```

Expected:

```text
libprotoc 31.1
```

---

# 🐍 Python Protobuf Setup

After installing `protoc`, install Python protobuf package.

---

# 1️⃣ Install Python Package

```bash
pip install protobuf
```

---

# 2️⃣ Verify Python Installation

```bash
pip show protobuf
```

---

# 📦 Create Your First `.proto` File

Example:

## 📄 user.proto

```proto
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
}
```

---

# ⚡ Compile `.proto` File

Run:

```bash
protoc --python_out=. user.proto
```

---

# 🧠 What Happens?

Protobuf generates:

```text
user_pb2.py
```

This file contains Python classes for your messages.

---

# 📁 Example Folder Structure

Before compile:

```text
project/
 ├── user.proto
```

After compile:

```text
project/
 ├── user.proto
 └── user_pb2.py
```

---

# 🐍 Python Usage Example

```python
import user_pb2

user = user_pb2.User()

user.id = 1
user.name = "Abhishek"

print(user)
```

---

# ⚡ Useful Protoc Commands

---

## Generate Python Code

```bash
protoc --python_out=. user.proto
```

---

## Generate Multiple Files

```bash
protoc --python_out=. user.proto address.proto
```

---

## Compile All Proto Files

Linux/macOS:

```bash
protoc --python_out=. *.proto
```

---

# 📦 Generate gRPC Python Code

Install gRPC tools:

```bash
pip install grpcio grpcio-tools
```

Then run:

```bash
python -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  user.proto
```

---

# 🧠 Understanding Command Parts

---

## `--python_out=.`

Generate Python files in current folder.

---

## `-I.`

Current directory contains `.proto` files.

---

## `--grpc_python_out=.`

Generate gRPC service code.

---

# 🚫 Common Errors

---

# ❌ `protoc: command not found`

Cause:
- PATH not configured properly

Fix:
- Add protoc `bin` folder to PATH

---

# ❌ `.proto file not found`

Cause:
- Wrong file path

Fix:
- Run command from correct directory

---

# ❌ `ModuleNotFoundError`

Cause:
- Python protobuf package missing

Fix:

```bash
pip install protobuf
```

---

# 🧠 Recommended Setup for Beginners

Install:

✅ protoc compiler  
✅ Python protobuf package  
✅ grpcio-tools (optional)

---

# 🎯 Final Thoughts

`protoc` is the core tool of Protocol Buffers.

It helps convert:

```text
.proto schema
```

into:

```text
real programming language code
```

Learning `protoc` is the first major step toward:

- Protobuf development 📦
- gRPC 🚀
- Microservices 🧩
- Distributed systems 🌐