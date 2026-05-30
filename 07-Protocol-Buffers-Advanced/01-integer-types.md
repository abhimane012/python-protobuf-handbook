# 🔢 Integer Types in Protocol Buffers

Protocol Buffers provide multiple integer types.

Different types exist because different applications need:

- smaller numbers 📦
- huge numbers 🚀
- negative values ➖
- optimized storage ⚡

---

# 🧠 Integer Types in Protobuf

| Type | Signed? | Size |
|---|---|---|
| int32 | ✅ Yes | 32-bit |
| int64 | ✅ Yes | 64-bit |
| uint32 | ❌ No | 32-bit |
| uint64 | ❌ No | 64-bit |
| sint32 | ✅ Yes | 32-bit |
| sint64 | ✅ Yes | 64-bit |
| fixed32 | ❌ No | Fixed 32-bit |
| fixed64 | ❌ No | Fixed 64-bit |
| sfixed32 | ✅ Yes | Fixed 32-bit |
| sfixed64 | ✅ Yes | Fixed 64-bit |

---

# 📦 1️⃣ `int32`

Signed 32-bit integer.

Supports:

✅ positive numbers  
✅ negative numbers  

---

# 📊 Range

```text
-2,147,483,648
to
2,147,483,647
```

---

# ✅ Example

```proto
int32 age = 1;
```

---

# 🧠 When to Use

Use for normal integers like:

- age 👤
- quantity 📦
- score 🎯
- count 🔢

---

# ⚠️ Note

Negative numbers are not storage-efficient in regular `int32`.

---

# 📦 2️⃣ `int64`

Signed 64-bit integer.

Stores very large numbers.

---

# 📊 Range

```text
-9,223,372,036,854,775,808
to
9,223,372,036,854,775,807
```

---

# ✅ Example

```proto
int64 population = 1;
```

---

# 🧠 When to Use

Use for:

- timestamps ⏰
- huge counters 📈
- database IDs 🗄️
- financial systems 💰

---

# 📦 3️⃣ `uint32`

Unsigned 32-bit integer.

Supports only:

✅ positive numbers  
❌ no negatives

---

# 📊 Range

```text
0
to
4,294,967,295
```

---

# ✅ Example

```proto
uint32 quantity = 1;
```

---

# 🧠 When to Use

Use when value can NEVER be negative.

Examples:

- quantity 📦
- inventory 🏬
- file size 📁

---

# 📦 4️⃣ `uint64`

Unsigned 64-bit integer.

Very large positive numbers only.

---

# 📊 Range

```text
0
to
18,446,744,073,709,551,615
```

---

# ✅ Example

```proto
uint64 views = 1;
```

---

# 🧠 When to Use

Use for:

- massive counters 📈
- analytics 📊
- large IDs 🗄️

---

# 📦 5️⃣ `sint32`

Signed integer optimized for negative numbers.

---

# 📊 Range

Same as `int32`

```text
-2,147,483,648
to
2,147,483,647
```

---

# ✅ Example

```proto
sint32 temperature = 1;
```

---

# 🧠 Why `sint32` Exists

Regular `int32` stores negative numbers inefficiently.

`sint32` uses:

```text
ZigZag Encoding
```

which saves space for negative values.

---

# 🧠 When to Use

Use when:

✅ many negative numbers exist

Examples:

- temperatures 🌡️
- balance changes 💰
- coordinates 📍

---

# 📦 6️⃣ `sint64`

Same idea as `sint32` but larger range.

---

# 📊 Range

Same as `int64`

```text
-9,223,372,036,854,775,808
to
9,223,372,036,854,775,807
```

---

# ✅ Example

```proto
sint64 account_balance = 1;
```

---

# 🧠 When to Use

Large signed numbers with many negatives.

---

# 📦 7️⃣ `fixed32`

Always uses fixed 4 bytes.

Unsigned.

---

# 📊 Range

```text
0
to
4,294,967,295
```

---

# ✅ Example

```proto
fixed32 hash = 1;
```

---

# 🧠 Why Use Fixed Types?

Regular integers use variable-length encoding.

Fixed types are better when values are usually large.

---

# 🧠 When to Use

Use for:

- hashes 🔐
- large numeric values 📊
- performance optimization ⚡

---

# 📦 8️⃣ `fixed64`

Fixed 8-byte unsigned integer.

---

# 📊 Range

```text
0
to
18,446,744,073,709,551,615
```

---

# ✅ Example

```proto
fixed64 big_hash = 1;
```

---

# 📦 9️⃣ `sfixed32`

Fixed-size signed 32-bit integer.

---

# 📊 Range

```text
-2,147,483,648
to
2,147,483,647
```

---

# ✅ Example

```proto
sfixed32 coordinate = 1;
```

---

# 📦 🔟 `sfixed64`

Fixed-size signed 64-bit integer.

---

# 📊 Range

```text
-9,223,372,036,854,775,808
to
9,223,372,036,854,775,807
```

---

# ✅ Example

```proto
sfixed64 large_coordinate = 1;
```

---

# ⚡ Variable vs Fixed Encoding

| Type | Storage Style |
|---|---|
| int32/int64 | Variable size |
| fixed32/fixed64 | Fixed size |

---

# 🧠 Variable Encoding

Small numbers use less space.

Efficient for small values ✅

---

# 🧠 Fixed Encoding

Always same size.

Efficient for consistently large values ✅

---

# 📊 Quick Recommendation Table

| Type | Best Use Case |
|---|---|
| int32 | normal integers |
| int64 | huge integers |
| uint32 | positive-only values |
| uint64 | huge positive-only values |
| sint32 | many negative values |
| sint64 | huge negative values |
| fixed32 | large fixed-size numbers |
| fixed64 | huge fixed-size numbers |
| sfixed32 | signed fixed-size numbers |
| sfixed64 | huge signed fixed-size numbers |

---

# 🚀 Most Commonly Used Types

In real projects, developers mostly use:

✅ int32  
✅ int64  
✅ uint32  
✅ sint32  

The fixed types are used less often.

---

# ⚠️ Important Tip

If unsure:

```text
Use int32 for normal numbers
Use int64 for very large numbers
```

---

# 🎯 Final Thoughts

Protocol Buffers provide multiple integer types to balance:

- storage efficiency 📦
- performance ⚡
- numeric range 📊

Choosing the correct type helps:

✅ reduce message size  
✅ improve performance  
✅ avoid overflow problems