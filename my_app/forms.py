from django import forms


# class ContractForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)
#
#


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(  # A hidden input for internal use
        max_length=50,  # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        # cleaned_data = super(ContactForm, self).clean()
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')


class ContractForm(forms.Form):
    f_name = forms.CharField(max_length=30)
    l_name = forms.CharField(max_length=30)
    pin = forms.CharField(max_length=13)
    phone = forms.CharField(max_length=10)
    room_no = forms.CharField(max_length=4)

    term = forms.IntegerField()

    # start_date = forms.DateField(widget=forms.TextInput(attrs={'id':'dp'}))
    start_date = forms.DateField()
    end_date = forms.DateField(widget=forms.TextInput())

    deposit = forms.DecimalField()
    deduct = forms.DecimalField()
    cum_ovd = forms.DecimalField()

    photo = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'disabled': 'disabled'}))
    adjust = forms.CharField(max_length=10)

    ecpu = forms.ChoiceField(widget=forms.CheckboxInput(attrs={'checked': 'checked', 'disabled': 'disabled'}))
    # ecpu = forms.MultipleChoiceField(widget=forms.CheckboxInput(attrs={'checked': 'checked', 'disabled': 'disabled'}))

    wcpu = forms.ChoiceField(widget=forms.CheckboxInput(attrs={'checked': 'checked', 'disabled': 'disabled'}))
    garb = forms.ChoiceField(widget=forms.CheckboxInput(attrs={'checked': 'checked', 'disabled': 'disabled'}))
    park = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    wifi = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    ubc = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    bed = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    bed_acc = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    dress_tb = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    cloth_cb = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    tv_tb = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    fridge = forms.ChoiceField(required=False, widget=forms.CheckboxInput())
    air = forms.ChoiceField(required=False, widget=forms.CheckboxInput())

    CHOICE=(('a', 'Fridge'), ('b', 'Air-conditioner'), ('c:', 'Cable TV'))

    # misc = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICE)
    # misc = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICE)
    # misc = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICE)
    misc = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICE)
