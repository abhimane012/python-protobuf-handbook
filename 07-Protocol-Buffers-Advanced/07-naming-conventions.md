# 🏷️ Naming Conventions in Protocol Buffers

Naming conventions are standard rules used to name:

- messages 📦
- fields 🏷️
- enums 🔢
- services 🚀
- files 📄

Good naming makes protobuf schemas:

✅ easier to read  
✅ easier to maintain  
✅ more professional  

---

# 🤔 Why Naming Conventions Matter?

Bad naming creates:

❌ confusion  
❌ inconsistent code  
❌ hard-to-read schemas  

Good naming improves:

✅ readability  
✅ consistency  
✅ teamwork  

---

# 📦 1️⃣ Message Naming Convention

Message names should use:

```text
PascalCase
```

Also called:

```text
UpperCamelCase
```

---

# ✅ Correct

```proto
message UserProfile {
}
```

```proto
message OrderItem {
}
```

---

# ❌ Wrong

```proto
message user_profile {
}
```

```proto
message USERPROFILE {
}
```

---

# 🧠 Rule

Each word starts with a capital letter.

---

# 📦 2️⃣ Field Naming Convention

Field names should use:

```text
snake_case
```

---

# ✅ Correct

```proto
string first_name = 1;
```

```proto
int32 total_count = 2;
```

---

# ❌ Wrong

```proto
string FirstName = 1;
```

```proto
string firstName = 1;
```

---

# 🧠 Rule

- lowercase only
- words separated using `_`

---

# 📦 3️⃣ Enum Naming Convention

Enum names should use:

```text
PascalCase
```

---

# ✅ Correct

```proto
enum OrderStatus {
}
```

---

# ❌ Wrong

```proto
enum order_status {
}
```

---

# 📦 4️⃣ Enum Value Naming Convention

Enum values should use:

```text
UPPER_SNAKE_CASE
```

---

# ✅ Correct

```proto
enum Status {
  STATUS_UNKNOWN = 0;
  STATUS_ACTIVE = 1;
}
```

---

# ❌ Wrong

```proto
Active = 1;
```

```proto
active = 1;
```

---

# 🧠 Why Prefix Enum Values?

Enum values are global in some languages.

This avoids conflicts.

---

# ✅ Recommended

```proto
enum PaymentStatus {
  PAYMENT_STATUS_PENDING = 0;
  PAYMENT_STATUS_SUCCESS = 1;
}
```

---

# 📦 5️⃣ Service Naming Convention

Service names should use:

```text
PascalCase
```

---

# ✅ Correct

```proto
service UserService {
}
```

---

# ❌ Wrong

```proto
service user_service {
}
```

---

# 📦 6️⃣ RPC Method Naming Convention

RPC methods should also use:

```text
PascalCase
```

---

# ✅ Correct

```proto
rpc GetUser(GetUserRequest) returns (User);
```

---

# ❌ Wrong

```proto
rpc get_user(GetUserRequest) returns (User);
```

---

# 📦 7️⃣ File Naming Convention

Proto file names should use:

```text
snake_case.proto
```

---

# ✅ Correct

```text
user.proto
order_item.proto
payment_service.proto
```

---

# ❌ Wrong

```text
User.proto
OrderItem.proto
```

---

# 📦 8️⃣ Package Naming Convention

Package names should use:

```text
lowercase
```

---

# ✅ Correct

```proto
package ecommerce.user;
```

---

# ❌ Wrong

```proto
package Ecommerce.User;
```

---

# 🧠 Package Best Practice

Use domain-style naming.

---

# ✅ Example

```proto
package company.project.auth;
```

---

# 📦 Full Good Example

```proto
syntax = "proto3";

package ecommerce.user;

message UserProfile {

  int32 user_id = 1;

  string first_name = 2;

  string last_name = 3;
}

enum UserStatus {
  USER_STATUS_UNKNOWN = 0;
  USER_STATUS_ACTIVE = 1;
}

service UserService {

  rpc GetUser(GetUserRequest) returns (UserProfile);
}
```

---

# 🚫 Common Beginner Mistakes

---

# ❌ Mixing Naming Styles

Bad:

```proto
string firstName = 1;
```

and:

```proto
string last_name = 2;
```

Use consistent style.

---

# ❌ Using Generic Names

Bad:

```proto
message Data {
}
```

Use meaningful names.

---

# ❌ Using Abbreviations Excessively

Bad:

```proto
message UsrPrf {
}
```

Prefer readability.

---

# ⚡ Best Practices

✅ Use meaningful names  
✅ Follow protobuf style guide  
✅ Keep naming consistent  
✅ Use snake_case for fields/files  
✅ Use PascalCase for messages/services  
✅ Use UPPER_SNAKE_CASE for enum values  

---

# 📊 Quick Summary

| Item | Convention |
|---|---|
| Message | PascalCase |
| Field | snake_case |
| Enum | PascalCase |
| Enum Value | UPPER_SNAKE_CASE |
| Service | PascalCase |
| RPC Method | PascalCase |
| File Name | snake_case.proto |
| Package | lowercase |

---

# 🎯 Final Thoughts

Good naming conventions make protobuf schemas:

✅ clean  
✅ professional  
✅ maintainable  
✅ easier to understand  

Following conventions is especially important in:

- large teams 👥
- microservices 🧩
- APIs 🌐
- enterprise systems 🏗️