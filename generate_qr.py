import os
import qrcode

output_folder = "QR_Codes"

os.makedirs(output_folder, exist_ok=True)

base_url = "https://qunghia.github.io/Waiting-List/"

for number in range(1, 501):

    url = f"{base_url}?number={number}"

    img = qrcode.make(url)

    filename = f"QR_{number:03}.png"
    filepath = os.path.join(output_folder, filename)

    img.save(filepath)

    print(f"Created {filename}")

print("Done! 500 QR codes created successfully.")