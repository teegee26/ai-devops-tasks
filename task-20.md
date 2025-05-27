### Explanation of the IPv4 Regex

The regex:
```
/^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$/
```
breaks down as follows:

- `^` and `$`: Ensure the match is for the entire string (start to end).
- `(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)`: Matches a single octet (0-255):
    - `25[0-5]`: 250-255
    - `2[0-4]\d`: 200-249
    - `1\d{2}`: 100-199
    - `[1-9]?\d`: 0-99 (handles leading zeros, but doesn't allow them except for 0 itself)
- `(\.(...)){3}`: The above octet pattern, repeated three more times, each preceded by a dot.

### Example Tests

```js
isValidIPv4("192.168.1.1");      // true (valid)
isValidIPv4("255.255.255.255");  // true (valid)
isValidIPv4("0.0.0.0");          // true (valid)
isValidIPv4("256.100.50.25");    // false (256 is out of range)
isValidIPv4("192.168.1");        // false (not enough octets)
isValidIPv4("192.168.01.1");     // false (leading zero in octet)
isValidIPv4("abc.def.ghi.jkl");  // false (not numbers)
```

This regex is strict and does not allow leading zeros in octets (except for zero itself).