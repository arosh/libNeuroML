"""

Utilities for checking generated code

"""

def validateNeuroML2(file_name):

    from lxml import etree
    from urllib import urlopen
    #schema_file = urlopen("https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta.xsd")
    schema_file = urlopen("https://raw.github.com/NeuroML/NeuroML2/development/Schemas/NeuroML2/NeuroML_v2beta1.xsd")
    xmlschema = etree.XMLSchema(etree.parse(schema_file))
    print "Validating %s against %s" %(file_name, schema_file.geturl())
    xmlschema.assertValid(etree.parse(file_name))
    print "It's valid!"


