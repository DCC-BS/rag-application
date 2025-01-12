import base64
import glob
import os
from io import BytesIO

import mammoth
from PyPDF2 import PdfReader, PdfWriter


def render_pdf(file_path: str, page_number: int) -> str:
    if not os.path.exists(file_path):
        raise ValueError(f"File path {file_path} does not exist")

    with open(file_path, "rb") as f:
        pdf_reader = PdfReader(f)

        if page_number < 1 or page_number > len(pdf_reader.pages):
            raise ValueError(
                f"Invalid page number. The PDF has {len(pdf_reader.pages)} pages."
            )

        page = pdf_reader.pages[page_number - 1]

        pdf_writer = PdfWriter()
        pdf_writer.add_page(page)

        output = BytesIO()
        pdf_writer.write(output)

        b64 = base64.b64encode(output.getvalue()).decode()

        href = f"<iframe src='data:application/pdf;base64,{b64}' width='100%' height='800px'></iframe>"

        return href


def render_docx(file_path: str, page_number: int) -> str:
    if not os.path.exists(file_path):
        raise ValueError(f"File path {file_path} does not exist")

    with open(file_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value
    # embedd html as iframe
    href = f"<iframe srcdoc='{html}' width='100%' height='800px'></iframe>"
    return href


def find_files(base_dir):
    """
    Recursively search for files in a given directory and its subdirectories.

    This function walks through the base directory and all its subdirectories,
    collecting file paths and organizing them by their file extensions.

    Args:
        base_dir (str): The path to the base directory to start the search from.

    Returns:
        dict: A dictionary where each key is a file extension (including the dot,
              e.g., '.pdf', '.docx') and each value is a list of full file paths
              for files with that extension.

    Example:
        >>> result = find_files('/path/to/directory')
        >>> print(result['.pdf'])  # List all PDF files found
    """
    file_list = {}

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension:  # Ensure the file has an extension
                file_path = os.path.join(root, file)
                if file_extension not in file_list:
                    file_list[file_extension] = []
                file_list[file_extension].append(file_path)

    return file_list


def remove_temp_docx(folder_path):
    # Pattern for temporary Word files
    pattern = os.path.join(folder_path, "**", "~$*.docx")

    # Find all temporary .docx files
    temp_files = glob.glob(pattern, recursive=True)

    # Remove each temporary file
    for file in temp_files:
        try:
            os.remove(file)
            print(f"Removed: {file}")
        except Exception as e:
            print(f"Error removing {file}: {e}")

    print(f"Total temporary .docx files removed: {len(temp_files)}")


if __name__ == "__main__":
    remove_temp_docx(".\data")
