# Generate a barcode image from user input
# Requires: pip install python-barcode pillow

import sys
from datetime import datetime

try:
    from barcode import get_barcode_class
    from barcode.writer import ImageWriter
except ImportError:
    print("Missing dependencies. Run: pip install python-barcode pillow")
    sys.exit(1)

BARCODES = {
    "code128": {"name": "Code128", "note": "Accepts letters, numbers, symbols."},
    "ean13":   {"name": "EAN13",   "note": "12 numeric digits; checksum auto-added."},
    "ean8":    {"name": "EAN8",    "note": "7 numeric digits; checksum auto-added."},
    "upca":    {"name": "UPCA",    "note": "11 numeric digits; checksum auto-added."}
}

def validate_data(kind: str, data: str) -> str:
    """Validate/normalize data for the selected barcode type."""
    k = kind.lower()
    if k == "code128":
        # Code128 accepts most ASCII; no extra validation here
        if not data:
            raise ValueError("Code128 data cannot be empty.")
        return data
    elif k in ("ean13", "ean8", "upca"):
        if not data.isdigit():
            raise ValueError(f"{BARCODES[k]['name']} requires digits only.")
        required = {"ean13": 12, "ean8": 7, "upca": 11}[k]
        if len(data) != required:
            raise ValueError(f"{BARCODES[k]['name']} requires exactly {required} digits (without checksum).")
        return data
    else:
        raise ValueError("Unsupported barcode type.")

def main():
    print("=== Barcode Generator ===")
    print("Available types:")
    for key, meta in BARCODES.items():
        print(f" - {key} : {meta['name']} — {meta['note']}")
    kind = input("\nChoose a type (code128/ean13/ean8/upca): ").strip().lower()
    if kind not in BARCODES:
        print("Invalid type selected.")
        sys.exit(1)

    data = input("Enter the data to encode: ").strip()

    try:
        normalized = validate_data(kind, data)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Build writer with some nice defaults
    writer = ImageWriter()
    options = {
        "module_width": 0.2,   # bar thickness
        "module_height": 15.0, # bar height (mm)
        "font_size": 10,
        "text_distance": 2.0,
        "quiet_zone": 6.5,
        # Leave default colors; you can customize with 'foreground'/'background'
    }

    try:
        BarcodeClass = get_barcode_class(kind)
        bc = BarcodeClass(normalized, writer=writer)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename_base = f"{kind}_{timestamp}"
        full_path = bc.save(filename_base, options)
    except Exception as e:
        print(f"Failed to generate barcode: {e}")
        sys.exit(1)

    print(f"Success! Saved barcode to: {full_path}")

if __name__ == "__main__":
    main()
