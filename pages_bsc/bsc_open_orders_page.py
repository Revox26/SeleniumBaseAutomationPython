from seleniumbase import BaseCase
from faker import Faker


class BscOpenOrdersPage(BaseCase):
    open_orders_button = "//div[@data-testid='open-orders-notification']"
    item = "//td[contains(.,'JDC Ready made company 1')]"
    transfer_company_page = "//a[contains(.,'Transfer Company')]"
    email_credentials_page = "//a[contains(.,'Email Credentials')]"
    company_name = "//label[starts-with(text(),'Company Name *')]/..//input[@class='form-control']"
    company_number = "//input[@placeholder='CRN must be 2 letters followed by 6 digits, or a single 0 or 1 followed by 7 digits']"
    tel_number = "//input[@placeholder='Telephone number must start with a zero and is followed by exactly 10 digits']"
    formation_date = "//div[@class='react-date-picker__inputGroup']"
    select_formation_date = "div[class='react-calendar__viewContainer'] button:nth-child(1)"
    order_email = "div[class='tab-pane active'] div input[placeholder='someone@example.com']"
    sic_code = "//label[.='SIC code *']/following-sibling::div[contains(.,'Select..')]"
    select_sic_code = "//div[contains(text(),'Accounting and auditing activities (69201)')]"
    country_of_registration = "//label[.='Country Of Registration']/following-sibling::div[contains(.,'Select..')]"
    select_country_of_registration = "//div[contains(text(),'United Kingdom')]"
    user_registration_saved_successfully = "//span[.='User registration saved successfully']"
    transfer_company_button = "//button[.='Transfer Company']"

    incoming_type = "//label[.='Type *']/following-sibling::div[contains(.,'Select..')]"
    select_imap = "//div[contains(text(),'IMAP')]"
    incoming_host = "//label[.='Host *']/..//input[@class='form-control']"
    incoming_port = "//label[.='Port *']/..//input[@placeholder='0-65535']"
    incoming_email = "//label[.='Email *']/..//input[@placeholder='someone@example.com']"
    incoming_password = "//label[.='Password *']/..//input[@class='form-control']"

    outgoing_smptp_host = "//label[.='SMTP Host *']/..//input[@class='form-control']"
    outgoing_smtp_port = "//label[.='SMTP Port *']/..//input[@placeholder='0-65535']"
    outgoing_smtp_encryption = "//label[.='SMTP Encryption *']/following-sibling::div[contains(.,'Select..')]"
    select_tls_encryption = "//div[contains(text(),'TLS')]"
    outgoing_smptp_email = "//label[.='SMTP Email *']/..//input[@placeholder='someone@example.com']"
    outgoing_smtp_password = "//label[.='SMTP Password *']/..//input[@class='form-control']"
    save_button_email_credentials = "//button[.='Save']"
    email_credentials_successfully_saved = "//span[.='Email credentials saved successfully']"

    def manage_orders(self):
        self.click(self.open_orders_button)
        self.click(self.item, timeout=60)

    def transfer_company_tab(self):
        fake = Faker()
        fake_company_name = fake.company()

        with open("..//data//first_name.txt", "r") as file:
            random_name = file.read().strip()
        with open("..//data//email.txt", "r") as file:
            random_email = file.read().strip()
        get_fake_company_name = fake_company_name + " " + random_name + " Ltd"

        self.click(self.transfer_company_page, timeout=60)
        self.scroll_into_view(self.transfer_company_page)
        self.type(self.company_name, get_fake_company_name, timeout=60)
        self.type(self.company_number, self.var1)
        self.type(self.tel_number, "01923125345")
        self.click(self.formation_date)
        self.click(self.select_formation_date)
        self.type(self.order_email, random_email)
        self.click(self.sic_code)
        self.click(self.select_sic_code)
        self.click(self.country_of_registration)
        self.click(self.select_country_of_registration)
        self.click(self.transfer_company_button)
        self.assert_element(self.user_registration_saved_successfully, timeout=60)

    def transmit_email_provider(self, incoming_host, incoming_email, incoming_password, outgoing_smtp_host, outgoing_smtp_email, outgoing_smtp_password):
        # INCOMING
        self.click(self.email_credentials_page)
        self.click(self.incoming_type)
        self.click(self.select_imap)
        self.type(self.incoming_host, incoming_host)
        self.type(self.incoming_port, "993")
        self.type(self.incoming_email, incoming_email)
        self.type(self.incoming_password, incoming_password)

        # OUTGOING
        self.type(self.outgoing_smptp_host, outgoing_smtp_host)
        self.type(self.outgoing_smtp_port, "587")
        self.click(self.outgoing_smtp_encryption)
        self.click(self.select_tls_encryption)
        self.type(self.outgoing_smptp_email, outgoing_smtp_email)
        self.type(self.outgoing_smtp_password, outgoing_smtp_password)
        self.click(self.save_button_email_credentials)
        self.assert_element(self.email_credentials_successfully_saved, timeout=60)

    def transmit_gmail_credentials(self):
        self.transmit_email_provider("imap.gmail.com", "richiesorhento@gmail.com", "toue pqeq upuz oxbc", "smtp.gmail.com", "richiesorhento@gmail.com", "toue pqeq upuz oxbc")

    def transmit_outlook_credentials(self):
        self.transmit_email_provider("outlook.office365.com", "rcharddpinili@outlook.com", "@Test123456", "smtp-mail.outlook.com", "rcharddpinili@outlook.com", "@Test123456")
