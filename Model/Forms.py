from wtforms import Form, StringField, IntegerField, EmailField, PasswordField, TelField, SelectField, SelectMultipleField, BooleanField, DateField, validators
from wtforms.validators import EqualTo


class SignUpForm1(Form):
    email = EmailField('Email Address *', [validators.Length(max=320), validators.DataRequired()])
    username = StringField('Username *', [validators.Length(min=3, max=32), validators.DataRequired()])
    password = PasswordField('Password *', [validators.Length(min=8, max=64), validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password *', [validators.DataRequired(), EqualTo("password")])


class SignUpForm2(Form):
    qns1 = SelectField('First Question *', [validators.DataRequired()], choices=[('', 'Select'), ('In what city were you born?', 'In what city were you born?'), ('What is the name of your favourite pet?', 'What is the name of your favourite pet?'), ("What is your mother's maiden name?", "What is your mother's maiden name?"), ('What high school did you attend?', 'What high school did you attend?'), ('What is the name of your first school?', 'What is the name of your first school?'), ('What was the make of your first car?', 'What was the make of your first car?'), ('What was your favourite food as a child?', 'What was your favourite food as a child?'), ('Where did you meet your spouse?', 'Where did you meet your spouse?')], default='')
    ans1 = PasswordField('Answer The Question *', [validators.DataRequired()])
    qns2 = SelectField('Second Question *', [validators.DataRequired()], choices=[('', 'Select'), ('In what city were you born?', 'In what city were you born?'), ('What is the name of your favourite pet?', 'What is the name of your favourite pet?'), ("What is your mother's maiden name?", "What is your mother's maiden name?"), ('What high school did you attend?', 'What high school did you attend?'), ('What is the name of your first school?', 'What is the name of your first school?'), ('What was the make of your first car?', 'What was the make of your first car?'), ('What was your favourite food as a child?', 'What was your favourite food as a child?'), ('Where did you meet your spouse?', 'Where did you meet your spouse?')], default='')
    ans2 = PasswordField('Answer The Question *', [validators.DataRequired()])
    qns3 = SelectField('Third Question *', [validators.DataRequired()], choices=[('', 'Select'), ('In what city were you born?', 'In what city were you born?'), ('What is the name of your favourite pet?', 'What is the name of your favourite pet?'), ("What is your mother's maiden name?", "What is your mother's maiden name?"), ('What high school did you attend?', 'What high school did you attend?'), ('What is the name of your first school?', 'What is the name of your first school?'), ('What was the make of your first car?', 'What was the make of your first car?'), ('What was your favourite food as a child?', 'What was your favourite food as a child?'), ('Where did you meet your spouse?', 'Where did you meet your spouse?')], default='')
    ans3 = PasswordField('Answer The Question *', [validators.DataRequired()])


class SignUpForm3(Form):
    first_name = StringField('First Name', [validators.Length(min=1), validators.optional()])
    last_name = StringField('Last Name', [validators.Length(min=1), validators.optional()])
    street = StringField('Building, Street', [validators.Length(min=1), validators.optional()])
    unit_no = StringField("Unit No.", [validators.Length(min=1), validators.optional()])
    postal = StringField("Postal Code", [validators.Length(min=1, max=12), validators.optional()])
    country = SelectField("Country", [validators.optional()], choices=[("", "select"), ("AF", "Afghanistan"), ("AL", "Albania"), ("DZ", "Algeria"), ("AS", "American Samoa"), ("AD", "Andorra"), ("AO", "Angola"), ("AI", "Anguilla"), ("AQ", "Antarctica"), ("AG", "Antigua and Barbuda"), ("AR", "Argentina"), ("AM", "Armenia"), ("AW", "Aruba"), ("AU", "Australia"), ("AT", "Austria"), ("AZ", "Azerbaijan"), ("BS", "Bahamas (the)"), ("BH", "Bahrain"), ("BD", "Bangladesh"), ("BB", "Barbados"), ("BY", "Belarus"), ("BE", "Belgium"), ("BZ", "Belize"), ("BJ", "Benin"), ("BM", "Bermuda"), ("BT", "Bhutan"), ("BO", "Bolivia (Plurinational State of)"), ("BQ", "Bonaire, Sint Eustatius and Saba"), ("BA", "Bosnia and Herzegovina"), ("BW", "Botswana"), ("BV", "Bouvet Island"), ("BR", "Brazil"), ("IO", "British Indian Ocean Territory (the)"), ("BN", "Brunei Darussalam"), ("BG", "Bulgaria"), ("BF", "Burkina Faso"), ("BI", "Burundi"), ("CV", "Cabo Verde"), ("KH", "Cambodia"), ("CM", "Cameroon"), ("CA", "Canada"), ("KY", "Cayman Islands (the)"), ("CF", "Central African Republic (the)"), ("TD", "Chad"), ("CL", "Chile"), ("CN", "China"), ("CX", "Christmas Island"), ("CC", "Cocos (Keeling) Islands (the)"), ("CO", "Colombia"), ("KM", "Comoros (the)"), ("CD", "Congo (the Democratic Republic of the)"), ("CG", "Congo (the)"), ("CK", "Cook Islands (the)"), ("CR", "Costa Rica"), ("HR", "Croatia"), ("CU", "Cuba"), ("CW", "Curaçao"), ("CY", "Cyprus"), ("CZ", "Czechia"), ("CI", "Côte d'Ivoire"), ("DK", "Denmark"), ("DJ", "Djibouti"), ("DM", "Dominica"), ("DO", "Dominican Republic (the)"), ("EC", "Ecuador"), ("EG", "Egypt"), ("SV", "El Salvador"), ("GQ", "Equatorial Guinea"), ("ER", "Eritrea"), ("EE", "Estonia"), ("SZ", "Eswatini"), ("ET", "Ethiopia"), ("FK", "Falkland Islands (the) [Malvinas]"), ("FO", "Faroe Islands (the)"), ("FJ", "Fiji"), ("FI", "Finland"), ("FR", "France"), ("GF", "French Guiana"), ("PF", "French Polynesia"), ("TF", "French Southern Territories (the)"), ("GA", "Gabon"), ("GM", "Gambia (the)"), ("GE", "Georgia"), ("DE", "Germany"), ("GH", "Ghana"), ("GI", "Gibraltar"), ("GR", "Greece"), ("GL", "Greenland"), ("GD", "Grenada"), ("GP", "Guadeloupe"), ("GU", "Guam"), ("GT", "Guatemala"), ("GG", "Guernsey"), ("GN", "Guinea"), ("GW", "Guinea-Bissau"), ("GY", "Guyana"), ("HT", "Haiti"), ("HM", "Heard Island and McDonald Islands"), ("VA", "Holy See (the)"), ("HN", "Honduras"), ("HK", "Hong Kong"), ("HU", "Hungary"), ("IS", "Iceland"), ("IN", "India"), ("ID", "Indonesia"), ("IR", "Iran (Islamic Republic of)"), ("IQ", "Iraq"), ("IE", "Ireland"), ("IM", "Isle of Man"), ("IL", "Israel"), ("IT", "Italy"), ("JM", "Jamaica"), ("JP", "Japan"), ("JE", "Jersey"), ("JO", "Jordan"), ("KZ", "Kazakhstan"), ("KE", "Kenya"), ("KI", "Kiribati"), ("KP", "Korea (the Democratic People's Republic of)"), ("KR", "Korea (the Republic of)"), ("KW", "Kuwait"), ("KG", "Kyrgyzstan"), ("LA", "Lao People's Democratic Republic (the)"), ("LV", "Latvia"), ("LB", "Lebanon"), ("LS", "Lesotho"), ("LR", "Liberia"), ("LY", "Libya"), ("LI", "Liechtenstein"), ("LT", "Lithuania"), ("LU", "Luxembourg"), ("MO", "Macao"), ("MG", "Madagascar"), ("MW", "Malawi"), ("MY", "Malaysia"), ("MV", "Maldives"), ("ML", "Mali"), ("MT", "Malta"), ("MH", "Marshall Islands (the)"), ("MQ", "Martinique"), ("MR", "Mauritania"), ("MU", "Mauritius"), ("YT", "Mayotte"), ("MX", "Mexico"), ("FM", "Micronesia (Federated States of)"), ("MD", "Moldova (the Republic of)"), ("MC", "Monaco"), ("MN", "Mongolia"), ("ME", "Montenegro"), ("MS", "Montserrat"), ("MA", "Morocco"), ("MZ", "Mozambique"), ("MM", "Myanmar"), ("NA", "Namibia"), ("NR", "Nauru"), ("NP", "Nepal"), ("NL", "Netherlands (the)"), ("NC", "New Caledonia"), ("NZ", "New Zealand"), ("NI", "Nicaragua"), ("NE", "Niger (the)"), ("NG", "Nigeria"), ("NU", "Niue"), ("NF", "Norfolk Island"), ("MP", "Northern Mariana Islands (the)"), ("NO", "Norway"), ("OM", "Oman"), ("PK", "Pakistan"), ("PW", "Palau"), ("PS", "Palestine, State of"), ("PA", "Panama"), ("PG", "Papua New Guinea"), ("PY", "Paraguay"), ("PE", "Peru"), ("PH", "Philippines (the)"), ("PN", "Pitcairn"), ("PL", "Poland"), ("PT", "Portugal"), ("PR", "Puerto Rico"), ("QA", "Qatar"), ("MK", "Republic of North Macedonia"), ("RO", "Romania"), ("RU", "Russian Federation (the)"), ("RW", "Rwanda"), ("RE", "Réunion"), ("BL", "Saint Barthélemy"), ("SH", "Saint Helena, Ascension and Tristan da Cunha"), ("KN", "Saint Kitts and Nevis"), ("LC", "Saint Lucia"), ("MF", "Saint Martin (French part)"), ("PM", "Saint Pierre and Miquelon"), ("VC", "Saint Vincent and the Grenadines"), ("WS", "Samoa"), ("SM", "San Marino"), ("ST", "Sao Tome and Principe"), ("SA", "Saudi Arabia"), ("SN", "Senegal"), ("RS", "Serbia"), ("SC", "Seychelles"), ("SL", "Sierra Leone"), ("SG", "Singapore"), ("SX", "Sint Maarten (Dutch part)"), ("SK", "Slovakia"), ("SI", "Slovenia"), ("SB", "Solomon Islands"), ("SO", "Somalia"), ("ZA", "South Africa"), ("GS", "South Georgia and the South Sandwich Islands"), ("SS", "South Sudan"), ("ES", "Spain"), ("LK", "Sri Lanka"), ("SD", "Sudan (the)"), ("SR", "Suriname"), ("SJ", "Svalbard and Jan Mayen"), ("SE", "Sweden"), ("CH", "Switzerland"), ("SY", "Syrian Arab Republic"), ("TW", "Taiwan (Province of China)"), ("TJ", "Tajikistan"), ("TZ", "Tanzania, United Republic of"), ("TH", "Thailand"), ("TL", "Timor-Leste"), ("TG", "Togo"), ("TK", "Tokelau"), ("TO", "Tonga"), ("TT", "Trinidad and Tobago"), ("TN", "Tunisia"), ("TR", "Turkey"), ("TM", "Turkmenistan"), ("TC", "Turks and Caicos Islands (the)"), ("TV", "Tuvalu"), ("UG", "Uganda"), ("UA", "Ukraine"), ("AE", "United Arab Emirates (the)"), ("GB", "United Kingdom of Great Britain and Northern Ireland (the)"), ("UM", "United States Minor Outlying Islands (the)"), ("US", "United States of America (the)"), ("UY", "Uruguay"), ("UZ", "Uzbekistan"), ("VU", "Vanuatu"), ("VE", "Venezuela (Bolivarian Republic of)"), ("VN", "Viet Nam"), ("VG", "Virgin Islands (British)"), ("VI", "Virgin Islands (U.S.)"), ("WF", "Wallis and Futuna"), ("EH", "Western Sahara"), ("YE", "Yemen"), ("ZM", "Zambia"), ("ZW", "Zimbabwe")])
    phone = TelField('Phone Number', [validators.optional()])
    credit_card = IntegerField('Credit Card', [validators.Length(min=16, max=16), validators.optional()])


class SignInForm(Form):
    email = EmailField('Email Address', [validators.DataRequired()], render_kw={"placeholder": "Enter your email address"})
    password = PasswordField('Password', [validators.DataRequired()], render_kw={"placeholder": "Enter your password"})
    remember = BooleanField("Remember me")


class ForgetPassword1(Form):
    email = EmailField('Email Address', [validators.DataRequired()], render_kw={"placeholder": "Enter your email"})


# class ForgetPassword2(Form):
#     qns1 = StringField('First Question', render_kw={"disabled": ""})
#     ans1 = PasswordField('Answer The Question *', [validators.DataRequired()])
#     ans2 = PasswordField('Answer The Question *', [validators.DataRequired()])
#     ans3 = PasswordField('Answer The Question *', [validators.DataRequired()])


class ForgetPassword3(Form):
    password = PasswordField('New Password *', [validators.Length(min=8, max=64), validators.DataRequired()])
    confirm_password = PasswordField('Confirm New Password *', [validators.DataRequired(), EqualTo("password")])


class DisplayInfo(Form):
    username = StringField('Username', [validators.Length(min=3, max=32), validators.DataRequired()])


class PersonalInfo(Form):
    first_name = StringField('First Name', [validators.Length(min=1), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1), validators.DataRequired()])
    address = StringField('Address', [validators.Length(min=1), validators.DataRequired()])
    phone = IntegerField('Phone Number', [validators.Length(max=8), validators.DataRequired()])
    Unit_no = IntegerField('Unit no', [validators.Length(min=16, max=16), validators.DataRequired()])
    Postal_code = IntegerField('Postal Code', [validators.Length(min=6, max=6), validators.DataRequired()])
    Name_on_card = StringField('Name on card',[validators.Length(min=1), validators.DataRequired()])
    exp_date = DateField('Exp date', format='%m-%Y')
    cvv_code = IntegerField("CVC/CVV Code", [validators.length(min=3, max=3), validators.DataRequired()])
    card_number = IntegerField("Card Number", [validators.Length(min=16, max=16), validators.DataRequired()])


class promo_code_information(Form):
    name_of_code = StringField('Name of code', [validators.Length(min=1), validators.DataRequired()])
    value = IntegerField('Value of Promo Code', [validators.Length(max=3), validators.DataRequired()])
    select = SelectField("", [validators.DataRequired()], choices=["Percentage","Discount amount"])
