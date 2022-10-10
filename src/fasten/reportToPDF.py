from fpdf import FPDF

class ReportToPDF:

    @staticmethod
    def reportToPDF(report, packageName):
        """Save the final report of the analysis in a pdf-file."""


        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'U', size = 15)
        pdf.cell(200, 10, txt = "Analysis report: "+packageName, ln = 1, align = 'C')

        pdf.set_font("Arial", size = 10)
        pdf.multi_cell(200, 5, txt = report, align = 'C')

        pdf.output("report-"+packageName+".pdf")
        print("Report written in file 'report-"+packageName+".pdf'.")
