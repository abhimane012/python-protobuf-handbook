# ⏳ Duration in Protocol Buffers

Protocol Buffers provide a special type called:

```text
Duration
```

used for storing:

- time intervals ⏱️
- elapsed time ⌛
- delays 🕒
- time differences 🔄

---

# 🤔 What is Duration?

Duration represents:

```text
amount of time
```

instead of an exact date/time.

---

# 🧠 Difference Between Timestamp and Duration

| Type | Meaning |
|---|---|
| Timestamp | exact point in time 📅 |
| Duration | length of time ⏳ |

---

# 📦 Example

---

# Timestamp

```text
2026-05-30 10:00:00 UTC
```

specific time.

---

# Duration

```text
5 minutes
```

time interval.

---

# 📦 Importing Duration

Duration is a built-in protobuf type.

Import it like this:

```proto
import "google/protobuf/duration.proto";
```

---

# 🏗️ Basic Syntax

```proto
syntax = "proto3";

import "google/protobuf/duration.proto";

message Video {

  google.protobuf.Duration length = 1;
}
```

---

# 🧠 Meaning

```text
Video duration = 2 hours
```

or

```text
5 minutes
```

or

```text
30 seconds
```

---

# 📊 Real-World Use Cases

Duration is commonly used for:

- video length 🎬
- song duration 🎵
- timeout settings ⏰
- retry delays 🔄
- API rate limits 📡
- stopwatch timers ⏱️

---

# 📦 Example: Video Platform

```proto
syntax = "proto3";

import "google/protobuf/duration.proto";

message Video {

  string title = 1;

  google.protobuf.Duration duration = 2;
}
```

---

# 🐍 Python Example

```python
from google.protobuf.duration_pb2 import Duration

video_duration = Duration()

video_duration.seconds = 300
```

---

# 🧠 Meaning

```text
300 seconds = 5 minutes
```

---

# 📦 Using Inside Message

```python
video = Video()

video.title = "Learning Protobuf"

video.duration.seconds = 600
```

---

# 🧠 Meaning

```text
10 minutes
```

---

# ⚡ Duration Internally

Internally, Duration stores:

```text
seconds
+
nanoseconds
```

---

# 📦 Internal Structure

```proto
message Duration {
  int64 seconds = 1;
  int32 nanos = 2;
}
```

---

# 📊 Example Values

| Duration | Seconds |
|---|---|
| 1 minute | 60 |
| 5 minutes | 300 |
| 1 hour | 3600 |
| 1 day | 86400 |

---

# 🐍 Example with Nanoseconds

```python
duration = Duration()

duration.seconds = 1
duration.nanos = 500000000
```

---

# 🧠 Meaning

```text
1.5 seconds
```

---

# 📦 Example: API Timeout

```proto
syntax = "proto3";

import "google/protobuf/duration.proto";

message RetryConfig {

  google.protobuf.Duration retry_delay = 1;

  google.protobuf.Duration timeout = 2;
}
```

---

# 🧠 Example Values

```text
retry_delay = 5 seconds
timeout = 30 seconds
```

---

# 🚀 Benefits of Duration

---

# ✅ 1. Standardized Time Intervals

Same structure across all languages.

---

# ✅ 2. Better Than Integer Seconds

Instead of:

```proto
int32 timeout_seconds = 1;
```

use:

```proto
google.protobuf.Duration timeout = 1;
```

Cleaner and more expressive.

---

# ✅ 3. Cross-Language Support

Works consistently everywhere.

---

# ✅ 4. Nanosecond Precision

Supports extremely precise timing.

---

# ⚠️ Important Notes

---

# ❗ Duration Is NOT a Date

This is wrong thinking:

```text
2026-05-30
```

That is a Timestamp, not Duration.

---

# ❗ Duration Represents Elapsed Time

Examples:

```text
5 minutes
2 hours
30 seconds
```

---

# ❗ Must Import Duration Proto

Without import:

```proto
google.protobuf.Duration
```

will fail ❌

---

# 📊 Duration vs int32

| Feature | int32 seconds | Duration |
|---|---|---|
| Standardized | ❌ | ✅ |
| Nanoseconds | ❌ | ✅ |
| Clear meaning | ⚠️ | ✅ |
| Cross-language support | ⚠️ | ✅ |

---

# 🧱 Full Example

```proto
syntax = "proto3";

import "google/protobuf/duration.proto";

message Podcast {

  string title = 1;

  google.protobuf.Duration episode_length = 2;
}
```

---

# 🐍 Full Python Example

```python
from google.protobuf.duration_pb2 import Duration

podcast = Podcast()

podcast.title = "Tech Talk"

podcast.episode_length.seconds = 1800
```

---

# 🧠 Meaning

```text
1800 seconds = 30 minutes
```

---

# 🎯 Final Thoughts

`Duration` is the recommended way to store time intervals in Protocol Buffers.

It provides:

✅ standardized structure  
✅ nanosecond precision  
✅ clean APIs  
✅ better readability  

👉 Always prefer:

```proto
google.protobuf.Duration
```

instead of manually storing time intervals as integers.