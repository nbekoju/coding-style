# [Builder Design Pattern] Design a document generator using the Builder Design Pattern. Create a DocumentBuilder that creates documents of various types (e.g., PDF, HTML, Plain Text). Implement the builder methods to format the document content and structure according to the chosen type. Demonstrate how the Builder Design Pattern allows for the creation of different document formats without tightly coupling the document generation logic.

from abc import ABC, abstractmethod


# Product: Document
class Document:
    def __init__(self):
        self.content = ""

    def add_content(self, content):
        self.content += content + "\n"

    def __str__(self):
        return self.content


# Abstract Builder
class DocumentBuilder(ABC):
    def __init__(self):
        self.document = Document()

    @abstractmethod
    def add_title(self, title):
        pass

    @abstractmethod
    def add_paragraph(self, paragraph):
        pass


# Concrete Builders
class PDFDocumentBuilder(DocumentBuilder):
    def add_title(self, title):
        self.document.add_content(f"<h1>{title}</h1>")

    def add_paragraph(self, paragraph):
        self.document.add_content(f"<p>{paragraph}</p>")


class HTMLDocumentBuilder(DocumentBuilder):
    def add_title(self, title):
        self.document.add_content(f"<h1>{title}</h1>")

    def add_paragraph(self, paragraph):
        self.document.add_content(f"<p>{paragraph}</p>")


class PlainTextDocumentBuilder(DocumentBuilder):
    def add_title(self, title):
        self.document.add_content(title)
        self.document.add_content("=" * len(title))

    def add_paragraph(self, paragraph):
        self.document.add_content(paragraph)


# Director
class DocumentGenerator:
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self, title, paragraphs):
        self.builder.add_title(title)
        for paragraph in paragraphs:
            self.builder.add_paragraph(paragraph)


def main():
    # Generating PDF Document
    pdf_builder = PDFDocumentBuilder()
    pdf_generator = DocumentGenerator(pdf_builder)
    pdf_generator.generate_document(
        "PDF Document", ["Paragraph 1", "Paragraph 2"]
    )
    pdf_document = pdf_builder.document
    print("PDF Document:")
    print(pdf_document)

    # Generating HTML Document
    html_builder = HTMLDocumentBuilder()
    html_generator = DocumentGenerator(html_builder)
    html_generator.generate_document(
        "HTML Document", ["Paragraph 1", "Paragraph 2"]
    )
    html_document = html_builder.document
    print("\nHTML Document:")
    print(html_document)

    # Generating Plain Text Document
    plaintext_builder = PlainTextDocumentBuilder()
    plaintext_generator = DocumentGenerator(plaintext_builder)
    plaintext_generator.generate_document(
        "Plain Text Document",
        ["Paragraph 1", "Paragraph 2"],
    )
    plaintext_document = plaintext_builder.document
    print("\nPlain Text Document:")
    print(plaintext_document)


if __name__ == "__main__":
    main()
