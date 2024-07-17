from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", size=40)
        header = "CS50 Shirtificate"
        centerHeader = (self.w - self.get_string_width(header)) / 2
        self.text(centerHeader, 20, header)

    def footer(self):
        self.set_font("helvetica", size=25)
        self.set_text_color(255, 255, 255)
        footer = input("Name: ") + " took CS50"
        centerFooter = (self.w - self.get_string_width(footer)) / 2
        self.text(centerFooter, 125, footer)


def main():
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", 10, 50, 190)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
