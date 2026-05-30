# 🚫 `reserved` Keyword in Protocol Buffers

In Protocol Buffers, the `reserved` keyword is used to block:

- Old field tags 🏷️
- Old field names 📝

from being reused in the future.

This helps prevent:

- Data corruption ❌
- Compatibility issues ❌
- Accidental mistakes ❌

---

# 🤔 Why Do We Need `reserved`?

Suppose you remove a field:

```proto
string email = 3;
```

Later another developer writes:

```proto
int32 age = 3;
```

Now old systems think:

```text
tag 3 = email
```

but new systems think:

```text
tag 3 = age
```

This creates broken data ❌

---

# ✅ Solution

Use:

```proto
reserved
```

to permanently block old tags.

---

# 🏗️ Basic Syntax

---

# Reserve Tag Numbers

```proto id="a1m9qp"
reserved 3;
```

---

# Reserve Multiple Tags

```proto id="b2n8tv"
reserved 3, 5, 7;
```

---

# Reserve Tag Range

```proto id="c3m7xp"
reserved 10 to 20;
```

---

# Reserve Field Names

```proto id="d4k6qp"
reserved "email";
```

---

# 📦 Example: Removing a Field Safely

---

# 🟢 Old Version

```proto id="e5v9mn"
message User {
  int32 id = 1;
  string email = 2;
}
```

---

# 🟡 New Version

```proto id="f6m2qp"
message User {

  reserved 2;

  int32 id = 1;
}
```

Now tag `2` is blocked forever ✅

---

# 🧠 What Happens Now?

If someone tries:

```proto
int32 age = 2;
```

Protobuf compiler throws an error 🚫

---

# 📦 Reserving Field Names

You can also reserve old field names.

---

## Example

```proto id="g7n3tv"
message User {

  reserved "email";

  int32 id = 1;
}
```

Now nobody can create:

```proto
string email = 5;
```

---

# 🧠 Why Reserve Names?

Helps avoid:

- confusion 🧠
- accidental reuse 🔄
- misleading schemas ❌

---

# 📊 Real-World Analogy

Think of old apartment numbers 🏢

Apartment:

```text
#3
```

was used earlier.

Instead of reassigning it, management marks it as:

```text
Reserved
```

so nobody accidentally uses it again.

That’s exactly how `reserved` works.

---

# ⚡ Reserved Tags vs Reserved Names

| Reserved Type | Purpose |
|---|---|
| reserved 3 | blocks tag number |
| reserved "email" | blocks field name |

---

# 🧱 Full Example

```proto id="h8m4xp"
syntax = "proto3";

message Employee {

  reserved 3, 5;

  reserved 10 to 20;

  reserved "old_email";

  int32 id = 1;

  string name = 2;
}
```

---

# 🧠 Meaning

Blocked forever:

```text
Tags:
3
5
10 → 20

Field Name:
old_email
```

---

# 🚀 Why `reserved` Is Important

It protects schema evolution.

Especially useful in:

- Microservices 🧩
- APIs 🌐
- gRPC 🚀
- Distributed systems 📡

where old and new systems coexist.

---

# ⚠️ Important Rules

---

# ✅ Use `reserved` After Removing Fields

Best practice:

```proto
reserved 3;
```

---

# ❌ Never Reuse Old Tags

Dangerous:

```proto
int32 age = 3;
```

if tag `3` was used earlier.

---

# ❌ Reserved Tags Cannot Be Used Again

Compiler will fail.

---

# 📦 Example Compiler Error

```text id="i9k5qp"
Field "age" uses reserved number 3
```

---

# 🧠 Best Practices

✅ Reserve deleted field tags  
✅ Reserve old field names  
✅ Use ranges for large removals  
✅ Document obsolete fields  

---

# 📊 Quick Summary

| Action | Recommended? |
|---|---|
| Remove field + reserve tag | ✅ |
| Reuse deleted tag | ❌ |
| Reserve old field name | ✅ |
| Reserve tag ranges | ✅ |

---

# 🎯 Final Thoughts

The `reserved` keyword is one of the most important safety features in Protocol Buffers.

It helps prevent:

- Broken compatibility ❌
- Data corruption ❌
- Accidental reuse ❌

👉 Golden Rule:

# 🏷️ Always reserve removed field tags