from PIL import Image, ImageDraw, ImageFont
import smtplib
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import uuid

def generate_and_send_email(receiver_email, participant_name, event_name, event_hashtags,organization_name, download_link, verification_link):
    
    email_hash_dict = {} 
    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)
    hashed_id = hashlib.sha1(unique_id_str.encode()).hexdigest()[:5]
    print(f" Unique ID for {receiver_email}: {hashed_id}")

    
    image_path = './iwoc3-cert.png'
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_position = (200, 320) 
    draw.text(text_position, f"{participant_name}", fill="black", font=font)
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
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">
 <head>
  <meta charset="UTF-8">
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta content="telephone=no" name="format-detection">
  <title>Empty template</title><!--[if (mso 16)]>
    <style type="text/css">
    a {{text-decoration: none; color: rgb(113, 194, 244); font-family: sans-serif;}}
    </style>
    <![endif]--><!--[if gte mso 9]><style>sup {{ font-size: 100% !important; }}</style><![endif]--><!--[if gte mso 9]>
<noscript>
         <xml>
           <o:OfficeDocumentSettings>
           <o:AllowPNG></o:AllowPNG>
           <o:PixelsPerInch>96</o:PixelsPerInch>
           </o:OfficeDocumentSettings>
         </xml>
      </noscript>
<![endif]--><!--[if mso]><xml>
    <w:WordDocument xmlns:w="urn:schemas-microsoft-com:office:word">
      <w:DontUseAdvancedTypographyReadingMail/>
    </w:WordDocument>
    </xml><![endif]-->
  <style type="text/css">
