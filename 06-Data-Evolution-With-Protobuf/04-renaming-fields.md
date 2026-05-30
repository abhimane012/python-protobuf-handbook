# ✏️ Renaming Fields in Protocol Buffers

In Protocol Buffers, you can safely change a field name without breaking compatibility.

This is because Protobuf uses:

```text
Field Tags
```

internally — not field names.

---

# 🧠 Important Concept

Protocol Buffers identify fields using:

```proto
= 1
= 2
= 3
```

NOT by:

```proto
name
email
age
```

So changing the field name is usually safe.

---

# 🟢 Old Version

```proto
syntax = "proto3";

message User {
  string full_name = 1;
}
```

---

# 🟡 New Version

```proto
syntax = "proto3";

message User {
  string name = 1;
}
```

---

# ✅ Why This Is Safe

The tag number is still:

```text
1
```

So Protobuf understands:

```text
tag 1 = same field
```

No compatibility issue ✅

---

# 🧠 What Actually Changed?

Only this changed:

```text
full_name → name
```

Tag remained:

```text
1
```

---

# 📦 Real Example

---

# 🟢 Version 1

```proto
message Product {
  string product_name = 1;
}
```

---

# 🟡 Version 2

```proto
message Product {
  string name = 1;
}
```

Safe ✅

---

# ⚡ Why Renaming Works

When Protobuf serializes data:

```proto
string name = 1;
```

it stores:

```text
tag 1 + value
```

It does NOT store:

```text
"name"
```

That’s why renaming is safe.

---

# 🚫 Dangerous Rename Example

Renaming alone is safe ❌

But renaming + changing tag is dangerous.

---

# ❌ Wrong

```proto
message User {
  string name = 5;
}
```

Previously:

```proto
string full_name = 1;
```

Now tag changed:

```text
1 → 5
```

This breaks compatibility ❌

---

# ✅ Correct Rename

```proto
message User {
  string name = 1;
}
```

Only rename the field name.

Keep the same tag.

---

# 🧠 Real-World Analogy

Think of a student roll number 🎓

---

## Before

```text
Roll No: 1
Name: Rahul
```

---

## After Name Change

```text
Roll No: 1
Name: Rahul Sharma
```

Roll number is still the same person.

Tags work similarly in Protobuf.

---

# ⚠️ Things to Remember

---

# ✅ Field Name Can Change

Safe:

```proto
full_name → name
```

---

# ❌ Tag Number Must NOT Change

Unsafe:

```proto
= 1 → = 5
```

---

# ❌ Field Type Should Usually Stay Same

Dangerous:

```proto
string age = 1;
```

to:

```proto
int32 age = 1;
```

---

# 📦 Example with Multiple Renames

---

# 🟢 Old Version

```proto
message Employee {
  string employee_name = 1;
  string employee_email = 2;
}
```

---

# 🟡 New Version

```proto
message Employee {
  string name = 1;
  string email = 2;
}
```

Safe ✅

---

# 🧠 Why Developers Rename Fields

Common reasons:

- Better readability 📖
- Cleaner naming ✨
- Shorter names 🧹
- Improved consistency 📦

---

# ⚡ Best Practices

✅ Keep tag numbers unchanged  
✅ Rename only when necessary  
✅ Use meaningful names  
✅ Avoid frequent renaming  

---

# 📊 Quick Summary

| Change | Safe? |
|---|---|
| Rename field only | ✅ |
| Rename + same tag | ✅ |
| Rename + new tag | ❌ |
| Rename + change type | ⚠️ Dangerous |

---

# 🎯 Final Thoughts

Renaming fields in Protocol Buffers is usually safe because:

👉 Protobuf cares about field tags, not field names.

As long as:

✅ Tag number stays same  
✅ Type stays compatible  

your systems will continue working correctly.