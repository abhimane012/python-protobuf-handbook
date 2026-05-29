# 🧩 Protocol Buffer Scalar Types

In Protocol Buffers, **scalar types** are the basic built-in data types used to store simple values.

Think of them like primitive data types in programming languages.

Examples:

- Integer
- String
- Boolean
- Decimal numbers

---

# 📦 Why Scalar Types Matter

Scalar types help Protobuf understand:

- What kind of data is being stored
- How much memory is needed
- How data should be serialized

Example:

```proto
string name = 1;
```

Here:

- `string` → Scalar type
- `name` → Field name
- `1` → Field tag

---

# 🧠 Common Scalar Types

---

# 🔢 Integer Types

Used for storing whole numbers.

---

## `int32`

Stores normal integer values.

```proto
int32 age = 1;
```

✅ Example values:

```text
10
25
100
```

---

## `int64`

Stores very large integer values.

```proto
int64 population = 1;
```

Used when numbers can become very large.

---

## `uint32`

Unsigned 32-bit integer.

Only positive numbers.

```proto
uint32 score = 1;
```

✅ Allowed:

```text
0
10
100
```

❌ Not allowed:

```text
-5
```

---

## `uint64`

Unsigned large integer.

```proto
uint64 total_users = 1;
```

---

## `sint32`

Optimized signed integer.

Better for storing negative numbers efficiently.

```proto
sint32 temperature = 1;
```

---

## `sint64`

Large optimized signed integer.

```proto
sint64 balance = 1;
```

---

## `fixed32`

Fixed-size 32-bit integer.

Good when values are usually large.

```proto
fixed32 big_number = 1;
```

---

## `fixed64`

Fixed-size large integer.

```proto
fixed64 huge_number = 1;
```

---

# 🔤 String Type

## `string`

Used for storing text.

```proto
string first_name = 1;
```

✅ Example values:

```text
"Abhishek"
"Hello"
"Protocol Buffers"
```

---

# ✅ Boolean Type

## `bool`

Stores:

- `true`
- `false`

```proto
bool is_active = 1;
```

Example:

```text
true
false
```

---

# 🔢 Decimal Number Types

Used for floating-point numbers.

---

## `float`

Stores decimal numbers.

```proto
float price = 1;
```

Example:

```text
10.5
99.99
```

Less precision than `double`.

---

## `double`

Stores larger and more precise decimal values.

```proto
double salary = 1;
```

More accurate than `float`.

---

# 📦 Binary Data Type

## `bytes`

Used for raw binary data.

```proto
bytes image = 1;
```

Commonly used for:

- Images
- Files
- Encrypted data

---

# 📊 Complete Scalar Type Table

| Scalar Type | Description | Example |
|---|---|---|
| int32 | Normal integer | 10 |
| int64 | Large integer | 999999999 |
| uint32 | Positive integer | 100 |
| uint64 | Large positive integer | 999999 |
| sint32 | Optimized signed integer | -20 |
| sint64 | Large signed integer | -99999 |
| fixed32 | Fixed-size integer | 500 |
| fixed64 | Large fixed-size integer | 999999 |
| bool | True/False | true |
| string | Text | "Hello" |
| float | Decimal number | 10.5 |
| double | Precise decimal | 99.999 |
| bytes | Binary data | image/file |

---

# 🏗️ Full Example

```proto
syntax = "proto3";

message User {

  int32 id = 1;

  string name = 2;

  bool is_verified = 3;

  float height = 4;

  double salary = 5;

  bytes profile_image = 6;
}
```

---

# 🔍 Breakdown

| Field | Scalar Type | Meaning |
|---|---|---|
| id | int32 | Integer ID |
| name | string | User name |
| is_verified | bool | Verification status |
| height | float | Decimal value |
| salary | double | Precise decimal |
| profile_image | bytes | Binary image data |

---

# ⚡ Important Notes

---

## ✅ Choose Correct Types

Example:

```proto
int32 age = 1;
```

Good for age because age is a small integer.

---

## ✅ Use `string` for Text

```proto
string email = 1;
```

---

## ✅ Use `bool` for True/False Values

```proto
bool is_admin = 1;
```

---

## ✅ Use `double` for High Precision

```proto
double account_balance = 1;
```

---

# 🚫 Common Beginner Mistakes

---

## ❌ Using Wrong Type

Wrong:

```proto
string age = 1;
```

Better:

```proto
int32 age = 1;
```

---

## ❌ Using `float` for Precise Financial Data

`float` can lose precision.

Use:

```proto
double
```

for better accuracy.

---

# 🎯 Final Thoughts

Scalar types are the foundation of every Protocol Buffer message.

They define:

- What kind of data is stored
- How data is serialized
- How efficiently data is transferred

Understanding scalar types is important before learning:

- Nested messages
- Repeated fields
- Enums
- gRPC
- Advanced Protobuf concepts