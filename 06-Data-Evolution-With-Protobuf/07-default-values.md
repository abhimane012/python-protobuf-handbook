# ⚠️ Beware of Default Values in Protocol Buffers

In Protocol Buffers, every field automatically gets a:

```text
Default Value
```

when no value is provided.

This is useful ✅

But it can also create confusion ⚠️

---

# 🧠 Important Concept

In `proto3`:

```text
Fields are NEVER null
```

If a field is missing, Protobuf uses a default value automatically.

---

# 📦 Default Values

| Type | Default Value |
|---|---|
| int32 | 0 |
| int64 | 0 |
| float | 0.0 |
| double | 0.0 |
| bool | false |
| string | "" |
| bytes | empty |
| enum | first enum value |

---

# 📦 Example

```proto
syntax = "proto3";

message User {
  int32 age = 1;
  string name = 2;
  bool verified = 3;
}
```

---

# 🧠 If Nothing Is Set

Protobuf automatically gives:

```text
age = 0
name = ""
verified = false
```

---

# ⚠️ The Big Problem

You often cannot tell the difference between:

```text
Field not sent
```

and

```text
Field explicitly set to default value
```

---

# 🧪 Example

Suppose client sends:

```proto
age = 0
```

Was it:

```text
User age is actually 0
```

OR:

```text
Field was never sent
```

👉 In normal proto3 fields, you cannot know.

---

# 📊 Real Example

---

# 📄 Schema

```proto
message Product {
  int32 stock = 1;
}
```

---

# 🟢 Case 1

Field not sent:

```text
{}
```

Result:

```text
stock = 0
```

---

# 🟡 Case 2

Field explicitly sent:

```text
stock = 0
```

Result:

```text
stock = 0
```

---

# ⚠️ Both Look Same

This creates ambiguity.

---

# 🧠 Why This Happens

Proto3 was designed to:

✅ keep messages small  
✅ simplify APIs  
✅ avoid null handling  

But the tradeoff is:

```text
missing field == default value
```

---

# 🚫 Common Beginner Mistakes

---

# ❌ Assuming Empty String Means User Sent Empty String

Example:

```proto
string name = 1;
```

Result:

```text
name = ""
```

You cannot know whether:

- user sent empty string
- OR field was missing

---

# ❌ Assuming `false` Was Explicitly Sent

```proto
bool verified = 1;
```

Result:

```text
false
```

Could mean:

- field missing
- OR explicitly false

---

# ⚡ Real-World Problems

This matters in:

- APIs 🌐
- PATCH updates 🔄
- Partial updates 📦
- Forms 🧾

---

# 🧱 Example Problem

Suppose API request:

```proto
message UpdateUser {
  string name = 1;
}
```

Client sends:

```text
name = ""
```

Did user want:

```text
Clear the name
```

OR:

```text
Did not send name field
```

Hard to know ❌

---

# ✅ Solution: Use `optional`

Proto3 supports:

```proto
optional
```

---

# Example

```proto
message User {
  optional int32 age = 1;
}
```

Now Protobuf tracks whether field was set.

---

# 🧠 Benefit

You can check:

```text
Was field actually present?
```

---

# 🐍 Python Example

```python
if user.HasField("age"):
    print("Age was sent")
```

---

# 📊 Without vs With Optional

| Feature | Normal Field | Optional Field |
|---|---|---|
| Default values | ✅ | ✅ |
| Detect missing field | ❌ | ✅ |
| Simpler | ✅ | ⚠️ Slightly more complex |

---

# ⚠️ Enum Default Problem

Enums also have defaults.

---

# Example

```proto
enum Status {
  UNKNOWN = 0;
  ACTIVE = 1;
}
```

If field missing:

```text
status = UNKNOWN
```

Again:

```text
missing == default
```

---

# 🧠 Best Practices

✅ Be careful with default values  
✅ Use `optional` when field presence matters  
✅ Design APIs carefully  
✅ Understand missing vs default behavior  

---

# 📦 Good Example

```proto
message User {
  optional string email = 1;
}
```

Now you can differentiate:

```text
Not sent
```

vs

```text
Sent as empty string
```

---

# 📊 Quick Summary

| Situation | Result |
|---|---|
| Missing int32 | 0 |
| Missing string | "" |
| Missing bool | false |
| Missing enum | first enum value |
| Missing normal field detectable? | ❌ |
| Missing optional field detectable? | ✅ |

---

# 🎯 Final Thoughts

Default values are very useful in Protocol Buffers, but they can also create hidden bugs if misunderstood.

The most important thing to remember is:

# ⚠️ In proto3:
```text
Missing field == Default value
```

unless you use:

```proto
optional
```