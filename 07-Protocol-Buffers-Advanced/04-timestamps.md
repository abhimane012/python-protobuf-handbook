# ⏰ Timestamps in Protocol Buffers

Protocol Buffers provide a special type called:

```text
Timestamp
```

used for storing:

- date 📅
- time ⏰
- UTC timestamps 🌍

in a standard format.

---

# 🤔 Why Use Timestamp?

You could store time as:

```proto
string created_at = 1;
```

But strings create problems:

❌ different formats  
❌ timezone confusion  
❌ hard date calculations  

So Protobuf provides a standard timestamp type ✅

---

# 📦 Timestamp Type

Timestamp comes from Google's built-in protobuf types.

Import it like this:

```proto
import "google/protobuf/timestamp.proto";
```

---

# 🏗️ Basic Syntax

```proto
syntax = "proto3";

import "google/protobuf/timestamp.proto";

message User {

  google.protobuf.Timestamp created_at = 1;
}
```

---

# 🧠 How It Works

`Timestamp` stores:

```text
seconds
+
nanoseconds
```

from:

```text
1970-01-01 UTC
```

(Unix Epoch)

---

# 📊 Real-World Example

```proto
syntax = "proto3";

import "google/protobuf/timestamp.proto";

message Order {

  int32 order_id = 1;

  google.protobuf.Timestamp order_time = 2;
}
```

---

# 🧠 Example Meaning

```text
order_id = 101
order_time = 2026-05-30 10:00:00 UTC
```

---

# 🐍 Python Example

```python
from google.protobuf.timestamp_pb2 import Timestamp
import datetime

timestamp = Timestamp()

timestamp.FromDatetime(datetime.datetime.utcnow())

print(timestamp)
```

---

# 📦 Output Example

```text
seconds: 1717065000
nanos: 123456000
```

---

# ⚡ Using Timestamp in Message

```python
order = Order()

order.order_id = 101

order.order_time.FromDatetime(
    datetime.datetime.utcnow()
)
```

---

# 🧠 Convert Timestamp Back to Datetime

```python
dt = order.order_time.ToDatetime()

print(dt)
```

---

# 📊 Real-World Use Cases

Timestamps are commonly used for:

- created_at 📅
- updated_at 🔄
- event_time 📡
- login_time 🔐
- payment_time 💳
- audit logs 🧾

---

# 📦 Example: User System

```proto
syntax = "proto3";

import "google/protobuf/timestamp.proto";

message User {

  int32 id = 1;

  string name = 2;

  google.protobuf.Timestamp created_at = 3;

  google.protobuf.Timestamp last_login = 4;
}
```

---

# 🚀 Benefits of Timestamp

---

# ✅ 1. Standardized Format

All systems use same structure.

---

# ✅ 2. Timezone Safe

Uses UTC internally 🌍

---

# ✅ 3. Language Independent

Works across all supported languages.

---

# ✅ 4. Better Than String Dates

Avoids parsing problems.

---

# ⚠️ Important Notes

---

# ❗ Must Import Timestamp Proto

Without import:

```proto
google.protobuf.Timestamp
```

will fail ❌

---

# ❗ Always Prefer UTC

Timestamps are usually stored in UTC.

---

# ❗ Timestamp Is Better Than String

Avoid:

```proto
string created_at = 1;
```

Prefer:

```proto
google.protobuf.Timestamp created_at = 1;
```

---

# 📦 Example JSON Representation

Timestamp often converts to:

```json
{
  "createdAt": "2026-05-30T10:00:00Z"
}
```

---

# 🧠 Internal Structure

Internally timestamp looks like:

```proto
message Timestamp {
  int64 seconds = 1;
  int32 nanos = 2;
}
```

But usually you never create this manually.

---

# 📊 Timestamp vs String

| Feature | String | Timestamp |
|---|---|---|
| Standardized | ❌ | ✅ |
| Timezone safe | ❌ | ✅ |
| Easy parsing | ❌ | ✅ |
| Cross-language support | ⚠️ | ✅ |

---

# 🧱 Full Example

```proto
syntax = "proto3";

import "google/protobuf/timestamp.proto";

message BlogPost {

  int32 id = 1;

  string title = 2;

  google.protobuf.Timestamp published_at = 3;
}
```

---

# 🐍 Full Python Example

```python
from google.protobuf.timestamp_pb2 import Timestamp
import datetime

post = BlogPost()

post.id = 1
post.title = "Learning Protobuf"

post.published_at.FromDatetime(
    datetime.datetime.utcnow()
)

print(post)
```

---

# 🎯 Final Thoughts

`Timestamp` is the recommended way to store date and time in Protocol Buffers.

It provides:

✅ standardization  
✅ timezone safety  
✅ better interoperability  
✅ cleaner APIs  

👉 Always prefer:

```proto
google.protobuf.Timestamp
```

instead of storing dates as strings.