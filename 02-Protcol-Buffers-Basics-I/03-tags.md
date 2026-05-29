# 🏷️ Understanding Tags in Protocol Buffers

In Protocol Buffers, every field has a unique number called a:

- Tag
- Field Tag
- Field Number

Example:

```proto
int32 id = 1;
```

Here:

| Part | Meaning |
|---|---|
| int32 | Field type |
| id | Field name |
| 1 | Field tag |

---

# 🤔 What is a Tag?

A tag is a unique number assigned to every field in a message.

Example:

```proto
message User {
  int32 id = 1;
  string name = 2;
  bool is_active = 3;
}
```

Here:

| Field | Tag |
|---|---|
| id | 1 |
| name | 2 |
| is_active | 3 |

---

# 📦 Why Are Tags Important?

Tags are extremely important in Protocol Buffers because Protobuf uses tags internally while serializing data.

Instead of sending:

```text
"id"
```

Protobuf sends:

```text
1
```

This makes messages:

- Smaller 💾
- Faster ⚡
- More efficient 🚀

---

# 🧠 Real-World Analogy

Imagine a school classroom.

Instead of calling students by long names:

```text
Abhishek
Rahul
Priya
```

the school gives roll numbers:

```text
1
2
3
```

Using numbers is:

- Faster
- Easier
- More efficient

Tags work the same way in Protobuf.

---

# 🏗️ Tag Syntax

## General Syntax

```proto
field_type field_name = tag;
```

---

## Example

```proto
string email = 4;
```

| Part | Meaning |
|---|---|
| string | Field type |
| email | Field name |
| 4 | Tag |

---

# 🔍 Full Example

```proto
syntax = "proto3";

message Product {

  int32 id = 1;

  string name = 2;

  float price = 3;

  bool in_stock = 4;
}
```

---

# 📊 Tag Breakdown

| Field | Tag |
|---|---|
| id | 1 |
| name | 2 |
| price | 3 |
| in_stock | 4 |

---

# ⚡ How Tags Help Serialization

Suppose you have:

```proto
int32 id = 1;
```

and the value:

```text
100
```

Internally Protobuf stores:

```text
Tag: 1
Value: 100
```

instead of storing:

```text
Field Name: "id"
Value: 100
```

This saves space.

---

# 🚀 Benefits of Tags

## ✅ Smaller Message Size

Numbers consume less space than text.

---

## ✅ Faster Serialization

Binary encoding becomes faster.

---

## ✅ Faster Deserialization

Protobuf quickly identifies fields using tags.

---

## ✅ Better Network Performance

Less data travels over the network.

---

# ⚠️ Important Rules for Tags

---

# 1️⃣ Tags Must Be Unique

Every field must have a different tag.

✅ Correct

```proto
message User {
  int32 id = 1;
  string name = 2;
}
```

❌ Wrong

```proto
message User {
  int32 id = 1;
  string name = 1;
}
```

Duplicate tags are not allowed.

---

# 2️⃣ Never Change Tags After Release

Once your Protobuf message is used in production:

🚫 Do NOT change tag numbers.

---

## ❌ Dangerous Example

Old Version:

```proto
string name = 2;
```

New Version:

```proto
string name = 5;
```

This can break communication between services.

---

# 3️⃣ Never Reuse Deleted Tags

Suppose you remove a field:

```proto
string email = 3;
```

Do NOT reuse tag `3` later for another field.

This can create data corruption problems.

---

# ✅ Best Practice: Reserved Tags

Protocol Buffers allow reserving tags so they cannot be reused accidentally.

Example:

```proto
message User {

  reserved 3;

  int32 id = 1;

  string name = 2;
}
```

Now tag `3` is permanently blocked.

---

# 🧠 Reserve Multiple Tags

You can reserve multiple tags together.

Example:

```proto
reserved 3, 5, 7;
```

---

# 🧠 Reserve Tag Ranges

You can also reserve ranges.

Example:

```proto
reserved 10 to 20;
```

This blocks all tags from:

```text
10 → 20
```

---

# 🚫 Why Reserved Tags Matter

Without reserving deleted tags:

Old Service:

```proto
string email = 3;
```

New Service:

```proto
int32 age = 3;
```

Now old binary data may be interpreted incorrectly.

This can cause:

- Wrong data
- Corruption
- Compatibility issues

Reserved tags prevent this problem.

---

# 🔢 How Many Tag Numbers Can We Use?

Protocol Buffers support field numbers from:

```text
1 → 536,870,911
```

This is the valid range.

---

# 🚫 Reserved Internal Range

The following range is reserved internally by Protobuf:

```text
19000 → 19999
```

You should NEVER use these numbers.

---

# ✅ Recommended Tag Usage

| Tag Range | Recommendation |
|---|---|
| 1 → 15 | Best for commonly used fields |
| 16 → 2047 | Good for normal fields |
| 2048+ | Less commonly used |

---

# ⚡ Why Small Tags Are Better

Smaller tag numbers take less storage space in binary encoding.

Example:

```proto
1
2
3
```

are more efficient than:

```proto
1000
5000
10000
```

---

# 🧠 Best Practice for Tag Planning

Use small tags for important fields.

Example:

```proto
message User {

  int32 id = 1;

  string name = 2;

  string email = 3;

  bool is_verified = 4;
}
```

---

# 🧱 Example with Reserved Tags

```proto
syntax = "proto3";

message Employee {

  reserved 5;

  reserved 10 to 15;

  int32 id = 1;

  string name = 2;

  string department = 3;

  bool is_active = 4;
}
```

---

# 📊 Visual Representation

```text
┌──────────────┬─────┐
│ Field Name   │ Tag │
├──────────────┼─────┤
│ id           │ 1   │
│ name         │ 2   │
│ department   │ 3   │
│ is_active    │ 4   │
│ reserved     │ 5   │
└──────────────┴─────┘
```

---

# 🎯 Final Thoughts

Tags are one of the most important concepts in Protocol Buffers.

They help Protobuf achieve:

- Fast serialization ⚡
- Small message size 💾
- Efficient communication 🚀

Always remember:

✅ Tags must be unique  
✅ Never change existing tags  
✅ Never reuse deleted tags  
✅ Reserve removed tags  
✅ Use small tags for common fields

Understanding tags is very important before learning:

- Schema evolution
- Backward compatibility
- Serialization
- gRPC
- Advanced Protobuf design