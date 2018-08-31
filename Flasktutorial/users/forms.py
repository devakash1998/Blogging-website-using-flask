from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from Flasktutorial.models import User







class RegistrationForm(FlaskForm):
    #username is of type String and it cannot be left empty and should be in r
    #range(2,21)
    username=StringField('Username',
                         validators=[DataRequired(),Length(min=2,max=20)])

    #same lets create a field for the Email
    email=StringField('Email',validators=[DataRequired(),Email()])

    #lets create a password field
    password=PasswordField('password',validators=[DataRequired()])

    confirm_password=PasswordField('confirm password',
                                   validators=[DataRequired(),EqualTo('password')])

    #creating a submit button

    submit=SubmitField('Sign up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken Try somethong else')



    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is already taken Try something else')



class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Log in')




class UpdateAccountForm(FlaskForm):
    #username is of type String and it cannot be left empty and should be in r
    #range(2,21)
    username=StringField('Username',
                         validators=[DataRequired(),Length(min=2,max=20)])

    #same lets create a field for the Email
    email=StringField('Email',validators=[DataRequired(),Email()])

    picture=FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])

    #creating a submit button

    submit=SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken Try somethong else')



    def validate_email(self,email):
        if email.data != current_user.email:
            email=User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('That email is already taken Try something else')



class RequestResetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])

    submit=SubmitField('Request Password reset')


    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
                raise ValidationError('There is no account with this email ..Register now')


class ResetPasswordForm(FlaskForm):
    password=PasswordField('password',validators=[DataRequired()])

    confirm_password=PasswordField('confirm password',
                                   validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField('Reset Password')
