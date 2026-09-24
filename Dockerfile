FROM odoo:19.0

USER root



# Copie tout le contenu du dossier custom_addons vers les extra-addons d'Odoo
COPY ./custom_addons /mnt/extra-addons/


RUN pip3 install --no-cache-dir --break-system-packages xlsxwriter

USER odoo