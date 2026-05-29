# ⚡ What are Protocol Buffers (Protobuf)?

Protocol Buffers, also called **Protobuf**, are a language-neutral and platform-neutral way to serialize structured data.

They were created by Google to make data communication:

- Faster ⚡
- Smaller 💾
- More efficient 🚀

Protobuf is mainly used when applications or services need to exchange data quickly.

---

# 🤔 Why Were Protocol Buffers Created?

Before Protobuf, many systems used formats like:

- CSV
- XML
- JSON

These formats are human-readable, but they have problems:

## ❌ Problems with JSON/XML

- Large message size
- Slower parsing
- More network usage
- More storage usage

As systems became larger and faster, companies needed a better solution.

Google created **Protocol Buffers** to solve these problems.

---

# 📦 What Does "Serialize Data" Mean?

Serialization means:

> Converting data into a format that can be stored or sent over a network.

For example:

```python
user = {
    "id": 1,
    "name": "Abhishek"
}
```

This Python dictionary needs to be converted into a transferable format.

That format could be:

- JSON
- XML
- Protocol Buffers

---

# 🧠 Simple Real-World Analogy

Imagine sending a parcel 📦.

## JSON Approach 🌐

- Big box
- Easy to open
- Easy to read
- Takes more space

## Protobuf Approach ⚡

- Compact box
- Optimized packaging
- Smaller and faster delivery
- Harder for humans to read directly

---

# 🏗️ How Protocol Buffers Work

Protocol Buffers work in 3 main steps.

---

# 1️⃣ Define Structure Using `.proto` File

You first define your data structure inside a `.proto` file.

Example:

```proto
syntax = "proto3";

message Person {
  int32 id = 1;
  string name = 2;
  int32 age = 3;
}
```

This acts like a blueprint for your data.

---

# 2️⃣ Generate Code

The Protobuf compiler (`protoc`) generates code automatically.

You can generate code for many languages:

- Python
- Java
- Go
- C++
- JavaScript
- Many more

For Python:

```bash
protoc --python_out=. person.proto
```

This generates:

```text
person_pb2.py
```

---

# 3️⃣ Serialize and Deserialize Data

## Serialize

Convert object → binary data

## Deserialize

Convert binary data → object

---

# 🐍 Python Example

## Step 1: Create Object

```python
import person_pb2

person = person_pb2.Person()
person.id = 1
person.name = "Abhishek"
person.age = 25
```

---

## Step 2: Serialize Data

```python
binary_data = person.SerializeToString()
```

Now the data becomes compact binary data.

---

## Step 3: Deserialize Data

```python
new_person = person_pb2.Person()
new_person.ParseFromString(binary_data)

print(new_person.name)
```

Output:

```text
Abhishek
```

---

# ⚡ Why Protobuf is Fast

Protobuf is fast because:

- Uses binary format
- Smaller message size
- Less network transfer
- Faster parsing
- Optimized encoding

Compared to JSON:

| Feature | JSON | Protobuf |
|---|---|---|
| Readable | ✅ | ❌ |
| Speed | Medium | Very Fast |
| Message Size | Large | Small |
| Parsing Speed | Slower | Faster |

---

# 🧩 Understanding Field Numbers

In Protobuf:

```proto
message Person {
  int32 id = 1;
  string name = 2;
}
```

The numbers:

```proto
= 1
= 2
```

are called **field numbers**.

They are very important because Protobuf uses them internally in binary encoding.

## ⚠️ Important Rule

Once released:

- Never change field numbers
- Never reuse deleted field numbers

---

# 🛡️ Schema-Based Format

Protobuf is schema-based.

That means:

- Data structure is predefined
- Validation becomes easier
- Communication becomes safer

This is different from JSON, where structure can change anytime.

---

# 🔄 Backward Compatibility

One of the biggest strengths of Protobuf is compatibility.

You can safely:

- Add new fields
- Remove old unused fields
- Upgrade services gradually

Older services simply ignore unknown fields.

This is very useful in:

- Microservices
- Distributed systems
- APIs

---

# 🌍 Where Protobuf is Used

Protocol Buffers are heavily used in:

- gRPC
- Microservices
- Distributed systems
- Real-time systems
- High-performance APIs
- Google internal systems

---

# 🧱 Common Data Types

| Protobuf Type | Meaning |
|---|---|
| int32 | Integer |
| int64 | Large Integer |
| string | Text |
| bool | True/False |
| float | Decimal Number |
| double | Large Decimal |
| bytes | Binary Data |

---

# 📂 File Structure Example

```text
project/
│
├── person.proto
├── person_pb2.py
└── app.py
```

---

# 🚀 Advantages of Protocol Buffers

## ✅ Small Message Size

Consumes less bandwidth.

---

## ✅ Very Fast

Excellent performance for large systems.

---

## ✅ Strong Schema

Clear structure and validation.

---

## ✅ Multi-Language Support

Works across many programming languages.

---

## ✅ Backward Compatible

Easy to evolve systems safely.

---

# ❌ Disadvantages of Protocol Buffers

## ❌ Not Human Readable

Binary data cannot be read directly.

---

## ❌ Requires Compilation

Need to generate code using `protoc`.

---

## ❌ Slight Learning Curve

More setup compared to JSON.

---

# 📊 JSON vs Protocol Buffers

| Feature | JSON | Protocol Buffers |
|---|---|---|
| Human Readable | ✅ | ❌ |
| Speed | Medium | Very Fast |
| Message Size | Large | Small |
| Schema Support | Optional | Required |
| Best For | APIs | High-performance systems |

---

# 🎯 When Should You Use Protobuf?

Use Protobuf when:

- Performance matters
- Network usage matters
- Systems communicate frequently
- Building microservices
- Using gRPC
- Working with distributed systems

---

# 🧠 Final Thoughts

Protocol Buffers are designed for:

- Speed ⚡
- Efficiency 🚀
- Scalability 📈

They are one of the most important technologies used in modern backend systems and distributed applications.

If JSON is easy-to-read communication, then Protobuf is optimized high-speed communication.