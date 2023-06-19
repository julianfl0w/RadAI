# imports for device based authentication
from flask import render_template, session, url_for, request, redirect
import	json
import requests
import base64

# settings for device based authentication, can be added to .env
#	your	domain, do not include an ending slash
domain	=	"yourdomain.com"
#	your origin	site (basically just adding https:// if you don't use a sub-domain), do not include an ending slash
domain_origin	=	"https://yourdomain.com"
# your site name
domain_name	=	"your site name"
# your api key (you'll recieve this if you signup on bloc.id, you'll find it under "Profile")
api_key = "your api key"
#	A	simple	way	to	persist	challenges	until	response	verification (extra layer of security that is required to use the api)
current_registration_challenge	=	None
current_authentication_challenge	=	None