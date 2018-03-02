from Cheetah.Template import Template
from subprocess import call


class TemplateProvider:
    def provideTemplate(self, fileTemplate, data):
        value = ""
        try:
            f = open( fileTemplate, "r")
            value = f.read()
            f.close()

        except IOError:
            print("error opening the file  in template : " + fileTemplate)

        return Template(value, data)
