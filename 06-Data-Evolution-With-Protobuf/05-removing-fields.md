# ❌ Removing Fields in Protocol Buffers

In Protocol Buffers, fields can be removed safely if done correctly.

This is an important part of:

```text
Data Evolution
```

---

# 🤔 Why Remove Fields?

Over time, some fields may become:

- Unused 🗑️
- Deprecated ⚠️
- Replaced 🔄
- No longer needed 📦

Example:

```proto
string fax_number = 3;
```

Maybe modern systems no longer use fax numbers.

---

# 🟢 Old Version

```proto
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
```

---

# 🟡 New Version

```proto
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
}
```

Field removed:

```proto
string email = 3;
```

---

# ✅ Is This Safe?

Yes ✅

Removing fields is safe IF:

```text
You NEVER reuse the old tag number
```

---

# 🧠 Why This Works

Protocol Buffers use:

```text
Field Tags
```

internally.

Old systems may still send:

```text
tag 3 = email
```

New systems simply ignore unknown fields safely.

---

# ⚠️ Biggest Danger

---

# ❌ Never Reuse Removed Tags

Dangerous:

---

## 🟢 Old Version

```proto
string email = 3;
```

---

## 🔴 Wrong New Version

```proto
int32 age = 3;
```

Now:

```text
Old data:
tag 3 = email

New data:
tag 3 = age
```

This can corrupt data ❌

---

# ✅ Correct Way: Reserve Removed Tags

Protocol Buffers provide:

```proto
reserved
```

---

# 🟡 Safe Version

```proto
message User {

  reserved 3;

  int32 id = 1;
  string name = 2;
}
```

Now tag `3` can never be reused accidentally.

---

# 🧠 What Does `reserved` Mean?

It tells Protobuf:

```text
"This tag is permanently blocked"
```

---

# 📦 Reserve Multiple Tags

```proto
reserved 3, 5, 7;
```

---

# 📦 Reserve Tag Ranges

```proto
reserved 10 to 20;
```

---

# 🧠 Alternative Option

Instead of deleting immediately, some teams rename fields.

---

# Example

```proto
string OBSOLETE_email = 3;
```

This means:

```text
Do not use this field anymore
```

But compatibility remains safe.

---

# ⚡ Why Some Teams Prefer This

Benefits:

- Easier migration 🔄
- Better documentation 📖
- Avoid accidental reuse 🚫

---

# 📊 Real Example

---

# 🟢 Version 1

```proto
message Product {
  int32 id = 1;
  string old_code = 2;
}
```

---

# 🟡 Version 2

```proto
message Product {

  reserved 2;

  int32 id = 1;
}
```

Safe ✅

---

# 🔴 Dangerous Version

```proto
message Product {
  int32 id = 1;
  double price = 2;
}
```

Now old data may be interpreted incorrectly ❌

---

# 🧠 Real-World Analogy

Imagine apartment numbers 🏢

Apartment:

```text
#3
```

was assigned to:

```text
Email Department
```

Later you remove it.

You should NOT assign apartment `#3` to a completely different department immediately.

Otherwise mail and deliveries get mixed up 📦❌

Tags behave similarly in Protobuf.

---

# 🚀 How Old/New Systems Behave

---

# 🟢 Old System

Knows:

```text
id
name
email
```

---

# 🟡 New System

Knows:

```text
id
name
```

When old data sends:

```text
email
```

new system ignores it safely.

---

# ⚠️ Important Rules

---

# ✅ Safe

- Remove field
- Reserve old tag
- Ignore unknown fields

---

# ❌ Unsafe

- Reuse removed tag
- Change removed field type
- Reassign old meaning

---

# 📊 Quick Summary

| Action | Safe? |
|---|---|
| Remove field | ✅ |
| Reserve removed tag | ✅ |
| Reuse removed tag | ❌ |
| Ignore old unknown field | ✅ |
| Change removed tag meaning | ❌ |

---

# 🧠 Best Practices

✅ Reserve removed tags  
✅ Document removed fields  
✅ Avoid immediate reuse  
✅ Plan schema evolution carefully  

---

# 🎯 Final Thoughts

Removing fields in Protocol Buffers is safe when done properly.

The most important rule is:

# 🏷️ Never reuse removed field tag numbers

Always use:

```proto
reserved
```

to protect old tags from accidental reuse.