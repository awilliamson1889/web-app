from wtforms import Form, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField


class AddDepartmentForm(Form):
    name = StringField('Department', validators=[Length(min=3, max=50, message='Department name length must be between '
                                                                               '%(min)d and %(max)d characters'),
                                                 DataRequired()])
    manager = StringField('Manager', validators=[Length(min=2, max=50, message='Manager length must be between %(min)d '
                                                                               'and %(max)d characters'),
                                                 DataRequired()])
    date_of_creation = DateField('Date of creation', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class AddSkillForm(Form):
    name = StringField('Skill', validators=[Length(min=3, max=50, message='Skill length must be between '
                                                                          '%(min)d and %(max)d characters'),
                                            DataRequired()])
    submit = SubmitField(label='Submit')


class AddAddressForm(Form):
    name = StringField('Address', validators=[Length(min=3, max=100, message='Address length must be between '
                                                                             '%(min)d and %(max)d characters'),
                                              DataRequired()])
    submit = SubmitField(label='Submit')


class AddLocationForm(Form):
    name = StringField('Location', validators=[Length(min=3, max=100, message='Location length must be between '
                                                                              '%(min)d and %(max)d characters'),
                                               DataRequired()])
    submit = SubmitField(label='Submit')


class AddPermissionForm(Form):
    name = StringField('Permission', validators=[Length(min=3, max=50, message='Permission length must be between '
                                                                               '%(min)d and %(max)d characters'),
                                                 DataRequired()])
    submit = SubmitField(label='Submit')
