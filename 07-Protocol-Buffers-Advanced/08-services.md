# 🚀 Services in Protocol Buffers

In Protocol Buffers, `service` is used to define:

```text
Remote Procedure Calls (RPC)
```

This is commonly used with:

```text
gRPC
```

to build APIs and microservices.

---

# 🤔 What is a Service?

A service defines:

```text
what operations are available
```

Example:

- Create User 👤
- Get User 🔍
- Delete User ❌

Think of it like an API contract.

---

# 🧠 Simple Analogy

Imagine a food delivery app 🍔

The app provides services like:

- place order
- track order
- cancel order

Similarly, protobuf services define operations.

---

# 🏗️ Basic Syntax

```proto
service ServiceName {

  rpc MethodName(RequestType)
      returns (ResponseType);
}
```

---

# 📦 Simple Example

```proto
syntax = "proto3";

message GetUserRequest {
  int32 user_id = 1;
}

message User {
  int32 id = 1;
  string name = 2;
}

service UserService {

  rpc GetUser(GetUserRequest)
      returns (User);
}
```

---

# 🧠 Meaning

Client sends:

```text
GetUserRequest
```

Server returns:

```text
User
```

---

# 📊 Flow Diagram

```text
Client
   |
   | GetUser(request)
   v
Server
   |
   | returns User
   v
Client
```

---

# 📦 Components of Service

| Part | Meaning |
|---|---|
| service | group of RPC methods |
| rpc | remote function |
| request type | input message |
| returns | output message |

---

# 🧱 Another Example

```proto
syntax = "proto3";

message CreateUserRequest {
  string name = 1;
}

message CreateUserResponse {
  int32 id = 1;
}

service UserService {

  rpc CreateUser(CreateUserRequest)
      returns (CreateUserResponse);
}
```

---

# 🧠 Meaning

Client sends:

```text
user name
```

Server returns:

```text
new user ID
```

---

# 🚀 Why Services Are Powerful

Services allow applications written in different languages to communicate.

Example:

| Client | Server |
|---|---|
| Python 🐍 | Go 🐹 |
| Java ☕ | Node.js 🟢 |
| C# 💜 | Rust 🦀 |

All can communicate using protobuf messages.

---

# 📦 Common Real-World Services

---

# 👤 User Service

```proto
service UserService {
}
```

Operations:

- create user
- get user
- update user

---

# 💳 Payment Service

```proto
service PaymentService {
}
```

Operations:

- make payment
- refund payment

---

# 📦 Order Service

```proto
service OrderService {
}
```

Operations:

- place order
- track order

---

# 🧠 Services Are Just Definitions

Important:

```proto
service UserService {
}
```

does NOT implement logic.

It only defines:

```text
contract/interface
```

Actual implementation is written in:

- Python 🐍
- Go 🐹
- Java ☕
- etc.

---

# 📦 Example with Multiple RPC Methods

```proto
service UserService {

  rpc CreateUser(CreateUserRequest)
      returns (User);

  rpc GetUser(GetUserRequest)
      returns (User);

  rpc DeleteUser(DeleteUserRequest)
      returns (DeleteUserResponse);
}
```

---

# ⚡ Unary RPC (Most Common)

Simple request → response.

---

# Example

```proto
rpc GetUser(GetUserRequest)
    returns (User);
```

---

# 🧠 Meaning

One request  
One response

---

# 🌊 Streaming RPC (Advanced)

gRPC also supports streaming.

---

# Server Streaming

```proto
rpc GetLogs(LogRequest)
    returns (stream Log);
```

Server sends multiple responses.

---

# Client Streaming

```proto
rpc Upload(stream Chunk)
    returns (UploadResponse);
```

Client sends multiple requests.

---

# Bidirectional Streaming

```proto
rpc Chat(stream Message)
    returns (stream Message);
```

Both client and server stream data.

---

# 🚀 Benefits of Services

---

# ✅ 1. Strongly Typed APIs

Clear request/response structure.

---

# ✅ 2. Cross-Language Communication

Different languages work together.

---

# ✅ 3. Fast Communication

gRPC + protobuf is very efficient.

---

# ✅ 4. Auto Code Generation

Protobuf generates client/server code automatically.

---

# 🐍 Python Example

After generating code:

```python
client.GetUser(request)
```

looks like a normal function call.

But internally it communicates over network 🌐

---

# ⚠️ Important Notes

---

# ❗ Services Usually Work with gRPC

Protocol Buffers define services.

gRPC executes them.

---

# ❗ Request and Response Must Be Messages

Correct:

```proto
rpc GetUser(GetUserRequest)
    returns (User);
```

---

# ❌ Wrong

```proto
rpc GetUser(int32)
```

Primitive types cannot be used directly.

---

# ❗ Service Names Use PascalCase

Correct:

```proto
service UserService
```

---

# 📊 Service vs Message

| Feature | Message | Service |
|---|---|---|
| Stores data | ✅ | ❌ |
| Defines API operations | ❌ | ✅ |
| Used in RPC | ⚠️ | ✅ |

---

# 🧱 Full Example

```proto
syntax = "proto3";

message GetProductRequest {
  int32 product_id = 1;
}

message Product {
  int32 id = 1;
  string name = 2;
  double price = 3;
}

service ProductService {

  rpc GetProduct(GetProductRequest)
      returns (Product);
}
```

---

# 🎯 Final Thoughts

Services in Protocol Buffers define:

```text
how applications communicate
```

They are the foundation of:

- gRPC 🚀
- microservices 🧩
- distributed systems 📡
- high-performance APIs 🌐

Services help create:

✅ clean APIs  
✅ strongly typed communication  
✅ cross-language systems  
✅ scalable architectures