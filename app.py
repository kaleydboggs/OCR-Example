import sys
from ocr.extract_text import extract_text_from_pdf
from analysis.analyze import analyze_text

def main(pdf_path):
    # Step 1: OCR
    text = extract_text_from_pdf(pdf_path)

    # Step 2: Analysis
    results = analyze_text(text)

    # Step 3: Output
    print("\n--- Extracted Text (first 500 chars) ---\n")
    print(text[:500])

    print("\n--- Analysis Results ---\n")
    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_pdf>")
    else:
        pdf_path = sys.argv[1]
        main(pdf_path)
