#A first class function can be passed as arguments to other functions, returned by other functions and assigned to variables or data structure. In language with first class functions, 
# the name of the functions do not have any special status, thy are treated like ordinary variables with a function type.
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}'.format(tag,msg))
    return wrap_text

print_h1= html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')
print_p= html_tag('p')
print_p('Test Paragram!')
