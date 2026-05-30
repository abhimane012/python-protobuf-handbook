# 🎯 `oneOf` in Protocol Buffers

`oneOf` is used when:

> ✅ Only ONE field out of multiple fields can exist at a time.

It helps save memory and enforce mutually exclusive fields.

---

# 🤔 Why Do We Need `oneof`?

Sometimes data can have different forms.

Example:

A user can log in using:

- email 📧
- phone 📱
- username 👤

But only one should be used at a time.

---

# ❌ Without `oneof`

```proto
message LoginRequest {
  string email = 1;
  string phone = 2;
  string username = 3;
}
```

Problem:

```text
All fields can be set together
```

This creates confusion ❌

---

# ✅ With `oneof`

```proto
syntax = "proto3";

message LoginRequest {

  oneof login_method {
    string email = 1;
    string phone = 2;
    string username = 3;
  }
}
```

Now only ONE field can exist at a time ✅

---

# 🧠 How `oneof` Works

If one field is set:

```text
all other fields inside oneof are automatically cleared
```

---

# 📦 Example

```proto
message Payment {

  oneof payment_method {
    string card_number = 1;
    string upi_id = 2;
    string paypal_email = 3;
  }
}
```

---

# 🧠 Meaning

A payment can happen using:

- card 💳
- UPI 📱
- PayPal 🌐

But not all together.

---

# 🐍 Python Example

```python
payment = Payment()

payment.card_number = "1234"
```

Now:

```text
upi_id = cleared
paypal_email = cleared
```

---

# ⚡ Setting Another Field

```python
payment.upi_id = "abc@upi"
```

Now Protobuf automatically removes:

```text
card_number
```

Only:

```text
upi_id
```

remains active.

---

# 📊 Real-World Analogy

Think of a light switch 💡

Only one option can be ON at a time.

Turning ON another switch automatically turns OFF the previous one.

That’s exactly how `oneof` behaves.

---

# 🧱 Full Example

```proto
syntax = "proto3";

message Notification {

  oneof message_type {
    string sms = 1;
    string email = 2;
    string push_notification = 3;
  }
}
```

---

# 🧠 Possible Valid States

✅ SMS only  
✅ Email only  
✅ Push notification only  

---

# ❌ Invalid State

```text
sms + email together
```

`oneof` prevents this.

---

# ⚡ Benefits of `oneof`

---

# ✅ 1. Prevents Invalid Data

Only one field can exist.

---

# ✅ 2. Saves Memory

Only active field is stored.

---

# ✅ 3. Cleaner API Design

Makes intent very clear.

---

# ✅ 4. Better Validation

Useful for requests with multiple possible formats.

---

# 🧠 Common Use Cases

`oneof` is commonly used for:

- login methods 🔐
- payment methods 💳
- message types 📩
- search filters 🔍
- API requests 🌐

---

# 📦 Example: Search API

```proto
message SearchRequest {

  oneof search_by {
    string username = 1;
    string email = 2;
    int32 user_id = 3;
  }
}
```

Search can happen using only one option.

---

# ⚠️ Important Rules

---

# ❗ Only One Field Can Be Active

Setting new field clears previous field automatically.

---

# ❗ Fields Inside `oneof` Share Memory

Only active field uses memory.

---

# ❗ Normal Fields Can Exist Outside `oneof`

Example:

```proto
message User {

  int32 id = 1;

  oneof contact {
    string email = 2;
    string phone = 3;
  }
}
```

`id` always exists normally.

---

# 🐍 Python Example

```python
user = User()

user.email = "abc@gmail.com"

print(user)
```

Output:

```text
email: "abc@gmail.com"
```

---

# Setting another field:

```python
user.phone = "9999999999"
```

Now output becomes:

```text
phone: "9999999999"
```

`email` gets removed automatically.

---

# 🧠 Check Which Field Is Active

Python:

```python
print(user.WhichOneof("contact"))
```

Output:

```text
phone
```

---

# 📊 oneof vs Normal Fields

| Feature | Normal Fields | oneof |
|---|---|---|
| Multiple fields allowed | ✅ | ❌ |
| Only one active field | ❌ | ✅ |
| Memory optimized | ❌ | ✅ |
| Auto-clear behavior | ❌ | ✅ |

---

# 🚫 Common Beginner Mistakes

---

# ❌ Assuming Multiple Fields Stay Together

Inside `oneof`, setting one field removes others.

---

# ❌ Using `oneof` for Unrelated Fields

Only group mutually exclusive fields.

---

# ❌ Forgetting Field Presence Behavior

Only one field can be active.

---

# 🎯 Final Thoughts

`oneof` is a powerful feature in Protocol Buffers used when:

👉 multiple fields are possible  
👉 but only ONE should exist at a time

It helps create:

✅ cleaner schemas  
✅ safer APIs  
✅ memory-efficient messages  
✅ better validation