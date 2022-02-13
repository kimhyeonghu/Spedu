from wtforms import Form, StringField, IntegerField, EmailField, PasswordField, TelField, SelectField, SelectMultipleField, BooleanField, DateField, validators
from wtforms.validators import EqualTo
from wtforms.validators import ValidationError


class SignUpForm1(Form):
    email = EmailField('Email Address *', [validators.Length(max=320), validators.DataRequired()], render_kw={"placeholder": "Enter your email address"})
    username = StringField('Username *', [validators.Length(min=3, max=32), validators.DataRequired()], render_kw={"placeholder": "Enter your username"})
    password = PasswordField('Password *', [validators.Length(min=8, max=64), validators.DataRequired()], render_kw={"placeholder": "Enter your password"})
    confirm_password = PasswordField('Confirm Password *', [validators.DataRequired(), EqualTo("password")], render_kw={"placeholder": "Confirm your password"})


class SignUpForm2(Form):
    qns1 = SelectField('First Question *', [validators.DataRequired()], choices=[('', 'Select'), ('In what city were you born?', 'In what city were you born?'), ('What is the name of your favourite pet?', 'What is the name of your favourite pet?'), ("What is your mother's maiden name?", "What is your mother's maiden name?"), ('What high school did you attend?', 'What high school did you attend?'), ('What is the name of your first school?', 'What is the name of your first school?'), ('What was the make of your first car?', 'What was the make of your first car?'), ('What was your favourite food as a child?', 'What was your favourite food as a child?'), ('Where did you meet your spouse?', 'Where did you meet your spouse?')], default='')
    ans1 = PasswordField('Answer The Question *', [validators.DataRequired()], render_kw={"placeholder": "Type your answer here"})
    qns2 = SelectField('Second Question *', [validators.DataRequired()], choices=[('', 'Select'), ('In what city were you born?', 'In what city were you born?'), ('What is the name of your favourite pet?', 'What is the name of your favourite pet?'), ("What is your mother's maiden name?", "What is your mother's maiden name?"), ('What high school did you attend?', 'What high school did you attend?'), ('What is the name of your first school?', 'What is the name of your first school?'), ('What was the make of your first car?', 'What was the make of your first car?'), ('What was your favourite food as a child?', 'What was your favourite food as a child?'), ('Where did you meet your spouse?', 'Where did you meet your spouse?')], default='')
    ans2 = PasswordField('Answer The Question *', [validators.DataRequired()], render_kw={"placeholder": "Type your answer here"})
    qns3 = SelectField('Third Question *', [validators.DataRequired()], choices=[('', 'Select'), ('In what city were you born?', 'In what city were you born?'), ('What is the name of your favourite pet?', 'What is the name of your favourite pet?'), ("What is your mother's maiden name?", "What is your mother's maiden name?"), ('What high school did you attend?', 'What high school did you attend?'), ('What is the name of your first school?', 'What is the name of your first school?'), ('What was the make of your first car?', 'What was the make of your first car?'), ('What was your favourite food as a child?', 'What was your favourite food as a child?'), ('Where did you meet your spouse?', 'Where did you meet your spouse?')], default='')
    ans3 = PasswordField('Answer The Question *', [validators.DataRequired()], render_kw={"placeholder": "Type your answer here"})


