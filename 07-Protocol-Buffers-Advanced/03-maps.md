# 🗺️ Maps in Protocol Buffers

Maps in Protocol Buffers store data as:

```text
key → value
```

pairs.

Just like a dictionary in Python 🐍.

---

# 🤔 Why Do We Need Maps?

Sometimes data is dynamic.

Example:

```text
Language → Greeting
```

```text
"en" → "Hello"
"hindi" → "Namaste"
```

Instead of creating many fields manually, maps make this easy.

---

# 🏗️ Basic Syntax

```proto
map<key_type, value_type> field_name = tag;
```

---

# 📦 Simple Example

```proto
syntax = "proto3";

message User {

  map<string, string> contacts = 1;
}
```

---

# 🧠 Meaning

```text
Key   → string
Value → string
```

Example data:

```text
"email" → "abc@gmail.com"
"phone" → "9999999999"
```

---

# 📊 Real-World Analogy

Think of a phone contacts app 📱

```text
Name → Number
```

Example:

```text
"Mom" → "9999999999"
"Dad" → "8888888888"
```

Maps work similarly.

---

# 🐍 Python Example

```python
user = User()

user.contacts["email"] = "abc@gmail.com"
user.contacts["phone"] = "9999999999"

print(user)
```

---

# 📦 Output

```text
contacts {
  key: "email"
  value: "abc@gmail.com"
}

contacts {
  key: "phone"
  value: "9999999999"
}
```

---

# ⚡ Another Example

```proto
message ProductInventory {

  map<string, int32> stock = 1;
}
```

---

# 🧠 Example Data

```text
"laptop" → 50
"mouse" → 200
"keyboard" → 120
```

---

# 🐍 Python Example

```python
inventory = ProductInventory()

inventory.stock["laptop"] = 50
inventory.stock["mouse"] = 200
```

---

# 📦 Supported Key Types

Map keys must be simple scalar types.

---

# ✅ Allowed Key Types

- string
- int32
- int64
- uint32
- uint64
- bool

---

# ❌ Not Allowed

```proto
map<User, string>
```

Messages cannot be map keys.

---

# 📦 Value Types

Map values can be:

✅ scalar types  
✅ enums  
✅ messages  

---

# Example with Message Value

```proto
message Address {
  string city = 1;
}

message User {

  map<string, Address> addresses = 1;
}
```

---

# 🧠 Example Data

```text
"home" → Address
"office" → Address
```

---

# 📦 Nested Map Example

```proto
message Scores {

  map<string, int32> student_scores = 1;
}
```

---

# 🧠 Example

```text
"Rahul" → 95
"Ankit" → 88
```

---

# ⚡ How Maps Work Internally

Internally, Protobuf converts maps into repeated messages.

---

# 🧠 Internal Representation

```proto
message ContactsEntry {
  string key = 1;
  string value = 2;
}
```

Then internally:

```proto
repeated ContactsEntry contacts = 1;
```

But Protobuf handles this automatically.

---

# 🚀 Benefits of Maps

---

# ✅ 1. Cleaner Schema

No need for many repeated fields.

---

# ✅ 2. Dynamic Data

Works well when keys are unknown beforehand.

---

# ✅ 3. Easy Lookup

Find values quickly using keys.

---

# ✅ 4. Better Readability

Schema becomes simpler.

---

# 📦 Real-World Use Cases

Maps are commonly used for:

- configurations ⚙️
- metadata 📦
- translations 🌐
- settings 🔧
- inventory systems 🏬
- caching 📊

---

# ⚠️ Important Rules

---

# ❗ Keys Must Be Unique

Bad:

```text
"email" → value1
"email" → value2
```

Only one key can exist.

---

# ❗ Map Ordering Is Not Guaranteed

Do not rely on insertion order.

---

# ❗ Keys Cannot Be Messages

Only scalar key types allowed.

---

# 📊 Map vs Repeated Fields

| Feature | repeated | map |
|---|---|---|
| Ordered list | ✅ | ❌ |
| Key-value structure | ❌ | ✅ |
| Fast lookup by key | ❌ | ✅ |
| Duplicate keys allowed | ✅ | ❌ |

---

# 🧱 Full Example

```proto
syntax = "proto3";

message Student {

  string name = 1;

  map<string, int32> marks = 2;
}
```

---

# 🧠 Example Data

```text
Math → 95
Science → 88
English → 91
```

---

# 🐍 Python Example

```python
student = Student()

student.name = "Abhishek"

student.marks["Math"] = 95
student.marks["Science"] = 88
```

---

# 🎯 Final Thoughts

Maps in Protocol Buffers provide an easy way to store:

```text
key → value
```

data.

They help create:

✅ cleaner schemas  
✅ dynamic structures  
✅ easier lookups  
✅ more readable APIs