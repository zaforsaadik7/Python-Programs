#A first class function can be passed as argument to other functions, returned by other functions and assigned to variables or data structure.
def html_tag(tag):
    def wrap_tag(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_tag

print_h1= html_tag('h1')
print_h1('this is a headline.')
print_h1('this is another headline.')
print_p= html_tag('p')
print_p('this is a paragraph.')
