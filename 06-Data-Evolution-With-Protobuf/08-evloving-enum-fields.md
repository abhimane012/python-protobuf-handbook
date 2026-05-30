# 🔄 Evolving Enum Fields in Protocol Buffers

Enums in Protocol Buffers can also evolve over time.

You can:

✅ Add new enum values  
✅ Rename enum values  
⚠️ Remove values carefully  

But you must follow some important rules to avoid breaking compatibility.

---

# 🧠 Reminder: What is an Enum?

Enums represent a fixed set of values.

Example:

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
  INACTIVE = 2;
}
```

---

# 📦 Used Inside Message

```proto
message User {
  Status status = 1;
}
```

---

# ⚡ Important Concept

Internally, Protobuf stores:

```text
Enum Numbers
```

NOT enum names.

Example:

```proto
ACTIVE = 1;
```

Stored internally as:

```text
1
```

This is very important for evolution.

---

# 1️⃣ Adding New Enum Values

Adding new enum values is safe ✅

---

# 🟢 Old Version

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
}
```

---

# 🟡 New Version

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
  INACTIVE = 2;
}
```

Safe ✅

---

# 🧠 What Happens?

Old systems know only:

```text
UNKNOWN
ACTIVE
```

If they receive:

```text
INACTIVE = 2
```

they treat it as an unknown enum value safely.

---

# ✅ Rule

Always use a NEW enum number.

---

# ❌ Wrong

```proto
ACTIVE = 2;
```

Previously:

```proto
ACTIVE = 1;
```

Changing enum numbers breaks compatibility ❌

---

# 2️⃣ Never Change Existing Enum Numbers

---

# ❌ Dangerous

## Old Version

```proto
enum Status {
  ACTIVE = 1;
}
```

---

## Wrong New Version

```proto
enum Status {
  ACTIVE = 5;
}
```

Now old systems think:

```text
1 = ACTIVE
```

but new systems think:

```text
5 = ACTIVE
```

Broken compatibility ❌

---

# ✅ Correct

Keep old numbers unchanged.

```proto
ACTIVE = 1;
```

---

# 🧠 Golden Rule

```text
Never change existing enum numeric values
```

---

# 3️⃣ Renaming Enum Values

Renaming enum names is usually safe ✅

because Protobuf stores numbers internally.

---

# 🟢 Old Version

```proto
enum Status {
  ACTIVE = 1;
}
```

---

# 🟡 New Version

```proto
enum Status {
  ENABLED = 1;
}
```

Safe ✅

---

# 🧠 Why?

Internally both still mean:

```text
1
```

Only the label changed.

---

# ⚠️ But Be Careful

Renaming may confuse developers and APIs.

So rename only when necessary.

---

# 4️⃣ Removing Enum Values

Removing enum values needs care ⚠️

---

# 🟢 Old Version

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
  INACTIVE = 2;
}
```

---

# 🟡 New Version

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
}
```

---

# ⚠️ Problem

Old systems may still send:

```text
INACTIVE = 2
```

New systems may not understand it.

---

# ✅ Better Approach

Reserve removed enum numbers.

---

# Example

```proto
enum Status {

  reserved 2;

  UNKNOWN = 0;
  ACTIVE = 1;
}
```

---

# 🧠 Why Reserve?

Prevents accidental reuse.

---

# ❌ Dangerous Reuse

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
  BLOCKED = 2;
}
```

Previously:

```text
2 = INACTIVE
```

Now:

```text
2 = BLOCKED
```

This changes meaning and breaks compatibility ❌

---

# 5️⃣ Reserve Enum Names Too

You can reserve old enum names.

---

# Example

```proto
enum Status {

  reserved "INACTIVE";

  UNKNOWN = 0;
  ACTIVE = 1;
}
```

---

# ⚡ Unknown Enum Values

Old systems may receive new enum values.

---

# Example

## Old Schema

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
}
```

---

## New Data

```text
status = 5
```

Old system does not know value `5`.

But Protobuf safely preserves unknown enum numbers.

---

# 🧠 Important Proto3 Rule

Proto3 enums must start with:

```proto
UNKNOWN = 0;
```

because:

```text
0 is default enum value
```

---

# 📊 Safe vs Unsafe Enum Changes

| Change | Safe? |
|---|---|
| Add new enum value | ✅ |
| Rename enum label | ✅ |
| Change enum number | ❌ |
| Reuse removed number | ❌ |
| Reserve removed number | ✅ |

---

# 🧱 Full Example

```proto
syntax = "proto3";

enum PaymentStatus {

  reserved 4;

  UNKNOWN = 0;
  SUCCESS = 1;
  FAILED = 2;
  PENDING = 3;
}
```

---

# 🚀 Best Practices

✅ Keep enum numbers stable  
✅ Add new values using new numbers  
✅ Reserve removed values  
✅ Start enums with `UNKNOWN = 0`  
✅ Avoid frequent renaming  

---

# 🎯 Final Thoughts

Enums evolve safely in Protocol Buffers if you follow a few important rules.

The most important rule is:

# 🔢 Never change existing enum numeric values

because Protobuf cares about:

```text
numbers
```

more than names.