class SignUpForm3(Form):
    first_name = StringField('First Name', [validators.Length(min=1), validators.optional()], render_kw={"placeholder": "Enter your first name"})
    last_name = StringField('Last Name', [validators.Length(min=1), validators.optional()], render_kw={"placeholder": "Enter your last name"})
    address = StringField('Address', [validators.Length(min=1), validators.optional()], render_kw={"placeholder": "Enter your address"})
    unit_no = StringField("Unit No.", [validators.Length(min=1), validators.optional()], render_kw={"placeholder": "Enter your unit no."})
    postal = StringField("Postal Code", [validators.Length(min=1, max=12), validators.optional()], render_kw={"placeholder": "Enter your postal code"})
    country = SelectField("Country", [validators.optional()], choices=[("", "Select"), ("AF", "Afghanistan"), ("AL", "Albania"), ("DZ", "Algeria"), ("AS", "American Samoa"), ("AD", "Andorra"), ("AO", "Angola"), ("AI", "Anguilla"), ("AQ", "Antarctica"), ("AG", "Antigua and Barbuda"), ("AR", "Argentina"), ("AM", "Armenia"), ("AW", "Aruba"), ("AU", "Australia"), ("AT", "Austria"), ("AZ", "Azerbaijan"), ("BS", "Bahamas"), ("BH", "Bahrain"), ("BD", "Bangladesh"), ("BB", "Barbados"), ("BY", "Belarus"), ("BE", "Belgium"), ("BZ", "Belize"), ("BJ", "Benin"), ("BM", "Bermuda"), ("BT", "Bhutan"), ("BO", "Bolivia"), ("BA", "Bosnia and Herzegovina"), ("BW", "Botswana"), ("BR", "Brazil"), ("BN", "Brunei Darussalam"), ("BG", "Bulgaria"), ("BF", "Burkina Faso"), ("BI", "Burundi"), ("CV", "Cabo Verde"), ("KH", "Cambodia"), ("CM", "Cameroon"), ("CA", "Canada"), ("KY", "Cayman Islands"), ("CF", "Central African Republic"), ("TD", "Chad"), ("CL", "Chile"), ("CN", "China"), ("CO", "Colombia"), ("KM", "Comoros"), ("CD", "Congo"), ("CR", "Costa Rica"), ("HR", "Croatia"), ("CU", "Cuba"), ("CW", "Curaçao"), ("CY", "Cyprus"), ("CZ", "Czechia"), ("CI", "Côte d'Ivoire"), ("DK", "Denmark"), ("DJ", "Djibouti"), ("DM", "Dominica"), ("DO", "Dominican Republic"), ("EC", "Ecuador"), ("EG", "Egypt"), ("SV", "El Salvador"), ("GQ", "Equatorial Guinea"), ("ER", "Eritrea"), ("EE", "Estonia"), ("SZ", "Eswatini"), ("ET", "Ethiopia"), ("FJ", "Fiji"), ("FI", "Finland"), ("FR", "France"), ("GF", "French Guiana"), ("PF", "French Polynesia"), ("GA", "Gabon"), ("GM", "Gambia"), ("GE", "Georgia"), ("DE", "Germany"), ("GH", "Ghana"), ("GI", "Gibraltar"), ("GR", "Greece"), ("GL", "Greenland"), ("GD", "Grenada"), ("GP", "Guadeloupe"), ("GU", "Guam"), ("GT", "Guatemala"), ("GG", "Guernsey"), ("GN", "Guinea"), ("GW", "Guinea-Bissau"), ("GY", "Guyana"), ("HT", "Haiti"), ("HN", "Honduras"), ("HK", "Hong Kong"), ("HU", "Hungary"), ("IS", "Iceland"), ("IN", "India"), ("ID", "Indonesia"), ("IR", "Iran"), ("IQ", "Iraq"), ("IE", "Ireland"), ("IM", "Isle of Man"), ("IL", "Israel"), ("IT", "Italy"), ("JM", "Jamaica"), ("JP", "Japan"), ("JE", "Jersey"), ("JO", "Jordan"), ("KZ", "Kazakhstan"), ("KE", "Kenya"), ("KI", "Kiribati"), ("KP", "North Korea"), ("KR", "South Korea"), ("KW", "Kuwait"), ("KG", "Kyrgyzstan"), ("LA", "Laos"), ("LV", "Latvia"), ("LB", "Lebanon"), ("LS", "Lesotho"), ("LR", "Liberia"), ("LY", "Libya"), ("LI", "Liechtenstein"), ("LT", "Lithuania"), ("LU", "Luxembourg"), ("MO", "Macao"), ("MG", "Madagascar"), ("MW", "Malawi"), ("MY", "Malaysia"), ("MV", "Maldives"), ("ML", "Mali"), ("MT", "Malta"), ("MH", "Marshall Islands"), ("MQ", "Martinique"), ("MR", "Mauritania"), ("MU", "Mauritius"), ("YT", "Mayotte"), ("MX", "Mexico"), ("FM", "Micronesia"), ("MD", "Moldova"), ("MC", "Monaco"), ("MN", "Mongolia"), ("ME", "Montenegro"), ("MS", "Montserrat"), ("MA", "Morocco"), ("MZ", "Mozambique"), ("MM", "Myanmar"), ("NA", "Namibia"), ("NR", "Nauru"), ("NP", "Nepal"), ("NL", "Netherlands"), ("NC", "New Caledonia"), ("NZ", "New Zealand"), ("NI", "Nicaragua"), ("NE", "Nigeria"), ("NG", "Nigeria"), ("NU", "Niue"), ("NF", "Norfolk Island"), ("MP", "Northern Mariana Islands"), ("NO", "Norway"), ("OM", "Oman"), ("PK", "Pakistan"), ("PW", "Palau"), ("PS", "Palestine"), ("PA", "Panama"), ("PG", "Papua New Guinea"), ("PY", "Paraguay"), ("PE", "Peru"), ("PH", "Philippines"), ("PN", "Pitcairn"), ("PL", "Poland"), ("PT", "Portugal"), ("PR", "Puerto Rico"), ("QA", "Qatar"), ("MK", "Republic of North Macedonia"), ("RO", "Romania"), ("RU", "Russia"), ("RW", "Rwanda"), ("RE", "Réunion"), ("BL", "Saint Barthélemy"), ("KN", "Saint Kitts and Nevis"), ("LC", "Saint Lucia"), ("MF", "Saint Martin"), ("PM", "Saint Pierre and Miquelon"), ("VC", "Saint Vincent and the Grenadines"), ("WS", "Samoa"), ("SM", "San Marino"), ("ST", "Sao Tome and Principe"), ("SA", "Saudi Arabia"), ("SN", "Senegal"), ("RS", "Serbia"), ("SC", "Seychelles"), ("SL", "Sierra Leone"), ("SG", "Singapore"), ("SX", "Sint Maarten"), ("SK", "Slovakia"), ("SI", "Slovenia"), ("SB", "Solomon Islands"), ("SO", "Somalia"), ("ZA", "South Africa"), ("SS", "South Sudan"), ("ES", "Spain"), ("LK", "Sri Lanka"), ("SD", "Sudan"), ("SR", "Suriname"), ("SJ", "Svalbard and Jan Mayen"), ("SE", "Sweden"), ("CH", "Switzerland"), ("SY", "Syrian Arab Republic"), ("TW", "Taiwan"), ("TJ", "Tajikistan"), ("TZ", "Tanzania"), ("TH", "Thailand"), ("TL", "Timor-Leste"), ("TG", "Togo"), ("TK", "Tokelau"), ("TO", "Tonga"), ("TT", "Trinidad and Tobago"), ("TN", "Tunisia"), ("TR", "Turkey"), ("TM", "Turkmenistan"), ("TV", "Tuvalu"), ("UG", "Uganda"), ("UA", "Ukraine"), ("AE", "United Arab Emirates (the)"), ("US", "United States of America"), ("UY", "Uruguay"), ("UZ", "Uzbekistan"), ("VU", "Vanuatu"), ("VE", "Venezuela"), ("VN", "Vietnam"), ("WF", "Wallis and Futuna"), ("EH", "Western Sahara"), ("YE", "Yemen"), ("ZM", "Zambia"), ("ZW", "Zimbabwe")])
    phone = TelField('Phone Number', [validators.optional(), validators.Regexp("\d+", message="Phone Number should only contain numbers.")], render_kw={"placeholder": "Enter your phone number"})


