# 🧩 Understanding Your First Protocol Buffer Message

Let’s understand this Protocol Buffer step-by-step.

```proto
syntax = "proto3";

message MyMessage {
  int32 id = 1;
  string first_name = 2;
  bool is_validated = 3;
}
```

This is called a **Protocol Buffer schema**.

It defines the structure of data.

Think of it like a blueprint 🏗️ for your data.

---

# 📄 Complete Breakdown

```proto
syntax = "proto3";

message MyMessage {
  int32 id = 1;
  string first_name = 2;
  bool is_validated = 3;
}
```

---

# 1️⃣ `syntax = "proto3";`

## 📌 What is This?

This line tells Protobuf:

> Which version of Protocol Buffers syntax you are using.

---

## ✅ Example

```proto
syntax = "proto3";
```

Here:

- `proto3` = Modern version of Protobuf
- Most commonly used version today

---

## 🤔 Why Is It Needed?

Different Protobuf versions have different rules and features.

This line helps the compiler understand:

- How to read the file
- Which features are available

---

## 🚀 Common Versions

| Version | Description |
|---|---|
| proto2 | Older version |
| proto3 | Newer and simpler version |

Today, most projects use:

```proto
syntax = "proto3";
```

---

# 2️⃣ `message MyMessage`

## 📌 What is a Message?

A `message` is like a class or structure that holds data.

It defines:

- What fields exist
- Their data types
- Their unique tags

---

## ✅ Syntax

```proto
message MessageName {
    
}
```

---

## ✅ Example

```proto
message MyMessage {

}
```

Here:

- `message` → Keyword
- `MyMessage` → Message name

---

## 🧠 Real-World Analogy

Think of a message like a form 📋.

Example:

```text
User Form
- ID
- Name
- Email
```

A Protobuf message works the same way.

---

# 3️⃣ Field Type

Inside a message, every field has a type.

Example:

```proto
int32 id = 1;
```

Here:

```proto
int32
```

is the **field type**.

---

# 📦 Common Field Types

| Type | Meaning |
|---|---|
| int32 | Integer number |
| int64 | Large integer |
| string | Text |
| bool | True or False |
| float | Decimal number |
| double | Large decimal number |
| bytes | Binary data |

---

# ✅ Your Example

```proto
int32 id = 1;
string first_name = 2;
bool is_validated = 3;
```

| Field | Type |
|---|---|
| id | int32 |
| first_name | string |
| is_validated | bool |

---

# 4️⃣ Field Name

The field name is the variable name used to store data.

Example:

```proto
string first_name = 2;
```

Here:

```proto
first_name
```

is the field name.

---

# ✅ Your Field Names

| Field Definition | Field Name |
|---|---|
| int32 id = 1; | id |
| string first_name = 2; | first_name |
| bool is_validated = 3; | is_validated |

---

# 🧠 Naming Convention

Usually field names use:

```text
snake_case
```

Example:

```proto
first_name
is_validated
user_email
```

---

# 5️⃣ Field Tag (Field Number)

The number after `=` is called the **field tag** or **field number**.

Example:

```proto
int32 id = 1;
```

Here:

```proto
1
```

is the field tag.

---

# 📌 Why Are Field Tags Important?

Protobuf uses field tags internally while converting data into binary format.

Instead of storing:

```text
"id"
```

Protobuf stores:

```text
1
```

This makes data:

- Smaller 💾
- Faster ⚡

---

# ✅ Your Field Tags

| Field | Tag |
|---|---|
| id | 1 |
| first_name | 2 |
| is_validated | 3 |

---

# ⚠️ Important Rules for Field Tags

## ✅ Field tags must be unique

Correct ✅

```proto
int32 id = 1;
string name = 2;
```

Wrong ❌

```proto
int32 id = 1;
string name = 1;
```

---

## ✅ Never change field tags after release

Changing tags can break compatibility between services.

---

## ✅ Never reuse deleted tags

If a field is removed, do not reuse its tag number.

---

# 🔍 Full Line Breakdown

## 🧩 Line 1

```proto
int32 id = 1;
```

| Part | Meaning |
|---|---|
| int32 | Field type |
| id | Field name |
| 1 | Field tag |

---

## 🧩 Line 2

```proto
string first_name = 2;
```

| Part | Meaning |
|---|---|
| string | Field type |
| first_name | Field name |
| 2 | Field tag |

---

## 🧩 Line 3

```proto
bool is_validated = 3;
```

| Part | Meaning |
|---|---|
| bool | Field type |
| is_validated | Field name |
| 3 | Field tag |

---

# 🏗️ Visual Structure

```text
message
   │
   ├── field type
   ├── field name
   └── field tag
```

---

# 🎯 Final Thoughts

A Protobuf message is made of:

- Syntax version
- Message definition
- Fields
- Field types
- Field names
- Field tags

Understanding these basics is the first step toward learning:

- Serialization
- Deserialization
- gRPC
- Microservices
- Distributed systems