# 🧩 Nested Messages in Protocol Buffers

In Protocol Buffers, a **nested message** means defining a message **inside another message**.

It helps you group related data together in a clean structure.

---

# 🤔 Why Use Nested Messages?

Nested messages are useful when:

- A structure belongs only to one parent 🧠
- You want better organization 📦
- You want to avoid global message clutter 🧹

---

# 🏗️ Basic Syntax

```proto id="a1x9qp"
message Parent {
  message Child {
    // fields here
  }
}
```

---

# 📦 Simple Example

```proto id="b2m8tv"
syntax = "proto3";

message User {

  message Address {
    string city = 1;
    string country = 2;
  }

  int32 id = 1;
  string name = 2;
  Address address = 3;
}
```

---

# 🧠 How to Read It

```proto id="c3n7xp"
message Address {
```

👉 This message exists **inside User**

So:

- `Address` belongs to `User`
- It is not a global message

---

# 📊 Example Structure

```text id="d4m6qp"
User
 ├── id
 ├── name
 └── Address
       ├── city
       └── country
```

---

# 🧱 Real-World Analogy

Think of a **User profile card 🪪**:

Inside it:

- Name
- ID
- Address (inside address box 📦)

Address is not separate — it belongs to the user.

---

# 📦 Full Example

```proto id="e5k9mn"
syntax = "proto3";

message Company {

  message Employee {

    message Address {
      string city = 1;
      string state = 2;
    }

    int32 id = 1;
    string name = 2;
    Address address = 3;
  }

  string company_name = 1;
  repeated Employee employees = 2;
}
```

---

# 🧠 How It Works

You can access nested messages like:

```text id="f6v2qp"
Company.Employee.Address
```

---

# 🐍 Python Example

```python id="g7m3tv"
company = Company()

employee = company.employees.add()
employee.id = 1
employee.name = "Abhishek"

employee.address.city = "Bangalore"
employee.address.state = "Karnataka"
```

---

# 🔁 Nested vs Separate Messages

---

## 🟢 Nested Message

```proto id="h8n4xp"
message User {
  message Address {
    string city = 1;
  }
}
```

### 👍 Benefits:
- Tightly related structure
- Better organization
- Cleaner hierarchy

---

## 🔵 Separate Message

```proto id="i9m5qp"
message Address {
  string city = 1;
}

message User {
  Address address = 1;
}
```

### 👍 Benefits:
- Reusable across multiple messages
- Better for shared models

---

# 🤔 When to Use Nested Messages

Use nested messages when:

✔ The inner message is only useful inside the parent  
✔ You want logical grouping  
✔ It improves readability  

---

# 🚫 When NOT to Use Nested Messages

Avoid nesting when:

❌ You need reuse across multiple messages  
❌ The structure is shared globally  
❌ It makes the file too deeply nested  

---

# 🧠 Key Rule

👉 Nesting is about **logical grouping**, not just structure.

---

# 📊 Example: Order System

```proto id="j1x7qp"
message Order {

  message Item {
    int32 product_id = 1;
    int32 quantity = 2;
  }

  int32 order_id = 1;
  repeated Item items = 2;
}
```

---

# 🧠 Why This Works Well

- `Item` only belongs to `Order`
- No need to reuse `Item` elsewhere
- Keeps schema clean

---

# ⚡ Benefits of Nested Messages

---

## ✅ 1. Better Organization

Everything related stays together.

---

## ✅ 2. Clear Hierarchy

You can clearly see relationships.

---

## ✅ 3. Avoids Global Pollution

No unnecessary global message names.

---

## ✅ 4. Improves Readability

Easier to understand structure at a glance.

---

# ⚠️ Important Notes

---

## 🔹 Nested messages are still full types

Even if nested, they behave like normal messages.

---

## 🔹 Can be deeply nested

But avoid too many levels:

```text
A → B → C → D ❌ (hard to read)
```

---

# 🎯 Final Thoughts

Nested messages in Protocol Buffers help you:

- Organize data better 📦
- Group related structures 🧩
- Improve readability 📖

But use them wisely:

👉 Use nesting for tight relationships  
👉 Use separate messages for reusable components