# 🔁 Repeated Fields in Protocol Buffers

In Protocol Buffers, a **repeated field** is used when you want to store **multiple values of the same type** in one field.

Think of it like an **array or list**.

---

# 🤔 Why Do We Need Repeated Fields?

Normal fields store only **one value**.

Example:

```proto
string name = 1;
```

This can store only one name.

But what if you want:

- multiple phone numbers 📞
- multiple emails 📧
- multiple tags 🏷️

👉 That’s where `repeated` comes in.

---

# 🏗️ Syntax of Repeated Field

```proto
repeated field_type field_name = tag;
```

---

# 📦 Example

```proto
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
  repeated string emails = 3;
}
```

---

# 🧠 How to Read It

```proto
repeated string emails = 3;
```

| Part | Meaning |
|---|---|
| repeated | Can store multiple values |
| string | Type of each value |
| emails | Field name |
| 3 | Tag |

---

# 📋 Example Data

A single user can have multiple emails:

```text
emails = ["abc@gmail.com", "abc@work.com", "abc@dev.com"]
```

---

# 🐍 Python Example

```python
import user_pb2

user = user_pb2.User()

user.id = 1
user.name = "Abhishek"

user.emails.append("abc@gmail.com")
user.emails.append("abc@work.com")

print(user)
```

---

# ➕ You Can Also Assign List Directly

```python
user.emails.extend([
    "abc@gmail.com",
    "abc@work.com"
])
```

---

# 📊 Real-World Example

```proto
message Order {
  int32 order_id = 1;
  string customer_name = 2;

  repeated string product_ids = 3;
}
```

Example:

```text
product_ids = ["p1", "p2", "p3"]
```

---

# 🧠 Internal Idea

Repeated fields behave like:

- Python → list
- Java → ArrayList
- Go → slice
- C++ → vector

---

# ⚡ Important Properties of Repeated Fields

---

# 1️⃣ Can Store Zero or More Values

```proto
repeated string tags = 1;
```

Valid cases:

```text
[]
["tech"]
["tech", "ai", "ml"]
```

---

# 2️⃣ Order is Preserved

```text
["A", "B", "C"]
```

will always remain in the same order.

---

# 3️⃣ Duplicate Values Are Allowed

```text
["A", "A", "B"]
```

Protobuf does NOT enforce uniqueness.

---

# 4️⃣ Works with Any Scalar Type

You can use repeated with:

- int32
- string
- bool
- float
- double
- bytes

Example:

```proto
repeated int32 scores = 1;
```

---

# 🧱 Example with Multiple Repeated Fields

```proto
message Student {
  int32 id = 1;
  string name = 2;

  repeated string subjects = 3;
  repeated int32 marks = 4;
}
```

---

# 📊 Example Data

```text
subjects = ["Math", "Science", "English"]
marks = [90, 85, 88]
```

---

# 🚀 Benefits of Repeated Fields

## ✅ Easy to model lists

No need for multiple fields.

---

## ✅ Efficient binary storage

Stored in compact format.

---

## ✅ Works across languages

Same structure in Python, Java, Go, etc.

---

## ✅ Perfect for APIs

Used heavily in:

- gRPC
- microservices
- event systems

---

# ⚠️ Common Mistakes

---

## ❌ Using multiple fields instead of repeated

Bad:

```proto
string email1 = 1;
string email2 = 2;
string email3 = 3;
```

Good:

```proto
repeated string emails = 1;
```

---

## ❌ Assuming uniqueness

Repeated fields allow duplicates unless you enforce logic in code.

---

# 📦 JSON vs Protobuf Repeated Fields

## JSON

```json
{
  "emails": ["a@gmail.com", "b@gmail.com"]
}
```

## Protobuf

```proto
repeated string emails = 1;
```

Same concept, but Protobuf is:

- smaller 💾
- faster ⚡
- schema-based 📦

---

# 🎯 Final Thoughts

Repeated fields are used to represent **lists of data** in Protocol Buffers.

They are:

- Simple
- Powerful
- Efficient

Use them whenever a field can have **multiple values**, such as:

- emails
- phone numbers
- tags
- items
- IDs
```