class SignInForm(Form):
    email = EmailField('Email Address', [validators.DataRequired()], render_kw={"placeholder": "Enter your email address"})
    password = PasswordField('Password', [validators.DataRequired()], render_kw={"placeholder": "Enter your password"})
    remember = BooleanField("Remember me")


class ForgetPassword1(Form):
    email = EmailField('Email Address', [validators.DataRequired()], render_kw={"placeholder": "Enter your email address"})


# class ForgetPassword2(Form):
#     qns1 = StringField('First Question', render_kw={"disabled": ""})
#     ans1 = PasswordField('Answer The Question *', [validators.DataRequired()])
#     ans2 = PasswordField('Answer The Question *', [validators.DataRequired()])
#     ans3 = PasswordField('Answer The Question *', [validators.DataRequired()])


class ForgetPassword3(Form):
    password = PasswordField('New Password *', [validators.Length(min=8, max=64), validators.DataRequired()], render_kw={"placeholder": "Enter a new password"})
    confirm_password = PasswordField('Confirm New Password *', [validators.DataRequired(), EqualTo("password")], render_kw={"placeholder": "Enter your new password again"})


class DisplayInfo(Form):
    username = StringField('Username', [validators.Length(min=3, max=32), validators.DataRequired()])


class ChangePassword(Form):
    old_password = PasswordField('Old Password', [validators.DataRequired()], render_kw={"placeholder": "Enter your old password"})
    new_password = PasswordField('New Password', [validators.Length(min=8, max=64), validators.DataRequired()], render_kw={"placeholder": "Enter a new password"})
    confirm_password = PasswordField('Confirm New Password', [validators.DataRequired(), EqualTo("new_password")], render_kw={"placeholder": "Enter your new password again"})


