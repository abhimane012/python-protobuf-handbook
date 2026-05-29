# 🎯 Default Values in Protocol Buffers

In Protocol Buffers, every field has a **default value** when no value is assigned.

This means:

👉 Even if you don’t set a field, it still has a value.

---

# 🤔 Why Do Default Values Exist?

Default values help Protobuf:

- Avoid null values ❌
- Keep data consistent 📦
- Simplify serialization ⚡
- Ensure safe reading of missing fields 🛡️

---

# 🧠 Important Concept

In Protobuf:

> Fields are NEVER null.  
> They always have a default value.

---

# 📦 Default Values by Type

---

# 🔢 1. Numeric Types (int, float, double)

## Types:
- `int32`
- `int64`
- `uint32`
- `uint64`
- `float`
- `double`
- `sint32`
- `sint64`

## Default Value:
```text
0
```

---

## Example

```proto id="xk2m9v"
message User {
  int32 age = 1;
}
```

If not set:

```text
age = 0
```

---

# 🔤 2. String Type

## Type:
- `string`

## Default Value:
```text
""
(empty string)
```

---

## Example

```proto id="v9q2mn"
message User {
  string name = 1;
}
```

If not set:

```text
name = ""
```

---

# ✅ 3. Boolean Type

## Type:
- `bool`

## Default Value:
```text
false
```

---

## Example

```proto id="t3m8xp"
message User {
  bool is_active = 1;
}
```

If not set:

```text
is_active = false
```

---

# 📦 4. Bytes Type

## Type:
- `bytes`

## Default Value:
```text
empty bytes
```

---

## Example

```proto id="k7m2qp"
message File {
  bytes data = 1;
}
```

If not set:

```text
data = ""
```

(empty byte array)

---

# 🧩 5. Enum Type

## Default Value:
👉 First enum value is always the default.

---

## Example

```proto id="n4x7pt"
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
  INACTIVE = 2;
}

message User {
  Status status = 1;
}
```

If not set:

```text
status = UNKNOWN
```

---

# 📊 Summary Table

| Field Type | Default Value |
|---|---|
| int32 / int64 | 0 |
| float / double | 0 |
| uint32 / uint64 | 0 |
| sint32 / sint64 | 0 |
| string | "" (empty string) |
| bool | false |
| bytes | empty |
| enum | first value |

---

# 🧠 Key Behavior in Protobuf

---

## ❗ 1. Missing Field ≠ Null

In JSON:

```json
{ }
```

In Protobuf:

```text
All fields still exist with default values
```

---

## ❗ 2. Default Value is NOT "set value"

Important difference:

| Situation | Meaning |
|---|---|
| Field not set | Returns default value |
| Field explicitly set to 0 | Same value, but "set" |

---

## ⚠️ 3. You Cannot Distinguish Missing vs Default (proto3)

Example:

```proto
int32 age = 1;
```

If you receive:

```text
age = 0
```

You cannot know if:

- It was not set
- OR explicitly set to 0

---

# 🧪 Example

```proto id="m9x7kp"
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
  bool is_verified = 3;
}
```

If no values are set:

```text
id = 0
name = ""
is_verified = false
```

---

# 🧠 Real-World Analogy

Think of a form 🧾:

| Field | Default |
|---|---|
| Age | 0 |
| Name | empty |
| Checkbox | unchecked |

Even if you don’t fill the form, it still has values.

---

# 🚀 Why Default Values Are Useful

## ✅ Avoid null checks

No need for:

```python
if name is not None:
```

---

## ✅ Simplifies parsing

No missing fields handling required.

---

## ✅ Saves memory logic complexity

Always predictable values.

---

# ⚠️ Common Mistakes

---

## ❌ Assuming NULL exists

Protobuf does NOT have null.

---

## ❌ Expecting missing detection (proto3)

Proto3 does not track if a field was set.

---

# 🧱 Example Full Message

```proto id="q8m2vt"
syntax = "proto3";

message Product {

  int32 id = 1;

  string name = 2;

  double price = 3;

  bool in_stock = 4;
}
```

If empty message is received:

```text
id = 0
name = ""
price = 0.0
in_stock = false
```

---

# 🎯 Final Thoughts

Default values are a core concept in Protocol Buffers.

They ensure:

- Every field always has a value
- No null handling is needed
- Data is predictable

But remember:

👉 In proto3, you cannot differentiate between:
- "not set"
- "set to default value"

This is an important design choice in Protobuf.