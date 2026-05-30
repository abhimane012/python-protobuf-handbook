# ➕ Adding Fields in Protocol Buffers

One of the best features of Protocol Buffers is:

> ✅ You can safely add new fields without breaking old applications.

This is a very important part of:

```text
Data Evolution
```

---

# 🤔 Why Adding Fields Matters?

Real applications keep growing over time.

Today you may have:

```proto
message User {
  int32 id = 1;
  string name = 2;
}
```

Later you may need:

- email 📧
- phone 📱
- address 🏠

Protocol Buffers allow this safely.

---

# 🟢 Version 1

```proto
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
}
```

---

# 🟡 Version 2 (Adding New Field)

```proto
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
```

---

# 🧠 What Changed?

New field added:

```proto
string email = 3;
```

Existing fields remain unchanged.

---

# ✅ Why This Is Safe

Old applications know only:

```text
id
name
```

When they receive:

```text
id
name
email
```

they simply ignore:

```text
email
```

No crash ✅

---

# 🔄 Forward Compatibility

Older systems can safely read newer data.

Unknown fields are ignored automatically.

---

# 🔙 Backward Compatibility

New systems can safely read older data.

If old data does not contain:

```proto
email = 3;
```

Protobuf uses default value:

```text
""
(empty string)
```

---

# 📊 Real Example

---

# 🟢 Old Application

Schema:

```proto
message User {
  int32 id = 1;
  string name = 2;
}
```

Data received:

```text
id = 1
name = "Abhishek"
email = "abc@gmail.com"
```

Old app behavior:

```text
Reads:
- id
- name

Ignores:
- email
```

---

# 🟡 New Application

Schema:

```proto
message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
```

Old data:

```text
id = 1
name = "Abhishek"
```

Behavior:

```text
email = ""
```

(default value)

---

# ⚡ Rule for Adding Fields

---

# ✅ Always Use a New Tag Number

Correct:

```proto
string email = 3;
```

---

# ❌ Never Reuse Existing Tags

Wrong:

```proto
string email = 2;
```

if tag `2` already belongs to another field.

---

# 🧠 Why Tags Matter

Protocol Buffers identify fields using:

```text
Field Tags
```

Example:

```proto
string name = 2;
```

Changing or reusing tags can break compatibility.

---

# 📦 Example with Multiple Additions

---

# 🟢 Version 1

```proto
message Product {
  int32 id = 1;
  string name = 2;
}
```

---

# 🟡 Version 2

```proto
message Product {
  int32 id = 1;
  string name = 2;

  double price = 3;
  bool in_stock = 4;
}
```

Safe ✅

---

# 🧠 What Happens Internally?

Older applications:

```text
Ignore tags:
3
4
```

Newer applications:

```text
Use default values if fields are missing
```

---

# 🚫 Common Mistakes

---

# ❌ Changing Existing Tags

Wrong:

```proto
string name = 5;
```

Previously:

```proto
string name = 2;
```

---

# ❌ Reusing Old Tags

Wrong:

```proto
string phone = 2;
```

if `2` already belonged to another field.

---

# ❌ Changing Existing Field Type

Wrong:

```proto
string name = 2;
```

to:

```proto
int32 name = 2;
```

This can break deserialization.

---

# 🧠 Best Practices

✅ Add new fields only at the end  
✅ Use new unique tag numbers  
✅ Keep old fields unchanged  
✅ Never change existing tags  
✅ Never reuse removed tags  

---

# 📊 Quick Summary

| Action | Safe? |
|---|---|
| Add new field with new tag | ✅ |
| Change old tag number | ❌ |
| Reuse existing tag | ❌ |
| Ignore unknown fields | ✅ |
| Missing new field uses default | ✅ |

---

# 🎯 Final Thoughts

Adding fields is one of the safest operations in Protocol Buffers.

This is what makes Protobuf excellent for:

- APIs 🌐
- Microservices 🧩
- gRPC 🚀
- Distributed systems 📡

👉 The key rule:

# 🏷️ Always add fields using NEW unique tag numbers