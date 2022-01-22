from wtforms import Form, StringField, IntegerField, EmailField, PasswordField, SelectMultipleField, BooleanField, DateField, validators
from wtforms.validators import EqualTo


class SignUpForm1(Form):
    email = EmailField('Email Address', [validators.Length(max=320), validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=3, max=32), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8, max=64), validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(), EqualTo("password")])


class SignUpForm2(Form):
    qns = SelectMultipleField('Security Questions', choices=[('', 'Select'), ('cityBorn', 'In what city were you born?'), ('petName', 'What is the name of your favourite pet?'), ('mumName', "What is your mother's maiden name?"), ('highSchool', 'What high school did you attend?'), ('firstSchool', 'What is the name of your first school?'), ('car', 'What was the make of your first car?'), ('food', 'What was your favourite food as a child?'), ('spouse', 'Where did you meet your spouse?')], default='')
    # qns1 = SelectField('First Question', [validators.DataRequired()], choices=[('', 'Select'), ('cityBorn', 'In what city were you born?'), ('petName', 'What is the name of your favourite pet?'), ('mumName', "What is your mother's maiden name?"), ('highSchool', 'What high school did you attend?'), ('firstSchool', 'What is the name of your first school?'), ('car', 'What was the make of your first car?'), ('food', 'What was your favourite food as a child?'), ('spouse', 'Where did you meet your spouse?')], default='')


class SignUpForm3(Form):
    first_name = StringField('First Name', [validators.Length(min=1), validators.optional()])
    last_name = StringField('Last Name', [validators.Length(min=1), validators.optional()])
    address = StringField('Address', [validators.Length(min=1), validators.optional()])
    phone = IntegerField('Phone Number', [validators.Length(max=15), validators.optional()])
    credit_card = IntegerField('Credit Card', [validators.Length(min=16, max=16), validators.optional()])


class SignInForm(Form):
    email = EmailField('Email Address', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember = BooleanField("Remember me")


class DisplayInfo(Form):
    username = StringField('Username', [validators.Length(min=3, max=32), validators.DataRequired()])


class PersonalInfo(Form):
    first_name = StringField('First Name', [validators.Length(min=1), validators.optional()])
    last_name = StringField('Last Name', [validators.Length(min=1), validators.optional()])
    address = StringField('Address', [validators.Length(min=1), validators.optional()])
    phone = IntegerField('Phone Number', [validators.Length(max=15), validators.optional()])
    Unit_no = IntegerField('Unit no', [validators.Length(min=16, max=16), validators.optional()])
    Postal_code= IntegerField('Postal Code', [validators.Length(min=6, max=6), validators.optional()])
    Name_on_card = StringField('Name on card',[validators.Length(min=1), validators.optional()])
    exp_date = DateField('Exp date', format='%m-%Y')
    cvv_code = IntegerField("CVC/CVV Code", [validators.length(min=3, max=3), validators.optional()])
    card_number = IntegerField("Card Number", [validators.Length(min=16, max=16), validators.optional()])


class promo_code_information(Form):
    name_of_code = StringField('Name of code', [validators.Length(min=1), validators.optional()])
    value = IntegerField('Value of Promo Code', [validators.Length(max=3), validators.optional()])
