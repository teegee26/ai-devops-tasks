```python
def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates
```

Yes, this code can be optimized for better performance. Using a set to track seen items and duplicates reduces the time complexity from O(n²) to O(n):

```python
def find_duplicates(list_of_items):
    seen = set()
    duplicates = set()
    for item in list_of_items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
```