# Week 7 — Web Fundamentals

## Goal

Understand how the web works at a fundamental level: how a client communicates with a server, how URLs and DNS fit into the process, how HTTP requests and responses are structured, and how common web concepts work.

---

## Topics

### Web Fundamentals

* Client
* Server
* Frontend
* Backend
* API
* URL
* Domain
* DNS

Basic request flow:

```text
Browser
   ↓
URL
   ↓
DNS
   ↓
IP address
   ↓
TCP connection
   ↓
HTTP request
   ↓
Server
   ↓
HTTP response
   ↓
Browser
```

---

### DNS

Learned how domain names are resolved into IP addresses.

Practiced using:

```bash
nslookup
dig
```

Understood that DNS can return:

* IPv4 addresses (`A`)
* IPv6 addresses (`AAAA`)
* other DNS records

Example:

```bash
dig example.com
```

---

### HTTP

Learned the structure of HTTP communication.

#### HTTP Request

```text
GET / HTTP/1.1
Host: example.com
User-Agent: ...
Accept: ...
Connection: keep-alive
```

#### HTTP Response

```text
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: ...

<body>
...
</body>
```

Understood the difference between:

* Request line
* Response status line
* Headers
* Body

---

### HTTP Methods

Studied:

* `GET` — retrieve data
* `POST` — send/create data
* `PUT` — replace/update data
* `PATCH` — partially update data
* `DELETE` — delete data

---

### HTTP Status Codes

Studied common status codes:

| Code  | Meaning                    |
| ----- | -------------------------- |
| `200` | OK                         |
| `201` | Created                    |
| `301` | Moved Permanently          |
| `302` | Found / temporary redirect |
| `400` | Bad Request                |
| `401` | Unauthorized               |
| `403` | Forbidden                  |
| `404` | Not Found                  |
| `429` | Too Many Requests          |
| `500` | Internal Server Error      |

---

### HTTP Headers

Learned that headers contain additional information about a request or response.

Important headers studied:

* `Host`
* `User-Agent`
* `Accept`
* `Content-Type`
* `Content-Length`
* `Connection`

---

### Cookies, Sessions and Tokens

Learned the basic purpose and differences between:

* Cookies
* Sessions
* Tokens

These mechanisms are commonly used to maintain state and authentication between requests.

---

## Tools

Used/studied:

* `curl`
* `wget`
* `openssl`
* `dig`
* `nslookup`
* Browser Developer Tools
* Burp Suite

Burp Suite was introduced as a tool for inspecting and modifying HTTP traffic, with the focus kept on legal training environments.

---

## Practice

Analyzed a real HTTP request and response between Firefox and `example.com`.

Identified:

### Request

* HTTP method
* HTTP version
* Headers
* User-Agent
* Accepted languages
* Encoding
* Keep-alive connection
* Absence of a request body
* Absence of cookies in the request

### Response

* HTTP status code `200`
* `Content-Type`
* Response headers
* Response body

The goal was to understand what is actually happening when a browser loads a website instead of treating HTTP as a black box.

---

## Cybersecurity Relevance

Web fundamentals are important for understanding:

* Web application security
* Authentication
* Sessions
* Cookies
* APIs
* HTTP-based attacks
* Request/response manipulation
* Access control
* Security testing
* Burp Suite
* Web vulnerabilities

Before studying vulnerabilities, it is important to understand the normal behavior of web applications and HTTP communication.

---

## Result

By the end of Week 7, I can explain the basic flow:

```text
URL
 ↓
DNS
 ↓
IP address
 ↓
Connection
 ↓
HTTP request
 ↓
Server processing
 ↓
HTTP response
 ↓
Browser
```

I can also read a basic HTTP request/response and identify its main components.

## Next

Continue applying these fundamentals through practical exercises and gradually move toward web security concepts and controlled labs.
