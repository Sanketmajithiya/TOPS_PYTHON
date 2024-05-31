# Q.3 Explain what does django-admin.py make messages command is used for?
""" 
The django-admin.py make messages command is used for generating language translation files for internationalization (i18n) and localization (l10n) in Django projects.

Runs over the entire source tree of the current directory and pulls out all strings marked for translation. It creates (or updates) a message file in the conf/locale (in the Django tree) or locale (for project and application) directory.


1 Extracting translatable strings: The command scans your Django project's codebase, including Python and HTML files, for strings wrapped in translation functions such as gettext() or its alias _(). These strings typically include user-visible text like error messages, form labels, and button text.

2 Generating .po files: After identifying translatable strings, makemessages generates or updates .po (Portable Object) files for each language specified in your project's settings. These .po files contain the original untranslated strings along with placeholders for translations.

3 Template for translators: The .po files serve as templates for translators. They contain the original strings that need to be translated and provide placeholders where translators can input the corresponding translations for each language.

""" 