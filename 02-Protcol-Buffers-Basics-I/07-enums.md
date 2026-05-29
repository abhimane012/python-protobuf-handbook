# 🧩 Enums in Protocol Buffers

In Protocol Buffers, an **enum (enumeration)** is a way to define a field that can take only a **fixed set of possible values**.

Think of it like a dropdown menu 🎛️ where you can choose only one option.

---

# 🤔 Why Do We Need Enums?

Without enums, you might use:

```proto
int32 status = 1;
```

But this is unclear:
- What does `1` mean?
- What does `2` mean?

👉 Enums solve this by giving **meaningful names to numbers**.

---

# 🏗️ Basic Enum Syntax

```proto
enum EnumName {
  OPTION_1 = 0;
  OPTION_2 = 1;
  OPTION_3 = 2;
}
```

---

# 📦 Example: User Status

```proto id="m2k9qp"
syntax = "proto3";

enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
  INACTIVE = 2;
  BLOCKED = 3;
}

message User {
  int32 id = 1;
  string name = 2;
  Status status = 3;
}
```

---

# 🧠 How to Read It

```proto
Status status = 3;
```

| Part | Meaning |
|---|---|
| Status | Enum type |
| status | Field name |
| 3 | Field tag |

---

# 📊 Enum Values Explained

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
  INACTIVE = 2;
  BLOCKED = 3;
}
```

| Name | Value | Meaning |
|---|---|---|
| UNKNOWN | 0 | Default value |
| ACTIVE | 1 | User is active |
| INACTIVE | 2 | User is inactive |
| BLOCKED | 3 | User is blocked |

---

# ⚠️ Important Rule (VERY IMPORTANT)

## 👉 First enum value MUST be 0

In proto3:

```proto
UNKNOWN = 0;
```

is required because:

- If no value is set, default is always 0
- So enum must have a valid default

---

# 🧪 Example Behavior

```proto
User user;
```

If `status` is not set:

```text
status = UNKNOWN (0)
```

---

# 🧠 Real-World Analogy

Think of an ATM card status 💳:

You can only have one state:

- ACTIVE
- BLOCKED
- EXPIRED

You CANNOT have multiple statuses at once.

That’s exactly what enums enforce.

---

# 🏗️ Enum Inside Message

Enums are usually used inside messages.

```proto id="v7m2xp"
message Order {

  enum OrderStatus {
    PLACED = 0;
    SHIPPED = 1;
    DELIVERED = 2;
    CANCELLED = 3;
  }

  int32 order_id = 1;
  OrderStatus status = 2;
}
```

---

# 📦 Example Data

```text
order_id = 101
status = SHIPPED
```

---

# 🔢 Enums Are Stored as Numbers

Even though you write:

```proto
ACTIVE
```

Protobuf stores it as:

```text
1
```

This makes it:

- Smaller 💾
- Faster ⚡
- Efficient 🚀

---

# 🧠 Key Properties of Enums

---

## ✅ 1. Only One Value Allowed

```proto
Status status = 3;
```

You can only assign one value:

```text
ACTIVE OR BLOCKED OR INACTIVE
```

---

## ❌ Not Allowed

Enums do NOT allow multiple values:

```text
ACTIVE + BLOCKED ❌
```

---

## ✅ 2. Works Like Integer Internally

```proto
ACTIVE = 1
```

So internally:

```text
status = 1
```

---

## ⚡ 3. Default Value is Always First Enum

```proto
UNKNOWN = 0;
```

If not set, Protobuf uses:

```text
0
```

---

# 🚀 Why Enums Are Useful

## ✅ Better Readability

Instead of:

```proto
int32 status = 1;
```

You get:

```proto
Status status = 1;
```

---

## ✅ Prevent Invalid Values

Bad:

```text
status = 999 ❌
```

Good:

```text
status = ACTIVE ✔
```

---

## ✅ Easier Maintenance

Code becomes self-explanatory.

---

## ✅ Cross-Language Support

Enums work in:

- Python
- Java
- Go
- C++
- JavaScript
- C#

---

# 🧱 Full Example

```proto id="p8m7xt"
syntax = "proto3";

message Payment {

  enum PaymentStatus {
    UNKNOWN = 0;
    SUCCESS = 1;
    FAILED = 2;
    PENDING = 3;
  }

  int32 payment_id = 1;
  double amount = 2;
  PaymentStatus status = 3;
}
```

---

# 📊 Example Output

```text
payment_id = 1
amount = 500.0
status = SUCCESS
```

---

# ⚠️ Common Mistakes

---

## ❌ Forgetting 0 value

Wrong:

```proto
enum Status {
  ACTIVE = 1;
  INACTIVE = 2;
}
```

Correct:

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
  INACTIVE = 2;
}
```

---

## ❌ Using enums for multiple values

Enums are NOT lists.

Use `repeated` for multiple values.

---

# 🧠 Enums vs Repeated Fields

| Feature | Enum | Repeated |
|---|---|---|
| Single value | ✅ | ❌ |
| Multiple values | ❌ | ✅ |
| Fixed options | ✅ | ❌ |
| List of items | ❌ | ✅ |

---

# 🎯 Final Thoughts

Enums are used in Protocol Buffers to represent:

- Fixed set of values
- Strongly defined states
- Better readability
- Safer data models

They are very useful for:

- Status fields
- Types
- Categories
- State machines

👉 If you need **only one choice from many options**, use enums.