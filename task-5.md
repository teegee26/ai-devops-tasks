```
+--------+        +-------------------+        +-----------+
| Client | <----> | Application Server | <----> | Database  |
+--------+        +-------------------+        +-----------+
```

```
    ^                ^                       ^
    |                |                       |
    |   HTTP/HTTPS   |      SQL Queries      |
    |                |                       |
    v                v                       v
+--------+        +-------------------+        +-----------+
| Client | <----> | Application Server | <----> | Database  |
+--------+        +-------------------+        +-----------+
     |                   |                          |
     |  User Interface   |   Business Logic/API     |  Data Storage
     |                   |                          |
```


