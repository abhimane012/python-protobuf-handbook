# 💬 Comments in Protocol Buffers

Comments in Protocol Buffers are used to **add notes or explanations** inside a `.proto` file.

They are ignored by the compiler and do NOT affect the generated code.

---

# 🤔 Why Do We Use Comments?

Comments help developers:

- Understand the code easily 🧠
- Explain field meaning 📌
- Document design decisions 🏗️
- Improve team collaboration 👥

---

# 🧾 Types of Comments in Protobuf

Protocol Buffers support **two types of comments**:

---

# 1️⃣ Single-line Comments

Use `//` for single-line comments.

## Example

```proto id="kq8m1z"
syntax = "proto3";

// This is a user message
message User {
  int32 id = 1; // Unique user ID
  string name = 2; // User's full name
}
```

---

## 🧠 How It Works

Everything after `//` on the same line is ignored.

```text id="x1v8qn"
// This is ignored by Protobuf compiler
```

---

# 2️⃣ Multi-line Comments

Use `/* */` for multiple lines.

## Example

```proto id="m9t2ab"
/*
This message represents a user in the system.
It contains basic user information like id and name.
*/
message User {
  int32 id = 1;
  string name = 2;
}
```

---

## 🧠 How It Works

Everything between:

```text
/* and */
```

is ignored.

---

# 📦 Where You Can Use Comments

You can add comments in many places:

---

## ✅ Before a message

```proto id="z7m4kp"
// Represents a product in the system
message Product {
  int32 id = 1;
}
```

---

## ✅ Before a field

```proto id="v3n8qt"
message Product {
  // Unique product ID
  int32 id = 1;

  // Name of the product
  string name = 2;
}
```

---

## ✅ Inline comments

```proto id="p2x7mn"
int32 price = 1; // price in USD
```

---

# 🧠 Why Comments Are Important in Protobuf

Unlike code logic, `.proto` files define a **data contract**.

So comments help explain:

- What the field means
- Why it exists
- How it should be used

---

# 📊 Real-World Example

```proto id="q8v1lm"
syntax = "proto3";

/*
Represents a user in the system.
Used across authentication and profile services.
*/
message User {

  // Unique identifier for the user
  int32 id = 1;

  // Full name of the user
  string name = 2;

  // Email address used for login
  string email = 3;

  // Indicates if the user is verified
  bool is_verified = 4;
}
```

---

# ⚡ Key Rules for Comments

---

## ✅ 1. Comments are ignored by compiler

They do NOT affect:

- Serialization
- Deserialization
- Generated code

---

## ✅ 2. Use comments for clarity

Bad:

```proto id="a1b2cd"
int32 id = 1;
```

Good:

```proto id="e4f5gh"
// Unique identifier for user
int32 id = 1;
```

---

## ✅ 3. Keep comments simple

Avoid writing long essays.

Keep it:

- Short
- Clear
- Useful

---

# 🚫 What Comments Cannot Do

Comments CANNOT:

- Change behavior of code ❌
- Affect field tags ❌
- Affect serialization ❌

They are ONLY for humans.

---

# 🧠 Best Practices

## ✔️ Use comments for:

- Field explanations
- Business meaning
- API usage notes
- Constraints (if any)

---

## ❌ Avoid:

- Over-commenting obvious things
- Writing duplicate information
- Long unnecessary descriptions

---

# 🧱 Example: Clean Protobuf File

```proto id="t6m9pq"
syntax = "proto3";

// User data model used in authentication system
message User {

  // Unique user ID
  int32 id = 1;

  // User's display name
  string name = 2;

  // Email used for login
  string email = 3;
}
```

---

# 🎯 Final Thoughts

Comments in Protocol Buffers are simple but very important.

They help make `.proto` files:

- Easier to read 📖
- Easier to maintain 🔧
- Easier to collaborate 👥

Use them to explain **why something exists**, not just what it is.