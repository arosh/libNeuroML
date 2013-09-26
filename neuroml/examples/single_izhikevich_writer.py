from neuroml import NeuroMLDocument
from neuroml import IzhikevichCell
from neuroml.writers import NeuroMLWriter
from neuroml.utils import validateNeuroML2


def write_izhikevich(filename="./tmp/SingleIzhikevich_test.nml"):
    nml_doc = NeuroMLDocument(id="SingleIzhikevich")
    nml_filename = filename

    iz0 = IzhikevichCell(id="iz0", v0="-70mV", thresh="30mV", a="0.02", b="0.2", c="-65.0", d="6")

    nml_doc.izhikevich_cells.append(iz0)

    NeuroMLWriter.write(nml_doc, nml_filename)
    validateNeuroML2(nml_filename)


if __name__ == "__main__":
    write_izhikevich()