.rollover:hover .rollover-first {{
  max-height:0px!important;
  display:none!important;
}}
.rollover:hover .rollover-second {{
  max-height:none!important;
  display:block!important;
}}
.rollover span {{
  font-size:0px;
}}
u + .body img ~ div div {{
  display:none;
}}
#outlook a {{
  padding:0;
}}
span.MsoHyperlink,
span.MsoHyperlinkFollowed {{
  color:inherit;
  mso-style-priority:99;
}}
a.es-button {{
  mso-style-priority:100!important;
  text-decoration:none!important;
}}
a[x-apple-data-detectors],
#MessageViewBody a {{
  color:inherit!important;
  text-decoration:none!important;
  font-size:inherit!important;
  font-family:inherit!important;
  font-weight:inherit!important;
  line-height:inherit!important;
}}
.es-desk-hidden {{
  display:none;
  float:left;
  overflow:hidden;
  width:0;
  max-height:0;
  line-height:0;
  mso-hide:all;
}}
@media only screen and (max-width:600px) {{.es-p-default {{ }} *[class="gmail-fix"] {{ display:none!important }} p, a {{ line-height:150%!important }} h1, h1 a {{ line-height:120%!important }} h2, h2 a {{ line-height:120%!important }} h3, h3 a {{ line-height:120%!important }} h4, h4 a {{ line-height:120%!important }} h5, h5 a {{ line-height:120%!important }} h6, h6 a {{ line-height:120%!important }} .es-header-body p {{ }} .es-content-body p {{ }} .es-footer-body p {{ }} .es-infoblock p {{ }} h1 {{ font-size:30px!important; text-align:left }} h2 {{ font-size:24px!important; text-align:left }} h3 {{ font-size:20px!important; text-align:left }} h4 {{ font-size:24px!important; text-align:left }} h5 {{ font-size:20px!important; text-align:left }} h6 {{ font-size:16px!important; text-align:left }} .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a {{ font-size:30px!important }} .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a {{ font-size:24px!important }} .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a {{ font-size:20px!important }} .es-header-body h4 a, .es-content-body h4 a, .es-footer-body h4 a {{ font-size:24px!important }} .es-header-body h5 a, .es-content-body h5 a, .es-footer-body h5 a {{ font-size:20px!important }} .es-header-body h6 a, .es-content-body h6 a, .es-footer-body h6 a {{ font-size:16px!important }} .es-menu td a {{ font-size:14px!important }} .es-header-body p, .es-header-body a {{ font-size:14px!important }} .es-content-body p, .es-content-body a {{ font-size:14px!important }} .es-footer-body p, .es-footer-body a {{ font-size:14px!important }} .es-infoblock p, .es-infoblock a {{ font-size:12px!important }} .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3, .es-m-txt-c h4, .es-m-txt-c h5, .es-m-txt-c h6 {{ text-align:center!important }} .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3, .es-m-txt-r h4, .es-m-txt-r h5, .es-m-txt-r h6 {{ text-align:right!important }} .es-m-txt-j, .es-m-txt-j h1, .es-m-txt-j h2, .es-m-txt-j h3, .es-m-txt-j h4, .es-m-txt-j h5, .es-m-txt-j h6 {{ text-align:justify!important }} .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3, .es-m-txt-l h4, .es-m-txt-l h5, .es-m-txt-l h6 {{ text-align:left!important }} .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img {{ display:inline!important }} .es-m-txt-r .rollover:hover .rollover-second, .es-m-txt-c .rollover:hover .rollover-second, .es-m-txt-l .rollover:hover .rollover-second {{ display:inline!important }} .es-m-txt-r .rollover span, .es-m-txt-c .rollover span, .es-m-txt-l .rollover span {{ line-height:0!important; font-size:0!important; display:block }} .es-spacer {{ display:inline-table }} a.es-button, button.es-button {{ font-size:18px!important; padding:10px 20px 10px 20px!important; line-height:120%!important }} a.es-button, button.es-button, .es-button-border {{ display:inline-block!important }} .es-m-fw, .es-m-fw.es-fw, .es-m-fw .es-button {{ display:block!important }} .es-m-il, .es-m-il .es-button, .es-social, .es-social td, .es-menu {{ display:inline-block!important }} .es-adaptive table, .es-left, .es-right {{ width:100%!important }} .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header {{ width:100%!important; max-width:600px!important }} .adapt-img {{ width:100%!important; height:auto!important }} .es-mobile-hidden, .es-hidden {{ display:none!important }} .es-desk-hidden {{ width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important }} tr.es-desk-hidden {{ display:table-row!important }} table.es-desk-hidden {{ display:table!important }} td.es-desk-menu-hidden {{ display:table-cell!important }} .es-menu td {{ width:1%!important }} table.es-table-not-adapt, .esd-block-html table {{ width:auto!important }} .h-auto {{ height:auto!important }} }}
@media screen and (max-width:384px) {{.mail-message-content {{ width:414px!important }} }}
.button-36,
        .wpbutton {{
            background-image: linear-gradient(92.88deg, #3e769b 9.16%, #38A8C7 43.89%, #4ED7FC 64.72%);
            border-radius: 8px;
            border-style: none;
            box-sizing: border-box;
            color: #FFFFFF;
            cursor: pointer;
            flex-shrink: 0;
            font-family: sans-serif;
            font-size: 14px;
            font-weight: 700;
            height: 2.5rem;
            padding: 0 1.5rem;
            text-align: center;
            text-shadow: rgba(0, 0, 0, 0.25) 0 3px 8px;
            transition: all .5s;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            display: block;

        }}

        .button-36:hover {{
            box-shadow: rgba(40, 138, 218, 0.5) 0 1px 30px;
            transition-duration: .1s;
        }}

        .wpbutton:hover {{
            box-shadow: rgba(40, 138, 218, 0.5) 0 1px 30px;
            transition-duration: .1s;
        }}

        @media (min-width: 768px) {{
            .button-36 {{
                padding: 0 2.6rem;
            }}
        }}
</style>
 </head>
 <body class="body" style="width:100%;height:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
  <div dir="ltr" class="es-wrapper-color" lang="en" style="background-color:#F6F6F6"><!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#f6f6f6"></v:fill>
			</v:background>
		<![endif]-->
   <table width="100%" cellspacing="0" cellpadding="0" class="es-wrapper" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;background-color:#F6F6F6">
     <tr>
      <td valign="top" style="padding:0;Margin:0">
       <table cellspacing="0" cellpadding="0" align="center" class="es-content" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;width:100%;table-layout:fixed !important">
         <tr>
          <td align="center" bgcolor="#ffffff" style="padding:0;Margin:0;background-color:#ffffff">
           <table cellspacing="0" cellpadding="0" bgcolor="#0a0a0a" align="center" class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#0a0a0a;width:600px">
             <tr>
              <td align="left" style="padding:0;Margin:0;padding-top:10px;padding-right:10px;padding-left:10px">
               <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                 <tr>
                  <td valign="top" align="center" style="padding:0;Margin:0;width:560px">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                     <tr>
                      <td align="center" style="padding:0;Margin:0;font-size:0"><img src="https://res.cloudinary.com/dib0peewu/image/upload/v1736798081/Black_and_Blue_Professional_Technology_Business_Project_Presentation_ybyki8.png" alt="" width="100%" class="adapt-img" style="display:block;font-size:14px;border:0;outline:none;text-decoration:none"></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
             <tr>
              <td align="left" style="padding:10px;Margin:0">
                  <table cellpadding="0" width="100%" cellspacing="0" style="border-collapse:collapse;border-spacing:0px">
                      <tr>
                          <td valign="top" align="center" style="padding:0;Margin:0;width:560px">
                              <table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse;border-spacing:0px">
                                  <tr>
                                      <td align="left" style="padding:0;Margin:0">
                                          <p style="Margin:0;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#ffffff;font-size:14px">
                                              <br><br>
                                              <strong>Hey {participant_name},</strong>
                                              <br><br>
                                              Thank you so much for your participation in <strong>{event_name} by {organization_name}</strong>.<br><br>
                                              Share your certificates on social media handles using hashtags <strong>{event_hashtags}</strong>
                                              <br><br>
                                          </p>
                                          <p style="text-align: center; color: #fff;font-family:arial, 'helvetica neue', helvetica, sans-serif;">
                                              Download or verify your certificate below
                                          </p>
                                          <p style="text-align: center;">
                                              <a target="_blank" rel="noopener noreferrer nofollow" class="editor_link editor_link_button" 
                                                 href="{download_link}" style="display:inline-block;padding:12px 24px;font-family:arial, 'helvetica neue', helvetica, sans-serif;
                                                 font-size:16px;color:#000;text-decoration:none;border-radius:6px;background-color:#4ED7FC; margin-right:10px;" 
                                                 title="Linked To: {download_link}">Download</a>
                                              <a target="_blank" rel="noopener noreferrer nofollow" class="editor_link editor_link_button" 
                                                 href="{verification_link}" style="display:inline-block;padding:12px 24px;font-family:arial, 'helvetica neue', helvetica, sans-serif;
                                                 font-size:16px;color:#000;text-decoration:none;border-radius:6px;background-color:#4ED7FC;" 
                                                 title="Linked To: {verification_link}">Verify</a>
                                          </p>
                                          <br>
                                          <p style="Margin:0;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#ffffff;font-size:14px">
                                             For your remarkable dedication, problem-solving skills and passion for innovation in  <strong>Innogeeks Winter of Code 3.0 (IWOC 3.0).
                                            </strong>
                                              <br><br>
                                              You dared to challenge limits, embraced collaboration and transformed ideas into impactful open-source contributions. Your journey in IWOC 3.0 is a testament to your growth as a developer and an innovator in the tech community.
                                              <br><br>                                      
This certificate isn’t just a recognition of participation—it's proof of your commitment to open-source, your resilience in solving real-world challenges and your role in shaping the future of technology.
                                              <br><br>
                                              We can’t wait to see where your skills take you next. The open-source world is yours to conquer!


                                              <br><br>
                                              <strong>Warm Regards,</strong>
                                              <br>
                                              Team Innogeeks
                                          </p>
                                      </td>
                                  </tr>
                              </table>
                          </td>
                      </tr>
                  </table>
              </td>
          </tr>
          
             <tr>
              <td align="left" style="padding:0;Margin:0;padding-top:10px;padding-right:10px;padding-left:10px">
               <table cellpadding="0" width="100%" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                 <tr>
                  <td valign="top" align="center" style="padding:0;Margin:0;width:560px">
                   <table cellspacing="0" cellpadding="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                     <tr>
                      <td align="center" style="padding:0;Margin:0;font-size:0"><img alt="" width="560" src="https://res.cloudinary.com/dib0peewu/image/upload/v1736793104/email_banner_2_wjyzvg.png" class="adapt-img" style="display:block;font-size:14px;border:0;outline:none;text-decoration:none"></td>
                     </tr>
                   </table></td>
                 </tr>
              
             <div class="u-row-container" style="padding: 0px;background-color: #000000;">
              <div class="u-row"
                style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                <div
                  style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                  <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: #000000;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
  
                  <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #000000;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                  <div class="u-col u-col-100"
                    style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                    <div
                      style="background-color: #000000;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <!--[if (!mso)&(!IE)]><!-->
                      <div
                        style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                        <!--<![endif]-->
  
                        <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                          cellspacing="0" width="100%" border="0">
                          <tbody>
                            <tr>
                              <td class="v-container-padding-padding"
                                style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                align="left">
  
                                <!-- <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                                  style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                  <tbody>
                                    <tr style="vertical-align: top">
                                      <td
                                        style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                        <span>&#160;</span>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table> -->
  
                              </td>
                            </tr>
                          </tbody>
                        </table>
  
                        <div class="u-row-container" style="padding: 10px;background-color:#0a0a0a;margin-top: -20px;">
                          <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                            <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                              <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: #000000;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
              
                              <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #000000;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
                              <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                <div style="background-color: #0a0a0a;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                  <!--[if (!mso)&(!IE)]><!-->
                                  <div style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                                    <!--<![endif]-->
              
                                    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                      <tbody>
                                        <tr>
                                          <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
              
                                            <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                              <tbody>
                                                <tr style="vertical-align: top">
                                                  <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                    <span>&nbsp;</span>
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
                                              <div style="display: table; max-width:309px;">
                                                <!--[if (mso)|(IE)]><table width="309" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:309px;"><tr><![endif]-->
              
              
                                                <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 30px;" valign="top"><![endif]-->
                                                <table align="center" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 30px">
                                                  <tbody>
                                                    <tr style="vertical-align: top">
                                                      <td align="center" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                        <a href="https://www.linkedin.com/company/innogeeks/mycompany/" title="LinkedIn" target="_blank">
                                                          <img src="https://innogeeks24.s3.ap-south-1.amazonaws.com/image-3.png" alt="LinkedIn" title="LinkedIn" width="32" style="outline: none;text-decoration: none; color: rgb(113, 194, 244); font-family: sans-serif;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                        </a>
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                                <!--[if (mso)|(IE)]></td><![endif]-->
              
                                                <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 30px;" valign="top"><![endif]-->
                                                <table align="center" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 30px">
                                                  <tbody>
                                                    <tr style="vertical-align: top">
                                                      <td align="center" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                        <a href="https://www.instagram.com/innogeeks.kiet/" title="Instagram" target="_blank">
                                                          <img src="https://innogeeks24.s3.ap-south-1.amazonaws.com/image-1.png" alt="Instagram" title="Instagram" width="32" style="outline: none;text-decoration: none; color: rgb(113, 194, 244); font-family: sans-serif;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                        </a>
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                                <!--[if (mso)|(IE)]></td><![endif]-->
              
                                                <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 30px;" valign="top"><![endif]-->
                                                <table align="center" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 30px">
                                                  <tbody>
                                                    <tr style="vertical-align: top">
                                                      <td align="center" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                        <a href="https://twitter.com/InnogeeksKiet" title="X" target="_blank">
                                                          <img src="https://innogeeks24.s3.ap-south-1.amazonaws.com/image-2.png" alt="X" title="X" width="32" style="outline: none;text-decoration: none; color: rgb(113, 194, 244); font-family: sans-serif;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                        </a>
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                                <!--[if (mso)|(IE)]></td><![endif]-->
              
                                                <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 30px;" valign="top"><![endif]-->
                                                <table align="center" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 30px">
                                                  <tbody>
                                                    <tr style="vertical-align: top">
                                                      <td align="center" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                        <a href="https://www.youtube.com/@innogeekskiet3679" title="YouTube" target="_blank">
                                                          <img src="https://innogeeks24.s3.ap-south-1.amazonaws.com/image-5.png" alt="YouTube" title="YouTube" width="32" style="outline: none;text-decoration: none; color: rgb(113, 194, 244); font-family: sans-serif;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                        </a>
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                                <!--[if (mso)|(IE)]></td><![endif]-->
              
                                                <!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->
                                                <table align="center" border="0" cellspacing="0" cellpadding="0" width="32" height="32" style="width: 32px !important;height: 32px !important;display: inline-block;border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 0px">
                                                  <tbody>
                                                    <tr style="vertical-align: top">
                                                      <td align="center" valign="middle" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                                                        <a href="mailto:innohacks@kiet.edu" title="Email" target="_blank">
                                                          <img src="https://innogeeks24.s3.ap-south-1.amazonaws.com/image-4.png" alt="Email" title="Email" width="32" style="outline: none;text-decoration: none; color: rgb(113, 194, 244); font-family: sans-serif;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;max-width: 32px !important">
                                                        </a>
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
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
                                              <p style="line-height: 0%;"><strong>Follow our social media handles!</strong></p>
                                            </div>
              
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
              
                                    <table id="u_content_image_3" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                      <tbody>
                                        <tr>
                                          <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px 0px;font-family:arial,helvetica,sans-serif;" align="left">
              
                                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                              <tbody><tr>
                                                <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">
              
                                                  <img align="center" border="0" src="https://innogeeks24.s3.ap-south-1.amazonaws.com/image-7.png" alt="image" title="image" style="outline: none;text-decoration: none; color: rgb(113, 194, 244); font-family: sans-serif;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 580px;" width="580" class="v-src-width v-src-max-width">
              
                                                </td>
                                              </tr>
                                            </tbody></table>
              
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
              
                                    <table id="u_content_text_2" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                      <tbody>
                                        <tr>
                                          <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 30px 8px;font-family:arial,helvetica,sans-serif;" align="left">
              
                                            <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; color: #ffffff; line-height: 110%; text-align: center; word-wrap: break-word;">
                                              <p style="font-size: 14px; line-height: 110%;"><span style="font-size: 8px; line-height: 8.8px;">The content of this email is
                                                  confidential and intended for the recipient specified in message only. It is
                                                  strictly forbidden to share any part of this message with any third party, without a
                                                  written consent of the sender. If you received this message by mistake, please reply
                                                  to this message and follow with its deletion, so that we can ensure such a mistake
                                                  does not occur in the future.</span></p>
                                            </div>
              
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
              
                                    <table id="u_content_text_8" style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                      <tbody>
                                        <tr>
                                          <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px 30px 8px;font-family:arial,helvetica,sans-serif;" align="left">
              
                                            <div class="v-text-align v-line-height v-font-size" style="font-size: 14px; color: #ffffff; line-height: 110%; text-align: center; word-wrap: break-word;">
                                              <p style="line-height: 110%;">.</p>
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
                                                    <span>&nbsp;</span>
                                                  </td>
                                                </tr>
                                              </tbody>
                                            </table>
              
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
              
                                    <!--[if (!mso)&(!IE)]><!-->
                                  </div><!--<![endif]-->
                                </div>
                              </div>
                              <!--[if (mso)|(IE)]></td><![endif]-->
                              <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
                            </div>
                          </div>
                        </div>
                      </table></td>
                    </tr>


           </table></td>
         </tr>
       </table></td>
     </tr>
   </table>
  </div>
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


