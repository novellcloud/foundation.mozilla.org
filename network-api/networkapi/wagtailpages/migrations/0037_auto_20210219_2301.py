# Generated by Django 2.2.17 on 2021-02-19 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0036_articlepage_article_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='body_pt',
            new_name='body_pt_BR',
        ),
        migrations.RenameField(
            model_name='buyersguidepage',
            old_name='header_pt',
            new_name='header_pt_BR',
        ),
        migrations.RenameField(
            model_name='buyersguidepage',
            old_name='intro_text_pt',
            new_name='intro_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='cta',
            old_name='description_pt',
            new_name='description_pt_BR',
        ),
        migrations.RenameField(
            model_name='cta',
            old_name='header_pt',
            new_name='header_pt_BR',
        ),
        migrations.RenameField(
            model_name='cta',
            old_name='name_pt',
            new_name='name_pt_BR',
        ),
        migrations.RenameField(
            model_name='dearinternetpage',
            old_name='cta_button_link_pt',
            new_name='cta_button_link_pt_BR',
        ),
        migrations.RenameField(
            model_name='dearinternetpage',
            old_name='cta_button_text_pt',
            new_name='cta_button_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='dearinternetpage',
            old_name='cta_pt',
            new_name='cta_pt_BR',
        ),
        migrations.RenameField(
            model_name='dearinternetpage',
            old_name='intro_texts_pt',
            new_name='intro_texts_pt_BR',
        ),
        migrations.RenameField(
            model_name='dearinternetpage',
            old_name='letters_pt',
            new_name='letters_pt_BR',
        ),
        migrations.RenameField(
            model_name='dearinternetpage',
            old_name='letters_section_heading_pt',
            new_name='letters_section_heading_pt_BR',
        ),
        migrations.RenameField(
            model_name='donationmodal',
            old_name='body_pt',
            new_name='body_pt_BR',
        ),
        migrations.RenameField(
            model_name='donationmodal',
            old_name='dismiss_text_pt',
            new_name='dismiss_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='donationmodal',
            old_name='donate_text_pt',
            new_name='donate_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='donationmodal',
            old_name='header_pt',
            new_name='header_pt_BR',
        ),
        migrations.RenameField(
            model_name='donationmodal',
            old_name='name_pt',
            new_name='name_pt_BR',
        ),
        migrations.RenameField(
            model_name='focusarea',
            old_name='description_pt',
            new_name='description_pt_BR',
        ),
        migrations.RenameField(
            model_name='focusarea',
            old_name='name_pt',
            new_name='name_pt_BR',
        ),
        migrations.RenameField(
            model_name='generalproductpage',
            old_name='ai_helptext_pt',
            new_name='ai_helptext_pt_BR',
        ),
        migrations.RenameField(
            model_name='generalproductpage',
            old_name='biometric_data_collected_pt',
            new_name='biometric_data_collected_pt_BR',
        ),
        migrations.RenameField(
            model_name='generalproductpage',
            old_name='how_can_you_control_your_data_pt',
            new_name='how_can_you_control_your_data_pt_BR',
        ),
        migrations.RenameField(
            model_name='generalproductpage',
            old_name='offline_use_description_pt',
            new_name='offline_use_description_pt_BR',
        ),
        migrations.RenameField(
            model_name='generalproductpage',
            old_name='personal_data_collected_pt',
            new_name='personal_data_collected_pt_BR',
        ),
        migrations.RenameField(
            model_name='generalproductpage',
            old_name='social_data_collected_pt',
            new_name='social_data_collected_pt_BR',
        ),
        migrations.RenameField(
            model_name='generalproductpage',
            old_name='track_record_details_pt',
            new_name='track_record_details_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='cause_statement_link_text_pt',
            new_name='cause_statement_link_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='cause_statement_pt',
            new_name='cause_statement_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_button_text_pt',
            new_name='hero_button_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_button_url_pt',
            new_name='hero_button_url_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_headline_pt',
            new_name='hero_headline_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_image_pt',
            new_name='hero_image_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='partner_heading_pt',
            new_name='partner_heading_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='partner_intro_text_pt',
            new_name='partner_intro_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='partner_page_text_pt',
            new_name='partner_page_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='quote_image_pt',
            new_name='quote_image_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='quote_source_job_title_pt',
            new_name='quote_source_job_title_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='quote_source_name_pt',
            new_name='quote_source_name_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='quote_text_pt',
            new_name='quote_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='spotlight_headline_pt',
            new_name='spotlight_headline_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='take_action_title_pt',
            new_name='take_action_title_pt_BR',
        ),
        migrations.RenameField(
            model_name='homepagetakeactioncards',
            old_name='text_pt',
            new_name='text_pt_BR',
        ),
        migrations.RenameField(
            model_name='indexpage',
            old_name='header_pt',
            new_name='header_pt_BR',
        ),
        migrations.RenameField(
            model_name='indexpage',
            old_name='intro_pt',
            new_name='intro_pt_BR',
        ),
        migrations.RenameField(
            model_name='modularpage',
            old_name='body_pt',
            new_name='body_pt_BR',
        ),
        migrations.RenameField(
            model_name='modularpage',
            old_name='header_pt',
            new_name='header_pt_BR',
        ),
        migrations.RenameField(
            model_name='partnerlogos',
            old_name='name_pt',
            new_name='name_pt_BR',
        ),
        migrations.RenameField(
            model_name='petition',
            old_name='share_email_pt',
            new_name='share_email_pt_BR',
        ),
        migrations.RenameField(
            model_name='petition',
            old_name='share_facebook_pt',
            new_name='share_facebook_pt_BR',
        ),
        migrations.RenameField(
            model_name='petition',
            old_name='share_link_pt',
            new_name='share_link_pt_BR',
        ),
        migrations.RenameField(
            model_name='petition',
            old_name='share_link_text_pt',
            new_name='share_link_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='petition',
            old_name='share_twitter_pt',
            new_name='share_twitter_pt_BR',
        ),
        migrations.RenameField(
            model_name='petition',
            old_name='thank_you_pt',
            new_name='thank_you_pt_BR',
        ),
        migrations.RenameField(
            model_name='primarypage',
            old_name='body_pt',
            new_name='body_pt_BR',
        ),
        migrations.RenameField(
            model_name='primarypage',
            old_name='header_pt',
            new_name='header_pt_BR',
        ),
        migrations.RenameField(
            model_name='primarypage',
            old_name='intro_pt',
            new_name='intro_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='blurb_pt',
            new_name='blurb_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='how_does_it_use_data_collected_pt',
            new_name='how_does_it_use_data_collected_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='manage_vulnerabilities_helptext_pt',
            new_name='manage_vulnerabilities_helptext_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='price_pt',
            new_name='price_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='privacy_policy_helptext_pt',
            new_name='privacy_policy_helptext_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='security_updates_helptext_pt',
            new_name='security_updates_helptext_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='signup_requirement_explanation_pt',
            new_name='signup_requirement_explanation_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='strong_password_helptext_pt',
            new_name='strong_password_helptext_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='user_friendly_privacy_policy_helptext_pt',
            new_name='user_friendly_privacy_policy_helptext_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='uses_encryption_helptext_pt',
            new_name='uses_encryption_helptext_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpage',
            old_name='worst_case_pt',
            new_name='worst_case_pt_BR',
        ),
        migrations.RenameField(
            model_name='productpageprivacypolicylink',
            old_name='label_pt',
            new_name='label_pt_BR',
        ),
        migrations.RenameField(
            model_name='redirectingpage',
            old_name='URL_pt',
            new_name='URL_pt_BR',
        ),
        migrations.RenameField(
            model_name='youtuberegretspage',
            old_name='faq_pt',
            new_name='faq_pt_BR',
        ),
        migrations.RenameField(
            model_name='youtuberegretspage',
            old_name='headline_pt',
            new_name='headline_pt_BR',
        ),
        migrations.RenameField(
            model_name='youtuberegretspage',
            old_name='intro_images_pt',
            new_name='intro_images_pt_BR',
        ),
        migrations.RenameField(
            model_name='youtuberegretspage',
            old_name='intro_text_pt',
            new_name='intro_text_pt_BR',
        ),
        migrations.RenameField(
            model_name='youtuberegretspage',
            old_name='regret_stories_pt',
            new_name='regret_stories_pt_BR',
        ),
        migrations.RenameField(
            model_name='youtuberegretsreporterpage',
            old_name='headline_pt',
            new_name='headline_pt_BR',
        ),
        migrations.RenameField(
            model_name='youtuberegretsreporterpage',
            old_name='intro_images_pt',
            new_name='intro_images_pt_BR',
        ),
        migrations.RenameField(
            model_name='youtuberegretsreporterpage',
            old_name='intro_text_pt',
            new_name='intro_text_pt_BR',
        ),
    ]