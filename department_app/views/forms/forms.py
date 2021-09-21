import re
from wtforms import Form, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from wtforms.fields.html5 import DateField, DecimalField


class DepartmentForm(Form):
    name = StringField('Department', validators=[Length(min=3, max=50, message='Department name length must be between '
                                                                               '%(min)d and %(max)d characters'),
                                                 DataRequired()])
    manager = StringField('Manager', validators=[Length(min=2, max=50, message='Manager length must be between %(min)d '
                                                                               'and %(max)d characters'),
                                                 DataRequired()])
    date_of_creation = DateField('Date of creation', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class SkillForm(Form):
    name = StringField('Skill', validators=[Length(min=3, max=50, message='Skill length must be between '
                                                                          '%(min)d and %(max)d characters'),
                                            DataRequired()])
    submit = SubmitField(label='Submit')


class AddressForm(Form):
    name = StringField('Address', validators=[Length(min=3, max=100, message='Address length must be between '
                                                                             '%(min)d and %(max)d characters'),
                                              DataRequired()])
    submit = SubmitField(label='Submit')


class LocationForm(Form):
    name = StringField('Location', validators=[Length(min=3, max=100, message='Location length must be between '
                                                                              '%(min)d and %(max)d characters'),
                                               DataRequired()])
    submit = SubmitField(label='Submit')


class PermissionForm(Form):
    name = StringField('Permission', validators=[Length(min=3, max=50, message='Permission length must be between '
                                                                               '%(min)d and %(max)d characters'),
                                                 DataRequired()])
    submit = SubmitField(label='Submit')


class EmployeeForm(Form):
    name = StringField('Name', validators=[Length(min=2, max=50, message='Name length must be between '
                                                                         '%(min)d and %(max)d characters'),
                                           DataRequired()])
    surname = StringField('Surname', validators=[Length(min=2, max=50, message='Surname length must be between '
                                                                               '%(min)d and %(max)d characters'),
                                                 DataRequired()])
    salary = DecimalField('Salary', validators=[NumberRange(min=1, max=9999999, message='Salary must be, min %(min)d '
                                                                                        'and max %(max)d'),
                                                DataRequired()])
    phone = StringField('Phone', validators=[Length(min=2, max=13, message='Phone length must be between '
                                                                           '%(min)d and %(max)d characters'),
                                             DataRequired()])
    email = StringField('Email', validators=[Length(min=4, max=50, message='Email length must be between '
                                                                           '%(min)d and %(max)d characters'),
                                             DataRequired()])
    date_of_birth = DateField('Date of birth', format='%Y-%m-%d', validators=[DataRequired()])
    date_of_joining = DateField('Date of joining', format='%Y-%m-%d', validators=[DataRequired()])
    work_address = SelectField(u'Address', choices=[], coerce=int, validators=[DataRequired()])
    key_skill = SelectField(u'Skill', choices=[], coerce=int, validators=[DataRequired()])
    location = SelectField(u'Location', choices=[], coerce=int, validators=[DataRequired()])
    department = SelectField(u'Department', choices=[], coerce=int, validators=[DataRequired()])
    permission = SelectField(u'Permission', choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField(label='Submit')

    def validate_email(self, email):
        regex = r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$'
        if not re.match(regex, self.email.data.lower()):
            raise ValidationError(
                f"Wrong email format")

    def validate_phone(self, phone):
        regex = r'[0-9]+$'
        if not re.match(regex, self.phone.data):
            raise ValidationError(
                f"Wrong phone format")
