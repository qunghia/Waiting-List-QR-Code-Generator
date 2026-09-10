# Waiting List QR Code System

A simple QR-based waiting list system that generates waiting numbers from 1 to 500.

Each QR code opens a webpage that displays the corresponding waiting number in a large, easy-to-read format.

## How It Works

Each QR code contains a unique URL.

For example:

```text
QR_001 → https://qunghia.github.io/Waiting-List/?number=1
QR_123 → https://qunghia.github.io/Waiting-List/?number=123
QR_500 → https://qunghia.github.io/Waiting-List/?number=500
```

When a customer scans the QR code, the browser opens a page displaying the assigned waiting number.

Example:

```text
WAITING NUMBER

123

Please wait for your number to be called.
```

## Project Structure

```text
Waiting-List/
├── index.html
├── generate_qr.py
├── README.md
└── QR_Codes/
    ├── QR_001.png
    ├── QR_002.png
    ├── QR_003.png
    ├── ...
    └── QR_500.png
```

## Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Python `qrcode` library
- GitHub Pages

## QR Code Generation

The QR codes are generated automatically using Python.

Install the required package:

```bash
pip install qrcode[pil]
```

Run the QR generator:

```bash
python generate_qr.py
```

The script generates 500 QR codes inside the `QR_Codes` folder.

Each QR code points to the waiting list webpage with a different number parameter.

For example:

```text
https://qunghia.github.io/Waiting-List/?number=25
```

This displays waiting number:

```text
25
```

## Live Website

The waiting number webpage is hosted using GitHub Pages:

https://qunghia.github.io/Waiting-List/

A waiting number is passed through the URL using the `number` parameter.

Example:

```text
https://qunghia.github.io/Waiting-List/?number=250
```

This displays waiting number **250**.

## Supported Numbers

The system currently supports waiting numbers from:

```text
1 to 500
```

If the number is missing or outside this range, the webpage displays an invalid-number message.

## Use Case

This system can be used for simple customer waiting lists in places such as:

- Restaurants
- Cafes
- Events
- Service counters
- Customer queues

Each customer can receive a QR code corresponding to their waiting number and scan it to view their number on their phone.

## Important Note

This project is currently a lightweight waiting-number display system.

It does not use a database, login system, or secure queue verification.

Because the waiting number is stored in the URL, users can manually change the number parameter.

For example:

```text
?number=123
```

can be manually changed to:

```text
?number=124
```

For a more secure queue-management system, a backend database and unique customer IDs or tokens should be used.

## Author

Developed by **Quang Nghia**
