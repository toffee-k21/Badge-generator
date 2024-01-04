from PIL import Image, ImageDraw, ImageFont
import smtplib
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import uuid

def generate_and_send_email(receiver_email):
    
    email_hash_dict = {} 
    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)
    hashed_id = hashlib.sha1(unique_id_str.encode()).hexdigest()[:5]
    print(f" Unique ID for {receiver_email}: {hashed_id}")

    
    image_path = './iwoc.png'
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_position = (200, 320) 
    draw.text(text_position, f"Unique ID: {hashed_id}", fill="black", font=font)
    edited_image_path = f'./Images/Iwoc_badge_{hashed_id}.png'
    image.save(edited_image_path, format="PNG")
    email_hash_dict[receiver_email] = hashed_id

    with open('Id_mapping.txt', 'a') as Id_file:
     for email, hash_value in email_hash_dict.items():
        Id_file.write(f"{email}: {hash_value}\n")

    

    sender_email = 'pictoholic123@gmail.com'
    subject = 'IWOC is live!'



    print(email_hash_dict)  
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject


    html_content = f"""
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<!--[if gte mso 9]>
<xml>
  <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings>
</xml>
<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
  <title></title>
  
    <style type="text/css">
      @media only screen and (min-width: 620px) {{
  .u-row {{
    width: 600px !important;
  }}
  .u-row .u-col {{
    vertical-align: top;
  }}

  .u-row .u-col-100 {{
    width: 600px !important;
  }}

}}

@media (max-width: 620px) {{
  .u-row-container {{
    max-width: 100% !important;
    padding-left: 0px !important;
    padding-right: 0px !important;
  }}
  .u-row .u-col {{
    min-width: 320px !important;
    max-width: 100% !important;
    display: block !important;
  }}
  .u-row {{
    width: 100% !important;
  }}
  .u-col {{
    width: 100% !important;
  }}
  .u-col > div {{
    margin: 0 auto;
  }}
}}
body{{
  margin: 0;
  padding: 0;
}}
table,
tr,
td {{
  vertical-align: top;
  border-collapse: collapse;
}}

p {{
  margin: 0;
}}

.ie-container table,
.mso-container table {{
  table-layout: fixed;
}}

* {{
  line-height: inherit;
}}

a[x-apple-data-detectors='true'] {{
  color: inherit !important;
  text-decoration: none !important;
}}

table, td {{ color: #000000; }} #u_body a{{color: #0000ee; text-decoration: underline; }} @media (max-width: 480px) {{#u_content_text_3 .v-container-padding-padding {{ padding: 40px 20px 20px 21px !important; }} #u_content_text_3 .v-font-size {{ font-size: 12px !important; }} #u_content_text_3 .v-line-height{{line-height: 130% !important; }} #u_content_text_5 .v-container-padding-padding {{ padding: 0px 10px !important; }} #u_content_text_6 .v-container-padding-padding {{ padding: 0px 10px !important; }} #u_content_text_6 .v-font-size {{font-size: 12px !important;}} #u_content_social_1 .v-container-padding-padding {{ padding: 12px 10px 24px !important; }} #u_content_image_3 .v-container-padding-padding {{ padding: 17px !important; }} #u_content_image_3 .v-text-align {{text-align: center !important; }} #u_content_text_2 .v-container-padding-padding {{ padding: 1px 10px 4px !important; }} }}
    </style>
  
  

</head>

<body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #ecf0f1;color: #000000">
  <!--[if IE]><div class="ie-container"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #ecf0f1;width:100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #ecf0f1;"><![endif]-->
    
  
  
    <!--[if gte mso 9]>
      <table cellpadding="0" cellspacing="0" border="0" style="margin: 0 auto;min-width: 320px;max-width: 600px;">
        <tr>
          <td background="https://assets.unlayer.com/stock-templates/1699459536076-Black%20and%20Blue%20Professional%20Technology%20Business%20Project%20Presentation.png" valign="top" width="100%">
      <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width: 600px;">
        <v:fill type="frame" src="https://assets.unlayer.com/stock-templates/1699459536076-Black%20and%20Blue%20Professional%20Technology%20Business%20Project%20Presentation.png" /><v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0">
      <![endif]-->
  
<div class="u-row-container" style="padding: 0px;background-color: #000000">
  <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-image: url('images/image-7.png');background-repeat: no-repeat;background-position: center center;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: #000000;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-image: url('images/image-7.png');background-repeat: no-repeat;background-position: center center;background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #000000;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
<div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
  <div style="background-color: #000000;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
  <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
  
<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:arial,helvetica,sans-serif;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">
      
      <img align="center" border="0" src="images/image-5.png" alt="" title="" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 600px;" width="600"/>
      
    </td>
  </tr>
</table>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
  </div>
  
    <!--[if gte mso 9]>
      </v:textbox></v:rect>
    </td>
    </tr>
    </table>
    <![endif]-->
    


  
  
<div class="u-row-container" style="padding: 0px;background-color: #000000">
  <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: #000000;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #000000;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
<div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
  <div style="background-color: #000000;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
  <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
  
<table id="u_content_text_3" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:20px 40px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; color: #ffffff; line-height: 140%; text-align: left; word-wrap: break-word;">
    <div>
<p style="line-height: 140%;"><strong>Hola Amigos!🪄</strong><br /><strong>The most awaited event is here, It's time for IWOC'24 - Innogeeks Winter Of Code! SEASON-2<br /><br /></strong></p>
</div>
<div>
<p style="line-height: 140%;"><em>Bid adieu to the chills of winter by becoming more productive while working on some hand-picked virtuous Open-Source projects. Even if you're a beginner, we've got your back!🌟<br /><br /></em></p>
</div>
<div>
<p style="line-height: 140%;">This event is offering a fantastic opportunity for all the technical scholars to learn and grow in the field of open-source technology. <br /><br /></p>
<p style="line-height: 140%;">IWOC'24 will feature offline speakers (On Weekends) from renowned organizations who will share their knowledge and experience on various technologies and domains. Additionally, there will be multiple workshops that will provide hands-on experience and a deeper understanding of the subject matter. <br /><br /></p>
<p style="line-height: 140%;">This event is an excellent opportunity for all students to learn about the latest trends and technologies in the open-source field. It is also an opportunity for you to network with industry experts and fellow students who share a passion for open-source technology. <br /><br /></p>
<p style="line-height: 140%;">We urge all students to take advantage of this fantastic opportunity and participate in IWOC'24. It promises to be an enriching and enlightening experience. <br /><br /></p>
<p style="line-height: 140%;"><strong>Registrations Open at - <a rel="noopener" href="https://www.iwoc.codes" target="_blank"><span style="color: #f1c40f; line-height: 19.6px;">www.iwoc.codes</span></a></strong></p>
<p style="line-height: 140%;"><strong>Discord -  <span style="color: #f1c40f; line-height: 19.6px;"><a rel="noopener" href="https://discord.com/invite/Hmy9a2Pr" target="_blank" style="color: #f1c40f;">iwoc_discord</a></span></strong></p>
</div>
  </div>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_text_5" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; line-height: 140%; text-align: center; word-wrap: break-word;">
    <p style="line-height: 140%;"><span style="color: #ecf0f1; line-height: 19.6px;"><strong>IWOC S2 PRIZES 🎉<br /></strong></span></p>
<p style="line-height: 140%;"><span style="color: #ecf0f1; line-height: 19.6px;"><strong>Expert - INR 7K + Swags and Goodies 🥇<br />Standard - INR 5K + Swags and Goodies 🥈</strong></span></p>
<p style="line-height: 140%;"><span style="color: #ecf0f1; line-height: 19.6px;"><strong>Novice - INR 2K + Swags and Goodies 🥉</strong></span></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_text_6" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px 40px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; line-height: 130%; text-align: center; word-wrap: break-word;">
    <p style="line-height: 130%;"> </p>
<p style="line-height: 130%;"><span style="color: #ecf0f1; line-height: 18.2px;"><strong>Mark your calendars and register now to be a part of IWOC'23. </strong></span></p>
<p style="line-height: 130%;"><span style="color: #ecf0f1; line-height: 18.2px;"><strong>Looking forward to seeing you all at the event! </strong></span></p>
<p style="line-height: 130%;"> </p>
<p style="line-height: 130%;"><span style="color: #ecf0f1; line-height: 18.2px;"><strong>Regards</strong></span><br /><span style="color: #ecf0f1; line-height: 18.2px;"><strong>Team Innogeeks</strong></span></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
  </div>
  


  
  
<div class="u-row-container" style="padding: 0px;background-color: #000000">
  <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: #000000;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #000000;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
<div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
  <div style="background-color: #000000;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
  <!--[if (!mso)&(!IE)]><!--><div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
  
<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_social_1" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 20px 20px;font-family:arial,helvetica,sans-serif;" align="left">
        
<div align="center">
  <div style="display: table; max-width:247px;">
  <!--[if (mso)|(IE)]><table width="247" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:247px;"><tr><![endif]-->
  
    
    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 30px;" valign="top"><![endif]-->
    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 30px">
      <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
        <a href="https://www.linkedin.com/company/innogeeks/mycompany/" title="LinkedIn" target="_blank">
          <img src="images/image-1.png" alt="LinkedIn" title="LinkedIn" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
        </a>
      </td></tr>
    </tbody></table>
    <!--[if (mso)|(IE)]></td><![endif]-->
    
    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 30px;" valign="top"><![endif]-->
    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 30px">
      <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
        <a href="https://www.instagram.com/innogeeks.kiet/" title="Instagram" target="_blank">
          <img src="images/image-3.png" alt="Instagram" title="Instagram" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
        </a>
      </td></tr>
    </tbody></table>
    <!--[if (mso)|(IE)]></td><![endif]-->
    
    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 30px;" valign="top"><![endif]-->
    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 30px">
      <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
        <a href="https://twitter.com/InnogeeksKiet" title="X" target="_blank">
          <img src="images/image-2.png" alt="X" title="X" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
        </a>
      </td></tr>
    </tbody></table>
    <!--[if (mso)|(IE)]></td><![endif]-->
    
    <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->
    <table align="left" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 0px">
      <tbody><tr style="vertical-align: top"><td align="left" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
        <a href="https://www.youtube.com/@innogeekskiet3679" title="YouTube" target="_blank">
          <img src="images/image-4.png" alt="YouTube" title="YouTube" width="32" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
        </a>
      </td></tr>
    </tbody></table>
    <!--[if (mso)|(IE)]></td><![endif]-->
    
    
    <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
  </div>
</div>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; color: #ffffff; line-height: -40%; text-align: center; word-wrap: break-word;">
    <p style="line-height: 0%;"><strong>Follow our social media handles to stay tuned!</strong></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_image_3" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px 10px;font-family:arial,helvetica,sans-serif;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">
      
      <img align="center" border="0" src="images/image-8.png" alt="image" title="image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 580px;" width="580"/>
      
    </td>
  </tr>
</table>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_text_2" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 30px 8px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; color: #ffffff; line-height: 110%; text-align: center; word-wrap: break-word;">
    <p style="font-size: 14px; line-height: 110%;"><span style="font-size: 8px; line-height: 8.8px;">The content of this email is confidential and intended for the recipient specified in message only. It is strictly forbidden to share any part of this message with any third party, without a written consent of the sender. If you received this message by mistake, please reply to this message and follow with its deletion, so that we can ensure such a mistake does not occur in the future.</span></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:arial,helvetica,sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:arial,helvetica,sans-serif;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">
      
      <img align="center" border="0" src="images/image-6.png" alt="" title="" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 600px;" width="600"/>
      
    </td>
  </tr>
</table>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
  </div>
  


    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    </td>
  </tr>
  </tbody>
  </table>
  <!--[if mso]></div><![endif]-->
  <!--[if IE]></div><![endif]-->
</body>

</html>

    """


    html_part = MIMEText(html_content, 'html')

    message.attach(html_part)

    with open(edited_image_path, 'rb') as file:
        img = MIMEImage(file.read())
        img.add_header('Content-Disposition', 'attachment', filename=f'image_{unique_id_str}.png')
        message.attach(img)

   
    with smtplib.SMTP('smtp-relay.brevo.com', 587) as server: 
        server.starttls()
        server.login(sender_email, '715ZRcaGEzJKmxkf')  
        # server.send_message(message)

emails = [ 'adityapachauri182003@gmail.com',"innogeeks@kiet.edu","devup@kiet.edu","aditya.2125csme1008@kiet.edu"]


for email in emails:
    generate_and_send_email(email)


