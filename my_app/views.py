from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.views.generic import TemplateView

from .forms import ContactForm, ContractForm
from django.core.mail import send_mail



class first_page(TemplateView):
    template_name = 'first_page.html'  # default template if not defined in the url




def render_file(request):
    return render(request, 'my_app/render_file.html')

def tab_order(request):
    return render(request, 'my_app/tab_order.html')


def data_validation(request):
    return render(request, 'my_app/data_validation.html')


def datalist(request):
    return render(request, 'my_app/datalist.html')


def url_email_tel(request):
    return render(request, 'my_app/url_email_tel.html')


def number_range(request):
    return render(request, 'my_app/number_range.html')


def date_time(request):
    return render(request, 'my_app/date_time.html')


def search(request):
    return render(request, 'my_app/search.html')


def output(request):
    return render(request, 'my_app/output.html')


def color(request):
    return render(request, 'my_app/color.html')


def progress_meter_bar(request):
    return render(request, 'my_app/progress_meter_bar.html')


def trial(request):
    return render(request, 'my_app/dm.html')


def radio_checkbox(request):
    return render(request, 'my_app/radio_checkbox.html')


def button(request):
    return render(request, 'my_app/button.html')


def textfield(request):
    return render(request, 'my_app/textfield.html')


def dropdownlist(request):
    return render(request, 'my_app/dropdownlist.html')


def listbox(request):
    return render(request, 'my_app/listbox.html')


def textarea(request):
    return render(request, 'my_app/textarea.html')


def fieldset(request):
    return render(request, 'my_app/fieldset.html')


def file(request):
    return render(request, 'my_app/file.html')


def create_table(request):
    return render(request, 'my_app/create_table.html')


def table_merge(request):
    return render(request, 'my_app/table_merge.html')


def month_billing(request):

    bills = [
        ['Bunpot Pongsai', '106A',3500,8,18,0,30,0,0,3556,3556],
        ['Ratchada Ruttakul', '105A', 3500, 8, 18, 0, 30, 0, 0, 3556, 3556],
        ['Sirirat Sirikul', '206A', 3500, 8, 18, 0, 30, 0, 0, 3556, 3556],
        ['Jarinya Jariyakul', '306A', 3500, 8, 18, 0, 30, 0, 0, 3556, 3556],
        ['Amila Ampaiphan', '203A', 3500, 8, 18, 0, 30, 0, 0, 3556, 3556],
    ]

    return render(request, 'my_app/month_billing.html', {'bills':bills})


def float(request):
    return render(request, 'my_app/float.html')


def float2(request):
    return render(request, 'my_app/float2.html')


def float3(request):
    return render(request, 'my_app/float3.html')


def show_image(request):
    tp = loader.get_template('my_app/show_image.html')
    return HttpResponse(tp.render(None, request))


def h_navigation(request):
    return render(request, 'my_app/h_navigation.html')


def list(request):
    return render(request, 'my_app/list.html')


def saroyan(request):
    return render(request, 'my_app/saroyan.html')


def text_block(request):
    return render(request, 'my_app/text_block.html')


def special_text_block(request):
    return render(request, 'my_app/special_text_block.html')


def abbr_text(request):
    return render(request, 'my_app/abbr_text.html')


def inline(request):
    return render(request, 'my_app/inline.html')


def html5_element(request):
    return render(request, 'my_app/html5_element.html')


def coreattr(request):
    return render(request, 'my_app/coreattr.html')


def link(request):
    return render(request, 'my_app/link.html')


def pbtest(request):
    return render(request, 'my_app/pbtest.html')


def list2(request):
    return render(request, 'my_app/list2.html')


def image(request):
    return render(request, 'my_app/image.html')


def relational_selector(request):
    return render(request, 'my_app/relational_selector.html')


def pseudo_class(request):
    return render(request, 'my_app/pseudo_class.html')


def format_list(request):
    return render(request, 'my_app/format_list.html')


def placeholder(request):
    return render(request, 'my_app/placeholder.html')


def two_tier_menu(request):
    return render(request, 'my_app/two_tier_menu.html')


# def contract_form(request):
#     if request.method == 'POST':
#         form = ContractForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#
#             subject = cd['subject']
#             message = cd['message']
#             sender = cd['sender']
#             cc_myself = cd['cc_myself']
#
#             recipients = ['Nancy', 'Ann']
#
#             if cc_myself:
#                 recipients.append(sender)
#             send_mail(subject, message, sender, recipients, fail_silently=False)
#
#     else:
#         form = ContractForm()
#
#     return render(request, 'my_app/contract_form.html', {'form': form})

# return render(request,'my_app/show_image.html')
# def show_image(request):
#     return HttpResponse()


# from django.shortcuts import render
# from .forms import ContactForm

def home(request):
    if request.method == 'POST':

        form = ContractForm(request.POST)

        if form.is_valid():
            pass  # does nothing, just trigger the validation

    else:
        form = ContractForm()

    return render(request, 'my_app/home2.html', {'form': form})

#
# def image(request):
#     return render(request,'my_app/image.html')

