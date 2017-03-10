from Cheetah.Template import Template

class TemplateProvider :

    def provideTemplate(self, fileTemplate, data):
        value = ""
        try:
            f = open(fileTemplate,  "r")
            value = f.read()
            f.close()
        except IOError:
            print "eerror opening the file"
        return Template(value, data)