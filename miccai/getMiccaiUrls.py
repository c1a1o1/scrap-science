import numpy as np
import pdfx

pdfs = ["2016_all.pdf","2017_1.pdf","2017_2.pdf","2017_3.pdf"]
urls = []
for pdf in iter(pdfs):
    pdfObj = pdfx.PDFx('miccai/' + pdf)
    references_list = pdfObj.get_references()
    urls.extend( [  str (x.ref) for x in references_list if "springer" not in str (x.ref) ] )

urls = np.save("miccaiUrls.npy",urls)
