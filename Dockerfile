FROM odoo:19.0

USER root


# Copie de ton module personnalisé dans le dossier d'addons d'Odoo
COPY ./parc_automobile /mnt/extra-addons/parc_automobile


RUN pip3 install --no-cache-dir xlsxwriter

USER odoo