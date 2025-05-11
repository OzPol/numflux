## 🧹 Maintenance

To clean up Python cache files:

```bash
    find . -name "__pycache__" -type d -exec rm -r {} +
```

or:

```bash
    rm -rf $(find . -name "__pycache__")
```
