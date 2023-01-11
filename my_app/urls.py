from django.urls import path
from my_app import views

# app_name = 'my_app'

urlpatterns = [
    path('alignment/', views.render_file, name='render_file'),
    path('tab_order/', views.tab_order, name='tab_order'),

    path('month_billing/', views.month_billing, name='month_billing'),

    path('data_validation/', views.data_validation, name='data_validation'),
    path('datalist/', views.datalist, name='datalist'),
    path('url_email_tel/', views.url_email_tel, name='url_email_tel'),
    path('number_range/', views.number_range, name='number_range'),
    path('date_time/', views.date_time, name='date_time'),
    path('search/', views.search, name='search'),
    path('output/', views.output, name='output'),
    path('color/', views.color, name='color'),
    path('progress_meter_bar/', views.progress_meter_bar, name='progress_meter_bar'),
    path('dm/', views.trial, name='trial'),
    path('radio_checkbox/', views.radio_checkbox, name='radio_checkbox'),
    path('button/', views.button, name='button'),
    path('textfield/', views.textfield, name='textfield'),
    path('dropdownlist/', views.dropdownlist, name='dropdownlist'),
    path('listbox/', views.listbox, name='listbox'),
    path('textarea/', views.textarea, name='textarea'),
    path('fieldset/', views.fieldset, name='fieldset'),
    path('file/', views.file, name='file'),
    path('create_table/', views.create_table, name='create_table'),
    path('table_merge/', views.table_merge, name='table_merge'),
    path('float/', views.float, name='float'),
    path('float2/', views.float2, name='float2'),
    path('float3/', views.float3, name='float3'),
    path('show_image/', views.show_image, name='show_image'),
    path('h_navigation/', views.h_navigation, name='h_navigation'),
    path('h_navigation/table_merge/', views.h_navigation, name='h_navigation'),
    path('list/', views.list, name='list'),
    path('saroyan/', views.saroyan, name='saroyan'),
    path('text_block/', views.text_block, name='text_block'),
    path('special_text_block/', views.special_text_block, name='special_text_block'),
    path('abbr_text/', views.abbr_text, name='abbr_text'),
    path('inline/', views.inline, name='inline'),
    path('html5_element/', views.html5_element, name='html5_element'),
    path('coreattr/', views.coreattr, name='coreattr'),
    path('link/', views.link, name='link'),
    path('pbtest/', views.pbtest, name='pbtest'),
    path('list2/', views.list2, name='list2'),
    path('image/', views.image, name='image'),
    path('relational_selector/', views.relational_selector, name='relational_selector'),
    path('pseudo_class/', views.pseudo_class, name='pseudo_class'),
    path('format_list/', views.format_list, name='format_list'),
    path('placeholder/', views.placeholder, name='placeholder'),
    path('two_tier_menu/', views.two_tier_menu, name='two_tier_menu'),

    path('home/', views.home, name='home'),
    # path('image/', views.image,name='image'),

]
