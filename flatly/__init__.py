from pyramid.scaffolds import PyramidTemplate

class FlatProjectTemplate(PyramidTemplate):
    _template_dir = 'flatly'
    summary = 'Pyramid template that is flat.  Kind of like Flask.'