class PersonalInfo(Form):
    first_name = StringField('First Name', [validators.Length(min=1), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1), validators.DataRequired()])
    address = StringField('Address 1', [validators.Length(min=1), validators.DataRequired()])
    phone = IntegerField('Phone Number', [validators.Length(max=8), validators.DataRequired()])
    Unit_no = IntegerField('Address 2', [validators.Length(min=16, max=16), validators.DataRequired()])
    Postal_code = IntegerField('Postal Code', [validators.Length(min=6, max=6), validators.DataRequired()])
    country = SelectField("Country", [validators.optional()], choices=[("", "Select"), ("AF", "Afghanistan"), ("AL", "Albania"), ("DZ", "Algeria"), ("AS", "American Samoa"), ("AD", "Andorra"), ("AO", "Angola"), ("AI", "Anguilla"), ("AQ", "Antarctica"), ("AG", "Antigua and Barbuda"), ("AR", "Argentina"), ("AM", "Armenia"), ("AW", "Aruba"), ("AU", "Australia"), ("AT", "Austria"), ("AZ", "Azerbaijan"), ("BS", "Bahamas"), ("BH", "Bahrain"), ("BD", "Bangladesh"), ("BB", "Barbados"), ("BY", "Belarus"), ("BE", "Belgium"), ("BZ", "Belize"), ("BJ", "Benin"), ("BM", "Bermuda"), ("BT", "Bhutan"), ("BO", "Bolivia"), ("BA", "Bosnia and Herzegovina"), ("BW", "Botswana"), ("BR", "Brazil"), ("BN", "Brunei Darussalam"), ("BG", "Bulgaria"), ("BF", "Burkina Faso"), ("BI", "Burundi"), ("CV", "Cabo Verde"), ("KH", "Cambodia"), ("CM", "Cameroon"), ("CA", "Canada"), ("KY", "Cayman Islands"), ("CF", "Central African Republic"), ("TD", "Chad"), ("CL", "Chile"), ("CN", "China"), ("CO", "Colombia"), ("KM", "Comoros"), ("CD", "Congo"), ("CR", "Costa Rica"), ("HR", "Croatia"), ("CU", "Cuba"), ("CW", "Curaçao"), ("CY", "Cyprus"), ("CZ", "Czechia"), ("CI", "Côte d'Ivoire"), ("DK", "Denmark"), ("DJ", "Djibouti"), ("DM", "Dominica"), ("DO", "Dominican Republic"), ("EC", "Ecuador"), ("EG", "Egypt"), ("SV", "El Salvador"), ("GQ", "Equatorial Guinea"), ("ER", "Eritrea"), ("EE", "Estonia"), ("SZ", "Eswatini"), ("ET", "Ethiopia"), ("FJ", "Fiji"), ("FI", "Finland"), ("FR", "France"), ("GF", "French Guiana"), ("PF", "French Polynesia"), ("GA", "Gabon"), ("GM", "Gambia"), ("GE", "Georgia"), ("DE", "Germany"), ("GH", "Ghana"), ("GI", "Gibraltar"), ("GR", "Greece"), ("GL", "Greenland"), ("GD", "Grenada"), ("GP", "Guadeloupe"), ("GU", "Guam"), ("GT", "Guatemala"), ("GG", "Guernsey"), ("GN", "Guinea"), ("GW", "Guinea-Bissau"), ("GY", "Guyana"), ("HT", "Haiti"), ("HN", "Honduras"), ("HK", "Hong Kong"), ("HU", "Hungary"), ("IS", "Iceland"), ("IN", "India"), ("ID", "Indonesia"), ("IR", "Iran"), ("IQ", "Iraq"), ("IE", "Ireland"), ("IM", "Isle of Man"), ("IL", "Israel"), ("IT", "Italy"), ("JM", "Jamaica"), ("JP", "Japan"), ("JE", "Jersey"), ("JO", "Jordan"), ("KZ", "Kazakhstan"), ("KE", "Kenya"), ("KI", "Kiribati"), ("KP", "North Korea"), ("KR", "South Korea"), ("KW", "Kuwait"), ("KG", "Kyrgyzstan"), ("LA", "Laos"), ("LV", "Latvia"), ("LB", "Lebanon"), ("LS", "Lesotho"), ("LR", "Liberia"), ("LY", "Libya"), ("LI", "Liechtenstein"), ("LT", "Lithuania"), ("LU", "Luxembourg"), ("MO", "Macao"), ("MG", "Madagascar"), ("MW", "Malawi"), ("MY", "Malaysia"), ("MV", "Maldives"), ("ML", "Mali"), ("MT", "Malta"), ("MH", "Marshall Islands"), ("MQ", "Martinique"), ("MR", "Mauritania"), ("MU", "Mauritius"), ("YT", "Mayotte"), ("MX", "Mexico"), ("FM", "Micronesia"), ("MD", "Moldova"), ("MC", "Monaco"), ("MN", "Mongolia"), ("ME", "Montenegro"), ("MS", "Montserrat"), ("MA", "Morocco"), ("MZ", "Mozambique"), ("MM", "Myanmar"), ("NA", "Namibia"), ("NR", "Nauru"), ("NP", "Nepal"), ("NL", "Netherlands"), ("NC", "New Caledonia"), ("NZ", "New Zealand"), ("NI", "Nicaragua"), ("NE", "Nigeria"), ("NG", "Nigeria"), ("NU", "Niue"), ("NF", "Norfolk Island"), ("MP", "Northern Mariana Islands"), ("NO", "Norway"), ("OM", "Oman"), ("PK", "Pakistan"), ("PW", "Palau"), ("PS", "Palestine"), ("PA", "Panama"), ("PG", "Papua New Guinea"), ("PY", "Paraguay"), ("PE", "Peru"), ("PH", "Philippines"), ("PN", "Pitcairn"), ("PL", "Poland"), ("PT", "Portugal"), ("PR", "Puerto Rico"), ("QA", "Qatar"), ("MK", "Republic of North Macedonia"), ("RO", "Romania"), ("RU", "Russia"), ("RW", "Rwanda"), ("RE", "Réunion"), ("BL", "Saint Barthélemy"), ("KN", "Saint Kitts and Nevis"), ("LC", "Saint Lucia"), ("MF", "Saint Martin"), ("PM", "Saint Pierre and Miquelon"), ("VC", "Saint Vincent and the Grenadines"), ("WS", "Samoa"), ("SM", "San Marino"), ("ST", "Sao Tome and Principe"), ("SA", "Saudi Arabia"), ("SN", "Senegal"), ("RS", "Serbia"), ("SC", "Seychelles"), ("SL", "Sierra Leone"), ("SG", "Singapore"), ("SX", "Sint Maarten"), ("SK", "Slovakia"), ("SI", "Slovenia"), ("SB", "Solomon Islands"), ("SO", "Somalia"), ("ZA", "South Africa"), ("SS", "South Sudan"), ("ES", "Spain"), ("LK", "Sri Lanka"), ("SD", "Sudan"), ("SR", "Suriname"), ("SJ", "Svalbard and Jan Mayen"), ("SE", "Sweden"), ("CH", "Switzerland"), ("SY", "Syrian Arab Republic"), ("TW", "Taiwan"), ("TJ", "Tajikistan"), ("TZ", "Tanzania"), ("TH", "Thailand"), ("TL", "Timor-Leste"), ("TG", "Togo"), ("TK", "Tokelau"), ("TO", "Tonga"), ("TT", "Trinidad and Tobago"), ("TN", "Tunisia"), ("TR", "Turkey"), ("TM", "Turkmenistan"), ("TV", "Tuvalu"), ("UG", "Uganda"), ("UA", "Ukraine"), ("AE", "United Arab Emirates (the)"), ("US", "United States of America"), ("UY", "Uruguay"), ("UZ", "Uzbekistan"), ("VU", "Vanuatu"), ("VE", "Venezuela"), ("VN", "Vietnam"), ("WF", "Wallis and Futuna"), ("EH", "Western Sahara"), ("YE", "Yemen"), ("ZM", "Zambia"), ("ZW", "Zimbabwe")])
    Name_on_card = StringField('Name on card', [validators.Length(min=1), validators.DataRequired()])
    exp_date = IntegerField('Exp date', [validators.Length(min=4, max=4), validators.DataRequired()])
    cvv_code = IntegerField("CVC/CVV Code", [validators.length(min=3, max=3), validators.DataRequired()])
    card_number = IntegerField("Card Number", [validators.Length(min=16, max=16), validators.DataRequired()])


class promo_code_information(Form):
    name_of_code = StringField('Name of code', [validators.Length(min=1), validators.DataRequired()])
    value = IntegerField('Value of Promo Code', [validators.Length(max=3), validators.DataRequired()])
    select = SelectField("", [validators.DataRequired()], choices=["Percentage","Discount amount"])
