# 🔄 Rules for Data Evolution in Protocol Buffers

Protocol Buffers are designed so your schema can change safely over time.

This is called:

```text
Data Evolution
```

Below are the most important rules you should follow.

---

# 1️⃣ Never Change Existing Field Tags

## ❌ Wrong

### Old Version

```proto
message User {
  string name = 1;
}
```

### New Version

```proto
message User {
  string name = 5;
}
```

This is dangerous because old systems expect:

```text
tag 1 = name
```

Changing the tag breaks compatibility.

---

## ✅ Correct

Keep old tags unchanged.

```proto
message User {
  string name = 1;
}
```

---

# 🧠 Golden Rule

```text
Never change field numbers once released.
```

---

# 2️⃣ You Can Add New Fields Safely

Adding new fields is completely safe.

---

## ✅ Old Version

```proto
message User {
  int32 id = 1;
  string name = 2;
}
```

---

## ✅ New Version

```proto
message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
```

---

# 🧠 What Happens?

Old applications:

```text
Know only:
- id
- name
```

They simply ignore:

```text
email
```

No crash ✅

---

# 3️⃣ Unknown Fields Are Ignored

If old or new code receives unknown fields, Protobuf safely ignores them.

Missing fields use default values.

---

## Example

### New Version

```proto
message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
```

---

## Old Version

```proto
message User {
  int32 id = 1;
  string name = 2;
}
```

---

# 🧠 What Happens?

Old code receives:

```text
id
name
email
```

But it only understands:

```text
id
name
```

So:

```text
email is ignored
```

---

# 🧠 Default Value Example

If new field is missing:

```proto
string email = 3;
```

Default becomes:

```text
""
(empty string)
```

---

# 4️⃣ Fields Can Be Removed Safely

You can remove fields safely IF:

✅ You never reuse the old tag number.

---

## 🟢 Old Version

```proto
message User {
  int32 id = 1;
  string email = 2;
}
```

---

## 🟡 New Version

```proto
message User {
  int32 id = 1;
}
```

This is safe ✅

---

# ❌ Dangerous

Do NOT reuse old tag numbers.

```proto
message User {
  int32 id = 1;
  int32 age = 2;
}
```

Previously:

```text
tag 2 = email
```

Now:

```text
tag 2 = age
```

This can corrupt data ❌

---

# ✅ Better Option: Reserve the Tag

```proto
message User {

  reserved 2;

  int32 id = 1;
}
```

Now nobody can accidentally reuse tag `2`.

---

# ✅ Alternative Option

Rename old field:

```proto
string OBSOLETE_email = 2;
```

This tells developers:

```text
Do not use this anymore
```

---

# 5️⃣ Some Type Changes Are Safe

Certain type changes are compatible.

Example:

```text
int32 → int64
```

---

# ✅ Example

### Old Version

```proto
message User {
  int32 age = 1;
}
```

---

## ✅ New Version

```proto
message User {
  int64 age = 1;
}
```

This is usually safe because:

```text
int64 can store everything int32 can store
```

---

# ⚠️ But Be Careful

Not all type changes are safe.

---

## ❌ Dangerous Type Change

```proto
string name = 1;
```

to:

```proto
int32 name = 1;
```

This breaks compatibility ❌

---

# 📊 Quick Summary Table

| Rule | Safe? |
|---|---|
| Add new fields | ✅ |
| Change existing tags | ❌ |
| Remove fields without reusing tags | ✅ |
| Reuse deleted tags | ❌ |
| Reserve removed tags | ✅ |
| int32 → int64 | ✅ |
| string → int32 | ❌ |

---

# 🎯 Final Thoughts

Protocol Buffers make schema evolution very safe IF you follow a few important rules.

Always remember:

✅ Keep old tags unchanged  
✅ Add new fields safely  
✅ Ignore unknown fields  
✅ Reserve removed tags  
✅ Be careful when changing field types  

The most important rule is:

# 🏷️ Never change existing field numbers