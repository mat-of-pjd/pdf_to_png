import fitz  # PyMuPDF
from PIL import Image
import io

pdf_path = "3m-respirator.pdf"
output_path = "combined3.png"

doc = fitz.open(pdf_path)
images = []

# Convert each page to PIL image
for page in doc:
    pix = page.get_pixmap(dpi=200)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    images.append(img)

# Calculate final image size
total_width = max(img.width for img in images)
total_height = sum(img.height for img in images)

# Create blank canvas
combined = Image.new("RGB", (total_width, total_height), "white")

# Paste pages vertically
y_offset = 0
for img in images:
    combined.paste(img, (0, y_offset))
    y_offset += img.height

combined.save(output_path)
print(f"Saved: {output_path}")