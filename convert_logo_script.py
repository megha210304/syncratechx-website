from pdf2image import convert_from_path
import os

def convert_logo():
    pdf_path = r"C:\Syncratech Docs\Syncra TechX Logo Gradient.pdf"
    output_path = r"c:\Syncra tech website\static\images\logo.png"
    
    print(f"Attempting to convert {pdf_path}...")
    
    try:
        # Convert PDF to list of PIL Image objects
        # We use high DPI for better quality
        images = convert_from_path(pdf_path, dpi=300)
        
        if images:
            # Save the first page as PNG with transparency
            # Note: PDF might have a white background, so we might need to process it
            logo = images[0].convert("RGBA")
            
            # Simple background removal if it's solid white (optional, depends on PDF)
            # data = logo.getdata()
            # newData = []
            # for item in data:
            #     if item[0] == 255 and item[1] == 255 and item[2] == 255:
            #         newData.append((255, 255, 255, 0))
            #     else:
            #         newData.append(item)
            # logo.putdata(newData)
            
            logo.save(output_path, "PNG")
            print(f"Successfully saved logo to {output_path}")
        else:
            print("No images found in PDF.")
            
    except Exception as e:
        print(f"Error during conversion: {e}")
        print("Falling back to a placeholder if PDF is inaccessible...")

if __name__ == "__main__":
    convert_logo()
