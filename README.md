# Deprecated Warning

This repository is not actively maintained and has been replaced by [Atno](https://github.com/shirsakm/atno) which is more user-friendly and has a GUI.

# Moserizer

Memorize physical properties about elements from the Modern Periodic Table.

## Usage

```sh
$ pip install -r requirements.txt
```

```sh
$ python src/main.py
```

## Error Handling

### `periodic_table.json` is missing

This error will occur when the file is not present in the local `data` directory. Please ensure you have a `data` directory and `periodic_table.json` in the current working directory.

### `periodic_table.json` is corrupt

This error will occur when the JSON file is present but cannot be decoded. Simply replace the file present in `data` directory with a [fresh copy](/data/periodic_table.json).

## Contributing

1. Fork the repository.
2. Implement something from [TO-DO](#to-do) or fix any [issue](https://github.com/dotmashrc/moserizer/issues).
3. Submit a pull request.

**IMPORTANT** Use 4 spaces for indentation.

## TO-DO

- [X] Implement atomic numbers.
- [ ] Implement atomic weights.
- [ ] Implement electronic configuration.
- [ ] Polish up the UX.

## Acknowledgements
- [Browserinator's Periodic Table JSON repo](https://github.com/Bowserinator/Periodic-Table-JSON).