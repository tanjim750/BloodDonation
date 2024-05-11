from django.shortcuts import render, redirect
from app.models import *
import datetime
from datetime import timedelta
from django.urls import reverse
from django.template.loader import render_to_string

from app.send_email import send_email

class EditProfile:
    def get(self, request, *args, **kwargs):
        if not request.user.profile.is_donner:
            return redirect('home')
        
        district = District.objects.all()
        upazila = Upazila.objects.all()
        unions = Unions.objects.all()
        # print(district.first().upazila_set.all())
        context = {
            "district": district,
            'upazila': upazila,
            "unions": unions
        }
        if request.user.profile.profile_completed < 50:
            context['warning'] = "Please complete your profile."

        return render(request, 'edit-profile.html',context=context)
    
    def post(self, request, *args, **kwargs):
        image = request.FILES.get('image', None)
        name = request.POST.get('name', None)
        number = request.POST.get('number', None)
        email = request.POST.get('email', None)
        donated_before = request.POST.get('donated_before', None)
        total_donation = request.POST.get('total_donation', None)
        last_donnation = request.POST.get('last_donnation', None)
        dob = request.POST.get('dob', None)
        gender = request.POST.get('gender', None)
        district = request.POST.get('district', None)
        upazila = request.POST.get('upazila', None)
        unions = request.POST.get('unions', None)
        address = request.POST.get('address', None)
        document = request.FILES.get('document', None)

        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=user)
        
        if profile.is_verified or profile.is_under_review:
            if (name and number and dob and gender 
                and district and upazila and unions and address):

                district = District.objects.filter(district=district).first()
                upazila = Upazila.objects.filter(district=district).first()
                unions = Unions.objects.filter(upazila=upazila).first()

                today = datetime.date.today()
                birthdate = datetime.datetime.strptime(dob, "%Y-%m-%d")
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

                if image:
                    profile.image = image

                profile.name = name
                user.email = email
                profile.dob = dob
                profile.age = age
                profile.gender = gender
                profile.district = district
                profile.upazila = upazila
                profile.unions = unions
                profile.address = address
                profile.save()
                user.save()

                context = {'status':200,'success':"Successfully saved chenges."}
            else:
                context = {'status':401,'error':"Missing required credentials."}
        else:
            if (name and number and dob and gender 
                and district and upazila and unions and address
                and donated_before and document):

                district = District.objects.filter(district=district).first()
                upazila = Upazila.objects.filter(district=district).first()
                unions = Unions.objects.filter(upazila=upazila).first()
                today = datetime.date.today()
                birthdate = datetime.datetime.strptime(dob, "%Y-%m-%d")
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

                if (donated_before == 'yes' and total_donation is None
                    and last_donnation is None):

                    context = {'status':401,'error':"Missing required credentials."}
                else:
                    completed = 13*6.67 # profile completed point '3'(name,blood_group,is_donner)
                    donated_before = True if donated_before == 'yes' else False
                    if last_donnation:
                        today = datetime.datetime.today().date()
                        last_donnation = today - timedelta(days=int(last_donnation)+3)

                    if image:
                        profile.image = image
                    profile.name = name
                    user.username = number
                    user.email = email
                    profile.donated_before = donated_before
                    profile.total_donation = total_donation if total_donation else profile.total_donation
                    profile.last_donation = last_donnation
                    profile.dob = dob
                    profile.age = age
                    profile.gender = gender
                    profile.district = district
                    profile.upazila = upazila
                    profile.unions = unions
                    profile.address = address
                    profile.document = document
                    profile.profile_completed = completed
                    profile.is_under_review = True
                    profile.save()
                    user.save()

                    context = {'status':200,'success':"Your account is under review."}
                    
                    # send email for confirm verification
                    admin_url = request.build_absolute_uri(reverse('admin:index')) 
                    profile_url = admin_url+'app/profile/'+str(profile.id)+'/change/'
                    data = {
                        'name':profile.name,
                        'number':profile.user.username,
                        'profile':request.build_absolute_uri(profile.image.url),
                        'document':request.build_absolute_uri(profile.document.url),
                        'goto_profile':profile_url
                    }

                    html_content = 'email_template/content.html'
                    notification_mail = NotificationMail.objects.filter(is_smtp = False)
                    smtp = NotificationMail.objects.filter(is_smtp = True).first()
                    email_list = [email.mail for email in notification_mail]
                    subject = "New user requested for confirm verification"

                    send_email.send(smtp_server=smtp.smtp_server,port=smtp.smtp_port,
                                   password=smtp.smtp_password,from_email=smtp.mail,
                                   recipient_list=email_list,subject=subject,
                                   template=html_content,data=data)
            else:
                context = {'status':401,'error':"Missing required credentials."}

        return render(request, 'edit-profile.html',context)